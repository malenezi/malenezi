
"""app/dashboard.py — the Tayseer self-service operations dashboard (Dash).

Run:  python app/dashboard.py   ->  http://127.0.0.1:8050

Design rules carried over from Modules 1-4:
  * the DEFAULT state answers the primary question with zero clicks
  * every non-additive measure is RECOMPUTED from its components, never averaged
  * the active filter / drill state is ALWAYS visible (state legibility)
  * one accent colour for the signal, grey for context; no gauges, no dual axes
"""
from __future__ import annotations

import pathlib
import sys

import pandas as pd
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output, State, callback_context, no_update

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
import tayseer_viz as tv                                            # noqa: E402

# ---------------------------------------------------------------------------
# Data and measures
# ---------------------------------------------------------------------------
DF = tv.load_facts()
SERVICES = tv.load("dim_services.csv")
DIRECTORS = tv.load("region_directors.csv")

# column -> (label, weight column, target, direction).  The WEIGHT DIFFERS per
# measure; it is transcribed from kpi_targets.csv, not guessed.
MEASURES = {
    "digital_adoption_pct": ("Digital adoption %", "unique_users", 65.0, "higher"),
    "cost_per_txn_sar": ("Cost per transaction (SAR)", "transactions", 18.0, "lower"),
    "csat": ("CSAT (1-5)", "transactions", 4.3, "higher"),
}
ACCENT, GREY, INK = tv.ACCENT, tv.GREY, tv.INK


def measure(frame: pd.DataFrame, col: str) -> float:
    """Recompute a non-additive measure. NEVER frame[col].mean()."""
    return tv.wmean(frame, col, MEASURES[col][1])


def by_key(frame: pd.DataFrame, key: str, col: str) -> pd.DataFrame:
    out = (frame.groupby(key)
                .apply(lambda x: measure(x, col), include_groups=False)
                .reset_index(name=col))
    return out.sort_values(col)


def scope(region=None, category=None, channel=None) -> pd.DataFrame:
    f = DF
    if region:
        f = f[f.region == region]
    if category:
        f = f[f.service_category == category]
    if channel and channel != "All channels":
        f = f[f.channel == channel]
    return f


def breadcrumb(region, category) -> str:
    parts = ["National"]
    if region:
        parts.append(region)
    if category:
        parts.append(category)
    return "  >  ".join(parts)


# ---------------------------------------------------------------------------
# Layout — the inverted pyramid: state, KPI band, breakdown + trend, drill
# ---------------------------------------------------------------------------
app = Dash(__name__, title="Tayseer operations dashboard")
CARD = {"padding": "14px 18px", "border": "1px solid #E4E7EB", "borderRadius": "8px",
        "background": "white"}

app.layout = html.Div(style={"fontFamily": "system-ui, sans-serif",
                             "background": "#FAFAFA", "padding": "18px",
                             "maxWidth": "1180px", "margin": "0 auto"}, children=[
    html.H2("Tayseer operations dashboard", style={"color": INK, "marginBottom": "2px"}),
    html.Div("Deputy Minister | weekly | is the programme on track, and where is it not?",
             style={"color": "#7B8794", "marginBottom": "14px"}),

    html.Div(style={"display": "flex", "gap": "12px", "marginBottom": "12px"}, children=[
        html.Div(style={"flex": "1"}, children=[
            html.Label("Measure", style={"fontSize": "12px", "color": "#7B8794"}),
            dcc.Dropdown(id="measure", clearable=False, value="digital_adoption_pct",
                         options=[{"label": v[0], "value": k}
                                  for k, v in MEASURES.items()]),      # TOGGLE pattern
        ]),
        html.Div(style={"flex": "1"}, children=[
            html.Label("Channel filter", style={"fontSize": "12px", "color": "#7B8794"}),
            dcc.Dropdown(id="channel", clearable=False, value="All channels",
                         options=[{"label": c, "value": c} for c in
                                  ["All channels"] + sorted(DF.channel.unique())]),
        ]),                                                            # FILTER pattern
        html.Div(style={"alignSelf": "flex-end"}, children=[
            html.Button("Reset to national", id="reset", n_clicks=0,
                        style={"padding": "7px 14px", "border": "1px solid #E4E7EB",
                               "borderRadius": "6px", "background": "white",
                               "cursor": "pointer"}),
        ]),
    ]),

    # STATE LEGIBILITY: the active scope is never hidden.
    html.Div(id="filter-state", style={**CARD, "fontWeight": "600", "color": INK,
                                       "marginBottom": "12px",
                                       "borderLeft": "4px solid " + ACCENT}),

    html.Div(id="kpi-band", style={**CARD, "marginBottom": "12px"}),
    html.Div(style={"display": "flex", "gap": "12px"}, children=[
        html.Div(style={**CARD, "flex": "1"},
                 children=[dcc.Graph(id="region-bar", config={"displayModeBar": False})]),
        html.Div(style={**CARD, "flex": "1"},
                 children=[dcc.Graph(id="trend", config={"displayModeBar": False})]),
    ]),
    html.Div(style={**CARD, "marginTop": "12px"},
             children=[dcc.Graph(id="drill", config={"displayModeBar": False})]),

    dcc.Store(id="sel-region", data=None),
    dcc.Store(id="sel-category", data=None),
])


# ---------------------------------------------------------------------------
# Callbacks
# ---------------------------------------------------------------------------
@app.callback(Output("sel-region", "data"), Output("sel-category", "data"),
              Input("region-bar", "clickData"), Input("drill", "clickData"),
              Input("reset", "n_clicks"),
              State("sel-region", "data"), State("sel-category", "data"))
def update_selection(bar_click, drill_click, _reset, region, category):
    """CROSS-FILTER (click a region) and DRILL (click a service category)."""
    trigger = callback_context.triggered_id
    if trigger == "reset":
        return None, None
    if trigger == "region-bar" and bar_click:
        clicked = bar_click["points"][0]["y"]
        return (None, None) if clicked == region else (clicked, None)   # click again clears
    if trigger == "drill" and drill_click:
        clicked = drill_click["points"][0]["y"]
        return region, (None if clicked == category else clicked)
    return no_update, no_update


@app.callback(Output("filter-state", "children"), Output("kpi-band", "children"),
              Input("measure", "value"), Input("channel", "value"),
              Input("sel-region", "data"), Input("sel-category", "data"))
def state_and_kpi(col, channel, region, category):
    label, _w, target, direction = MEASURES[col]
    frame = scope(region, category, channel)
    latest = frame[frame.month == frame.month.max()]
    value = measure(latest, col)
    delta = value - target
    good = (delta >= 0) if direction == "higher" else (delta <= 0)
    state = ("{}   |   measure: {}   |   channel: {}".format(
                 breadcrumb(region, category), label, channel)
             + ("" if (region or category) else "   |   click a bar to cross-filter"))
    band = html.Div(style={"display": "flex", "alignItems": "baseline", "gap": "18px"},
                    children=[
        html.Div("{:,.1f}".format(value),
                 style={"fontSize": "44px", "fontWeight": "700", "color": INK}),
        html.Div(label, style={"fontSize": "15px", "color": "#7B8794"}),
        html.Div("{:+.1f} vs target {:g}".format(delta, target),
                 style={"fontSize": "15px", "fontWeight": "600",
                        "color": "#009E73" if good else ACCENT}),
        html.Div("({:,} fact rows in scope)".format(len(latest)),
                 style={"fontSize": "12px", "color": "#9AA5B1", "marginLeft": "auto"}),
    ])
    return state, band


@app.callback(Output("region-bar", "figure"),
              Input("measure", "value"), Input("channel", "value"),
              Input("sel-region", "data"))
def region_bar(col, channel, region):
    label, _w, target, direction = MEASURES[col]
    frame = scope(None, None, channel)
    latest = frame[frame.month == frame.month.max()]
    d = by_key(latest, "region", col)
    if region:
        colors = [ACCENT if r == region else GREY for r in d.region]
    elif direction == "higher":
        colors = [ACCENT if v < target else GREY for v in d[col]]
    else:
        colors = [ACCENT if v > target else GREY for v in d[col]]
    fig = go.Figure(go.Bar(x=d[col], y=d.region, orientation="h", marker_color=colors,
                           hovertemplate="<b>%{y}</b><br>%{x:.1f}<extra></extra>"))
    fig.add_vline(x=target, line_dash="dash", line_color=INK)
    fig.update_layout(template="plotly_white", height=430, showlegend=False,
                      margin=dict(t=54, l=8, r=18, b=36), bargap=.28,
                      title=label + " by region - click to cross-filter",
                      xaxis_title=label, font=dict(color=INK))
    return fig


@app.callback(Output("trend", "figure"),
              Input("measure", "value"), Input("channel", "value"),
              Input("sel-region", "data"), Input("sel-category", "data"))
def trend(col, channel, region, category):
    label, _w, target, _d = MEASURES[col]
    frame = scope(region, category, channel)
    monthly = by_key(frame, "month", col).sort_values("month")
    fig = go.Figure(go.Scatter(x=monthly.month, y=monthly[col], mode="lines",
                               line=dict(color=tv.ACCENT_2, width=3),
                               hovertemplate="%{x|%b %Y}<br>%{y:.1f}<extra></extra>"))
    fig.add_hline(y=target, line_dash="dash", line_color=ACCENT,
                  annotation_text="target {:g}".format(target),
                  annotation_position="top left")
    fig.update_layout(template="plotly_white", height=430, showlegend=False,
                      margin=dict(t=54, l=8, r=18, b=36),
                      # state made legible IN THE TITLE, so a screenshot carries its scope
                      title="{} - {}".format(label, breadcrumb(region, category)),
                      yaxis_title=label, font=dict(color=INK))
    return fig


@app.callback(Output("drill", "figure"),
              Input("measure", "value"), Input("channel", "value"),
              Input("sel-region", "data"), Input("sel-category", "data"))
def drill(col, channel, region, category):
    """DRILL path: national -> region -> service category -> channel."""
    label, _w, target, direction = MEASURES[col]
    frame = scope(region, None, channel)
    latest = frame[frame.month == frame.month.max()]
    if category:
        n_services = len(SERVICES[SERVICES.service_category == category])
        sub = latest[latest.service_category == category]
        d = by_key(sub, "channel", col)
        key = "channel"
        title = "{} by channel - {} ({} named services here)".format(
            label, breadcrumb(region, category), n_services)
    else:
        d = by_key(latest, "service_category", col)
        key = "service_category"
        title = "{} by service category - {} - click to drill".format(
            label, breadcrumb(region, category))
    colors = ([ACCENT if v < target else GREY for v in d[col]] if direction == "higher"
              else [ACCENT if v > target else GREY for v in d[col]])
    fig = go.Figure(go.Bar(x=d[col], y=d[key], orientation="h", marker_color=colors,
                           hovertemplate="<b>%{y}</b><br>%{x:.1f}<extra></extra>"))
    fig.add_vline(x=target, line_dash="dash", line_color=INK)
    fig.update_layout(template="plotly_white", height=380, showlegend=False,
                      margin=dict(t=54, l=8, r=18, b=36), bargap=.28,
                      title=title, xaxis_title=label, font=dict(color=INK))
    return fig


# ---------------------------------------------------------------------------
# Row-level security — the code version of the BI role (Task 9)
# ---------------------------------------------------------------------------
def rls_scope(email: str) -> pd.DataFrame:
    """A region director sees only their own region. Deny by default."""
    row = DIRECTORS[DIRECTORS.email.str.lower() == email.lower()]
    if row.empty:
        raise PermissionError(email + " has no RLS mapping - deny by default")
    region = row.iloc[0]["region"]
    return DF if region in ("All", "National") else DF[DF.region == region]


if __name__ == "__main__":
    app.run(debug=True, port=8050)

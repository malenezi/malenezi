# Builds sdaia-success-stories-standalone.html — a single self-contained file (CSS, JS, icons and
# all local images inlined) generated from index.html + css/ + js/ + assets/ and the shared design system.
# Run after any change to the site:   powershell -ExecutionPolicy Bypass -File build-standalone.ps1
$ErrorActionPreference = 'Stop'
$site = $PSScriptRoot
$academy = Resolve-Path (Join-Path $site '..\..')
$utf8 = New-Object System.Text.UTF8Encoding($false)
function ReadText($p) { [IO.File]::ReadAllText($p, [Text.Encoding]::UTF8) }
function DataUri($p) {
  $ext = [IO.Path]::GetExtension($p).ToLower()
  $mime = @{ '.png'='image/png'; '.jpg'='image/jpeg'; '.jpeg'='image/jpeg'; '.webp'='image/webp'; '.svg'='image/svg+xml'; '.gif'='image/gif' }[$ext]
  if (-not $mime) { return $null }
  'data:' + $mime + ';base64,' + [Convert]::ToBase64String([IO.File]::ReadAllBytes($p))
}

$html = ReadText (Join-Path $site 'index.html')
$uiCss = ReadText (Join-Path $academy 'assets\sdaia-ui.css')
$siteCss = ReadText (Join-Path $site 'css\style.css')
$icons = ReadText (Join-Path $academy 'assets\sdaia-icons.js')
$ui = ReadText (Join-Path $academy 'assets\sdaia-ui.js')
$data = ReadText (Join-Path $site 'js\data.js')
$main = ReadText (Join-Path $site 'js\main.js')

# the shared runtime resolves the Academy root from its own <script src>; inline scripts have none,
# so the standalone declares the root explicitly (it lives in SuccessStories/website/).
$html = $html -replace '<html lang="ar" dir="rtl">', '<html lang="ar" dir="rtl" data-root="../../">'

# inline the official logo used by the shared header/footer
$logo = DataUri (Join-Path $academy 'assets\academy-logo.png')
$ui = $ui.Replace("' + ROOT + 'assets/academy-logo.png", $logo)
if ($ui.Contains("assets/academy-logo.png")) { throw "Standalone build: shared logo path not inlined (sdaia-ui.js changed?)" }

# inline local images referenced by the page and the data file
$inlineAssets = {
  param($text)
  [regex]::Replace($text, "assets/[A-Za-z0-9_\-\.؀-ۿ%\(\) ]+?\.(png|jpg|jpeg|webp|svg|gif)", {
    param($m)
    $rel = [Uri]::UnescapeDataString($m.Value)
    $file = Join-Path $site ($rel -replace '/', '\')
    if (Test-Path $file) { $d = DataUri $file; if ($d) { return $d } }
    return $m.Value
  })
}
$html = & $inlineAssets $html
$data = & $inlineAssets $data
foreach ($blob in @($uiCss, $siteCss, $icons, $ui, $data, $main)) {
  if ($blob -match '</script') { throw 'Standalone build: an inlined file contains a closing script tag' }
}

# swap external references for inline blocks (literal String.Replace — the JS contains `$` template syntax)
$html = $html.Replace('<link rel="stylesheet" href="../../assets/sdaia-ui.css">', ('<style>' + "`n" + $uiCss + "`n" + '</style>'))
$html = $html.Replace('<link rel="stylesheet" href="css/style.css">', ('<style>' + "`n" + $siteCss + "`n" + '</style>'))
$html = $html.Replace('<script src="../../assets/sdaia-icons.js"></script>', ('<script>' + "`n" + $icons + "`n" + '</script>'))
$html = $html.Replace('<script src="../../assets/sdaia-ui.js"></script>', ('<script>' + "`n" + $ui + "`n" + '</script>'))
$html = $html.Replace('<script src="js/data.js"></script>', ('<script>' + "`n" + $data + "`n" + '</script>'))
$html = $html.Replace('<script src="js/main.js"></script>', ('<script>' + "`n" + $main + "`n" + '</script>'))
foreach ($needle in @('href="../../assets/sdaia-ui.css"','src="../../assets/sdaia-icons.js"','src="../../assets/sdaia-ui.js"','src="js/data.js"','src="js/main.js"','href="css/style.css"')) {
  if ($html.Contains($needle)) { throw "Standalone build: reference not inlined: $needle" }
}

# links to sibling sites must stay relative to the Academy root (same folder as index.html, so unchanged)
$out = Join-Path $site 'sdaia-success-stories-standalone.html'
[IO.File]::WriteAllText($out, $html, $utf8)
"Built $out  ($([math]::Round((Get-Item $out).Length / 1MB, 2)) MB)"

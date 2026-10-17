# -*- coding: utf-8 -*-
# Round 17 Oct 2026: fetch GitHub profile + README evidence for candidate owners (no API; github.com HTML + raw)
import json, re, sys, os, time, html, subprocess, concurrent.futures as cf
D = os.path.expanduser('~/mnt/Academy/Graduates/tools/round_2026-10-17b/')
cands = json.load(open(D + sys.argv[1], encoding='utf-8'))   # {owner:[repo,...]}
out_p = D + sys.argv[2]
out = json.load(open(out_p, encoding='utf-8')) if os.path.exists(out_p) else {}

def get(url):
    try:
        r = subprocess.run(['curl', '-sL', '--max-time', '25', '-w', '\n%{http_code}', url], capture_output=True, timeout=40)
        t = r.stdout.decode('utf-8', 'replace')
        body, _, code = t.rpartition('\n')
        return code.strip(), body
    except Exception as e:
        return '0', ''

KW = re.compile(r'(sdaia|سدايا|submitted by|prepared by|presented by|team|group|author|name\s*:|by\s*:|trainee|student|instructor|trainer|bootcamp|course|program|programme|capstone|cohort|SDA-[A-Z]{3}-\d{3}|T5|أكاديمية|المتدرب|إعداد|الاسم|فريق)', re.I)

def profile(o):
    c, b = get('https://github.com/' + o)
    if c != '200':
        return {'code': c}
    t = re.search(r'<title>([^<]*)</title>', b)
    title = html.unescape(t.group(1)) if t else ''
    m = re.match(r"\s*\S+\s+\((.+)\)", title)
    name = m.group(1).strip() if m else ''
    bio = re.search(r'<div class="p-note user-profile-bio[^>]*>\s*<div>(.*?)</div>', b, re.S)
    bio = re.sub('<[^>]+>', '', html.unescape(bio.group(1))).strip()[:200] if bio else ''
    lis = sorted(set(re.findall(r'https://(?:www\.)?linkedin\.com/in/[A-Za-z0-9\-_%]+/?', b)))
    loc = re.search(r'itemprop="homeLocation"[^>]*>.*?<span class="p-label">([^<]*)', b, re.S)
    return {'code': c, 'name': html.unescape(name), 'bio': html.unescape(bio), 'li': lis[:2], 'loc': loc.group(1).strip() if loc else ''}

def readme(o, r):
    for f in ('README.md', 'readme.md', 'Readme.md', 'README.MD', 'README'):
        c, b = get(f'https://github.com/{o}/{r}/raw/HEAD/{f}')
        if c == '200' and b and not b.lstrip().startswith('<!DOCTYPE'):
            lines = [l.strip() for l in b.splitlines() if l.strip()]
            hits = [l[:220] for l in lines if KW.search(l)][:14]
            return {'h1': (lines[0][:150] if lines else ''), 'hits': hits, 'len': len(b)}
    return {'h1': '', 'hits': [], 'len': 0}

def work(o):
    p = profile(o)
    rs = {}
    for r in cands[o][:3]:
        rs[r] = readme(o, r)
    return o, {'p': p, 'r': rs}

todo = [o for o in cands if o not in out][:int(sys.argv[3])]
print('todo', len(todo), flush=True)
t0 = time.time()
with cf.ThreadPoolExecutor(6) as ex:
    for i, (o, res) in enumerate(ex.map(work, todo)):
        out[o] = res
        if i % 25 == 0:
            json.dump(out, open(out_p, 'w', encoding='utf-8'), ensure_ascii=False)
            print(i, round(time.time() - t0), flush=True)
json.dump(out, open(out_p, 'w', encoding='utf-8'), ensure_ascii=False)
print('done', len(out), 'remaining', len([o for o in cands if o not in out]))

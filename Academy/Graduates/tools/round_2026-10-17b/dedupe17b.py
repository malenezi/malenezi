# -*- coding: utf-8 -*-
import json, os, sys, re, collections, urllib.parse
sys.path[:0] = [os.path.expanduser('~/mnt/Academy/Graduates/tools/round_2026-10-07'), os.path.expanduser('~/mnt/Academy/Graduates/tools')]
import translit as TR
H = os.path.expanduser('~/mnt/Academy/')
D = H + 'Graduates/tools/round_2026-10-17b/'
s = open(H + 'Graduates/index.html', encoding='utf-8').read()
i = s.index('const DATA = ') + len('const DATA = '); j = s.index('\nconst SITE_STATS')
g = json.loads(s[i:j].rstrip()[:-1])['grads']
idx = TR.build_index(g)
K = json.load(open(D + 'known.json', encoding='utf-8'))
mode = sys.argv[1]
if mode == 'li':
    C = json.load(open(D + 'li_cands17.json', encoding='utf-8'))
    for c in C:
        slug = urllib.parse.unquote(c[0]).lower()
        hit = K['li'].get(slug) or K['li'].get(c[0].lower())
        m = sorted({x[0] for x in TR.match(c[2] or c[1], c[1], idx)})
        ex = [k + 1 for k, r in enumerate(g) if (r.get('en') or '').lower() == c[1].lower()]
        print(c[1], '| slug', hit, '| match', m[:6], '| exact', ex)
elif mode == 'prog':
    for kw in sys.argv[2:]:
        cnt = collections.Counter((r['prog'], r['tr']) for r in g if kw.lower() in r['prog'].lower())
        print('==', kw)
        for (p, t), n in cnt.most_common(3): print('  ', n, t, p[:160])

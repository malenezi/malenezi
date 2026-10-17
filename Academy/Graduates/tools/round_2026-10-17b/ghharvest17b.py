# -*- coding: utf-8 -*-
# Resumable GitHub repo-search harvest (github.com search JSON, logged-out) — round 17 Oct 2026
import json, os, sys, time, subprocess, urllib.parse
D = os.path.expanduser('~/mnt/Academy/Graduates/tools/round_2026-10-17b/')
SP = D + 'harvest_state.json'
S = json.load(open(SP, encoding='utf-8')) if os.path.exists(SP) else {'H': {}, 'Q': {}}
Q = [l.strip() for l in open(D + 'queries.txt', encoding='utf-8') if l.strip()]
BUDGET = float(sys.argv[1]) if len(sys.argv) > 1 else 160
t0 = time.time()

def fetch(q, p):
    u = 'https://github.com/search?q=' + urllib.parse.quote(q) + '&type=repositories&p=%d' % p
    r = subprocess.run(['curl', '-s', '--max-time', '20', '-H', 'Accept: application/json', '-w', '\n%{http_code}', u], capture_output=True)
    t = r.stdout.decode('utf-8', 'replace'); body, _, code = t.rpartition('\n')
    return code.strip(), body

def save():
    json.dump(S, open(SP, 'w', encoding='utf-8'), ensure_ascii=False)

stop = False
for q in Q:
    st = S['Q'].setdefault(q, {'p': 1, 'pc': None, 'done': False})
    while not st['done']:
        if time.time() - t0 > BUDGET:
            stop = True; break
        code, body = fetch(q, st['p'])
        if code != '200':
            print('rate', code, q, st['p'], flush=True); time.sleep(12); continue
        try:
            j = json.loads(body); b = j['payload'].get('blackbirdSearchRoute') or j['payload']
        except Exception as e:
            print('parse', e); time.sleep(10); continue
        st['pc'] = b.get('page_count', 0); st['count'] = b.get('result_count', 0)
        for x in b.get('results', []):
            rr = x['repo']['repository']; k = rr['owner_login'] + '/' + rr['name']
            if k not in S['H']:
                S['H'][k] = {'d': (x.get('hl_trunc_description') or '').replace('<em>', '').replace('</em>', '')[:160], 'u': rr['updated_at'][:10], 'q': q}
        st['p'] += 1
        if st['p'] > (st['pc'] or 0) or st['p'] > 100:
            st['done'] = True
        save(); time.sleep(3)
    if stop: break
save()
print('repos', len(S['H']), 'queries done', sum(1 for v in S['Q'].values() if v['done']), '/', len(Q),
      [(q[-26:], v.get('count'), v['p'] - 1, v.get('pc')) for q, v in S['Q'].items() if not v['done']][:3])

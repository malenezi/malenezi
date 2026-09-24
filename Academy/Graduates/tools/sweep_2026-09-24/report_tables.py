import json
g=json.load(open('grads_after.json')); st=json.load(open('stats24.json')); S=json.load(open('sets.json'))
TRL={'ai':'مهندس ذكاء اصطناعي','ds':'عالم بيانات','other':'برامج متخصصة أخرى','dmg':'إدارة وحوكمة البيانات','genai':'أكاديمية الذكاء الاصطناعي التوليدي','coop':'التدريب التعاوني'}
def esc(t): return (t or '').replace('|','\\|')
def new_table():
    out=['| # | الاسم العربي | الاسم الإنجليزي | البرنامج | الدفعة | المسار المعياري | الثقة | الروابط |','|---|---|---|---|---|---|---|---|']
    for i in range(st['base']+1,len(g)+1):
        x=g[i-1]; lk=' · '.join('[%s](%s)'%(l,u) for l,u in x['links'])
        out.append('| %d | %s | %s | %s | %s | %s | %d | %s |'%(i,esc(x['n']),esc(x['en']),esc(x['prog']),esc(x['co']),TRL[x['tr']],x['score'],lk))
    return '\n'.join(out)
def enr_table():
    out=['| # | السجل | حساب GitHub | ما أضافته الجولة |','|---|---|---|---|']
    for o,i in sorted(S['ENR'].items(),key=lambda t:t[1]):
        x=g[i-1]; d=x['d'].split('[جولة 24 سبتمبر 2026] ')[-1]
        out.append('| #%d | %s | `%s` | %s |'%(i,esc(x['n']),o,esc(d)))
    return '\n'.join(out)
if __name__=='__main__':
    print(new_table()[:600]); print(enr_table()[:600])

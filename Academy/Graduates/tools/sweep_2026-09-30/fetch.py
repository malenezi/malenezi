import json,re,urllib.request,time,os,sys,html
C=json.load(open('cand_gh.json'))
EXC=set('Mona-Alzahrani serrysibaee Wadha-Almattar Vision-CAIR alaqsa-akbar khaledhosni metauto-ai S0x7E2 kadi21447 mohamedalgharib26 AmeerAlmaamari ashikiut SDAISergioMunozPintor Bhanu9a99 khalil-allam Abdomash Danashmand MohammedAlherz hkmkmh MoudiAlhazzaa omaromeir OhoudHassan1 Shujaat123 hossam99-9 ManarEyad7 3bdulah Mahmood-Anaam Aziz-Th Layan-Alsaud MariaLogic NaifALSHARARI ruixiang-wang MahmuedAlardawi JTSIV1 KhaledSaud70 asmayamani NouraAlGahtani obser2024 JSALT2024 JKc66 anassaadhamad Alicanefee agibalyA2B yousefalbareq-netizen Mohanad1st Calmer26 AliRadwan sarajay19 RawanAljohni'.split())
F=json.load(open('fetched.json')) if os.path.exists('fetched.json') else {}
def get(u):
    try:
        with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=20) as r: return r.read().decode('utf-8','ignore')
    except Exception as e: return 'ERR '+str(e)[:50]
t0=time.time()
for o,rs in C.items():
    if o in EXC or o in F: continue
    if time.time()-t0>150: break
    p=get('https://github.com/'+o)
    nm=re.search(r'itemprop="name">\s*([^<]*?)\s*<',p); bio=re.search(r'data-bio-text="([^"]*)"',p)
    li=sorted(set(re.findall(r'https?://(?:www\.|sa\.)?linkedin\.com/in/[^"\s<&?]+',p)))
    ws=re.search(r'itemprop="url"[^>]*href="([^"]+)"',p)
    rd={}
    seen=set()
    for (n,c,d,f) in rs[:3]:
        if n in seen: continue
        seen.add(n)
        t=get('https://raw.githubusercontent.com/%s/%s/HEAD/README.md'%(o,n))
        rd[n]=t[:2500]
    F[o]={'name':html.unescape(nm.group(1)) if nm else '','bio':html.unescape(bio.group(1)) if bio else '','li':li,'web':ws.group(1) if ws else '','readme':rd}
    json.dump(F,open('fetched.json','w'),ensure_ascii=False)
print(len(F),'of',len([o for o in C if o not in EXC]))

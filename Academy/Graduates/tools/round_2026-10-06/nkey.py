import re,hashlib
def nkey(s):
    s=s.lower(); s=re.sub(r'\b(eng|dr|mr|ms)\.?\s+','',s)
    s=re.sub(r',.*$','',s)              # drop ", PMP" etc
    s=re.sub(r'\bal[\s\-_]+','al',s); s=re.sub(r'[^a-z ]','',s)
    t=s.split()
    if len(t)<2: return None
    f,l=t[0],t[-1]
    f=re.sub(r'(ah|a|h)$','',f); l=re.sub(r'^el','al',l)
    for a,b in (('ou','u'),('oo','u'),('ee','i'),('ei','i'),('y','i'),('ph','f'),('q','k'),('dh','d'),('th','t'),('w','u')):
        f=f.replace(a,b); l=l.replace(a,b)
    f=re.sub(r'(.)\1',r'\1',f); l=re.sub(r'(.)\1',r'\1',l)
    return f+'_'+l
def h(s): return hashlib.sha1(s.encode()).hexdigest()[:6]

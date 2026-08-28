# -*- coding: utf-8 -*-
"""Arabic<->Latin rough transliteration + consonant-skeleton matcher for the
SDAIA Academy graduates DB.  Rebuilt 28 Aug 2026 (was not persisted after the
22 Aug round).  Match rule: first-name match AND >=2 shared skeleton tokens."""
import re, unicodedata, json

AR_MAP = {
 'ا':'a','أ':'a','إ':'a','آ':'a','ٱ':'a','ب':'b','ت':'t','ث':'th','ج':'j','ح':'h',
 'خ':'kh','د':'d','ذ':'th','ر':'r','ز':'z','س':'s','ش':'sh','ص':'s','ض':'d','ط':'t',
 'ظ':'z','ع':'a','غ':'gh','ف':'f','ق':'q','ك':'k','ل':'l','م':'m','ن':'n','ه':'h',
 'و':'w','ي':'y','ى':'a','ة':'h','ء':'','ئ':'y','ؤ':'w','ّ':'','َ':'','ِ':'','ُ':'',
 'ْ':'','ً':'','ٍ':'','ٌ':'','ـ':'',
}
STOP = {'al','el','bin','ben','ibn','abu','abo','bint','the','of','dr','eng','a','abd'}

def ar2lat(s):
    return ''.join(AR_MAP.get(ch, ch) for ch in s)

def _skel(tok):
    t = tok.lower()
    t = re.sub(r'[^a-z]', '', t)
    # digraphs -> single symbol
    for a,b in (('kh','K'),('sh','S'),('th','T'),('gh','G'),('ch','S'),('dh','T'),('ph','f')):
        t = t.replace(a,b)
    t = re.sub(r'[aeiouwy]', '', t)          # drop vowels + semivowels
    t = re.sub(r'(.)\1+', r'\1', t)          # collapse doubles
    return t

def tokens(name):
    if not name: return []
    n = unicodedata.normalize('NFKD', name)
    n = ar2lat(n)
    n = re.sub(r'[^A-Za-z؀-ۿ ]', ' ', n)
    out = []
    for t in n.split():
        t = t.lower()
        t = re.sub(r'^(al|el)-?', '', t)
        if t in STOP or len(t) < 2:
            continue
        sk = _skel(t)
        if sk:
            out.append(sk)
    return out

def key(rec_ar, rec_en=''):
    a = tokens(rec_ar); b = tokens(rec_en)
    return a if len(a) >= len(b) else b

def match(cand_ar, cand_en, idx):
    """idx: list of (id, ar, en, toks). Returns list of (id, ar, en, score)."""
    ct = key(cand_ar, cand_en)
    if not ct: return []
    hits = []
    for rid, ar, en, rt in idx:
        if not rt: continue
        if ct[0] != rt[0]:      # first name must match
            continue
        shared = len(set(ct[1:]) & set(rt[1:]))
        if shared >= 1:
            hits.append((rid, ar, en, shared + 1))
    return sorted(hits, key=lambda x: -x[3])

def build_index(grads):
    return [(i+1, g.get('n',''), g.get('en',''), key(g.get('n',''), g.get('en','')))
            for i, g in enumerate(grads)]

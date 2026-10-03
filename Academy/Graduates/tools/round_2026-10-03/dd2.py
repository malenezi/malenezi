import json,sys
sys.path.insert(0,'..')
import translit as T
I=json.load(open('idx.json',encoding='utf-8'))
idx=[(i,n,en,T.key(n,'')) for i,n,en,p,co in I['names']]
meta={i:(p,co) for i,n,en,p,co in I['names']}
for line in sys.stdin.read().strip().split(';'):
    s,n=line.split('|',1)
    h=T.match('',n,idx)
    print(n,'->',[(r,a,meta[r][0][:30],meta[r][1][:25]) for r,a,e,sc in h[:4]])

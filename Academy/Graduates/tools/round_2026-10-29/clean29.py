# -*- coding: utf-8 -*-
# Cleaning round 29 Oct 2026: correct #26/#29 story wording, reciprocal cross-notes for same-name new records.
import json,re,os,openpyxl
H=os.path.expanduser('~/mnt/Academy/'); TAG='[تنظيف 29 أكتوبر 2026] '
P=H+'Graduates/index.html'; s=open(P,encoding='utf-8').read()
i=s.index('const DATA = ')+13; j=s.index('\nconst SITE_STATS'); D=json.loads(s[i:j].rstrip()[:-1]); g=D['grads']; assert len(g)>0
X=H+'Graduates/Graduates_Database.xlsx'; wb=openpyxl.load_workbook(X); ws=wb['قاعدة البيانات']
def fix(k,old,new):
    assert old in g[k-1]['d'],(k,old[:40]); g[k-1]['d']=g[k-1]['d'].replace(old,new)
    v=ws.cell(k+1,21).value or ''; assert old in v,(k,'xlsx'); ws.cell(k+1,21).value=v.replace(old,new)
def note(k,t):
    g[k-1]['d']=(g[k-1]['d']+' '+TAG+t).strip(); ws.cell(k+1,21).value=((ws.cell(k+1,21).value or '')+' '+TAG+t).strip()
fix(26,'ليست قصة: أدوار شبكات وأنظمة تشغيل غير مرتبطة بعلوم البيانات (§5-و).','لا قصة توظيف إضافية: أدوار شبكات وأنظمة تشغيل غير مرتبطة بعلوم البيانات (§5-و) — وتبقى قصته المنشورة «fares-altoukhi» (مساهمات مفتوحة المصدر) كما هي.')
fix(29,'قد يكون الحساب قد أُغلق أو غيّر معرّفه.','قد يكون الحساب قد أُغلق أو غيّر معرّفه. قصته المنشورة «mohammed-almalki» (مفتوحة المصدر) لا تتأثر، لكن رابط LinkedIn فيها يحتاج تحققًا.')
fix(16,'قصتها منشورة (lena-alenazi).','قصتها المنشورة «lena-alenazi» من فئة الجوائز؛ ودور محللة البيانات في وزارة الاتصالات (مارس 2025) إنجاز توظيفي إضافي يمكن إضافته إلى البطاقة إذا عُرف شهر إتمام معسكر T5.')
for k in (399,3062,3493): note(k,'إشارة: سجل جديد #3926 «رغد العنزي» (رفع الإنتاجية وتحسين العمليات، ~يوليو 2026، حساب LinkedIn raghadalenzi) — برنامج وحساب مختلفان، فلا دمج.')
note(3346,'إشارة: سجل جديد #3927 «لمى العنزي» (رفع الإنتاجية، حساب LinkedIn lama-alanzai) — حساب مختلف عن lama-alanazi28، فهما شخصان مختلفان.')
for r in g: assert '**' not in r['d']
D['grads']=g; open(P,'w',encoding='utf-8').write(s[:i]+json.dumps(D,ensure_ascii=False)+';'+s[j:]); wb.save(X); print('clean ok')

import json,re,sys
sys.path.insert(0,'..')
import translit as TR
s=open('../../index.html',encoding='utf-8').read();i=s.index('const DATA = ')+13;j=s.index('\nconst SITE_STATS');g=json.loads(s[i:j].rstrip()[:-1])['grads']
idx=TR.build_index(g)
C=[('','Abdullah Mohammed Alabdullah'),('','Ibtihal Aloush Alanazi'),('','Maad Ali Almubarak'),('','Fahad Alharbi'),('','Deem Alqudaimi'),('','Shahad Bandar Al Shammari'),('','Fulwah Bin Aqil'),('','Dana Alateeq'),('','Raghad Alamri'),('','Joud Ali Alqhtani'),('','Abdulmajeed Fahad Alshammari'),('','Deemah Alsalamah'),('','Nawaf Almalki'),('','Rana Albarrak'),('','Sarah AlShathri'),('','Nawaf Alzhrani'),('','Arif Alshehri'),('','Remaz Abuarab'),('','Raneem Alsaqat'),('','Hussain Abdullah AlSharari'),('','Abdullah AlRashoudi'),('','Mohanad Alghanim'),('','Asyah Saad Alqahtani'),('','Mishael Fahad AlJubeir'),('','Khalid Almuhanna'),('','Alanoud Sultan Abaalkhail'),('','Fayha Almutairy'),('','Faisal Alkhunain'),('','Norah ALShahrani'),
('الجازي رسام القحطاني','Aljazi Rassam Alqahtani'),('','Munirah Bin Dukhayn'),('سمر علي الصفيري','Samar Ali Alsufairi'),('نايف خالد الصحبي','Naif Khalid Alsahabi'),('اسيل ضيف الله الغامدي','Aseel Dhaifallah Alghamdi'),('','Ruba Alajlan'),('','Essa Alshammari'),('','Rana Kenani'),('مشاعل ناصر العتيبي','Mashael Nasser Alotaibi'),('','Ahmad Bahwarith'),('','Norah Turki')]
for ar,en in C:
    m=TR.match(ar,en,idx)
    ex=[k+1 for k,r in enumerate(g) if (r.get('en') or '').lower().replace(' ','')==en.lower().replace(' ','')]
    print(en,'| ex',ex,'| tr',[(x[0],x[1],x[2],x[3]) for x in m[:3]])

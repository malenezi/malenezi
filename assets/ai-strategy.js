/* AI Strategy executive reference: behaviour only.
   The reading content is already in the HTML (built from data/ai-strategy.json);
   this file adds tabs, filters, the in-page navigation state and the seven working tools.
   Tool entries are kept in this browser's localStorage and never leave it. */
(function(){
'use strict';
var $=function(s,r){return (r||document).querySelector(s)};
var $$=function(s,r){return Array.prototype.slice.call((r||document).querySelectorAll(s))};
function esc(s){return String(s).replace(/[&<>"']/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]})}
var store={get:function(k,d){try{var v=localStorage.getItem('aisx:'+k);return v?JSON.parse(v):d}catch(e){return d}},set:function(k,v){try{localStorage.setItem('aisx:'+k,JSON.stringify(v))}catch(e){}}};
function fmt(n){return (Math.round(n)).toLocaleString('en-US')}
var reduce=window.matchMedia('(prefers-reduced-motion: reduce)').matches;

/* ---------- tabs over pre-rendered panels, with arrow keys ---------- */
var pickers={};
$$('[role=tablist][data-tabs]').forEach(function(host){
  var bs=$$('[role=tab]',host);
  function pick(i,focus){
    bs.forEach(function(b,j){var on=j===i;b.setAttribute('aria-selected',on?'true':'false');b.tabIndex=on?0:-1;
      var p=document.getElementById(b.getAttribute('aria-controls'));if(p)p.classList.toggle('on',on)});
    if(focus)bs[i].focus();
  }
  bs.forEach(function(b,i){
    pickers[b.getAttribute('aria-controls')]=function(){pick(i)};
    b.addEventListener('click',function(){pick(i)});
    b.addEventListener('keydown',function(e){var k=e.key,n=null;
      if(k==='ArrowRight'||k==='ArrowDown')n=(i+1)%bs.length;
      else if(k==='ArrowLeft'||k==='ArrowUp')n=(i-1+bs.length)%bs.length;
      else if(k==='Home')n=0;else if(k==='End')n=bs.length-1;
      if(n!==null){e.preventDefault();pick(n,true)}});
  });
});
/* deep links such as /ai-strategy/#t-prior open the right tab */
function openHash(){var id=location.hash.slice(1);if(id&&pickers[id]){pickers[id]();var el=document.getElementById(id);if(el)el.scrollIntoView()}}
window.addEventListener('hashchange',openHash);

/* ---------- filter chips over pre-rendered items ---------- */
var refK='all';
$$('[data-filter]').forEach(function(host){
  var target=$(host.getAttribute('data-filter'));
  host.addEventListener('click',function(e){var b=e.target.closest('.chip');if(!b)return;
    $$('.chip',host).forEach(function(c){c.setAttribute('aria-pressed',c===b?'true':'false')});
    var k=b.getAttribute('data-k');
    if(target.id==='refList'){refK=k;drawRefs();return}
    $$('[data-k]',target).forEach(function(it){it.hidden=!(k==='all'||it.getAttribute('data-k')===k)});
  });
});
function drawRefs(){var q=$('#refSearch').value.trim().toLowerCase(),n=0;
  $$('#refList li').forEach(function(li){var ok=(refK==='all'||li.getAttribute('data-k')===refK)&&(!q||li.textContent.toLowerCase().indexOf(q)>-1);li.hidden=!ok;if(ok)n++});
  $('#refEmpty').hidden=n>0}
$('#refSearch').addEventListener('input',drawRefs);

/* ---------- hero chart: animate the bars in ---------- */
if(!reduce){var fills=$$('.ax-gap__fill');fills.forEach(function(f){f.dataset.w=f.style.width;f.style.width='0'});
  requestAnimationFrame(function(){setTimeout(function(){fills.forEach(function(f,i){f.style.transitionDelay=(i*0.18)+'s';f.style.width=f.dataset.w})},120)})}

/* ---------- EU AI Act timeline: mark what has passed and what is next ---------- */
(function(){var now=new Date(),next=false;$$('#euTl li').forEach(function(li){var t=$('time',li);
  if(new Date(t.getAttribute('datetime'))<=now)li.className='past';
  else if(!next){next=true;li.className='next';t.insertAdjacentHTML('beforeend',' <span class="ax-tag">next</span>')}})})();

/* ---------- tool: maturity check ---------- */
var DIM=$$('#dims [role=tab]').map(function(b){return b.getAttribute('data-name')});
var A=store.get('assess',DIM.map(function(){return 3}));
if(!Array.isArray(A)||A.length!==DIM.length)A=DIM.map(function(){return 3});
$('#assessRows').innerHTML=DIM.map(function(d,i){return '<div class="ax-rate"><label for="as'+i+'">'+(i+1)+'. '+esc(d)+'</label><input type="range" id="as'+i+'" min="1" max="5" step="1" value="'+A[i]+'" data-i="'+i+'"><output for="as'+i+'">'+A[i]+'</output></div>'}).join('');
function radar(v){var n=v.length,c=150,R=105,pts=[],g='';
  for(var r=1;r<=5;r++){var ring=[];for(var i=0;i<n;i++){var a=-Math.PI/2+i*2*Math.PI/n;ring.push((c+R*r/5*Math.cos(a)).toFixed(1)+','+(c+R*r/5*Math.sin(a)).toFixed(1))}g+='<polygon points="'+ring.join(' ')+'" fill="none" stroke="#e4e0d8"/>'}
  for(var j=0;j<n;j++){var b=-Math.PI/2+j*2*Math.PI/n;pts.push((c+R*v[j]/5*Math.cos(b)).toFixed(1)+','+(c+R*v[j]/5*Math.sin(b)).toFixed(1));
    g+='<text x="'+(c+(R+18)*Math.cos(b)).toFixed(1)+'" y="'+(c+(R+18)*Math.sin(b)+4).toFixed(1)+'" text-anchor="middle" font-size="11" fill="#6b7383">'+(j+1)+'</text>'}
  return '<svg viewBox="0 0 300 300" width="100%" role="img" aria-label="Radar chart of the twelve ratings, numbered in the order listed">'+g+'<polygon points="'+pts.join(' ')+'" fill="rgba(15,86,70,.2)" stroke="#0f5646" stroke-width="2"/></svg>'}
function drawAssess(){var avg=A.reduce(function(a,b){return a+b},0)/A.length;
  var band=avg<2?'Experimenting: activity without shared direction. Fix ownership and ambition first.':avg<3?'Piloting: capabilities exist in pockets. The work now is choosing what to scale.':avg<4?'Scaling: foundations are in place. Focus on workflow redesign and reuse.':'Embedded: AI is part of how the organization runs. Guard against drift and keep measuring.';
  $('#assessScore').textContent=avg.toFixed(1)+' / 5';$('#assessBand').textContent=band;$('#radar').innerHTML=radar(A);
  var idx=A.map(function(v,i){return [v,i]}).sort(function(a,b){return a[0]-b[0]||a[1]-b[1]}).slice(0,3);
  $('#assessWeak').innerHTML=idx.map(function(p){return '<li>'+esc(DIM[p[1]])+' ('+p[0]+')</li>'}).join('');store.set('assess',A)}
$('#assessRows').addEventListener('input',function(e){var t=e.target;if(t.type!=='range')return;A[+t.dataset.i]=+t.value;t.nextElementSibling.textContent=t.value;drawAssess()});
$('#assessReset').addEventListener('click',function(){A=DIM.map(function(){return 3});$$('#assessRows input').forEach(function(r){r.value=3;r.nextElementSibling.textContent=3});drawAssess()});
drawAssess();

/* ---------- tool: use-case prioritizer ---------- */
var CRIT=['Strategic alignment','Financial or public value','Technical feasibility','Data readiness','Simplicity to implement','Adoption readiness','Low risk exposure'];
var DEF={w:[20,20,15,15,10,10,10],c:[{n:'Customer service assistant',s:[5,4,4,4,4,4,4]},{n:'Predictive maintenance',s:[4,5,4,3,3,4,5]},{n:'Enterprise knowledge agent',s:[4,3,4,4,4,5,4]},{n:'Autonomous credit decisions',s:[4,5,3,3,2,2,1]}]};
var P=store.get('prior',null);if(!P||!Array.isArray(P.w)||P.w.length!==7||!Array.isArray(P.c))P=JSON.parse(JSON.stringify(DEF));
function pScore(c){var tw=P.w.reduce(function(a,b){return a+b},0)||1;return c.s.reduce(function(a,v,i){return a+v*P.w[i]},0)/tw}
function pGate(c){return c.s[3]<=2||c.s[6]<=2}
function drawPrior(full){
  if(full){var h='<thead><tr><th scope="col">Use case</th>'+CRIT.map(function(c){return '<th scope="col">'+c+'</th>'}).join('')+'<th scope="col">Score</th><th scope="col"><span class="ax-vh">Remove</span></th></tr><tr><th scope="row">Weight</th>'+P.w.map(function(w,i){return '<td><input type="number" min="0" max="100" value="'+w+'" data-w="'+i+'" aria-label="Weight for '+CRIT[i]+'" style="width:64px"></td>'}).join('')+'<td></td><td></td></tr></thead><tbody>';
    h+=P.c.map(function(c,r){return '<tr><td><input type="text" value="'+esc(c.n)+'" data-n="'+r+'" aria-label="Use case name" style="min-width:190px"></td>'+c.s.map(function(v,i){return '<td><select data-r="'+r+'" data-c="'+i+'" aria-label="'+CRIT[i]+'">'+[1,2,3,4,5].map(function(o){return '<option'+(o===v?' selected':'')+'>'+o+'</option>'}).join('')+'</select></td>'}).join('')+'<td class="sc" data-s="'+r+'"></td><td><button type="button" class="ax-x" data-x="'+r+'" aria-label="Remove '+esc(c.n)+'">×</button></td></tr>'}).join('');
    $('#priorTable').innerHTML='<caption class="ax-vh">Use-case prioritization</caption>'+h+'</tbody>'}
  P.c.forEach(function(c,r){var td=$('[data-s="'+r+'"]');if(td)td.textContent=pScore(c).toFixed(2)});
  var tw=P.w.reduce(function(a,b){return a+b},0);$('#priorWeightNote').textContent='Weights total '+tw+(tw===100?'.':'. Scores are normalized, so they need not sum to 100.');
  var rank=P.c.map(function(c){return {n:c.n,v:pScore(c),g:pGate(c)}}).sort(function(a,b){return b.v-a.v});
  $('#priorRank').innerHTML=rank.length?rank.map(function(r){var dec=r.g?['caution','Hold: fix data or risk first']:r.v>=4?['good','Fund now']:r.v>=3?['','Develop the case']:['caution','Park'];
    return '<div class="ax-rate rank"><span>'+esc(r.n)+' <span class="ax-tag '+dec[0]+'">'+dec[1]+'</span></span><span class="ax-meter" style="margin:0"><i style="width:'+(r.v/5*100).toFixed(0)+'%"></i></span><output>'+r.v.toFixed(2)+'</output></div>'}).join(''):'<p class="ax-note">No use cases yet. Add one to start ranking.</p>';
  store.set('prior',P)}
$('#priorTable').addEventListener('input',function(e){var t=e.target;
  if(t.dataset.w!==undefined){P.w[+t.dataset.w]=Math.max(0,+t.value||0)}
  else if(t.dataset.n!==undefined){P.c[+t.dataset.n].n=t.value}
  else if(t.dataset.r!==undefined){P.c[+t.dataset.r].s[+t.dataset.c]=+t.value}
  drawPrior(false)});
$('#priorTable').addEventListener('click',function(e){var b=e.target.closest('[data-x]');if(b){P.c.splice(+b.dataset.x,1);drawPrior(true)}});
$('#priorAdd').addEventListener('click',function(){P.c.push({n:'New use case',s:[3,3,3,3,3,3,3]});drawPrior(true);var ins=$$('#priorTable input[type=text]');var last=ins[ins.length-1];last.focus();last.select()});
$('#priorReset').addEventListener('click',function(){P=JSON.parse(JSON.stringify(DEF));drawPrior(true)});
$('#priorCsv').addEventListener('click',function(){var q=function(s){return '"'+String(s).replace(/"/g,'""')+'"'};
  var rows=[['Use case'].concat(CRIT).concat(['Score','Gate']).map(q).join(',')];rows.push([q('Weight')].concat(P.w).join(','));
  P.c.forEach(function(c){rows.push([q(c.n)].concat(c.s).concat([pScore(c).toFixed(2),pGate(c)?'Hold':'']).join(','))});
  var a=document.createElement('a');a.href=URL.createObjectURL(new Blob([rows.join('\n')],{type:'text/csv'}));a.download='ai-use-case-priorities.csv';document.body.appendChild(a);a.click();a.remove()});
drawPrior(true);

/* ---------- tool: business case ---------- */
var BROWS=[['build','Build and implementation'],['run','Run: infrastructure, models, support'],['change','Change and training'],['ben','Gross benefits']];
var BDEF={build:[1200,300,100],run:[200,350,400],change:[300,150,100],ben:[600,2200,3200]};
var B=store.get('bc',null);if(!B||!B.ben||!B.build||!B.run||!B.change)B=JSON.parse(JSON.stringify(BDEF));
$('#bcTable').innerHTML='<caption class="ax-vh">Business case inputs</caption><thead><tr><th scope="col">Thousands</th><th scope="col">Year 1</th><th scope="col">Year 2</th><th scope="col">Year 3</th></tr></thead><tbody>'+BROWS.map(function(r){return '<tr><th scope="row">'+r[1]+'</th>'+[0,1,2].map(function(y){return '<td><input type="number" min="0" step="50" value="'+B[r[0]][y]+'" data-k="'+r[0]+'" data-y="'+y+'" aria-label="'+r[1]+', year '+(y+1)+'"></td>'}).join('')+'</tr>'}).join('')+'<tr><th scope="row">Net value after realization</th><td id="bcN0"></td><td id="bcN1"></td><td id="bcN2"></td></tr></tbody>';
function drawBC(){var real=Math.min(100,Math.max(0,+$('#bcReal').value||0))/100,rate=Math.max(0,+$('#bcRate').value||0)/100,net=[],cum=0,pay=null,tb=0,tc=0,npv=0;
  for(var y=0;y<3;y++){var c=B.build[y]+B.run[y]+B.change[y],b=B.ben[y]*real;tb+=b;tc+=c;net[y]=b-c;cum+=net[y];if(pay===null&&cum>=0)pay=y+1;npv+=net[y]/Math.pow(1+rate,y+1);$('#bcN'+y).textContent=fmt(net[y])}
  var roi=tc?((tb-tc)/tc*100):0;
  $('#bcKpis').innerHTML=[[fmt(tb-tc),'Three-year net value'],[roi.toFixed(0)+'%','Return on investment'],[fmt(npv),'Net present value'],[pay?'Year '+pay:'Beyond year 3','Payback']].map(function(k){return '<div class="ax-kpi"><b>'+k[0]+'</b><span>'+k[1]+'</span></div>'}).join('');
  var mx=Math.max.apply(null,net.map(Math.abs).concat([1])),bars='';
  net.forEach(function(v,i){var h=Math.abs(v)/mx*70,x=60+i*130;bars+='<rect x="'+x+'" y="'+(v>=0?90-h:90)+'" width="70" height="'+h.toFixed(1)+'" rx="4" fill="'+(v>=0?'#1f7a55':'#a94d16')+'"/><text x="'+(x+35)+'" y="186" text-anchor="middle" font-size="12" fill="#6b7383">Year '+(i+1)+'</text><text x="'+(x+35)+'" y="'+(v>=0?90-h-6:90+h+14).toFixed(1)+'" text-anchor="middle" font-size="12" fill="#15181d">'+fmt(v)+'</text>'});
  $('#bcChart').innerHTML='<svg viewBox="0 0 460 195" style="max-width:520px;width:100%" role="img" aria-label="Net value by year: '+net.map(function(v,i){return 'year '+(i+1)+' '+fmt(v)}).join(', ')+'"><line x1="30" x2="440" y1="90" y2="90" stroke="#6b7383"/>'+bars+'</svg>';
  store.set('bc',B)}
$('#bcTable').addEventListener('input',function(e){var t=e.target;if(t.dataset.k){B[t.dataset.k][+t.dataset.y]=Math.max(0,+t.value||0);drawBC()}});
$('#bcReal').addEventListener('input',drawBC);$('#bcRate').addEventListener('input',drawBC);drawBC();

/* ---------- tool: build, buy or partner ---------- */
var SQ=[
 ['Does this capability set you apart from competitors or peers?',[['It is a core differentiator',{build:3,partner:1}],['Important, but others have it too',{buy:2,partner:1,orch:1}],['It is a commodity',{buy:3}]]],
 ['Are there mature products on the market?',[['Yes, several',{buy:3}],['Emerging, not yet proven',{partner:2,orch:1,build:1}],['No',{build:3,partner:1}]]],
 ['Do you have the people to build and run it?',[['Yes, a strong team',{build:2,orch:1}],['Partly',{partner:2,orch:1}],['Very few',{buy:2,partner:1}]]],
 ['Does it depend on proprietary or sensitive data?',[['Heavily',{build:2,orch:1}],['To some extent',{orch:1,partner:1}],['No',{buy:1}]]],
 ['How many models, vendors and systems must it span?',[['One',{buy:1}],['A few',{orch:2}],['Many',{orch:3}]]]
];
var SOPT={build:['Build','Develop it in-house. Justified when the capability is a source of advantage and you can staff and run it for years, not just deliver it once.'],buy:['Buy','Adopt a product. Fastest to value for common capabilities. Negotiate data ownership, exit terms and price protection before signing.'],partner:['Partner','Co-develop with a specialist. Use it to gain expertise or access you lack, with an explicit plan to transfer capability inward.'],orch:['Orchestrate','Combine several providers behind your own integration and control layer. You own the architecture, evaluation and governance; the components are replaceable.']};
$('#srcForm').innerHTML=SQ.map(function(q,i){return '<fieldset><legend>'+q[0]+'</legend>'+q[1].map(function(o,j){return '<label><input type="radio" name="sq'+i+'" value="'+j+'"> '+o[0]+'</label>'}).join('')+'</fieldset>'}).join('');
function drawSrc(){var sc={build:0,buy:0,partner:0,orch:0},n=0;
  SQ.forEach(function(q,i){var c=$('input[name=sq'+i+']:checked');if(c){n++;var add=q[1][+c.value][1];Object.keys(add).forEach(function(k){sc[k]+=add[k]})}});
  if(n<SQ.length){$('#srcResult').innerHTML='<h4 class="ax-sub-h" style="margin-top:0">Answer all five questions</h4><p class="ax-note" style="margin-top:8px">'+n+' of '+SQ.length+' answered.</p>';return}
  var order=Object.keys(sc).sort(function(a,b){return sc[b]-sc[a]}),top=order[0],second=order[1];
  $('#srcResult').innerHTML='<p class="ax-note" style="margin:0">Starting position</p><div class="ax-big" style="margin:4px 0 12px">'+SOPT[top][0]+'</div><p>'+SOPT[top][1]+'</p>'+(sc[top]-sc[second]<=1?'<p class="ax-note">Close call with <b>'+SOPT[second][0].toLowerCase()+'</b>. Cost both options.</p>':'')+'<h4>Test it against</h4><ul class="ax-ul" style="margin-bottom:0"><li>Three-year total cost of ownership</li><li>Time to first production use</li><li>Data ownership and portability</li><li>Dependence on one vendor</li><li>Security and regulatory requirements</li></ul>'}
$('#srcForm').addEventListener('change',drawSrc);drawSrc();

/* ---------- tool: governance ---------- */
var GQ=['Who approves a new AI use case?','Who owns the business outcome?','Who is accountable for the data?','Who validates models and outputs?','Who accepts residual risk?','Who monitors deployed systems?','Who can suspend or retire a system?'];
var G=store.get('gov',{o:[],a:[]});if(!G||!Array.isArray(G.o)||!Array.isArray(G.a))G={o:[],a:[]};
$('#govTable').innerHTML='<caption class="ax-vh">Decision rights</caption><thead><tr><th scope="col">Decision</th><th scope="col">Named owner</th></tr></thead><tbody>'+GQ.map(function(q,i){return '<tr><td><label for="go'+i+'">'+q+'</label></td><td><input type="text" id="go'+i+'" data-g="'+i+'" value="'+esc(G.o[i]||'')+'" placeholder="Role or name"></td></tr>'}).join('')+'</tbody>';
$('#govTable').addEventListener('input',function(e){if(e.target.dataset.g!==undefined){G.o[+e.target.dataset.g]=e.target.value;store.set('gov',G)}});
var AC=[['Agent identity','Every agent has its own identity and credentials, separate from any person’s.'],['Scoped tool permissions','Each agent can reach only the tools and data its task needs.'],['Action authorization','Defined classes of action require approval before they execute.'],['Human approval points','A person signs off on irreversible or high-impact steps.'],['Transaction limits','Hard caps on value, volume and frequency.'],['Audit trail','Every action, input and decision is logged and attributable.'],['Emergency stop','A named person can halt an agent immediately, and the stop has been tested.']];
$('#agentChecks').innerHTML=AC.map(function(c,i){return '<div class="ax-check"><input type="checkbox" id="ac'+i+'" data-a="'+i+'"'+(G.a[i]?' checked':'')+'><label for="ac'+i+'"><b>'+c[0]+'</b><span>'+c[1]+'</span></label></div>'}).join('');
function drawAgent(){var n=AC.filter(function(c,i){return G.a[i]}).length;$('#agentMeter').style.width=(n/AC.length*100)+'%';$('#agentNote').textContent=n+' of '+AC.length+' controls in place.'+(n<AC.length?' Agents should not act autonomously in production until all seven are.':' Keep testing them.')}
$('#agentChecks').addEventListener('change',function(e){if(e.target.dataset.a!==undefined){G.a[+e.target.dataset.a]=e.target.checked;store.set('gov',G);drawAgent()}});drawAgent();

/* ---------- tool: board decisions ---------- */
var DEC=[['Strategic ambition','Are we optimizing, transforming, or creating new businesses?'],['Value ownership','Which executives own the expected benefits?'],['Portfolio choices','Which ten to twenty use cases get investment first?'],['Operating model','Who builds, owns and operates AI?'],['Data foundation','Do we have the data the priority use cases need?'],['Technology strategy','What do we build, buy or partner for?'],['Governance','What may AI decide on its own, and what may it not?'],['Workforce','How will jobs, roles and skills change?'],['Investment','What is the total three-year commitment?'],['Performance','How will the board know AI is delivering value?']];
var D=store.get('dec',[]);if(!Array.isArray(D))D=[];
$('#decList').innerHTML=DEC.map(function(d,i){return '<div class="ax-check"><input type="checkbox" id="dc'+i+'" data-d="'+i+'"'+(D[i]?' checked':'')+'><label for="dc'+i+'"><b>'+d[0]+'</b><span>'+d[1]+'</span></label></div>'}).join('');
function drawDec(){var n=DEC.filter(function(d,i){return D[i]}).length;$('#decMeter').style.width=(n*10)+'%';$('#decNote').textContent=n+' of 10 settled.'+(n===10?' Ready for an investment decision.':' Do not approve the program until an accountable owner, a prioritized portfolio, an investment model and measurable outcomes are all in place.')}
$('#decList').addEventListener('change',function(e){if(e.target.dataset.d!==undefined){D[+e.target.dataset.d]=e.target.checked;store.set('dec',D);drawDec()}});drawDec();

/* ---------- tool: strategy canvas ---------- */
var CV=[['Ambition','Where AI takes us in three years'],['Value pools','The problems worth solving'],['How we win','What will be hard to copy'],['Now: 0 to 6 months','Low risk, proven value'],['Next: 6 to 18 months','Workflow redesign'],['Later: 18 to 36 months','New products and models'],['Data','What we need and who owns it'],['People','Skills, roles and leadership'],['Technology','Build, buy, partner'],['Governance','Who decides and how we control'],['Risks','What could go wrong'],['Measures','How the board will know']];
var C=store.get('canvas',[]);if(!Array.isArray(C))C=[];
$('#canvas').innerHTML=CV.map(function(c,i){return '<label>'+c[0]+'<small>'+c[1]+'</small><textarea data-v="'+i+'" rows="3">'+esc(C[i]||'')+'</textarea></label>'}).join('');
function say(m){$('#cvStatus').textContent=m;setTimeout(function(){$('#cvStatus').textContent=''},2500)}
$('#canvas').addEventListener('input',function(e){if(e.target.dataset.v!==undefined){C[+e.target.dataset.v]=e.target.value;store.set('canvas',C)}});
$('#cvCopy').addEventListener('click',function(){var txt=CV.map(function(c,i){return c[0].toUpperCase()+'\n'+(C[i]||'(empty)')}).join('\n\n');
  function fallback(){var ta=document.createElement('textarea');ta.value=txt;document.body.appendChild(ta);ta.select();var ok=false;try{ok=document.execCommand('copy')}catch(e){}ta.remove();say(ok?'Copied':'Copy is blocked in this browser. Select the text and copy it manually.')}
  if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(txt).then(function(){say('Copied')},fallback)}else fallback()});
$('#cvPrint').addEventListener('click',function(){window.print()});
$('#cvClear').addEventListener('click',function(){C=[];$$('#canvas textarea').forEach(function(t){t.value=''});store.set('canvas',C);say('Canvas cleared')});

/* ---------- in-page navigation state and reading progress ---------- */
var links=$$('#ax-toc a'),secs=links.map(function(a){return $(a.getAttribute('href'))}),ul=$('#ax-toc'),bar=$('#ax-progress');
var last=-2,tick=false;
function onScroll(){tick=false;var h=document.documentElement,max=h.scrollHeight-h.clientHeight;bar.style.width=(max>0?h.scrollTop/max*100:0)+'%';
  var cur=-1;secs.forEach(function(s,i){if(s.getBoundingClientRect().top<=150)cur=i});
  if(cur!==last){last=cur;links.forEach(function(a,i){if(i===cur)a.setAttribute('aria-current','true');else a.removeAttribute('aria-current')});
    if(cur>=0&&ul.scrollWidth>ul.clientWidth)ul.scrollLeft=links[cur].parentNode.offsetLeft-ul.offsetLeft-16}}
window.addEventListener('scroll',function(){if(!tick){tick=true;requestAnimationFrame(onScroll)}},{passive:true});onScroll();
openHash();
})();

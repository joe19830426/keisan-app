# -*- coding: utf-8 -*-
"""算数 朝学習プリント自動生成（Streamlit版）
起動:  pip install streamlit  →  streamlit run app.py
外部APIは不要。問題生成ロジックはすべて下のHTML(JavaScript)内で動きます。
"""
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="算数 朝学習プリント", page_icon="📐", layout="wide")
st.markdown("<style>.block-container{padding:0.5rem 0.5rem 0}header{visibility:hidden}</style>", unsafe_allow_html=True)

APP_HTML = r'''
<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>算数 朝学習プリント自動生成</title>
<script src="https://cdn.tailwindcss.com"></script>
<style>
body{font-family:"BIZ UDPGothic","Hiragino Kaku Gothic ProN","Yu Gothic","Meiryo",sans-serif}
/* ===== A4シート ===== */
.sheet{width:210mm;height:297mm;padding:11mm 13mm 8mm;box-sizing:border-box;background:#fff;color:#111;
  --k:1;--fs:1;font-size:calc(12.5pt*var(--fs));line-height:1.55;position:relative;overflow:hidden;
  display:flex;flex-direction:column;box-shadow:0 2px 12px rgba(0,0,0,.25);transform-origin:top left}
.sheet>*{flex-shrink:0}
.hd{border-bottom:2.5px solid #111;padding-bottom:2mm;margin-bottom:3mm}
.hd .top{display:flex;align-items:center;gap:4mm}
.hd h1{font-size:1.5em;font-weight:800;letter-spacing:.05em;margin:0}
.hd .gr{border:2px solid #111;border-radius:999px;padding:0 3.5mm;font-weight:700;font-size:.95em}
.hd .units{font-size:.68em;color:#444;margin-left:auto;text-align:right;max-width:80mm;line-height:1.3}
.hd .fields{display:flex;gap:5mm;margin-top:2.5mm;font-size:.85em;align-items:flex-end}
.hd .fld{display:flex;align-items:flex-end;gap:1.5mm}
.hd .ln{display:inline-block;border-bottom:1.3px solid #111;min-width:18mm;height:1.3em;text-align:center}
.hd .score{margin-left:auto;border:2px solid #111;border-radius:3mm;padding:.2mm 4mm;min-width:26mm;text-align:right}
.sec{font-weight:800;font-size:.85em;background:#111;color:#fff;display:inline-block;padding:0 3mm;border-radius:1mm;margin:1.5mm 0 1.5mm}
.grid{display:grid;grid-template-columns:1fr 1fr;column-gap:8mm}
.pb{break-inside:avoid;margin-bottom:.5mm}
.pb.word,.pb.apply{grid-column:1/-1}
.qt{display:flex;gap:2mm;align-items:baseline}
.no{font-weight:800;font-size:1.05em;min-width:1.4em}
.qx{flex:1}
.sp{position:relative;margin:1mm 0 2.5mm;border:1px dashed #aaa;border-radius:1.5mm;
  background-image:radial-gradient(circle,#8a8a8a .7px,transparent .85px);background-size:5mm 5mm;background-position:2.5mm 2.5mm}
.s1{height:calc(9mm*var(--k))}.s2{height:calc(21mm*var(--k))}.s3{height:calc(30mm*var(--k))}
.blank{position:relative;display:inline-block;min-width:4.2em;height:1.15em;border-bottom:1.5px solid #111;margin:0 .25em;vertical-align:baseline}
.blank i{position:absolute;left:.3em;bottom:1px;font-style:normal;color:#d40000;font-weight:700;white-space:nowrap;display:none}
.al{text-align:right;margin-top:1mm}
.ex{display:none;position:absolute;right:2mm;top:.5mm;font-size:8.5pt;color:#d40000;background:rgba(255,255,255,.85);padding:0 1mm}
.show-ans .blank i{display:inline}.show-ans .ex{display:block}
.ft{margin-top:auto;font-size:7.5pt;color:#666;text-align:right;border-top:1px solid #ccc;padding-top:1mm}
.fr{display:inline-flex;flex-direction:column;align-items:center;vertical-align:middle;line-height:1.15;margin:0 .15em;font-size:.95em}
.fr>span:first-child{border-bottom:1.5px solid currentColor;padding:0 .25em}
.empty{padding:30mm 0;text-align:center;color:#888}
/* ===== 印刷 ===== */
@media print{
  @page{size:A4 portrait;margin:0}
  html,body{background:#fff!important}
  .noprint{display:none!important}
  main{padding:0!important}
  #holder{width:auto!important;height:auto!important}
  #sheet{transform:none!important;box-shadow:none!important;height:296mm}
  *{-webkit-print-color-adjust:exact;print-color-adjust:exact}
}
</style>
</head>
<body class="bg-slate-100 text-slate-800">
<div class="flex flex-col lg:flex-row min-h-screen">
 <!-- ===== 設定パネル ===== -->
 <aside class="noprint w-full lg:w-80 lg:h-screen lg:sticky lg:top-0 lg:overflow-y-auto bg-white border-b lg:border-r border-slate-300 p-4 space-y-4 shrink-0">
  <h1 class="text-lg font-bold">📐 算数プリント生成</h1>
  <div class="grid grid-cols-2 gap-2">
   <label class="text-sm">教科書会社
    <select id="pub" class="mt-1 w-full border rounded p-1.5 text-sm">
     <option>東京書籍</option><option>学校図書</option><option>啓林館</option><option>教育出版</option><option>大日本図書</option><option>日本文教出版</option><option>指定なし</option>
    </select></label>
   <label class="text-sm">学年
    <select id="grade" class="mt-1 w-full border rounded p-1.5 text-sm">
     <option value="1">小1</option><option value="2">小2</option><option value="3">小3</option><option value="4" selected>小4</option><option value="5">小5</option><option value="6">小6</option>
    </select></label>
  </div>
  <div>
   <div class="flex items-center justify-between text-sm"><span class="font-semibold">単元（複数選択可）</span>
    <span><button id="allOn" class="text-blue-600 underline text-xs">全選択</button> <button id="allOff" class="text-blue-600 underline text-xs ml-1">解除</button></span></div>
   <div id="units" class="mt-1 space-y-1 text-sm"></div>
  </div>
  <div>
   <label class="text-sm font-semibold">問題数：<span id="nv">10</span>問</label>
   <input id="n" type="range" min="1" max="20" value="10" class="w-full">
   <div id="mix" class="text-xs text-slate-500"></div>
  </div>
  <div class="text-sm">
   <div class="font-semibold mb-1">出題モード</div>
   <label class="mr-3"><input type="radio" name="mode" value="random" checked> ランダム問題</label>
   <label><input type="radio" name="mode" value="fixed"> 定番の固定問題</label>
  </div>
  <div class="space-y-2 text-sm">
   <label class="block">タイトル<input id="title" class="mt-1 w-full border rounded p-1.5" value="算数 朝のプリント"></label>
   <label class="block">学校名（空欄なら記入欄）<input id="school" class="mt-1 w-full border rounded p-1.5" placeholder="例：〇〇小学校"></label>
   <label class="block"><input id="date" type="checkbox" checked> 日付欄を入れる</label>
   <label class="block"><input id="score" type="checkbox" checked> 得点欄を入れる</label>
  </div>
  <div class="space-y-2">
   <button id="shuffle" class="w-full bg-emerald-600 hover:bg-emerald-700 disabled:opacity-40 text-white rounded py-2 font-semibold">🔀 問題を再シャッフル</button>
   <button id="ans" class="w-full bg-amber-500 hover:bg-amber-600 text-white rounded py-2 font-semibold">✅ 解答・解説を表示</button>
   <button id="print" class="w-full bg-blue-600 hover:bg-blue-700 text-white rounded py-2 font-semibold">🖨 印刷 / PDF保存</button>
   <p class="text-xs text-slate-500">印刷ダイアログで「A4・縦・余白なし（なし）・ヘッダーとフッター OFF」を選んでください。</p>
  </div>
 </aside>
 <!-- ===== プレビュー ===== -->
 <main class="flex-1 p-3 lg:p-6 overflow-auto">
  <div id="holder" style="margin:0 auto"><div id="sheet" class="sheet"></div></div>
 </main>
</div>

<script>
/* ========== ユーティリティ ========== */
const $=s=>document.querySelector(s);
const mul32=a=>()=>{a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296};
const hash=s=>{let h=2166136261;for(const c of String(s)){h^=c.charCodeAt(0);h=Math.imul(h,16777619)}return h>>>0};
const ri=(r,a,b)=>a+Math.floor(r()*(b-a+1));
const pk=(r,arr)=>arr[Math.floor(r()*arr.length)];
const gcd=(a,b)=>b?gcd(b,a%b):a;
const lcm=(a,b)=>a/gcd(a,b)*b;
const fr=(n,d)=>`<span class="fr"><span>${n}</span><span>${d}</span></span>`;
const mx=(n,d)=>{const w=Math.floor(n/d),m=n%d;return m?(w?w:'')+fr(m,d):''+w};            // 帯分数（約分しない）
const fa=(n,d)=>{const g=gcd(n,d);n/=g;d/=g;return d==1?''+n:mx(n,d)};                    // 約分した答え
const num=x=>String(+x.toFixed(6));
const d1=x=>(x/10).toFixed(1);
const cma=n=>n.toLocaleString('en-US');
const NM=['たろう','はな','けんた','ゆい','そうた','みさき','りく','あおい','だいき','ひなた','さくら','ゆうと'];
const IT=[['りんご','こ'],['みかん','こ'],['えんぴつ','ほん'],['シール','まい'],['あめ','こ'],['おり紙','まい'],['クッキー','まい'],['ビー玉','こ']];
const GD=['ノート','パン','ジュース','けしゴム','おにぎり'];
const who=r=>pk(r,NM)+'さん', item=r=>pk(r,IT);
const Q=(q,a,e,sp=1)=>({q,a,e,sp});
const tstr=m=>{const h=Math.floor(m/60),mm=m%60;return `${h<12?'午前':'午後'}${h%12?h%12:12}時${mm}分`};

/* ========== 文章題ヘルパー ========== */
const W={
 add:(lo,hi)=>r=>{const n=who(r),[t,u]=item(r),a=ri(r,lo,hi),b=ri(r,lo,hi);return{q:`${n}は ${t}を ${a}${u} もっています。${b}${u} もらいました。ぜんぶで いくつに なりましたか。`,a:`${a+b} ${u}`,e:`${a}＋${b}＝${a+b}`}},
 sub:(lo,hi)=>r=>{const n=who(r),[t,u]=item(r),a=ri(r,lo,hi),b=ri(r,1,a-1);return{q:`${n}は ${t}を ${a}${u} もっています。${b}${u} つかいました。のこりは いくつですか。`,a:`${a-b} ${u}`,e:`${a}－${b}＝${a-b}`}},
 two:(lo,hi)=>r=>{const n=who(r),[t,u]=item(r),a=ri(r,lo,hi),b=ri(r,lo,hi),c=ri(r,1,Math.min(a+b-1,hi));return{q:`${n}は ${t}を ${a}${u} もっています。${b}${u} もらってから、${c}${u} あげました。のこりは いくつですか。`,a:`${a+b-c} ${u}`,e:`${a}＋${b}－${c}＝${a+b-c}`}},
 mul:(lo,hi)=>r=>{const n=who(r),[t,u]=item(r),a=ri(r,lo,hi),b=ri(r,lo,hi);return{q:`${n}は ${a}人の ともだちに ${t}を ${b}${u}ずつ くばります。${t}は ぜんぶで いくつ いりますか。`,a:`${a*b} ${u}`,e:`${b}×${a}＝${a*b}`}},
 div:(lo,hi)=>r=>{const [t,u]=item(r),a=ri(r,lo,hi),b=ri(r,lo,hi);return{q:`${t}が ${a*b}${u} あります。${a}人で おなじ数ずつ わけると、1人ぶんは いくつですか。`,a:`${b} ${u}`,e:`${a*b}÷${a}＝${b}`}},
 divr:r=>{const [t,u]=item(r),b=ri(r,2,9),k=ri(r,2,9),m=ri(r,1,b-1),N=b*k+m;return{q:`${t}が ${N}${u} あります。1人に ${b}${u}ずつ くばると、なん人に くばれて、いくつ あまりますか。`,a:`${k}人、${m}${u} あまる`,e:`${N}÷${b}＝${k}あまり${m}`}}
};

/* ========== 単元データ（学習指導要領 算数科の系統に基づく） ========== */
const UNITS=[];
const U=(id,g,name,b,w,a)=>UNITS.push({id,g,name,b,w,a});

/* ---- 小1 ---- */
U('1a',1,'たし算（10までの数）',r=>{const a=ri(r,1,9),b=ri(r,1,10-a);return Q(`${a} ＋ ${b} ＝ §`,a+b,`${a}＋${b}＝${a+b}`)},W.add(1,5),W.two(3,9));
U('1b',1,'ひき算（10までの数）',r=>{const a=ri(r,2,10),b=ri(r,1,a-1);return Q(`${a} － ${b} ＝ §`,a-b,`${a}－${b}＝${a-b}`)},W.sub(5,10),W.two(2,8));
U('1c',1,'くり上がりのあるたし算',r=>{const a=ri(r,2,9),b=ri(r,Math.max(2,11-a),9);return Q(`${a} ＋ ${b} ＝ §`,a+b,`${a}＋${b}＝10＋${a+b-10}＝${a+b}`)},W.add(6,9),W.two(6,12));
U('1d',1,'くり下がりのあるひき算',r=>{const a=ri(r,11,18),b=ri(r,a%10+1,9);return Q(`${a} － ${b} ＝ §`,a-b,`${a}－${b}＝${a-b}`)},W.sub(11,18),W.two(8,14));
U('1e',1,'100までの数',r=>{if(r()<.5){const o=ri(r,0,8),a=ri(r,1,9)*10+o,b=ri(r,1,9-o);return Q(`${a} ＋ ${b} ＝ §`,a+b,`${a}＋${b}＝${a+b}`)}const a=ri(r,2,9)*10+ri(r,1,9),b=ri(r,1,a%10);return Q(`${a} － ${b} ＝ §`,a-b,`${a}－${b}＝${a-b}`)},W.add(10,45),W.two(20,50));

/* ---- 小2 ---- */
U('2a',2,'たし算の筆算',r=>{const a=r()<.5?ri(r,11,99):ri(r,100,899),b=ri(r,11,99);return Q(`${a} ＋ ${b} ＝ §`,a+b,`${a}＋${b}＝${a+b}`,2)},W.add(20,99),W.two(30,99));
U('2b',2,'ひき算の筆算',r=>{const a=r()<.5?ri(r,30,99):ri(r,100,999),b=ri(r,11,Math.min(99,a-1));return Q(`${a} － ${b} ＝ §`,a-b,`${a}－${b}＝${a-b}`,2)},W.sub(30,150),W.two(50,120));
U('2c',2,'かけ算（九九）',r=>{const a=ri(r,2,9),b=ri(r,2,9);return Q(`${a} × ${b} ＝ §`,a*b,`${a}×${b}＝${a*b}`)},W.mul(2,9),r=>{const [t,u]=item(r),a=ri(r,3,9),b=ri(r,2,9),c=ri(r,1,b-1);return{q:`${a}人に ${t}を ${b}${u}ずつ くばったら、${c}${u} あまりました。はじめに ${t}は いくつ ありましたか。`,a:`${a*b+c} ${u}`,e:`${a}×${b}＋${c}＝${a*b+c}`}});
U('2d',2,'長さ（cm・mm）',r=>{if(r()<.5){const a=ri(r,1,9),b=ri(r,1,9);return Q(`${a}cm ${b}mm ＝ § mm`,a*10+b,`${a}cm＝${a*10}mm → ${a*10}＋${b}`)}const x=ri(r,10,50),y=ri(r,10,50);return Q(`${x}cm ＋ ${y}cm ＝ § cm`,x+y,`${x}＋${y}＝${x+y}`)},
  r=>{const n=who(r),a=ri(r,20,60),b=ri(r,1,a-1);return{q:`${n}は ${a}cmの テープから ${b}cm きりとりました。のこりは なんcmですか。`,a:`${a-b} cm`,e:`${a}－${b}＝${a-b}`}},
  r=>{const x=ri(r,2,9),y=ri(r,3,9),z=ri(r,2,9),w=ri(r,3,9),t=(x+z)*10+y+w;return{q:`${x}cm ${y}mm の テープと ${z}cm ${w}mm の テープを つなぎます。ぜんぶで なんcm なんmm ですか。`,a:`${Math.floor(t/10)}cm ${t%10}mm`,e:`mmに そろえて ${x*10+y}＋${z*10+w}＝${t}mm`}});
U('2e',2,'かさ（L・dL・mL）',r=>{if(r()<.5){const a=ri(r,1,9),b=ri(r,1,9);return Q(`${a}L ${b}dL ＝ § dL`,a*10+b,`1L＝10dL だから ${a*10}＋${b}`)}const a=ri(r,1,9);return Q(`${a}L ＝ § mL`,a*1000,`1L＝1000mL`)},
  r=>{const a=ri(r,1,5),b=ri(r,1,9),c=ri(r,2,9);return{q:`水が ${a}L ${b}dL あります。${c}dL つぎたしました。あわせて なんdL に なりましたか。`,a:`${a*10+b+c} dL`,e:`${a}L${b}dL＝${a*10+b}dL → ＋${c}`}},
  r=>{const a=ri(r,1,4),b=pk(r,[2,5]);return{q:`${a}Lの ジュースを 1人に ${b}dLずつ くばります。なん人に くばれますか。`,a:`${a*10/b} 人`,e:`${a}L＝${a*10}dL → ${a*10}÷${b}`}});

/* ---- 小3 ---- */
U('3a',3,'かけ算の筆算',r=>{const a=r()<.6?ri(r,12,99):ri(r,100,399),b=ri(r,2,9);return Q(`${a} × ${b} ＝ §`,a*b,`${a}×${b}＝${a*b}`,2)},
  r=>{const t=pk(r,GD),a=ri(r,12,99),b=ri(r,2,9);return{q:`1こ ${a}円の ${t}を ${b}こ かいます。だい金は いくらですか。`,a:`${a*b} 円`,e:`${a}×${b}＝${a*b}`}},
  r=>{const n=who(r),t=pk(r,GD),a=ri(r,30,120),b=ri(r,2,6),c=a*b,p=Math.ceil((c+1)/100)*100;return{q:`${n}は ${p}円を もって、1こ ${a}円の ${t}を ${b}こ かいました。おつりは いくらですか。`,a:`${p-c} 円`,e:`${a}×${b}＝${c}、${p}－${c}＝${p-c}`}});
U('3b',3,'わり算',r=>{const b=ri(r,2,9),k=ri(r,2,9);if(r()<.5)return Q(`${b*k} ÷ ${b} ＝ §`,k,`${b}×${k}＝${b*k}`);const m=ri(r,1,b-1);return Q(`${b*k+m} ÷ ${b} ＝ §`,`${k} あまり ${m}`,`${b}×${k}＝${b*k}、${b*k+m}－${b*k}＝${m}`)},
  r=>(r()<.5?W.div(2,9):W.divr)(r),
  r=>{const b=ri(r,3,8),k=ri(r,3,9),m=ri(r,1,b-1),N=b*k+m;return{q:`${N}人が 1きゃく ${b}人がけの 長いすに すわります。みんなが すわるには 長いすは なんきゃく いりますか。`,a:`${k+1} きゃく`,e:`${N}÷${b}＝${k}あまり${m} → あまりの ${m}人の 分も いる`}});
U('3c',3,'分数（同じ分母の加減）',r=>{const d=ri(r,4,10);if(r()<.5){const a=ri(r,1,d-2),b=ri(r,1,d-1-a);return Q(`${fr(a,d)} ＋ ${fr(b,d)} ＝ §`,fr(a+b,d),`分子どうしを たす：${a}＋${b}＝${a+b}`,1)}const a=ri(r,2,d-1),b=ri(r,1,a-1);return Q(`${fr(a,d)} － ${fr(b,d)} ＝ §`,fr(a-b,d),`分子どうしを ひく：${a}－${b}＝${a-b}`,1)},
  r=>{const d=ri(r,4,10),a=ri(r,1,d-2),b=ri(r,1,d-1-a),n=who(r);return{q:`${n}は ジュースを ${fr(a,d)}L のみ、そのあと ${fr(b,d)}L のみました。あわせて なんL のみましたか。`,a:`${fr(a+b,d)} L`,e:`${a}＋${b}＝${a+b}`}},
  r=>{const d=ri(r,5,10),a=ri(r,2,d-1),b=ri(r,1,a-1);return{q:`ペットボトルに ${fr(a,d)}L、びんに ${fr(b,d)}L の お茶が あります。どちらが なんL おおいですか。`,a:`ペットボトルが ${fr(a-b,d)} L`,e:`${a}－${b}＝${a-b}`}});
U('3d',3,'小数（たし算・ひき算）',r=>{if(r()<.5){const a=ri(r,11,89),b=ri(r,11,89);return Q(`${d1(a)} ＋ ${d1(b)} ＝ §`,num((a+b)/10),`位をそろえて ${a}＋${b}＝${a+b} → 10分の1`,2)}const a=ri(r,21,99),b=ri(r,11,a-1);return Q(`${d1(a)} － ${d1(b)} ＝ §`,num((a-b)/10),`位をそろえて ${a}－${b}＝${a-b} → 10分の1`,2)},
  r=>{const a=ri(r,11,89),b=ri(r,11,89);return{q:`水とうに ${d1(a)}L の お茶が 入っています。${d1(b)}L たしました。ぜんぶで なんL ですか。`,a:`${num((a+b)/10)} L`,e:`${d1(a)}＋${d1(b)}`}},
  r=>{const a=ri(r,21,89),b=ri(r,11,89),c=ri(r,1,a+b-1);return{q:`${d1(a)}L の 水が あります。${d1(b)}L たして、${d1(c)}L つかいました。のこりは なんL ですか。`,a:`${num((a+b-c)/10)} L`,e:`${d1(a)}＋${d1(b)}－${d1(c)}`}});
U('3e',3,'時刻と時間',r=>{const s=ri(r,7,10)*60+ri(r,1,11)*5,d=ri(r,5,12)*5;return Q(`${tstr(s)} の ${d}分後は § です。`,tstr(s+d),`${tstr(s)} ＋ ${d}分`)},
  r=>{const n=who(r),s=ri(r,7,8)*60+ri(r,1,11)*5,d=ri(r,3,9)*5;return{q:`${n}は ${tstr(s)} に 家を 出て、${d}分 かけて 学校に つきました。学校に ついた 時こくは なん時なん分 ですか。`,a:tstr(s+d),e:`${tstr(s)} ＋ ${d}分`}},
  r=>{const s=ri(r,8,10)*60+ri(r,0,11)*5,d=ri(r,13,42)*5;return{q:`${tstr(s)} から ${tstr(s+d)} までは、なん時間なん分 ですか。`,a:`${Math.floor(d/60)}時間${d%60}分`,e:`${d}分＝${Math.floor(d/60)}時間${d%60}分`}});

/* ---- 小4 ---- */
U('4a',4,'大きな数・がい数',r=>{if(r()<.5){const n=ri(r,10000,99999);return Q(`${cma(n)} を 四捨五入して 千の位までの がい数に すると § 。`,cma(Math.round(n/1000)*1000),`百の位 ${Math.floor(n/100)%10} を 見て 切り上げ／切り捨て`)}const x=ri(r,120,980);return Q(`一万を ${x}こ あつめた 数は 数字で かくと § 。`,cma(x*10000),`${x}×10000`)},
  r=>{const n=ri(r,15000,94999),a=Math.round(n/10000);return{q:`ある 町の 人口は ${cma(n)}人 です。四捨五入して 万の位までの がい数で あらわすと、およそ なん万人 ですか。`,a:`${a}万人`,e:`千の位 ${Math.floor(n/1000)%10} を 四捨五入`}},
  r=>{const a=ri(r,21000,89999),b=ri(r,21000,89999),x=Math.round(a/1000)*1000,y=Math.round(b/1000)*1000;return{q:`A市の 人口は ${cma(a)}人、B市の 人口は ${cma(b)}人 です。それぞれ 千の位までの がい数に して、合計を 見つもりましょう。`,a:`${cma(x+y)} 人`,e:`${cma(x)}＋${cma(y)}`}});
U('4b',4,'わり算の筆算',r=>{let b,k,m;if(r()<.5){b=ri(r,2,9);k=ri(r,12,99);m=ri(r,0,b-1)}else{b=ri(r,11,39);k=ri(r,5,40);m=ri(r,0,b-1)}const a=b*k+m;return Q(`${a} ÷ ${b} ＝ §`,m?`${k} あまり ${m}`:k,`${b}×${k}＝${b*k}、${a}－${b*k}＝${m}`,2)},
  r=>{const b=ri(r,6,30),k=ri(r,5,20),m=ri(r,1,b-1),N=b*k+m;return{q:`${N}ページの 本を 1日 ${b}ページずつ 読みます。読みおわるまでに なん日 かかりますか。`,a:`${k+1} 日`,e:`${N}÷${b}＝${k}あまり${m} → あまりの 分も 1日`}},
  r=>{const a=ri(r,300,900),b=ri(r,30,90),k=Math.floor(a/b),m=a%b;return{q:`${a}円 もって、1こ ${b}円の パンを できるだけ たくさん かいます。なんこ かえて、おつりは いくら ですか。`,a:`${k}こ かえて、おつりは ${m}円`,e:`${a}÷${b}＝${k}あまり${m}`}});
U('4c',4,'小数×整数・小数÷整数',r=>{const x=ri(r,12,99),n=ri(r,2,9);if(r()<.5)return Q(`${d1(x)} × ${n} ＝ §`,num(x*n/10),`${x}×${n}＝${x*n} → 10分の1`,2);return Q(`${d1(x*n)} ÷ ${n} ＝ §`,num(x/10),`${x*n}÷${n}＝${x} → 10分の1`,2)},
  r=>{const x=ri(r,12,99),n=ri(r,2,9);return{q:`1本 ${d1(x)}L の ジュースを ${n}本 かいました。ぜんぶで なんL ですか。`,a:`${num(x*n/10)} L`,e:`${d1(x)}×${n}`}},
  r=>{const x=ri(r,12,59),n=ri(r,2,9),y=ri(r,11,59);return{q:`${d1(x*n)}m の リボンを ${n}人で おなじ 長さずつ 分けます。1人ぶんの 長さに あと ${d1(y)}m たすと、ぜんぶで なんm ですか。`,a:`${num((x+y)/10)} m`,e:`${d1(x*n)}÷${n}＝${d1(x)}、${d1(x)}＋${d1(y)}`}});
U('4d',4,'分数（帯分数・同じ分母）',r=>{const d=ri(r,4,9);let w1=ri(r,1,4),w2=ri(r,1,4),a=ri(r,1,d-1),b=ri(r,1,d-1);let n1=w1*d+a,n2=w2*d+b;if(r()<.5)return Q(`${mx(n1,d)} ＋ ${mx(n2,d)} ＝ §`,fa(n1+n2,d),`${n1}/${d}＋${n2}/${d}＝${n1+n2}/${d}`,1);if(n1===n2)n1+=1;if(n1<n2)[n1,n2]=[n2,n1];return Q(`${mx(n1,d)} － ${mx(n2,d)} ＝ §`,fa(n1-n2,d),`仮分数に して ${n1}/${d}－${n2}/${d}`,1)},
  r=>{const d=ri(r,4,9),n1=ri(r,1,3)*d+ri(r,1,d-1),n2=ri(r,1,3)*d+ri(r,1,d-1);return{q:`${mx(n1,d)}m の ひもと ${mx(n2,d)}m の ひもを つなぎます。ぜんぶで なんm ですか。`,a:`${fa(n1+n2,d)} m`,e:`${n1}/${d}＋${n2}/${d}`}},
  r=>{const d=ri(r,4,9),n1=ri(r,1,3)*d+ri(r,1,d-1),n2=ri(r,1,3)*d+ri(r,1,d-1),n3=ri(r,d,n1+n2-1);return{q:`ジュースが ${mx(n1,d)}L と ${mx(n2,d)}L あります。${mx(n3,d)}L のむと、のこりは なんL ですか。`,a:`${fa(n1+n2-n3,d)} L`,e:`(${n1}＋${n2}－${n3})/${d}`}});
U('4e',4,'面積（長方形・正方形）',r=>{const a=ri(r,3,15),b=ri(r,3,15);if(r()<.6)return Q(`たて ${a}cm、よこ ${b}cm の 長方形の 面積は § cm² 。`,a*b,`${a}×${b}`,1);return Q(`1辺 ${a}cm の 正方形の 面積は § cm² 。`,a*a,`${a}×${a}`,1)},
  r=>{const a=ri(r,4,15),b=ri(r,4,15);return{q:`たて ${a}m、よこ ${b}m の 長方形の 花だんが あります。この 花だんの 面積は なんm² ですか。`,a:`${a*b} m²`,e:`${a}×${b}`}},
  r=>{const A=ri(r,10,20),B=ri(r,10,20),c=ri(r,2,6),d=ri(r,2,6);return{q:`たて ${A}m、よこ ${B}m の 長方形の 土地の 中に、たて ${c}m、よこ ${d}m の 長方形の 池が あります。池を のぞいた 土地の 面積は なんm² ですか。`,a:`${A*B-c*d} m²`,e:`${A}×${B}－${c}×${d}`}});
U('4f',4,'角の大きさ',r=>{if(r()<.5){const a=ri(r,30,150);return Q(`一直線の 角は 180°です。一方の 角が ${a}° のとき、もう一方は § ° 。`,180-a,`180－${a}`)}const a=ri(r,30,80),b=ri(r,30,80);return Q(`三角形の 2つの 角が ${a}°と ${b}° のとき、のこりの 角は § ° 。`,180-a-b,`180－${a}－${b}`)},
  r=>{const a=ri(r,30,80),b=ri(r,30,80);return{q:`三角形の 3つの 角のうち、2つが ${a}°と ${b}° です。のこりの 角は なん度 ですか。`,a:`${180-a-b}°`,e:`180－${a}－${b}`}},
  r=>{const a=ri(r,60,110),b=ri(r,60,110),c=ri(r,60,110);return{q:`四角形の 3つの 角が ${a}°、${b}°、${c}° です。のこりの 角は なん度 ですか。`,a:`${360-a-b-c}°`,e:`四角形の 角の和は360°：360－${a}－${b}－${c}`}});

/* ---- 小5 ---- */
U('5a',5,'小数のかけ算',r=>{const y=ri(r,12,99);if(r()<.7){const x=ri(r,12,99);return Q(`${d1(x)} × ${d1(y)} ＝ §`,num(x*y/100),`${x}×${y}＝${x*y} → 100分の1`,2)}const n=ri(r,2,9);return Q(`${n} × ${d1(y)} ＝ §`,num(n*y/10),`${n}×${y}＝${n*y} → 10分の1`,2)},
  r=>{const x=ri(r,12,59),y=ri(r,12,59);return{q:`1mの おもさが ${d1(x)}kg の ぼうが あります。この ぼう ${d1(y)}m の おもさは なんkg ですか。`,a:`${num(x*y/100)} kg`,e:`${d1(x)}×${d1(y)}`}},
  r=>{const p=ri(r,2,9)*10,y=ri(r,11,49),c=p*y/10,pay=Math.ceil((c+1)/100)*100;return{q:`1mの ねだんが ${p}円 の リボンを ${d1(y)}m かって、${pay}円 はらいました。おつりは いくらですか。`,a:`${pay-c} 円`,e:`${p}×${d1(y)}＝${c}、${pay}－${c}`}});
U('5b',5,'小数のわり算',r=>{const k=r();if(k<.35){const d=ri(r,2,9),q=ri(r,2,20);return Q(`${d1(d*q)} ÷ ${d1(d)} ＝ §`,q,`両方を 10倍して ${d*q}÷${d}`,2)}if(k<.7){const d=ri(r,2,9),q=ri(r,12,49);return Q(`${num(d*q/100)} ÷ ${d1(d)} ＝ §`,num(q/10),`両方を 10倍して ${num(d*q/10)}÷${d}`,2)}const n=ri(r,2,9),q=ri(r,12,59);return Q(`${d1(n*q)} ÷ ${n} ＝ §`,num(q/10),`${n*q}÷${n}＝${q} → 10分の1`,2)},
  r=>{const b=ri(r,2,9),k=ri(r,3,12);return{q:`${d1(b*k)}L の ジュースを ${d1(b)}L ずつ びんに 入れます。なん本 できますか。`,a:`${k} 本`,e:`${d1(b*k)}÷${d1(b)}＝${b*k}÷${b}`}},
  r=>{const Y=ri(r,3,9),k=ri(r,3,12),R=ri(r,1,Y-1),X=Y*k+R;return{q:`${d1(X)}m の ひもから ${d1(Y)}m ずつ きりとります。なん本 とれて、なんm あまりますか。`,a:`${k}本 とれて、${num(R/10)}m あまる`,e:`${X}÷${Y}＝${k}あまり${R} → あまりは ${num(R/10)}m`}});
const DEN=[2,3,4,5,6,8,9,10,12];
U('5c',5,'分数（約分・通分・異分母の加減）',r=>{if(r()<.2){const d=pk(r,[3,4,5,7,9]),a=ri(r,1,d-1),k=ri(r,2,4);return Q(`${fr(a*k,d*k)} を 約分すると § 。`,fa(a*k,d*k),`分子と分母を ${gcd(a*k,d*k)}で わる`,1)}let d1_=pk(r,DEN),d2=pk(r,DEN.filter(x=>x!==d1_)),a=ri(r,1,d1_-1),b=ri(r,1,d2-1);const L=lcm(d1_,d2);let x=a*L/d1_,y=b*L/d2;if(r()<.5)return Q(`${fr(a,d1_)} ＋ ${fr(b,d2)} ＝ §`,fa(x+y,L),`通分して ${x}/${L}＋${y}/${L}`,2);if(x===y)x+=0;if(x<y){[a,b]=[b,a];[d1_,d2]=[d2,d1_];[x,y]=[y,x]}if(x===y)return Q(`${fr(a,d1_)} ＋ ${fr(b,d2)} ＝ §`,fa(x+y,L),`通分して ${x}/${L}＋${y}/${L}`,2);return Q(`${fr(a,d1_)} － ${fr(b,d2)} ＝ §`,fa(x-y,L),`通分して ${x}/${L}－${y}/${L}`,2)},
  r=>{const n=who(r),p=pk(r,DEN),q=pk(r,DEN.filter(x=>x!==p)),a=ri(r,1,p-1),b=ri(r,1,q-1),L=lcm(p,q),s=a*L/p+b*L/q;return{q:`${n}は ジュースを ${fr(a,p)}L のみ、そのあと ${fr(b,q)}L のみました。あわせて なんL のみましたか。`,a:`${fa(s,L)} L`,e:`通分して ${a*L/p}/${L}＋${b*L/q}/${L}`}},
  r=>{let D=[3,4,6,4,1,4],o=[3,4,1,6,1,4],ok=false;for(let i=0;i<300;i++){const p=pk(r,DEN),q=pk(r,DEN),s=pk(r,DEN),a=ri(r,1,p-1),b=ri(r,1,q-1),c=ri(r,1,s-1),L=lcm(lcm(p,q),s),N=a*L/p-b*L/q-c*L/s;if(N>0){D=[a,p,b,q,c,s,L,N];ok=true;break}}if(!ok)D=[3,4,1,6,1,4,12,6];const [a,p,b,q,c,s,L,N]=D;return{q:`牛乳が ${fr(a,p)}L あります。朝に ${fr(b,q)}L、夜に ${fr(c,s)}L つかいました。のこりは なんL ですか。`,a:`${fa(N,L)} L`,e:`通分して (${a*L/p}－${b*L/q}－${c*L/s})/${L}`}});
U('5d',5,'平均',r=>{const n=ri(r,3,5),m=ri(r,55,90),v=[];let s=0;for(let i=0;i<n-1;i++){const d=ri(r,-12,12);v.push(m+d);s+=d}v.push(m-s);return Q(`${v.join('、')} の 平均は § 。`,m,`(${v.join('＋')})÷${n}＝${m}`,1)},
  r=>{const m=ri(r,10,30),v=[];let s=0;for(let i=0;i<4;i++){const d=ri(r,-7,7);v.push(m+d);s+=d}v.push(m-s);return{q:`${who(r)}は 5日間で 本を ${v.join('、')} ページ 読みました。1日 平均 なんページ 読みましたか。`,a:`${m} ページ`,e:`合計 ${m*5} ÷ 5`}},
  r=>{const avg=ri(r,70,90),b=60+(avg%5)+5*ri(r,0,7);return{q:`4回の テストの 平均が ${avg}点 でした。5回目が ${b}点 のとき、5回の 平均は なん点 ですか。`,a:`${(4*avg+b)/5} 点`,e:`(${avg}×4＋${b})÷5`}});
U('5e',5,'体積（直方体・立方体）',r=>{if(r()<.7){const a=ri(r,2,9),b=ri(r,2,9),c=ri(r,2,9);return Q(`たて ${a}cm、よこ ${b}cm、高さ ${c}cm の 直方体の 体積は § cm³ 。`,a*b*c,`${a}×${b}×${c}`,1)}const a=ri(r,2,9);return Q(`1辺 ${a}cm の 立方体の 体積は § cm³ 。`,a*a*a,`${a}×${a}×${a}`,1)},
  r=>{const a=ri(r,2,6),b=ri(r,2,6),c=ri(r,2,6);return{q:`たて ${a}m、よこ ${b}m、高さ ${c}m の 直方体の 部屋が あります。体積は なんm³ ですか。`,a:`${a*b*c} m³`,e:`${a}×${b}×${c}`}},
  r=>{const x=ri(r,1,5),y=ri(r,1,5),z=ri(r,1,5);return{q:`たて ${x*10}cm、よこ ${y*10}cm、深さ ${z*10}cm の 直方体の 水そうが あります。いっぱいに 入る 水は なんL ですか。（1L＝1000cm³）`,a:`${x*y*z} L`,e:`${x*10*y*10*z*10}cm³ ÷ 1000`}});
U('5f',5,'図形の面積（三角形・平行四辺形・台形）',r=>{const k=r();if(k<.34){const a=ri(r,2,8)*2,h=ri(r,3,12);return Q(`底辺 ${a}cm、高さ ${h}cm の 三角形の 面積は § cm² 。`,a*h/2,`${a}×${h}÷2`,1)}if(k<.67){const a=ri(r,3,12),h=ri(r,3,12);return Q(`底辺 ${a}cm、高さ ${h}cm の 平行四辺形の 面積は § cm² 。`,a*h,`${a}×${h}`,1)}const u=ri(r,2,8),d=ri(r,u+1,12);let h=ri(r,2,10);if((u+d)*h%2)h++;return Q(`上底 ${u}cm、下底 ${d}cm、高さ ${h}cm の 台形の 面積は § cm² 。`,(u+d)*h/2,`(${u}＋${d})×${h}÷2`,1)},
  r=>{const a=ri(r,2,9)*2,h=ri(r,3,12);return{q:`底辺 ${a}cm、高さ ${h}cm の 三角形の 面積は なんcm² ですか。`,a:`${a*h/2} cm²`,e:`${a}×${h}÷2`}},
  r=>{const a=ri(r,2,8)*2,h=ri(r,3,10),b=ri(r,3,10);let k=ri(r,3,10);if(a*h/2===b*k)k++;const A=a*h/2,B=b*k;return{q:`底辺 ${a}cm、高さ ${h}cm の 三角形と、底辺 ${b}cm、高さ ${k}cm の 平行四辺形が あります。面積の ちがいは なんcm² ですか。`,a:`${Math.abs(A-B)} cm²`,e:`三角形 ${A}cm²、平行四辺形 ${B}cm²`}});
const pickPct=(r,as)=>{for(let i=0;i<200;i++){const a=pk(r,as),p=ri(r,1,19)*5;if((a*p)%100===0)return[a,p]}return[200,25]};
U('5g',5,'割合・百分率',r=>{const [a,p]=pickPct(r,[20,25,40,50,80,200,250,400,500]);if(r()<.55)return Q(`${a*p/100} は ${a} の なん％ ですか。 §％`,p,`${a*p/100}÷${a}×100`,1);return Q(`${a} の ${p}％ は § 。`,a*p/100,`${a}×${p/100}`,1)},
  r=>{const [a,p]=pickPct(r,[20,25,40,50,80]);return{q:`定員 ${a}人の バスに ${a*p/100}人 のっています。定員に たいする のっている 人の 割合は なん％ ですか。`,a:`${p} ％`,e:`${a*p/100}÷${a}×100`}},
  r=>{const [a,p]=pickPct(r,[200,400,500,800,1000,1200]),t=pk(r,GD);return{q:`${a}円の ${t}セットを ${p}％引き で うっています。ねだんは いくらですか。`,a:`${a*(100-p)/100} 円`,e:`${a}×(1－${p/100})`}});

/* ---- 小6 ---- */
const FR=r=>{const b=ri(r,2,9),d=ri(r,2,9);return[ri(r,1,b-1)||1,b,ri(r,1,d-1)||1,d]};
U('6a',6,'分数のかけ算',r=>{const [a,b,c,d]=FR(r);if(r()<.2){const n=ri(r,2,9);return Q(`${n} × ${fr(a,b)} ＝ §`,fa(n*a,b),`${n}×${a}/${b}`,2)}return Q(`${fr(a,b)} × ${fr(c,d)} ＝ §`,fa(a*c,b*d),`分子×分子 ${a*c}、分母×分母 ${b*d} → 約分`,2)},
  r=>{const [a,b,c,d]=FR(r);return{q:`1mの おもさが ${fr(a,b)}kg の ぼうが あります。この ぼう ${fr(c,d)}m の おもさは なんkg ですか。`,a:`${fa(a*c,b*d)} kg`,e:`${a}/${b}×${c}/${d}`}},
  r=>{const b=ri(r,2,9),a=ri(r,1,b-1)||1,d=ri(r,3,9),c=ri(r,1,d-1)||1;return{q:`さとうが ${fr(a,b)}kg あります。その ${fr(c,d)} を つかいました。のこりは なんkg ですか。`,a:`${fa(a*(d-c),b*d)} kg`,e:`${a}/${b}×(1－${c}/${d})`}});
U('6b',6,'分数のわり算',r=>{const [a,b,c,d]=FR(r);if(r()<.2){const n=ri(r,2,9);return Q(`${fr(a,b)} ÷ ${n} ＝ §`,fa(a,b*n),`${a}/${b}×1/${n}`,2)}return Q(`${fr(a,b)} ÷ ${fr(c,d)} ＝ §`,fa(a*d,b*c),`わる数の 逆数を かける：${a}/${b}×${d}/${c}`,2)},
  r=>{const c=ri(r,1,3),d=ri(r,4,9),k=ri(r,2,6),m=ri(r,1,3);return{q:`${fr(k*c*m,d*m)}L の ジュースを ${fr(c,d)}L ずつ びんに 入れます。なん本 できますか。`,a:`${k} 本`,e:`${k*c*m}/${d*m}÷${c}/${d}`}},
  r=>{const [a,b,c,d]=FR(r);return{q:`${fr(a,b)}kg の ぼうの 長さが ${fr(c,d)}m です。1mあたりの おもさは なんkg ですか。`,a:`${fa(a*d,b*c)} kg`,e:`${a}/${b}÷${c}/${d}`}});
U('6c',6,'円の面積・円周',r=>{if(r()<.5){const x=ri(r,2,12);return Q(`半径 ${x}cm の 円の 面積は § cm² 。（円周率 3.14）`,num(x*x*314/100),`${x}×${x}×3.14`,1)}const d=ri(r,3,20);return Q(`直径 ${d}cm の 円の 円周は § cm 。（円周率 3.14）`,num(d*314/100),`${d}×3.14`,1)},
  r=>{const d=ri(r,3,20);return{q:`直径 ${d}cm の 円形の ケーキの まわりの 長さは なんcm ですか。（円周率 3.14）`,a:`${num(d*314/100)} cm`,e:`${d}×3.14`}},
  r=>{const a=ri(r,5,12),b=ri(r,2,a-2);return{q:`半径 ${a}cm の 円から 半径 ${b}cm の 円を くりぬきました。のこった 部分の 面積は なんcm² ですか。（円周率 3.14）`,a:`${num((a*a-b*b)*314/100)} cm²`,e:`(${a}×${a}－${b}×${b})×3.14`}});
const RP=[[1,2],[1,3],[2,3],[3,4],[2,5],[3,5],[3,2],[5,2],[5,3],[4,3],[1,4],[3,7]];
U('6d',6,'比',r=>{const [x,y]=pk(r,RP),g=ri(r,2,9);return Q(`${x*g} ： ${y*g} を もっとも かんたんな 整数の 比に すると § 。`,`${x} ： ${y}`,`${g}で わる`,1)},
  r=>{const [x,y]=pk(r,RP),g=ri(r,2,9);return{q:`男子が ${x*g}人、女子が ${y*g}人 います。男子と 女子の 人数の 比を、もっとも かんたんな 整数の 比で あらわしましょう。`,a:`${x} ： ${y}`,e:`${g}で わる`}},
  r=>{const [x,y]=pk(r,RP),k=ri(r,2,9),L=(x+y)*k;return{q:`${L}cm の ひもを ${x}：${y} に 分けます。長い ほうは なんcm ですか。`,a:`${Math.max(x,y)*k} cm`,e:`${L}÷(${x}＋${y})＝${k} → ${Math.max(x,y)}×${k}`}});
U('6e',6,'速さ',r=>{const v=ri(r,30,80),t=ri(r,2,5);if(r()<.5)return Q(`時速 ${v}km で ${t}時間 走ると、道のりは § km 。`,v*t,`${v}×${t}`,1);return Q(`${v*t}km を ${t}時間 で 走る 速さは 時速 § km 。`,v,`${v*t}÷${t}`,1)},
  r=>{const v=ri(r,50,90),t=ri(r,5,20);return{q:`分速 ${v}m で ${t}分 歩くと、なんm すすみますか。`,a:`${v*t} m`,e:`${v}×${t}`}},
  r=>{const a=pk(r,[40,50,60,80]),b=ri(r,2,6),D=a*b,cs=[20,30,40,60].filter(c=>c!==a&&D%c===0),c=cs.length?pk(r,cs):a;return{q:`A町から B町まで 時速 ${a}km で ${b}時間 かかりました。帰りは 時速 ${c}km で 帰りました。帰りに かかった 時間は なん時間 ですか。`,a:`${D/c} 時間`,e:`道のり ${a}×${b}＝${D}km → ${D}÷${c}`}});
U('6f',6,'文字と式',r=>{const k=r();if(k<.35){const a=ri(r,2,15),x=ri(r,2,20);return Q(`x ＋ ${a} ＝ ${x+a} のとき、x ＝ § 。`,x,`${x+a}－${a}`,1)}if(k<.7){const a=ri(r,2,9),x=ri(r,2,12);return Q(`${a} × x ＝ ${a*x} のとき、x ＝ § 。`,x,`${a*x}÷${a}`,1)}const a=ri(r,2,9),b=ri(r,1,9),x=ri(r,2,9);return Q(`x＝${x} のとき、${a}x＋${b} の 値は § 。`,a*x+b,`${a}×${x}＋${b}`,1)},
  r=>{const t=pk(r,GD),n=ri(r,2,6),x=ri(r,2,9)*10;return{q:`1こ x円 の ${t}を ${n}こ かうと、だい金は ${n*x}円 でした。x に あてはまる 数を もとめましょう。`,a:`x ＝ ${x}`,e:`${n}×x＝${n*x} → x＝${n*x}÷${n}`}},
  r=>{const n=ri(r,2,6),x=ri(r,2,9)*10;return{q:`1こ x円 の りんごを ${n}こ と、100円の ケーキを 1こ かうと、だい金は ${n*x+100}円 でした。x の 値を もとめましょう。`,a:`x ＝ ${x}`,e:`${n}×x＋100＝${n*x+100} → x＝(${n*x+100}－100)÷${n}`}});
U('6g',6,'角柱・円柱の体積',r=>{if(r()<.5){const S=ri(r,10,60),h=ri(r,3,15);return Q(`底面積が ${S}cm²、高さが ${h}cm の 角柱の 体積は § cm³ 。`,S*h,`${S}×${h}`,1)}const x=ri(r,2,8),h=ri(r,3,12);return Q(`底面の 半径が ${x}cm、高さが ${h}cm の 円柱の 体積は § cm³ 。（円周率 3.14）`,num(x*x*h*314/100),`${x}×${x}×3.14×${h}`,1)},
  r=>{const x=ri(r,2,8),h=ri(r,3,12);return{q:`底面の 半径が ${x}cm、高さが ${h}cm の 円柱の 体積は なんcm³ ですか。（円周率 3.14）`,a:`${num(x*x*h*314/100)} cm³`,e:`${x}×${x}×3.14×${h}`}},
  r=>{const b=ri(r,2,8)*2,hh=ri(r,3,10),H=ri(r,4,12);return{q:`底面が 底辺 ${b}cm、高さ ${hh}cm の 三角形で、高さが ${H}cm の 三角柱の 体積は なんcm³ ですか。`,a:`${b*hh/2*H} cm³`,e:`底面積 ${b}×${hh}÷2＝${b*hh/2}、×${H}`}});

/* ========== 状態・生成 ========== */
const state={grade:4,sel:new Set(),n:10,mode:'random',seed:(Math.random()*2**32)>>>0,ans:false};
const plan=n=>{const a=Math.round(n*.12),w=Math.round(n*.22);return{a,w,b:n-a-w}};
function build(){
  const sel=UNITS.filter(u=>state.sel.has(u.id));if(!sel.length)return[];
  const {a,w,b}=plan(state.n),out=[],cnt={},seen=new Set();
  const off=state.mode==='fixed'?0:state.seed%sel.length;
  [['basic','b',b],['word','w',w],['apply','a',a]].forEach(([cat,f,m])=>{
    for(let i=0;i<m;i++){
      const u=sel[(i+off)%sel.length],key=u.id+cat;let p;
      for(let t=0;t<12;t++){
        const k=(cnt[key]||0)+t*97;
        const r=mul32(state.mode==='fixed'?hash(key+k):((state.seed^hash(key+k))>>>0));
        p=u[f](r);if(!seen.has(p.q))break;
      }
      cnt[key]=(cnt[key]||0)+1;seen.add(p.q);
      out.push({...p,cat,unit:u.name,sp:cat==='basic'?(p.sp||1):cat==='word'?2:3});
    }
  });
  return out;
}

/* ========== 描画 ========== */
const SEC={basic:'けいさん もんだい',word:'ぶんしょう だい',apply:'おうよう もんだい'};
function probHTML(p,i){
  const no=i<20?String.fromCharCode(0x2460+i):i+1;
  let q=p.q.includes('§')?p.q:p.q+`<div class="al">答え　§</div>`;
  q=q.replace(/§/g,()=>`<span class="blank"><i>${p.a}</i></span>`);
  return `<div class="pb ${p.cat}"><div class="qt"><span class="no">${no}</span><div class="qx">${q}</div></div><div class="sp s${p.sp}">${p.e?`<span class="ex">解説：${p.e}</span>`:''}</div></div>`;
}
function render(){
  const P=build(),sheet=$('#sheet');
  const {a,w,b}=plan(state.n);$('#mix').textContent=`内訳の目安：基礎 ${b}問 ／ 文章題 ${w}問 ／ 応用 ${a}問`;
  const school=$('#school').value.trim(),title=$('#title').value.trim()||'算数 朝のプリント';
  const used=[...new Set(P.map(p=>p.unit))];
  let h=`<div class="hd"><div class="top"><h1>${title.replace(/</g,'&lt;')}</h1><span class="gr">${state.grade}年</span><div class="units">${used.join('／')}</div></div>
  <div class="fields"><span class="fld">${school?`<b>${school.replace(/</g,'&lt;')}</b>`:'<span class="ln" style="min-width:34mm"></span>小学校'}</span>
  <span class="fld"><span class="ln" style="min-width:9mm"></span>年 <span class="ln" style="min-width:9mm"></span>組 <span class="ln" style="min-width:9mm"></span>番</span>
  <span class="fld">名前 <span class="ln" style="min-width:44mm"></span></span>
  ${$('#date').checked?'<span class="fld"><span class="ln" style="min-width:9mm"></span>月 <span class="ln" style="min-width:9mm"></span>日</span>':''}
  ${$('#score').checked?'<span class="score">点</span>':''}</div></div>`;
  if(!P.length)h+='<div class="empty">単元を 1つ以上 選んでください</div>';
  let i=0;
  ['basic','word','apply'].forEach(c=>{
    const L=P.filter(p=>p.cat===c);if(!L.length)return;
    h+=`<div class="sec">${SEC[c]}</div><div class="grid">`+L.map(p=>probHTML(p,i++)).join('')+'</div>';
  });
  h+=`<div class="ft">${$('#pub').value==='指定なし'?'':$('#pub').value+' 使用校向け ／ '}小学校学習指導要領（算数科）の学年・単元に沿った自動生成問題</div>`;
  sheet.innerHTML=h;sheet.classList.toggle('show-ans',state.ans);
  fit();scalePreview();
}
function fit(){
  const s=$('#sheet'),set=(k,f)=>{s.style.setProperty('--k',k);s.style.setProperty('--fs',f)},over=()=>s.scrollHeight>s.clientHeight+1;
  let k=1,f=1;set(k,f);
  if(!over()){while(k<3&&(set(k+.25,f),!over()))k+=.25;set(k,f);return}
  while(over()&&k>.3){k-=.1;set(k,f)}
  while(over()&&f>.75){f-=.05;set(k,f)}
  while(over()&&k>0){k=Math.max(0,k-.1);set(k,f)}
}
function scalePreview(){
  const s=$('#sheet'),hd=$('#holder'),main=document.querySelector('main');
  s.style.transform='none';
  const sc=Math.min(1,(main.clientWidth-(innerWidth<1024?16:48))/s.offsetWidth);
  s.style.transform=`scale(${sc})`;hd.style.width=s.offsetWidth*sc+'px';hd.style.height=s.offsetHeight*sc+'px';
}

/* ========== UI ========== */
function buildUnits(selectAll=true){
  const L=UNITS.filter(u=>u.g===state.grade);
  if(selectAll)state.sel=new Set(L.map(u=>u.id));
  $('#units').innerHTML=L.map(u=>`<label class="flex items-start gap-1.5"><input type="checkbox" value="${u.id}" ${state.sel.has(u.id)?'checked':''} class="mt-1 unit"><span>${u.name}</span></label>`).join('');
  document.querySelectorAll('.unit').forEach(c=>c.onchange=()=>{c.checked?state.sel.add(c.value):state.sel.delete(c.value);render()});
}
$('#grade').onchange=e=>{state.grade=+e.target.value;buildUnits();render()};
$('#allOn').onclick=()=>{UNITS.filter(u=>u.g===state.grade).forEach(u=>state.sel.add(u.id));buildUnits(false);render()};
$('#allOff').onclick=()=>{UNITS.filter(u=>u.g===state.grade).forEach(u=>state.sel.delete(u.id));buildUnits(false);render()};
$('#n').oninput=e=>{state.n=+e.target.value;$('#nv').textContent=state.n;render()};
document.querySelectorAll('input[name=mode]').forEach(r=>r.onchange=()=>{state.mode=r.value;$('#shuffle').disabled=state.mode==='fixed';render()});
['#title','#school','#date','#score','#pub'].forEach(s=>$(s).addEventListener('input',render));
$('#shuffle').onclick=()=>{state.seed=(Math.random()*2**32)>>>0;render()};
$('#ans').onclick=()=>{state.ans=!state.ans;$('#ans').textContent=state.ans?'🙈 解答・解説を隠す':'✅ 解答・解説を表示';render()};
$('#print').onclick=()=>window.print();
addEventListener('resize',scalePreview);
buildUnits();render();
</script>
</body>
</html>

'''

components.html(APP_HTML, height=1500, scrolling=True)

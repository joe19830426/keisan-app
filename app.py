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
.hd .fields{display:flex;gap:3.5mm;margin-top:2.5mm;font-size:.85em;align-items:flex-end}
.hd .fld{display:flex;align-items:flex-end;gap:1mm;white-space:nowrap;flex-shrink:0}
.hd .ln{display:inline-block;border-bottom:1.3px solid #111;min-width:18mm;height:1.3em;text-align:center}
.hd .score{margin-left:auto;white-space:nowrap;flex-shrink:0;border:2px solid #111;border-radius:3mm;padding:.2mm 2mm;min-width:15mm;text-align:right}
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
.blank i{position:absolute;left:50%;transform:translateX(-50%);bottom:1px;font-style:normal;color:#d40000;font-weight:700;white-space:nowrap;display:none}
.al{text-align:right;margin-top:1mm}
.al .blank{min-width:9em}
.ex{display:none;position:absolute;right:2mm;top:.5mm;font-size:8.5pt;color:#d40000;background:rgba(255,255,255,.85);padding:0 1mm}
.show-ans .blank i{display:inline}.show-ans .ex{display:block}
.ft{margin-top:auto;font-size:7.5pt;color:#666;text-align:right;border-top:1px solid #ccc;padding-top:1mm}
.fr{display:inline-flex;flex-direction:column;align-items:center;vertical-align:middle;line-height:1.15;margin:0 .15em;font-size:.95em}
.fr>span:first-child{border-bottom:1.5px solid currentColor;padding:0 .25em}
.empty{padding:30mm 0;text-align:center;color:#888}
.tb{border-collapse:collapse;margin:1mm 0;font-size:.85em}.tb th,.tb td{border:1px solid #111;padding:0 2mm;text-align:center;line-height:1.35}.tb th{background:#eee;font-weight:600}
.ag{display:none}.show-ans .ag{display:inline}
.sp.s0{display:none}
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
  <p class="text-xs text-slate-500">準拠：小学校学習指導要領（平成29年告示・令和2年度全面実施）算数科。次期改訂は告示前のため対象外です。</p>
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
U('3a',3,'かけ算の筆算',r=>{const a=r()<.6?ri(r,12,99):ri(r,100,399),b=r()<.65?ri(r,2,9):ri(r,12,39);return Q(`${a} × ${b} ＝ §`,a*b,`${a}×${b}＝${a*b}`,2)},
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
U('4b',4,'わり算の筆算',r=>{let b,k,m;if(r()<.5){b=ri(r,2,9);k=ri(r,12,99);m=ri(r,0,b-1)}else{b=ri(r,11,39);k=ri(r,5,Math.min(40,Math.floor(998/b)-1));m=ri(r,0,b-1)}const a=b*k+m;return Q(`${a} ÷ ${b} ＝ §`,m?`${k} あまり ${m}`:k,`${b}×${k}＝${b*k}、${a}－${b*k}＝${m}`,2)},
  r=>{const b=ri(r,6,30),k=ri(r,5,20),m=ri(r,1,b-1),N=b*k+m;return{q:`${N}ページの 本を 1日 ${b}ページずつ 読みます。読みおわるまでに なん日 かかりますか。`,a:`${k+1} 日`,e:`${N}÷${b}＝${k}あまり${m} → あまりの 分も 1日`}},
  r=>{const a=ri(r,300,900),b=ri(r,30,90),k=Math.floor(a/b),m=a%b;return{q:`${a}円 もって、1こ ${b}円の パンを できるだけ たくさん かいます。なんこ かえて、おつりは いくら ですか。`,a:`${k}こ かえて、おつりは ${m}円`,e:`${a}÷${b}＝${k}あまり${m}`}});
U('4c',4,'小数×整数・小数÷整数',r=>{const x=ri(r,12,99),n=ri(r,2,9);if(r()<.5)return Q(`${d1(x)} × ${n} ＝ §`,num(x*n/10),`${x}×${n}＝${x*n} → 10分の1`,2);return Q(`${d1(x*n)} ÷ ${n} ＝ §`,num(x/10),`${x*n}÷${n}＝${x} → 10分の1`,2)},
  r=>{const x=ri(r,12,99),n=ri(r,2,9);return{q:`1本 ${d1(x)}L の ジュースを ${n}本 かいました。ぜんぶで なんL ですか。`,a:`${num(x*n/10)} L`,e:`${d1(x)}×${n}`}},
  r=>{const x=ri(r,12,59),n=ri(r,2,9),y=ri(r,11,59);return{q:`${d1(x*n)}m の リボンを ${n}人で おなじ 長さずつ 分けます。1人ぶんの 長さに あと ${d1(y)}m たすと、ぜんぶで なんm ですか。`,a:`${num((x+y)/10)} m`,e:`${d1(x*n)}÷${n}＝${d1(x)}、${d1(x)}＋${d1(y)}`}});
U('4d',4,'分数（帯分数・同じ分母）',r=>{const d=ri(r,4,9);let w1=ri(r,1,4),w2=ri(r,1,4),a=ri(r,1,d-1),b=ri(r,1,d-1);let n1=w1*d+a,n2=w2*d+b;if(r()<.5)return Q(`${mx(n1,d)} ＋ ${mx(n2,d)} ＝ §`,mx(n1+n2,d),`${n1}/${d}＋${n2}/${d}＝${n1+n2}/${d}`,1);if(n1===n2)n1+=1;if(n1<n2)[n1,n2]=[n2,n1];return Q(`${mx(n1,d)} － ${mx(n2,d)} ＝ §`,mx(n1-n2,d),`仮分数に して ${n1}/${d}－${n2}/${d}`,1)},
  r=>{const d=ri(r,4,9),n1=ri(r,1,3)*d+ri(r,1,d-1),n2=ri(r,1,3)*d+ri(r,1,d-1);return{q:`${mx(n1,d)}m の ひもと ${mx(n2,d)}m の ひもを つなぎます。ぜんぶで なんm ですか。`,a:`${mx(n1+n2,d)} m`,e:`${n1}/${d}＋${n2}/${d}`}},
  r=>{const d=ri(r,4,9),n1=ri(r,1,3)*d+ri(r,1,d-1),n2=ri(r,1,3)*d+ri(r,1,d-1),n3=ri(r,d,n1+n2-1);return{q:`ジュースが ${mx(n1,d)}L と ${mx(n2,d)}L あります。${mx(n3,d)}L のむと、のこりは なんL ですか。`,a:`${mx(n1+n2-n3,d)} L`,e:`(${n1}＋${n2}－${n3})/${d}`}});
U('4e',4,'面積（長方形・正方形）',r=>{const a=ri(r,3,15),b=ri(r,3,15);if(r()<.6)return Q(`たて ${a}cm、よこ ${b}cm の 長方形の 面積は § cm² 。`,a*b,`${a}×${b}`,1);return Q(`1辺 ${a}cm の 正方形の 面積は § cm² 。`,a*a,`${a}×${a}`,1)},
  r=>{const a=ri(r,4,15),b=ri(r,4,15);return{q:`たて ${a}m、よこ ${b}m の 長方形の 花だんが あります。この 花だんの 面積は なんm² ですか。`,a:`${a*b} m²`,e:`${a}×${b}`}},
  r=>{const A=ri(r,10,20),B=ri(r,10,20),c=ri(r,2,6),d=ri(r,2,6);return{q:`たて ${A}m、よこ ${B}m の 長方形の 土地の 中に、たて ${c}m、よこ ${d}m の 長方形の 池が あります。池を のぞいた 土地の 面積は なんm² ですか。`,a:`${A*B-c*d} m²`,e:`${A}×${B}－${c}×${d}`}});
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
U('5f',5,'図形の面積（三角形・平行四辺形・ひし形・台形）',r=>{const k=r();if(k>.85){const a=ri(r,2,8)*2,b=ri(r,3,10);return Q(`対角線が ${a}cmと ${b}cm の ひし形の 面積は § cm² 。`,a*b/2,`${a}×${b}÷2`,1)}if(k<.34){const a=ri(r,2,8)*2,h=ri(r,3,12);return Q(`底辺 ${a}cm、高さ ${h}cm の 三角形の 面積は § cm² 。`,a*h/2,`${a}×${h}÷2`,1)}if(k<.67){const a=ri(r,3,12),h=ri(r,3,12);return Q(`底辺 ${a}cm、高さ ${h}cm の 平行四辺形の 面積は § cm² 。`,a*h,`${a}×${h}`,1)}const u=ri(r,2,8),d=ri(r,u+1,12);let h=ri(r,2,10);if((u+d)*h%2)h++;return Q(`上底 ${u}cm、下底 ${d}cm、高さ ${h}cm の 台形の 面積は § cm² 。`,(u+d)*h/2,`(${u}＋${d})×${h}÷2`,1)},
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
const RP=[[1,2],[1,3],[2,3],[3,4],[2,5],[3,5],[3,2],[5,2],[5,3],[4,3],[1,4],[3,7]];
U('6d',6,'比',r=>{const [x,y]=pk(r,RP),g=ri(r,2,9);return Q(`${x*g} ： ${y*g} を もっとも かんたんな 整数の 比に すると § 。`,`${x} ： ${y}`,`${g}で わる`,1)},
  r=>{const [x,y]=pk(r,RP),g=ri(r,2,9);return{q:`男子が ${x*g}人、女子が ${y*g}人 います。男子と 女子の 人数の 比を、もっとも かんたんな 整数の 比で あらわしましょう。`,a:`${x} ： ${y}`,e:`${g}で わる`}},
  r=>{const [x,y]=pk(r,RP),k=ri(r,2,9),L=(x+y)*k;return{q:`${L}cm の ひもを ${x}：${y} に 分けます。長い ほうは なんcm ですか。`,a:`${Math.max(x,y)*k} cm`,e:`${L}÷(${x}＋${y})＝${k} → ${Math.max(x,y)}×${k}`}});
U('6f',6,'文字と式',r=>{const k=r();if(k<.35){const a=ri(r,2,15),x=ri(r,2,20);return Q(`x ＋ ${a} ＝ ${x+a} のとき、x ＝ § 。`,x,`${x+a}－${a}`,1)}if(k<.7){const a=ri(r,2,9),x=ri(r,2,12);return Q(`${a} × x ＝ ${a*x} のとき、x ＝ § 。`,x,`${a*x}÷${a}`,1)}const a=ri(r,2,9),b=ri(r,1,9),x=ri(r,2,9);return Q(`x＝${x} のとき、${a}x＋${b} の 値は § 。`,a*x+b,`${a}×${x}＋${b}`,1)},
  r=>{const t=pk(r,GD),n=ri(r,2,6),x=ri(r,2,9)*10;return{q:`1こ x円 の ${t}を ${n}こ かうと、だい金は ${n*x}円 でした。x に あてはまる 数を もとめましょう。`,a:`x ＝ ${x}`,e:`${n}×x＝${n*x} → x＝${n*x}÷${n}`}},
  r=>{const n=ri(r,2,6),x=ri(r,2,9)*10;return{q:`1こ x円 の りんごを ${n}こ と、100円の ケーキを 1こ かうと、だい金は ${n*x+100}円 でした。x の 値を もとめましょう。`,a:`x ＝ ${x}`,e:`${n}×x＋100＝${n*x+100} → x＝(${n*x+100}－100)÷${n}`}});
U('6g',6,'角柱・円柱の体積',r=>{if(r()<.5){const S=ri(r,10,60),h=ri(r,3,15);return Q(`底面積が ${S}cm²、高さが ${h}cm の 角柱の 体積は § cm³ 。`,S*h,`${S}×${h}`,1)}const x=ri(r,2,8),h=ri(r,3,12);return Q(`底面の 半径が ${x}cm、高さが ${h}cm の 円柱の 体積は § cm³ 。（円周率 3.14）`,num(x*x*h*314/100),`${x}×${x}×3.14×${h}`,1)},
  r=>{const x=ri(r,2,8),h=ri(r,3,12);return{q:`底面の 半径が ${x}cm、高さが ${h}cm の 円柱の 体積は なんcm³ ですか。（円周率 3.14）`,a:`${num(x*x*h*314/100)} cm³`,e:`${x}×${x}×3.14×${h}`}},
  r=>{const b=ri(r,2,8)*2,hh=ri(r,3,10),H=ri(r,4,12);return{q:`底面が 底辺 ${b}cm、高さ ${hh}cm の 三角形で、高さが ${H}cm の 三角柱の 体積は なんcm³ ですか。`,a:`${b*hh/2*H} cm³`,e:`底面積 ${b}×${hh}÷2＝${b*hh/2}、×${H}`}});


/* ========== 平成29年告示 学習指導要領に合わせた追加・差し替え単元 ========== */
const dv=(r,n,lo,hi)=>{const s=new Set();while(s.size<n)s.add(ri(r,lo,hi));return [...s].sort(()=>r()-.5)};
const dvs=n=>{const a=[];for(let i=1;i<=n;i++)if(n%i===0)a.push(i);return a};
const TBL=(hd,v,l1,l2)=>`<table class="tb"><tr><th>${l1}</th>${hd.map(x=>`<th>${x}</th>`).join('')}</tr><tr><th>${l2}</th>${v.map(x=>`<td>${x}</td>`).join('')}</tr></table>`;
const DAYS=['月','火','水','木','金'];
const SETS=[['すきな くだもの',['りんご','みかん','バナナ','ぶどう']],['すきな どうぶつ',['いぬ','ねこ','うさぎ','とり']],['すきな スポーツ',['サッカー','やきゅう','すいえい','バスケ']]];
const BAR=(L,V,max)=>{const w=34,gap=12,H=64,sc=H/max,W=L.length*(w+gap)+40;let s=`<svg viewBox="0 0 ${W} ${H+28}" style="display:block;margin:1mm 0;width:calc(${W}px*var(--fs));height:auto"><g font-size="9" fill="#111">`;for(let t=0;t<=max;t+=2){const y=H+4-t*sc;s+=`<line x1="30" x2="${W}" y1="${y}" y2="${y}" stroke="#bbb" stroke-width=".6"/><text x="26" y="${y+3}" text-anchor="end">${t}</text>`}L.forEach((l,i)=>{const x=36+i*(w+gap),hh=V[i]*sc;s+=`<rect x="${x}" y="${H+4-hh}" width="${w}" height="${hh}" fill="#888"/><text x="${x+w/2}" y="${H+16}" text-anchor="middle">${l}</text>`});return s+'</g></svg>'};
const kg=t=>`${Math.floor(t/1000)}kg ${t%1000}g`;

/* ---- 小2 ---- */
U('2f',2,'分数（1/2・1/4）',
  r=>{const d=pk(r,[2,4]);return Q(`1を ${d}こに おなじ 大きさに わけた 1こ分を 分数で あらわすと § 。`,fr(1,d),`${d}こに わけた 1つ分`)},
  r=>{const n=who(r),[t]=item(r),d=pk(r,[2,4]);return{q:`${n}は ${t}を おなじ 大きさに ${d}こに わけました。1こ分は もとの 大きさの なんぶんの いち ですか。`,a:fr(1,d),e:`${d}こに わけた 1こ分`}},
  r=>{const n=who(r);return{q:`${n}は ピザを おなじ 大きさに 4つに わけて、1つ たべました。たべた 分は ピザ ぜんたいの なんぶんの いち ですか。また、のこりは いくつ ですか。`,a:`${fr(1,4)}、のこりは 3つ`,e:'4－1＝3'}});
U('2g',2,'表とグラフ（かんたんな表）',
  r=>{const [ti,L]=pk(r,SETS),V=dv(r,4,1,9);return Q(`${ti}しらべ（人）${TBL(L,V,'しゅるい','人数')}いちばん おおいのは § です。`,L[V.indexOf(Math.max(...V))],'数が いちばん 大きい ところ')},
  r=>{const [ti,L]=pk(r,SETS),V=dv(r,4,1,9),s=V.reduce((a,b)=>a+b,0);return{q:`${ti}しらべの 表です。${TBL(L,V,'しゅるい','人数')}ぜんぶで なん人 ですか。`,a:`${s} 人`,e:V.join('＋')+`＝${s}`}},
  r=>{const [ti,L]=pk(r,SETS),V=dv(r,4,1,9),o=V.map((v,i)=>i).sort((a,b)=>V[b]-V[a]);return{q:`${ti}しらべの 表です。${TBL(L,V,'しゅるい','人数')}いちばん おおい ものと 2ばんめに おおい ものの ちがいは なん人 ですか。`,a:`${V[o[0]]-V[o[1]]} 人（${L[o[0]]}が おおい）`,e:`${V[o[0]]}－${V[o[1]]}`}});

/* ---- 小3 ---- */
U('3f',3,'重さ（g・kg）',
  r=>{const a=ri(r,1,9),b=ri(r,1,9)*100;if(r()<.5)return Q(`${a}kg ${b}g ＝ § g`,a*1000+b,`1kg＝1000g`);return Q(`${a*1000+b}g は なんkg なんg ですか。 §`,`${a}kg ${b}g`,`1000gで 1kg`)},
  r=>{const n=who(r),a=ri(r,1,3),b=ri(r,2,8)*100,c=ri(r,3,9)*100,t=a*1000+b+c;return{q:`${n}の ランドセルの おもさは ${a}kg ${b}g です。この ランドセルに ${c}g の 本を 入れると、ぜんぶで なんkg なんg ですか。`,a:kg(t),e:`${a*1000+b}＋${c}＝${t}g`}},
  r=>{const [tt]=item(r),a=ri(r,2,8)*50,n=ri(r,3,9),b=ri(r,2,8)*100,t=a*n+b;return{q:`1こ ${a}g の ${tt}を ${n}こ はこに 入れます。はこの おもさは ${b}g です。ぜんぶで なんkg なんg ですか。`,a:kg(t),e:`${a}×${n}＋${b}＝${t}g`}});
U('3g',3,'表と棒グラフ',
  r=>{const [ti,L]=pk(r,SETS),V=dv(r,4,2,10);return Q(`${ti}しらべ（人）${BAR(L,V,10)}いちばん おおいのは § です。`,L[V.indexOf(Math.max(...V))],'棒が いちばん 高い もの')},
  r=>{const [ti,L]=pk(r,SETS),V=dv(r,4,2,10),s=V.reduce((a,b)=>a+b,0);return{q:`${ti}しらべ（人）の 棒グラフです。${BAR(L,V,10)}ぜんぶで なん人 ですか。`,a:`${s} 人`,e:V.join('＋')+`＝${s}`}},
  r=>{const [ti,L]=pk(r,SETS),V=dv(r,4,2,10),o=V.map((v,i)=>i).sort((a,b)=>V[b]-V[a]);return{q:`${ti}しらべ（人）の 棒グラフです。${BAR(L,V,10)}${L[o[0]]}と ${L[o[1]]}を あわせると なん人 ですか。また、ちがいは なん人 ですか。`,a:`あわせて ${V[o[0]]+V[o[1]]}人、ちがいは ${V[o[0]]-V[o[1]]}人`,e:`${V[o[0]]}＋${V[o[1]]}、${V[o[0]]}－${V[o[1]]}`}});
U('3h',3,'三角形・円・球',
  r=>{const k=r();if(k<.34){const x=ri(r,2,12);return Q(`半径が ${x}cm の 円の 直径は § cm 。`,x*2,`直径＝半径×2`)}if(k<.67){const a=ri(r,3,15);return Q(`1辺が ${a}cm の 正三角形の まわりの 長さは § cm 。`,a*3,`${a}×3`)}const a=ri(r,4,12),b=ri(r,2,a+a-1);return Q(`辺の 長さが ${a}cm、${a}cm、${b}cm の 二等辺三角形の まわりの 長さは § cm 。`,a*2+b,`${a}＋${a}＋${b}`)},
  r=>{const n=ri(r,3,9),d=ri(r,4,12);return{q:`直径 ${d}cm の ボールを、はこに 1れつに ${n}こ ならべて 入れます。はこの 中の 長さは なんcm 以上 いりますか。`,a:`${d*n} cm`,e:`${d}×${n}`}},
  r=>{const a=ri(r,4,12),b=ri(r,2,a+a-1),P=2*a+b;return{q:`まわりの 長さが ${P}cm の 二等辺三角形が あります。おなじ 長さの 2つの 辺が ${a}cm の とき、のこりの 1つの 辺は なんcm ですか。`,a:`${b} cm`,e:`${P}－${a}－${a}`}});
U('3j',3,'□を使った式',
  r=>{const k=r(),a=ri(r,2,9);if(k<.34){const s=ri(r,12,60);return Q(`□ ＋ ${a} ＝ ${s} のとき、□ ＝ §`,s-a,`${s}－${a}`)}if(k<.67){const b=ri(r,2,9);return Q(`□ × ${a} ＝ ${a*b} のとき、□ ＝ §`,b,`${a*b}÷${a}`)}const b=ri(r,5,30);return Q(`□ － ${a} ＝ ${b} のとき、□ ＝ §`,a+b,`${b}＋${a}`)},
  r=>{const n=who(r),[t,u]=item(r),a=ri(r,2,9),s=ri(r,12,40);return{q:`${n}は ${t}を □${u} もっていました。${a}${u} もらったので、ぜんぶで ${s}${u} に なりました。はじめに もっていた ${t}は いくつ ですか。`,a:`${s-a} ${u}`,e:`□＋${a}＝${s} → □＝${s}－${a}`}},
  r=>{const t=pk(r,GD),a=ri(r,3,9)*10,n=ri(r,2,6),b=ri(r,3,9)*10;return{q:`1こ ${a}円の ${t}を □こ と、${b}円の けしゴムを 1こ かって、ぜんぶで ${a*n+b}円 でした。${t}は なんこ かいましたか。`,a:`${n} こ`,e:`${a}×□＋${b}＝${a*n+b} → □＝(${a*n+b}－${b})÷${a}`}});

/* ---- 小4 ---- */
U('4f',4,'角の大きさ',
  r=>{const k=r();if(k<.34){const a=ri(r,30,150);return Q(`一直線の 角は 180°です。一方の 角が ${a}° のとき、もう一方は § ° 。`,180-a,`180－${a}`)}if(k<.67){const a=ri(r,60,300);return Q(`1回転の 角は 360°です。${a}° の 角と あわせて 1回転に なる 角は § ° 。`,360-a,`360－${a}`)}const a=ri(r,10,80);return Q(`直角は 90°です。${a}° の 角と あわせて 直角に なる 角は § ° 。`,90-a,`90－${a}`)},
  r=>{const a=ri(r,20,100),b=ri(r,20,100);return{q:`分度器で はかったら、角アは ${a}°、角イは ${b}° でした。2つの 角を あわせると なん度 ですか。`,a:`${a+b}°`,e:`${a}＋${b}`}},
  r=>{const a=ri(r,30,80),b=ri(r,30,80);return{q:`一直線の 上に 3つの 角が ならんでいます。2つの 角が ${a}°と ${b}° のとき、のこりの 角は なん度 ですか。`,a:`${180-a-b}°`,e:`180－${a}－${b}`}});
U('4g',4,'ともなって変わる量・倍',
  r=>{const x=ri(r,3,12);if(r()<.5){const p=pk(r,[40,50,60,80]);return Q(`1こ ${p}円の おかしを x こ かうときの だい金を y円 と します。x＝${x} のとき、y ＝ §`,p*x,`y＝${p}×x＝${p}×${x}`)}const b=ri(r,3,9),m=ri(r,2,9);return Q(`${b*m}cm は ${b}cm の § 倍 です。`,m,`${b*m}÷${b}`)},
  r=>{const x=ri(r,3,12);return{q:`1辺が x cm の 正方形の まわりの 長さを y cm と します。x＝${x} のとき、y は なんcm ですか。`,a:`${4*x} cm`,e:`y＝4×x`}},
  r=>{if(r()<.5){const b=ri(r,3,9),m=ri(r,2,6);return{q:`赤い ひもは ${b}cm、青い ひもは 赤い ひもの ${m}倍 です。青い ひもは なんcm、2本 あわせると なんcm ですか。`,a:`青 ${b*m}cm、あわせて ${b+b*m}cm`,e:`${b}×${m}＝${b*m}、${b}＋${b*m}`}}const p=pk(r,[30,40,50,60]);return{q:`1本 ${p}円の えんぴつを x本 かうときの だい金を y円 と します。${TBL([1,2,3,4],[p,p*2,p*3,p*4],'x（本）','y（円）')}表を 見て、y ＝ ○ × x の ○ に あてはまる 数を 答えましょう。`,a:`${p}`,e:`x が 1ふえると y は ${p}ふえる`}});
U('4h',4,'折れ線グラフ・表の読み取り',
  r=>{const V=dv(r,5,5,40),n=who(r);return Q(`${n}が 1週間に 読んだ ページ数です。${TBL(DAYS,V,'曜日','ページ')}いちばん 多く 読んだのは § 曜日 です。`,DAYS[V.indexOf(Math.max(...V))],'いちばん 大きい 数')},
  r=>{const V=dv(r,5,5,40),n=who(r),s=V.reduce((a,b)=>a+b,0);return{q:`${n}が 5日間に 読んだ ページ数です。${TBL(DAYS,V,'曜日','ページ')}ぜんぶで なんページ 読みましたか。`,a:`${s} ページ`,e:V.join('＋')+`＝${s}`}},
  r=>{const t0=ri(r,14,18),inc=dv(r,4,0,6),T=[t0];inc.forEach(d=>T.push(T[T.length-1]+d));const i=inc.indexOf(Math.max(...inc));return{q:`ある 日の 気温を 1時間ごとに はかった 表です。${TBL(['9時','10時','11時','12時','13時'],T.map(x=>x+'℃'),'時こく','気温')}気温が いちばん 大きく 上がったのは、なん時から なん時の あいだ ですか。`,a:`${9+i}時から ${10+i}時（${inc[i]}℃ 上がった）`,e:'となりどうしの 差を くらべる'}});

/* ---- 小5 ---- */
U('5h',5,'整数の性質（偶数・奇数・倍数・約数）',
  r=>{const k=r();if(k<.2){const n=ri(r,11,99);return Q(`${n} は 偶数 ですか、奇数 ですか。 §`,n%2?'奇数':'偶数','2で わりきれるか')}if(k<.4){const a=ri(r,3,9);return Q(`${a} の 倍数を 小さい ほうから 3つ 書きましょう。 §`,`${a}、${a*2}、${a*3}`,`${a}×1、${a}×2、${a}×3`)}if(k<.6){const n=pk(r,[12,18,20,24,28,30,36,40,42,45,48]);return Q(`${n} の 約数を すべて 書きましょう。 §`,dvs(n).join('、'),'わりきれる 整数を さがす',2)}if(k<.8){const a=ri(r,2,9);let b=ri(r,2,9);if(a===b)b=a===9?2:a+1;return Q(`${a}と ${b} の 最小公倍数は § 。`,lcm(a,b),`${a}の 倍数と ${b}の 倍数で 最初の 共通の 数`)}const [a,b]=pk(r,[[12,18],[8,12],[12,20],[18,24],[16,24],[20,30],[24,36],[15,25]]);return Q(`${a}と ${b} の 最大公約数は § 。`,gcd(a,b),`${a}と ${b} の 共通の 約数の うち いちばん 大きい 数`,2)},
  r=>{const a=pk(r,[3,4,5,6,8]);let b=pk(r,[3,4,5,6,8,10]);if(a===b)b=12;return{q:`${who(r)}は ${a}日ごとに、${who(r)}は ${b}日ごとに 図書室へ 行きます。きょう 2人は 会いました。つぎに 2人が 図書室で 会うのは なん日後 ですか。`,a:`${lcm(a,b)} 日後`,e:`${a}と ${b} の 最小公倍数`}},
  r=>{const [a,b]=pk(r,[[12,18],[16,24],[20,30],[24,36],[18,27],[30,45]]);return{q:`たて ${a}cm、よこ ${b}cm の 長方形の 紙を、あまりが 出ないように おなじ 大きさの 正方形に 切ります。できるだけ 大きい 正方形の 1辺は なんcm ですか。`,a:`${gcd(a,b)} cm`,e:`${a}と ${b} の 最大公約数`}});
U('5i',5,'円周と円周率',
  r=>{if(r()<.5){const d=ri(r,2,20);return Q(`直径 ${d}cm の 円の 円周は § cm 。（円周率 3.14）`,num(d*314/100),`円周＝直径×3.14＝${d}×3.14`,1)}const d=pk(r,[5,10,20,25,50]);return Q(`円周が ${num(d*314/100)}cm の 円の 直径は § cm 。（円周率 3.14）`,d,`直径＝円周÷3.14`,1)},
  r=>{const d=ri(r,3,20);return{q:`直径 ${d}cm の 円形の ケーキの まわりに、リボンを 1しゅう まきます。リボンは なんcm いりますか。（円周率 3.14）`,a:`${num(d*314/100)} cm`,e:`${d}×3.14`}},
  r=>{const d=ri(r,3,12),n=ri(r,2,5);return{q:`直径 ${d}m の 円形の 池の まわりを ${n}しゅう 歩きました。歩いた 道のりは なんm ですか。（円周率 3.14）`,a:`${num(d*314*n/100)} m`,e:`${d}×3.14×${n}`}});
U('5j',5,'速さ・単位量あたりの大きさ',
  r=>{const v=ri(r,30,80),t=ri(r,2,5),k=r();if(k<.34)return Q(`時速 ${v}km で ${t}時間 走ると、道のりは § km 。`,v*t,`道のり＝速さ×時間：${v}×${t}`);if(k<.67)return Q(`${v*t}km を ${t}時間 で 走る 速さは 時速 § km 。`,v,`速さ＝道のり÷時間：${v*t}÷${t}`);return Q(`${v*t}km の 道のりを 時速 ${v}km で 走ると、かかる 時間は § 時間 。`,t,`時間＝道のり÷速さ：${v*t}÷${v}`)},
  r=>{const v=ri(r,50,90),t=ri(r,5,20);return{q:`分速 ${v}m で ${t}分 歩くと、なんm すすみますか。`,a:`${v*t} m`,e:`${v}×${t}`}},
  r=>{if(r()<.5){const m1=ri(r,4,9),m2=ri(r,4,9),d1=ri(r,2,5);let d2=ri(r,2,5);if(d2===d1)d2=d1===5?2:d1+1;return{q:`A室は ${m1}m²に ${m1*d1}人、B室は ${m2}m²に ${m2*d2}人 います。1m²あたりの 人数で くらべると、どちらが こんでいますか。`,a:`${d1>d2?'A室':'B室'}（A室 ${d1}人／B室 ${d2}人）`,e:'人数÷面積 で くらべる'}}const a=pk(r,[40,50,60,80]),b=ri(r,2,6),D=a*b,cs=[20,30,40,60].filter(c=>c!==a&&D%c===0),c=cs.length?pk(r,cs):a;return{q:`A町から B町まで 時速 ${a}km で ${b}時間 かかりました。帰りは 時速 ${c}km で 帰りました。帰りに かかった 時間は なん時間 ですか。`,a:`${D/c} 時間`,e:`道のり ${a}×${b}＝${D}km → ${D}÷${c}`}});
U('5k',5,'三角形・四角形・多角形の角',
  r=>{const k=r();if(k<.34){const a=ri(r,30,80),b=ri(r,30,80);return Q(`三角形の 2つの 角が ${a}°と ${b}° のとき、のこりの 角は § ° 。`,180-a-b,`三角形の 角の 和は 180°：180－${a}－${b}`)}if(k<.67){const a=ri(r,60,110),b=ri(r,60,110),c=ri(r,60,110);return Q(`四角形の 3つの 角が ${a}°、${b}°、${c}° のとき、のこりの 角は § ° 。`,360-a-b-c,`四角形の 角の 和は 360°`)}const n=pk(r,[5,6,7,8]);return Q(`${['','','','','','五','六','七','八'][n]}角形の 角の 和は § ° 。`,(n-2)*180,`(${n}－2)×180`)},
  r=>{const a=ri(r,30,80),b=ri(r,30,80);return{q:`三角形の 3つの 角のうち、2つが ${a}°と ${b}° です。のこりの 角は なん度 ですか。`,a:`${180-a-b}°`,e:`180－${a}－${b}`}},
  r=>{const a=ri(r,60,110),b=ri(r,60,110),c=ri(r,60,110);return{q:`四角形の 3つの 角が ${a}°、${b}°、${c}° です。のこりの 角は なん度 ですか。`,a:`${360-a-b-c}°`,e:`四角形の 角の 和は 360°：360－${a}－${b}－${c}`}});

/* ---- 小6 ---- */
U('6c',6,'円の面積',
  r=>{if(r()<.5){const x=ri(r,2,12);return Q(`半径 ${x}cm の 円の 面積は § cm² 。（円周率 3.14）`,num(x*x*314/100),`半径×半径×3.14＝${x}×${x}×3.14`,1)}const d=ri(r,2,10)*2,x=d/2;return Q(`直径 ${d}cm の 円の 面積は § cm² 。（円周率 3.14）`,num(x*x*314/100),`半径は ${x}cm：${x}×${x}×3.14`,1)},
  r=>{const x=ri(r,3,15);return{q:`半径 ${x}cm の 円形の 花だんが あります。この 花だんの 面積は なんcm² ですか。（円周率 3.14）`,a:`${num(x*x*314/100)} cm²`,e:`${x}×${x}×3.14`}},
  r=>{const a=ri(r,5,12),b=ri(r,2,a-2);return{q:`半径 ${a}cm の 円から 半径 ${b}cm の 円を くりぬきました。のこった 部分の 面積は なんcm² ですか。（円周率 3.14）`,a:`${num((a*a-b*b)*314/100)} cm²`,e:`(${a}×${a}－${b}×${b})×3.14`}});
U('6e',6,'比例・反比例',
  r=>{const k=ri(r,2,9),x1=ri(r,2,6),x2=ri(r,7,12);if(r()<.5)return Q(`y は x に 比例 します。x＝${x1} のとき y＝${k*x1} です。x＝${x2} のとき、y ＝ §`,k*x2,`y＝${k}×x`);const P=pk(r,[12,24,36,48]),ds=dvs(P).filter(d=>d>1&&d<P),a=pk(r,ds);let b=pk(r,ds);if(b===a)b=ds.find(d=>d!==a);return Q(`y は x に 反比例 します。x＝${a} のとき y＝${P/a} です。x＝${b} のとき、y ＝ §`,P/b,`x×y＝${P} で 決まった 数`)},
  r=>{const k=ri(r,2,9),x1=ri(r,2,6),x2=ri(r,7,12);return{q:`ばねに ${x1}g の おもりを つるすと ${k*x1}mm のびました。のびは おもりの おもさに 比例します。${x2}g の おもりでは なんmm のびますか。`,a:`${k*x2} mm`,e:`1gあたり ${k}mm → ${k}×${x2}`}},
  r=>{const P=12*ri(r,2,10),ds=[2,3,4,6,12],a=pk(r,ds);let b=pk(r,ds);if(a===b)b=a===12?2:a+1<=12&&ds.includes(a+1)?a+1:12;if(b===a)b=2;return{q:`${P}L の 水そうに 水を 入れます。1分間に ${a}L ずつ 入れると ${P/a}分 かかります。水を 入れる 量が 1分間 ${b}L の とき、いっぱいに なるまで なん分 かかりますか。（時間は 1分間に 入れる 量に 反比例）`,a:`${P/b} 分`,e:`${P}÷${b}`}});
U('6h',6,'データの活用（代表値・度数分布）',
  r=>{const m=ri(r,6,15),o=[];while(o.length<4){const v=ri(r,3,20);if(v!==m&&!o.includes(v))o.push(v)}const arr=[m,m,m,...o].sort(()=>r()-.5),s=[...arr].sort((a,b)=>a-b);if(r()<.5)return Q(`ソフトボール投げの きろく（m）：${arr.join('、')}。この データの 最頻値は § m 。`,m,'いちばん 多く 出てくる 数');return Q(`ソフトボール投げの きろく（m）：${arr.join('、')}。この データの 中央値は § m 。`,s[3],`小さい じゅんに ならべて 真ん中：${s.join('、')}`)},
  r=>{const m=ri(r,40,80),o=[];while(o.length<6){const v=ri(r,m-20,m+20);if(v!==m&&!o.includes(v))o.push(v)}const arr=[...o,m].sort(()=>r()-.5),s=[...arr].sort((a,b)=>a-b);return{q:`7人の クイズの 得点（点）です。${arr.join('、')}。中央値は なん点 ですか。`,a:`${s[3]} 点`,e:`小さい じゅんに：${s.join('、')} の 真ん中`}},
  r=>{const C=dv(r,5,1,9),cut=pk(r,[20,25]),idx=cut===20?[2,3,4]:[3,4],s=idx.reduce((a,i)=>a+C[i],0);return{q:`6年生の ソフトボール投げの きろくを 度数分布表に しました。${TBL(['10以上<br>15未満','15以上<br>20未満','20以上<br>25未満','25以上<br>30未満','30以上<br>35未満'],C,'きょり（m）','人数（人）')}${cut}m 以上 投げた 人は あわせて なん人 ですか。`,a:`${s} 人`,e:idx.map(i=>C[i]).join('＋')+`＝${s}`}});
U('6i',6,'場合の数（並べ方・組み合わせ）',
  r=>{if(r()<.5){const n=ri(r,3,4),f=n===3?6:24;return Q(`${['','','','A、B、C の 3人','A、B、C、D の 4人'][n]}が 1列に ならぶ ならび方は § 通り 。`,f,n===3?'3×2×1':'4×3×2×1')}const n=ri(r,4,6),c=n*(n-1)/2;return Q(`${n}人の 中から 2人の 委員を えらぶ えらび方は § 通り 。`,c,`${n}×${n-1}÷2`)},
  r=>{const n=ri(r,4,7);return{q:`${n}チームで、どのチームとも 1回ずつ 試合を する 総当たり戦を します。試合は ぜんぶで なん試合 ですか。`,a:`${n*(n-1)/2} 試合`,e:`${n}×${n-1}÷2`}},
  r=>{if(r()<.5)return{q:`1、2、3、4 の 4まいの カードから 3まいを えらんで ならべて、3けたの 整数を つくります。同じ カードは 1回しか つかえません。整数は なん通り できますか。`,a:'24 通り',e:'4×3×2'};return{q:`0、1、2、3 の 4まいの カードから 3まいを えらんで ならべて、3けたの 整数を つくります。同じ カードは 1回しか つかえません。整数は なん通り できますか。`,a:'18 通り',e:'百の位は 0 以外：3×3×2'}});
U('6j',6,'拡大図と縮図',
  r=>{const S=pk(r,[500,1000,2000,5000]),a=ri(r,2,12);if(r()<.5)return Q(`縮尺が 1：${S} の 地図で ${a}cm の 道は、実さいには なんm ですか。 §m`,a*S/100,`${a}×${S}＝${a*S}cm → m に なおす`);const k=ri(r,2,4),b=ri(r,3,9);return Q(`ある 図形を ${k}倍に 拡大しました。もとの 図形の 辺が ${b}cm の とき、拡大図の 対応する 辺は § cm 。`,b*k,`${b}×${k}`)},
  r=>{const S=pk(r,[500,1000,2000,5000]),a=ri(r,3,10);return{q:`縮尺が 1：${S} の 地図で、2つの 家の きょりは ${a}cm でした。実さいの きょりは なんm ですか。`,a:`${a*S/100} m`,e:`${a}×${S}＝${a*S}cm＝${a*S/100}m`}},
  r=>{const S=pk(r,[500,1000,2000,5000]),D=(S/100)*ri(r,2,10);return{q:`実さいには ${D}m ある 道を、縮尺 1：${S} の 地図に かきます。地図の 上では なんcm に なりますか。`,a:`${D*100/S} cm`,e:`${D}m＝${D*100}cm → ${D*100}÷${S}`}});


/* ========== 作図・図を使う問題（方眼ベース / 平成29年告示 図形・データの活用） ========== */
const RED='#d40000';
const mkG=(c,rw,s,m={})=>{
  const l=m.l??8,t=m.t??8,rr=m.r??8,b=m.b??8,W=c*s+l+rr,H=rw*s+t+b;
  const X=x=>+(l+x*s).toFixed(2),Y=y=>+(t+(rw-y)*s).toFixed(2);
  let g='';
  for(let i=0;i<=c;i++)g+=`<line x1="${X(i)}" y1="${t}" x2="${X(i)}" y2="${t+rw*s}" stroke="#c4c4c4" stroke-width=".7"/>`;
  for(let j=0;j<=rw;j++)g+=`<line x1="${l}" y1="${Y(j)}" x2="${l+c*s}" y2="${Y(j)}" stroke="#c4c4c4" stroke-width=".7"/>`;
  const pts=a=>a.map(p=>X(p[0])+','+Y(p[1])).join(' ');
  return{W,H,c,rw,s,X,Y,base:g,
   poly:(a,col='#111',w=1.9)=>`<polygon points="${pts(a)}" fill="none" stroke="${col}" stroke-width="${w}" stroke-linejoin="round"/>`,
   pl:(a,col='#111',w=1.9)=>`<polyline points="${pts(a)}" fill="none" stroke="${col}" stroke-width="${w}" stroke-linejoin="round" stroke-linecap="round"/>`,
   ln:(p,q,col='#111',w=1.9,dash='')=>`<line x1="${X(p[0])}" y1="${Y(p[1])}" x2="${X(q[0])}" y2="${Y(q[1])}" stroke="${col}" stroke-width="${w}" ${dash?`stroke-dasharray="${dash}"`:''} stroke-linecap="round"/>`,
   dot:(p,col='#111',r=3)=>`<circle cx="${X(p[0])}" cy="${Y(p[1])}" r="${r}" fill="${col}"/>`,
   lab:(p,tx,dx=5,dy=-5,col='#111')=>`<text x="${X(p[0])+dx}" y="${Y(p[1])+dy}" font-size="12" font-weight="700" fill="${col}">${tx}</text>`,
   text:(x,y,tx,an='middle',size=9)=>`<text x="${x}" y="${y}" font-size="${size}" text-anchor="${an}" fill="#111">${tx}</text>`,
   long:(p,d,col='#111',w=1.9)=>{let t0=-1e9,t1=1e9;[[p[0],d[0],c],[p[1],d[1],rw]].forEach(([q,v,M])=>{if(v===0)return;const a=(0-q)/v,b2=(M-q)/v;t0=Math.max(t0,Math.min(a,b2));t1=Math.min(t1,Math.max(a,b2))});
     return `<line x1="${X(p[0]+t0*d[0])}" y1="${Y(p[1]+t0*d[1])}" x2="${X(p[0]+t1*d[0])}" y2="${Y(p[1]+t1*d[1])}" stroke="${col}" stroke-width="${w}" stroke-linecap="round"/>`}
  }};
const SVG=(G,inner)=>`<svg viewBox="0 0 ${G.W} ${G.H}" style="display:block;margin:1mm 0;width:calc(${G.W}px*var(--fs));height:auto;max-width:100%">${G.base}${inner}</svg>`;
const AG=s=>`<g class="ag">${s}</g>`;
const DR=(q,e)=>({q,a:'',e,sp:0,draw:true});
const cross=(a,b)=>a[0]*b[1]-a[1]*b[0];

/* ---- 小3 ---- */
U('3k',3,'二等辺三角形をかく（方眼）',
  r=>{const m=ri(r,2,4),h=ri(r,2,4),G=mkG(13,6,17),x0=ri(r,1,12-2*m),A=[x0,1],B=[x0+2*m,1],M=[x0+m,1+h];
    return DR(`点Aと 点Bを むすぶ 線を 底辺に して、二等辺三角形を かきましょう。${SVG(G,G.ln(A,B)+G.dot(A)+G.dot(B)+G.lab(A,'A',-12,13)+G.lab(B,'B',3,13)+AG(G.ln(A,M,RED)+G.ln(M,B,RED)+G.dot(M,RED)))}`,`ちょう点は 底辺の まん中（Aから ${m}めもり 右）の 真上 ${h}めもり`)},
  r=>{const a=ri(r,3,15);return{q:`1辺が ${a}cm の 正三角形の 形に ひもを まげました。ひもの 長さは なんcm ですか。`,a:`${3*a} cm`,e:`${a}×3`}},
  r=>{const a=ri(r,5,12),b=ri(r,2,2*a-2),P=2*a+b;return{q:`まわりの 長さが ${P}cm で、底辺が ${b}cm の 二等辺三角形が あります。等しい 辺の 長さは 1つ なんcm ですか。`,a:`${a} cm`,e:`(${P}－${b})÷2`}});
const BARDRAW=(L,V)=>{const G=mkG(8,10,17,{l:24,b:16});let s='';for(let t=0;t<=10;t+=2)s+=G.text(G.X(0)-4,G.Y(t)+3,t,'end',9);
  L.forEach((x,i)=>{s+=G.text(G.X(2*i+1),G.Y(0)+12,x,'middle',8)});
  let ans='';V.forEach((v,i)=>{ans+=`<rect x="${G.X(2*i+.4)}" y="${G.Y(v)}" width="${+(1.2*G.s).toFixed(1)}" height="${v*G.s}" fill="${RED}" fill-opacity=".5" stroke="${RED}"/>`});
  return SVG(G,s+AG(ans))};
U('3m',3,'棒グラフをかく（方眼）',
  r=>{const [ti,L]=pk(r,SETS),V=dv(r,4,2,9);return DR(`${ti}しらべの 結果です。${TBL(L,V,'しゅるい','人数（人）')}棒グラフに あらわしましょう。（たてのめもり 1つぶんが 1人）${BARDRAW(L,V)}`,'表の 数だけ 下から ぼうを ぬる')},
  r=>{const [ti,L]=pk(r,SETS),V=dv(r,4,2,10),o=V.map((v,i)=>i).sort((a,b)=>V[b]-V[a]);return{q:`${ti}しらべの 棒グラフです。${BAR(L,V,10)}いちばん 多い ものと いちばん 少ない ものの ちがいは なん人 ですか。`,a:`${V[o[0]]-V[o[3]]} 人`,e:`${V[o[0]]}－${V[o[3]]}`}},
  r=>{const [ti,L]=pk(r,SETS),V=dv(r,4,2,10);return{q:`${ti}しらべの 棒グラフです。${BAR(L,V,10)}${L[0]}と ${L[1]}を あわせた 人数は、${L[2]}より なん人 多い ですか。（少ない ときは「なん人 少ない」）`,a:`${Math.abs(V[0]+V[1]-V[2])} 人 ${V[0]+V[1]>=V[2]?'多い':'少ない'}`,e:`${V[0]}＋${V[1]}＝${V[0]+V[1]}、${V[2]}と くらべる`}});

/* ---- 小4 ---- */
U('4i',4,'平行・垂直な直線をかく（方眼）',
  r=>{const G=mkG(13,8,17),D=pk(r,[[3,1],[2,1],[1,2],[3,2],[2,3],[1,1],[1,3]]),d=[D[0],D[1]*(r()<.5?1:-1)];let A,B,C,ok=false;
    for(let i=0;i<80&&!ok;i++){A=[ri(r,2,7),ri(r,2,6)];B=[A[0]+d[0],A[1]+d[1]];C=[ri(r,1,12),ri(r,1,7)];const cr=Math.abs(cross([C[0]-A[0],C[1]-A[1]],d));ok=B[0]<=13&&B[1]>=0&&B[1]<=8&&cr>=3&&Math.hypot(C[0]-A[0],C[1]-A[1])>2.5&&Math.hypot(C[0]-B[0],C[1]-B[1])>2.5}
    if(!ok){A=[3,3];B=[A[0]+d[0],A[1]+d[1]];C=[8,1]}
    const par=r()<.5,dir=par?d:[-d[1],d[0]];
    return DR(`点Cを 通って、直線ABに ${par?'平行':'垂直'}な 直線を 引きましょう。${SVG(G,G.long(A,d)+G.dot(A)+G.dot(B)+G.dot(C)+G.lab(A,'A',-12,13)+G.lab(B,'B',6,B[1]>=7?14:-6)+G.lab(C,'C',6,C[1]>=7?14:-6)+AG(G.long(C,dir,RED)))}`,par?`Cから 直線ABと 同じ 向き（右へ ${d[0]}、${d[1]>0?'上':'下'}へ ${Math.abs(d[1])}）に すすむ 線を ひく`:`Cから 向きを 90°かえた（右へ ${Math.abs(dir[0])}、${dir[0]*dir[1]>0?'上':'下'}へ ...）線`)},
  r=>{const a=r()<.5?ri(r,50,85):ri(r,95,130);return{q:`平行四辺形ABCDで、角Aは ${a}° です。角Bは なん度 ですか。`,a:`${180-a}°`,e:`となりあう 角の 和は 180°：180－${a}`}},
  r=>{const x=ri(r,4,12),y=ri(r,3,10),a=ri(r,55,85);return{q:`平行四辺形ABCDで、辺ABは ${x}cm、辺BCは ${y}cm、角Aは ${a}° です。まわりの 長さは なんcm ですか。また、角Cは なん度 ですか。`,a:`${2*(x+y)}cm、${a}°`,e:`向かいあう 辺・角は 等しい：(${x}＋${y})×2、角C＝角A`}});
const TIMES=['9時','10時','11時','12時','13時'];
const genT=r=>{for(let k=0;k<60;k++){let v=ri(r,6,9)*2;const T=[v],rs=[];for(let i=0;i<4;i++){let d=ri(r,-2,2)*2;if(v+d<10||v+d>26)d=-d;if(v+d<10||v+d>26)d=0;v+=d;T.push(v);rs.push(d)}const m=Math.max(...rs);if(m>0&&rs.filter(x=>x===m).length===1&&new Set(T).size>=3)return T}return[12,14,18,20,22]};
const uniqMax=T=>T.filter(x=>x===Math.max(...T)).length===1;
const LINEG=(T,given)=>{const G=mkG(6,8,21,{l:28,t:20,b:16});let s=G.text(G.X(0)-4,11,'(℃)','end',9);for(let j=0;j<=8;j++)s+=G.text(G.X(0)-4,G.Y(j)+3,10+2*j,'end',9);
  TIMES.forEach((t,i)=>s+=G.text(G.X(i+1),G.Y(0)+12,t,'middle',9));
  const pts=T.map((v,i)=>[i+1,(v-10)/2]),dr=col=>G.pl(pts,col,1.9)+pts.map(p=>G.dot(p,col,3)).join('');
  return SVG(G,s+(given?dr('#111'):AG(dr(RED))))};
U('4j',4,'折れ線グラフをかく・読む（方眼）',
  r=>{const T=genT(r);return DR(`ある 日の 気温を 1時間ごとに はかりました。${TBL(TIMES,T.map(x=>x+'℃'),'時こく','気温')}折れ線グラフに あらわしましょう。（点を うって、線で むすぶ）${LINEG(T,false)}`,'時こくごとに 点を うち、となりの 点を 線で むすぶ')},
  r=>{let T,i=0;do{T=genT(r)}while(!uniqMax(T)&&++i<30);const im=T.indexOf(Math.max(...T));return{q:`ある 日の 気温の 折れ線グラフです。${LINEG(T,true)}気温が いちばん 高かったのは なん時で、そのときの 気温は なん℃ ですか。`,a:`${TIMES[im]}、${T[im]}℃`,e:'グラフの いちばん 高い 点'}},
  r=>{const T=genT(r),rs=T.slice(1).map((v,i)=>v-T[i]),im=rs.indexOf(Math.max(...rs));return{q:`ある 日の 気温の 折れ線グラフです。${LINEG(T,true)}気温が いちばん 大きく 上がったのは、なん時から なん時の あいだ ですか。また、なん℃ 上がりましたか。`,a:`${TIMES[im]}から ${TIMES[im+1]}、${rs[im]}℃`,e:'線の かたむきが いちばん 急な ところ'}});
U('4k',4,'平行四辺形をかく（方眼）',
  r=>{const G=mkG(13,7,17),u1=ri(r,3,5),v1=ri(r,0,1),u2=ri(r,-2,1),v2=ri(r,2,3),rel=[[0,0],[u1,v1],[u1+u2,v1+v2],[u2,v2]],xs=rel.map(p=>p[0]),ys=rel.map(p=>p[1]),ox=ri(r,1-Math.min(...xs),12-Math.max(...xs)),oy=ri(r,1-Math.min(...ys),6-Math.max(...ys)),[A,B,C,D]=rel.map(p=>[p[0]+ox,p[1]+oy]);
    return DR(`点A、B、C を ちょう点に もつ 平行四辺形ABCD を かきましょう。${SVG(G,G.pl([A,B,C])+G.dot(A)+G.dot(B)+G.dot(C)+G.lab(A,'A',-12,13)+G.lab(B,'B',4,13)+G.lab(C,'C',4,-6)+AG(G.pl([C,D,A],RED)+G.dot(D,RED)+G.lab(D,'D',-13,-6,RED)))}`,`点Dは、点Aから 辺BCと 同じ だけ すすんだ ところ（辺ADは 辺BCと 平行で 同じ 長さ）`)},
  r=>{const a=ri(r,3,15);return{q:`ひし形の 1辺が ${a}cm の とき、まわりの 長さは なんcm ですか。`,a:`${4*a} cm`,e:`${a}×4`}},
  r=>{const x=r()<.5?ri(r,60,85):ri(r,95,120);return{q:`台形ABCDで、辺ADと 辺BCが 平行です。角Aが ${x}° のとき、角Bは なん度 ですか。`,a:`${180-x}°`,e:`平行な 線に はさまれた 角の 和は 180°：180－${x}`}});

/* ---- 小5 ---- */
U('5l',5,'合同な三角形をかく（方眼）',
  r=>{const G=mkG(17,7,16),bx=ri(r,2,4),by=ri(r,0,1);let cx=ri(r,0,3),cy=ri(r,2,4);if(cross([bx,by],[cx,cy])<=0){cx=0;cy=3}
    const a0=[ri(r,1,2),ri(r,1,2)],A=a0,B=[a0[0]+bx,a0[1]+by],C=[a0[0]+cx,a0[1]+cy],Pt=[ri(r,9,11),ri(r,1,2)],B2=[Pt[0]+bx,Pt[1]+by],C2=[Pt[0]+cx,Pt[1]+cy];
    return DR(`三角形ABCと 合同な 三角形を、点Pを 点Aに 対応する ちょう点に して かきましょう。（向きは 同じで よい）${SVG(G,G.poly([A,B,C])+G.dot(A)+G.dot(Pt)+G.lab(A,'A',-12,13)+G.lab(B,'B',4,13)+G.lab(C,'C',4,-6)+G.lab(Pt,'P',-12,13)+AG(G.poly([Pt,B2,C2],RED)+G.dot(B2,RED)+G.dot(C2,RED)))}`,`点Aから B・C まで すすんだ 分だけ、点Pからも すすんで 点を とる`)},
  r=>{const x=ri(r,3,12),y=ri(r,35,85);return{q:`三角形ABCと 三角形DEFは 合同で、ちょう点A、B、Cに D、E、Fが それぞれ 対応しています。辺ABが ${x}cm、角Bが ${y}° のとき、辺DEは なんcm、角Eは なん度 ですか。`,a:`${x}cm、${y}°`,e:'合同な 図形では 対応する 辺の 長さ・角の 大きさは 等しい'}},
  r=>{const p=ri(r,30,80),q=ri(r,30,80);return{q:`三角形ABCと 三角形DEFは 合同で、A、B、Cに D、E、Fが それぞれ 対応しています。角Aが ${p}°、角Bが ${q}° のとき、角Fは なん度 ですか。`,a:`${180-p-q}°`,e:`角C＝180－${p}－${q}、角F＝角C`}});
const PIE=(L,Pc)=>{const cx=70,cy=70,R=62,cl=['#ececec','#d2d2d2','#b9b9b9','#a0a0a0'];let a0=-Math.PI/2,s='';
  Pc.forEach((p,i)=>{const a1=a0+p/100*2*Math.PI,x0=cx+R*Math.cos(a0),y0=cy+R*Math.sin(a0),x1=cx+R*Math.cos(a1),y1=cy+R*Math.sin(a1),am=(a0+a1)/2,tx=cx+R*.66*Math.cos(am),ty=cy+R*.66*Math.sin(am);
    s+=`<path d="M${cx},${cy} L${x0.toFixed(1)},${y0.toFixed(1)} A${R},${R} 0 ${p>50?1:0} 1 ${x1.toFixed(1)},${y1.toFixed(1)} Z" fill="${cl[i]}" stroke="#111" stroke-width="1"/><text x="${tx.toFixed(1)}" y="${(ty-1).toFixed(1)}" font-size="8" text-anchor="middle" fill="#111">${L[i]}</text><text x="${tx.toFixed(1)}" y="${(ty+9).toFixed(1)}" font-size="8" text-anchor="middle" fill="#111">${p}%</text>`;a0=a1});
  return `<svg viewBox="0 0 140 140" style="display:block;margin:1mm 0;width:calc(140px*var(--fs));height:auto">${s}</svg>`};
const PCT=[[40,30,20,10],[50,25,15,10],[35,30,20,15],[45,25,20,10],[40,25,20,15],[30,30,25,15]];
const pieSet=r=>{const [ti,L]=pk(r,SETS),Pc=[...pk(r,PCT)],T=pk(r,[200,300,400,500]);return[ti,L,Pc,T]};
U('5m',5,'円グラフの読み取り',
  r=>{const [ti,L,Pc,T]=pieSet(r),i=ri(r,0,3);return{q:`${ti}しらべの 結果を あらわした 円グラフです。（全体を 100％ と します）${PIE(L,Pc)}全体の 人数は ${T}人 です。「${L[i]}」と 答えた 人は § 人 です。`,a:Pc[i]*T/100,e:`${T}×${Pc[i]}/100`,sp:1}},
  r=>{const [ti,L,Pc,T]=pieSet(r),mxi=Pc.indexOf(Math.max(...Pc)),mni=Pc.indexOf(Math.min(...Pc));return{q:`${ti}しらべの 結果を あらわした 円グラフです。${PIE(L,Pc)}全体の 人数は ${T}人 です。いちばん 多い ものと いちばん 少ない ものの 人数の ちがいは なん人 ですか。`,a:`${(Pc[mxi]-Pc[mni])*T/100} 人`,e:`(${Pc[mxi]}－${Pc[mni]})％ ＝ ${(Pc[mxi]-Pc[mni])*T/100}人`}},
  r=>{const [ti,L,Pc,T]=pieSet(r),i=ri(r,0,1),j=ri(r,2,3);return{q:`${ti}しらべの 結果を あらわした 円グラフです。${PIE(L,Pc)}全体の 人数は ${T}人 です。「${L[i]}」と「${L[j]}」を あわせると、全体の なん％ で、なん人 ですか。`,a:`${Pc[i]+Pc[j]}％、${(Pc[i]+Pc[j])*T/100}人`,e:`${Pc[i]}＋${Pc[j]}＝${Pc[i]+Pc[j]}％、${T}×${(Pc[i]+Pc[j])/100}`}});

/* ---- 小6 ---- */
const KJ={3:'三',4:'四',5:'五',6:'六',8:'八'};
U('6k',6,'線対称・点対称な図形をかく（方眼）',
  r=>{const G=mkG(14,8,16);
    if(r()<.5){const y1=ri(r,1,2),y2=ri(r,5,7),n=Math.min(ri(r,2,3),y2-y1-1),ys=[];while(ys.length<n){const y=ri(r,y1+1,y2-1);if(!ys.includes(y))ys.push(y)}ys.sort((a,b)=>a-b);
      const half=[[7,y1],...ys.map(y=>[7-ri(r,1,5),y]),[7,y2]],mir=half.map(p=>[14-p[0],p[1]]);
      return DR(`直線ℓを 対称の 軸と する 線対称な 図形を、右がわに かんせい させましょう。${SVG(G,G.ln([7,0],[7,8],'#111',1.2,'5 3')+G.lab([7,8],'ℓ',5,-1)+G.pl(half)+AG(G.pl(mir,RED)))}`,'軸から おなじ きょりの ところに、点を 反対がわに うつす')}
    let A,B,C,D,ok=false;const g=()=>[ri(r,8,12),ri(r,3,7)];
    for(let i=0;i<80&&!ok;i++){A=g();B=g();C=g();if(cross([B[0]-A[0],B[1]-A[1]],[C[0]-A[0],C[1]-A[1]])===0)continue;D=r()<.5?[A[0]+C[0]-B[0],A[1]+C[1]-B[1]]:null;if(D&&(D[0]<8||D[0]>12||D[1]<3||D[1]>7))D=null;ok=true}
    if(!ok){A=[9,4];B=[11,4];C=[10,6];D=null}
    const sh=D?[A,B,C,D]:[A,B,C],rot=sh.map(p=>[14-p[0],8-p[1]]);
    return DR(`点Oを 対称の 中心と する 点対称な 図形を、点Oの 反対がわに かんせい させましょう。${SVG(G,G.poly(sh)+G.dot([7,4],'#111',3.5)+G.lab([7,4],'O',5,-6)+AG(G.poly(rot,RED)+rot.map(p=>G.dot(p,RED,2.5)).join('')))}`,'点Oを 通る 直線の 上に、Oからの きょりが 同じに なるように 点を うつす')},
  r=>{const x=ri(r,2,9);return{q:`線対称な 図形で、対応する 点Aと 点Bを むすぶ 直線は、対称の 軸と 垂直に 交わります。点Aから 対称の 軸までの きょりが ${x}cm の とき、点Aと 点Bの あいだの 長さは なんcm ですか。`,a:`${2*x} cm`,e:`軸から A・B までの きょりは 等しい：${x}×2`}},
  r=>{const n=pk(r,[3,4,5,6,8]);return{q:`正${KJ[n]}角形の 線対称の 軸は なん本 ありますか。また、点対称な 図形ですか。`,a:`${n}本、${n%2?'点対称では ない':'点対称'}`,e:`正n角形の 対称の 軸は n本。辺の 数が 偶数 なら 点対称`}});
U('6l',6,'拡大図・縮図をかく（方眼）',
  r=>{const G=mkG(14,8,16),enl=r()<.5;let bx,by,cx,cy,i=0;do{bx=ri(r,1,3);by=ri(r,0,1);cx=ri(r,0,2);cy=ri(r,2,3)}while(cross([bx,by],[cx,cy])<=0&&++i<50);if(cross([bx,by],[cx,cy])<=0){bx=2;by=0;cx=1;cy=2}
    const A=[ri(r,1,3),ri(r,1,2)],m=(k,p)=>[A[0]+k*p[0],A[1]+k*p[1]],S=[A,m(1,[bx,by]),m(1,[cx,cy])],Bg=[A,m(2,[bx,by]),m(2,[cx,cy])],giv=enl?S:Bg,ans=enl?Bg:S;
    return DR(`三角形ABCの ${enl?'2倍の 拡大図':fr(1,2)+' の 縮図'}を、点Aを 1つの ちょう点と して かきましょう。${SVG(G,G.poly(giv)+G.dot(A)+G.lab(A,'A',-12,13)+G.lab(giv[1],'B',4,13)+G.lab(giv[2],'C',4,-6)+AG(G.poly(ans,RED)+G.dot(ans[1],RED)+G.dot(ans[2],RED)))}`,`点Aから B・C までの すすみ方を ${enl?'2倍':'半分'}に して 点を とる`)},
  r=>{const k=ri(r,2,4),a=ri(r,2,8),p=ri(r,35,85);return{q:`三角形DEFは 三角形ABCの ${k}倍の 拡大図です。辺ABが ${a}cm、角Aが ${p}° のとき、辺DEは なんcm、角Dは なん度 ですか。`,a:`${a*k}cm、${p}°`,e:`辺の 長さは ${k}倍、角の 大きさは 変わらない`}},
  r=>{const k=ri(r,2,4),a=ri(r,2,6),c=ri(r,3,9);return{q:`三角形DEFは 三角形ABCの 拡大図です。辺ABが ${a}cm、対応する 辺DEが ${a*k}cm で、辺BCが ${c}cm の とき、辺EFは なんcm ですか。`,a:`${c*k} cm`,e:`${a}cm→${a*k}cm より ${k}倍：${c}×${k}`}});

/* ========== 領域（平成29年告示：数と計算／図形／測定・変化と関係／データの活用）========== */
const AREA={'3k':'図形','3m':'データの活用','4i':'図形','4j':'データの活用','4k':'図形','5l':'図形','5m':'データの活用','6k':'図形','6l':'図形','2d':'測定','2e':'測定','2g':'データの活用','3e':'測定','3f':'測定','3g':'データの活用','3h':'図形',
 '4e':'図形','4f':'図形','4g':'変化と関係','4h':'データの活用',
 '5d':'データの活用','5e':'図形','5f':'図形','5g':'変化と関係','5i':'図形','5j':'変化と関係','5k':'図形',
 '6c':'図形','6d':'変化と関係','6e':'変化と関係','6g':'図形','6h':'データの活用','6i':'データの活用','6j':'図形'};
UNITS.forEach(u=>u.ar=AREA[u.id]||'数と計算');
const AR_ORDER=['数と計算','図形','測定','変化と関係','データの活用'];

/* ========== 状態・生成 ========== */
const state={grade:4,sel:new Set(),n:10,mode:'random',seed:(Math.random()*2**32)>>>0,ans:false};
const plan=n=>{const a=Math.round(n*.12),w=Math.round(n*.22);return{a,w,b:n-a-w}};
function build(){
  const sel=UNITS.filter(u=>state.sel.has(u.id));if(!sel.length)return[];
  const {a,w,b}=plan(state.n),out=[],cnt={},seen=new Set();let nd=0;
  const off=state.mode==='fixed'?0:state.seed%sel.length;
  [['basic','b',b],['word','w',w],['apply','a',a]].forEach(([cat,f,m])=>{
    for(let i=0;i<m;i++){
      const u=sel[(i+off)%sel.length],key=u.id+cat;let p;
      for(let t=0;t<12;t++){
        const k=(cnt[key]||0)+t*97;
        const r=mul32(state.mode==='fixed'?hash(key+k):((state.seed^hash(key+k))>>>0));
        p=u[f](r);if(!seen.has(p.q))break;
      }
      if(p.draw){if(nd>=3){const k2=cnt[key]||0,r2=mul32(state.mode==='fixed'?hash(key+'w'+k2):((state.seed^hash(key+'w'+k2))>>>0));p=u.w(r2)}else nd++}
      cnt[key]=(cnt[key]||0)+1;seen.add(p.q);
      out.push({...p,cat,unit:u.name,sp:p.draw?0:(cat==='basic'?(p.sp||1):cat==='word'?2:3)});
    }
  });
  return out;
}

/* ========== 描画 ========== */
const SEC={basic:'けいさん もんだい',word:'ぶんしょう だい',apply:'おうよう もんだい'};
function probHTML(p,i){
  const no=i<20?String.fromCharCode(0x2460+i):i+1;
  let q=(p.q.includes('§')||p.draw)?p.q:p.q+`<div class="al">答え　§</div>`;
  q=q.replace(/§/g,()=>`<span class="blank"><i>${p.a}</i></span>`);
  return `<div class="pb ${p.cat}"><div class="qt"><span class="no">${no}</span><div class="qx">${q}</div></div><div class="sp s${p.sp}">${p.e?`<span class="ex">解説：${p.e}</span>`:''}</div></div>`;
}
function render(){
  let P=build(),dropped=0;paint(P);const s0=$('#sheet');
  while(s0.scrollHeight>s0.clientHeight+1&&P.length>1){P=P.slice(0,-1);dropped++;paint(P)}
  if(dropped)$('#mix').textContent+=` ／ A4に収まるよう ${dropped}問 減らしました`;
}
function paint(P){
  const sheet=$('#sheet');
  const {a,w,b}=plan(state.n);$('#mix').textContent=`内訳の目安：基礎 ${b}問 ／ 文章題 ${w}問 ／ 応用 ${a}問`;
  const school=$('#school').value.trim(),title=$('#title').value.trim()||'算数 朝のプリント';
  const used=[...new Set(P.map(p=>p.unit))];
  let h=`<div class="hd"><div class="top"><h1>${title.replace(/</g,'&lt;')}</h1><span class="gr">${state.grade}年</span><div class="units">${used.join('／')}</div></div>
  <div class="fields"><span class="fld">${school?`<b>${school.replace(/</g,'&lt;')}</b>`:'<span class="ln" style="min-width:24mm"></span>小学校'}</span>
  <span class="fld"><span class="ln" style="min-width:9mm"></span>年 <span class="ln" style="min-width:9mm"></span>組 <span class="ln" style="min-width:9mm"></span>番</span>
  <span class="fld">名前 <span class="ln" style="min-width:36mm"></span></span>
  ${$('#date').checked?'<span class="fld"><span class="ln" style="min-width:9mm"></span>月 <span class="ln" style="min-width:9mm"></span>日</span>':''}
  ${$('#score').checked?'<span class="score">点</span>':''}</div></div>`;
  if(!P.length)h+='<div class="empty">単元を 1つ以上 選んでください</div>';
  let i=0;
  ['basic','word','apply'].forEach(c=>{
    const L=P.filter(p=>p.cat===c);if(!L.length)return;
    h+=`<div class="sec">${SEC[c]}</div><div class="grid">`+L.map(p=>probHTML(p,i++)).join('')+'</div>';
  });
  h+=`<div class="ft">${$('#pub').value==='指定なし'?'':$('#pub').value+' 使用校向け ／ '}小学校学習指導要領（平成29年告示）算数科の学年・領域に沿った自動生成問題</div>`;
  sheet.innerHTML=h;sheet.classList.toggle('show-ans',state.ans);
  fit();scalePreview();
}
function fit(){
  const s=$('#sheet'),set=(k,f)=>{s.style.setProperty('--k',k);s.style.setProperty('--fs',f)},over=()=>s.scrollHeight>s.clientHeight+1;
  let k=1,f=1;set(k,f);
  if(!over()){while(k<3&&(set(k+.25,f),!over()))k+=.25;set(k,f);return}
  while(over()&&k>.3){k-=.1;set(k,f)}
  const fl=s.querySelector('svg')?.8:.55;while(over()&&f>fl){f-=.03;set(k,f)}
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
  $('#units').innerHTML=AR_ORDER.map(a=>{const X=L.filter(u=>u.ar===a);return X.length?`<div class="mt-2 text-xs font-bold text-slate-500 border-b">${a}</div>`+X.map(u=>`<label class="flex items-start gap-1.5"><input type="checkbox" value="${u.id}" ${state.sel.has(u.id)?'checked':''} class="mt-1 unit"><span>${u.name}</span></label>`).join(''):''}).join('');
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

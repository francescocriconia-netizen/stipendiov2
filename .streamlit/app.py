import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="🍕 Ore Pizzeria",
    page_icon="🍕",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
#MainMenu, footer, header {visibility: hidden;}
.block-container {padding-top: 0 !important; padding-bottom: 0 !important; max-width: 100% !important; padding-left: 0 !important; padding-right: 0 !important;}
iframe {border: none !important;}
</style>
""", unsafe_allow_html=True)

components.html("""
<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no, viewport-fit=cover">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,600;9..40,700&family=Space+Mono:wght@400;700&display=swap');

* { margin: 0; padding: 0; box-sizing: border-box; -webkit-tap-highlight-color: transparent; }

:root {
  --red: #D94F30;
  --red-dark: #B8391F;
  --orange: #F2994A;
  --cream: #FFFAF5;
  --dark: #1A1A2E;
  --green: #27AE60;
  --gold: #F2C94C;
  --grey: #6B7280;
  --grey-light: #E5E7EB;
  --card-bg: #FFF8F0;
}

body {
  font-family: 'DM Sans', -apple-system, sans-serif;
  background: var(--cream);
  color: var(--dark);
  min-height: 100vh;
  padding: 0 16px 80px;
  -webkit-font-smoothing: antialiased;
}

.header {
  text-align: center;
  padding: 20px 0 16px;
  border-bottom: 3px solid var(--red);
  margin-bottom: 20px;
  position: sticky;
  top: 0;
  background: var(--cream);
  z-index: 100;
}
.header h1 {
  font-family: 'Space Mono', monospace;
  font-size: 1.5rem;
  color: var(--red);
  letter-spacing: -0.5px;
}
.header p {
  color: var(--grey);
  font-size: 0.78rem;
  margin-top: 2px;
}

.rate-bar {
  display: flex;
  align-items: center;
  gap: 10px;
  background: var(--dark);
  border-radius: 14px;
  padding: 12px 16px;
  margin-bottom: 20px;
}
.rate-bar label {
  font-family: 'Space Mono', monospace;
  font-size: 0.72rem;
  color: rgba(255,255,255,0.6);
  text-transform: uppercase;
  letter-spacing: 0.5px;
  white-space: nowrap;
}
.rate-bar input {
  flex: 1;
  background: rgba(255,255,255,0.1);
  border: 1px solid rgba(255,255,255,0.15);
  border-radius: 8px;
  color: var(--gold);
  font-family: 'Space Mono', monospace;
  font-size: 1.1rem;
  font-weight: 700;
  padding: 6px 10px;
  width: 80px;
  text-align: center;
  outline: none;
}
.rate-bar input:focus { border-color: var(--gold); }
.rate-bar .euro-sign {
  color: var(--gold);
  font-family: 'Space Mono', monospace;
  font-weight: 700;
  font-size: 1.1rem;
}

.month-nav {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 12px;
}
.month-nav button {
  background: none;
  border: 2px solid var(--grey-light);
  border-radius: 10px;
  width: 40px;
  height: 40px;
  font-size: 1.1rem;
  cursor: pointer;
  color: var(--dark);
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.15s;
}
.month-nav button:active { background: var(--grey-light); }
.month-nav .month-title {
  font-family: 'Space Mono', monospace;
  font-size: 1.05rem;
  font-weight: 700;
}

.cal-grid {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  gap: 4px;
  margin-bottom: 20px;
}
.cal-head {
  text-align: center;
  font-family: 'Space Mono', monospace;
  font-size: 0.6rem;
  font-weight: 700;
  color: var(--grey);
  padding: 6px 0;
  text-transform: uppercase;
}
.cal-day {
  aspect-ratio: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  border-radius: 11px;
  font-size: 0.88rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.12s;
  border: 2px solid transparent;
  position: relative;
  user-select: none;
}
.cal-day:active { transform: scale(0.92); }
.cal-day.empty { visibility: hidden; }
.cal-day.today { border-color: var(--red); }
.cal-day.selected { background: var(--red) !important; color: #fff !important; border-color: var(--red); }
.cal-day.has-hours { background: #FEE2D5; }
.cal-day .dot {
  font-size: 0.45rem;
  color: var(--orange);
  font-family: 'Space Mono', monospace;
  margin-top: 1px;
  line-height: 1;
}
.cal-day.selected .dot { color: rgba(255,255,255,0.8); }

.entry-panel {
  background: #fff;
  border-radius: 16px;
  padding: 18px;
  margin-bottom: 16px;
  box-shadow: 0 2px 12px rgba(0,0,0,0.04);
  border: 1px solid rgba(0,0,0,0.04);
}
.entry-title {
  font-family: 'Space Mono', monospace;
  font-size: 0.78rem;
  color: var(--grey);
  text-transform: uppercase;
  letter-spacing: 0.8px;
  margin-bottom: 14px;
}
.entry-title span { color: var(--red); font-weight: 700; }

.input-row {
  display: flex;
  gap: 12px;
  margin-bottom: 14px;
}
.input-group {
  flex: 1;
  text-align: center;
}
.input-group label {
  display: block;
  font-size: 0.7rem;
  color: var(--grey);
  font-family: 'Space Mono', monospace;
  text-transform: uppercase;
  margin-bottom: 6px;
  letter-spacing: 0.5px;
}
.stepper {
  display: flex;
  align-items: center;
  background: var(--card-bg);
  border-radius: 12px;
  overflow: hidden;
  border: 1px solid rgba(0,0,0,0.06);
}
.stepper button {
  width: 44px;
  height: 48px;
  border: none;
  background: none;
  font-size: 1.3rem;
  cursor: pointer;
  color: var(--red);
  font-weight: 700;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background 0.1s;
}
.stepper button:active { background: rgba(217,79,48,0.1); }
.stepper .stepper-val {
  flex: 1;
  font-family: 'Space Mono', monospace;
  font-size: 1.4rem;
  font-weight: 700;
  color: var(--dark);
  text-align: center;
  min-width: 36px;
}

.btn-save {
  width: 100%;
  background: var(--red);
  color: #fff;
  border: none;
  border-radius: 12px;
  padding: 14px;
  font-family: 'Space Mono', monospace;
  font-weight: 700;
  font-size: 0.88rem;
  cursor: pointer;
  letter-spacing: 0.5px;
  transition: all 0.15s;
}
.btn-save:active { background: var(--red-dark); transform: scale(0.97); }

.btn-delete {
  width: 100%;
  background: none;
  color: var(--grey);
  border: 1.5px dashed var(--grey-light);
  border-radius: 12px;
  padding: 11px;
  font-family: 'Space Mono', monospace;
  font-size: 0.75rem;
  cursor: pointer;
  margin-top: 8px;
}
.btn-delete:active { background: #FEE2E2; color: var(--red); border-color: var(--red); }

.section-title {
  font-family: 'Space Mono', monospace;
  font-size: 0.72rem;
  color: var(--grey);
  text-transform: uppercase;
  letter-spacing: 1px;
  margin: 24px 0 10px;
  padding-bottom: 6px;
  border-bottom: 2px dashed rgba(107,114,128,0.15);
}

.week-card {
  background: var(--dark);
  color: #fff;
  border-radius: 14px;
  padding: 14px 16px;
  margin-bottom: 8px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.week-card .wl {
  font-size: 0.62rem;
  color: rgba(255,255,255,0.5);
  font-family: 'Space Mono', monospace;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}
.week-card .wh {
  font-family: 'Space Mono', monospace;
  font-size: 0.95rem;
  font-weight: 700;
  margin-top: 2px;
}
.week-card .we {
  font-family: 'Space Mono', monospace;
  font-size: 0.88rem;
  font-weight: 700;
  color: var(--gold);
}

.stats-row {
  display: flex;
  gap: 8px;
  margin-top: 10px;
}
.stat-card {
  flex: 1;
  background: #fff;
  border-radius: 14px;
  padding: 14px 8px;
  text-align: center;
  border: 1px solid rgba(0,0,0,0.04);
  box-shadow: 0 1px 6px rgba(0,0,0,0.03);
}
.stat-card .sl {
  font-size: 0.58rem;
  color: var(--grey);
  text-transform: uppercase;
  letter-spacing: 0.5px;
  font-family: 'Space Mono', monospace;
}
.stat-card .sv {
  font-size: 1.15rem;
  font-weight: 700;
  font-family: 'Space Mono', monospace;
  margin-top: 4px;
}
.stat-card .sv.euro { color: var(--green); }

.footer {
  text-align: center;
  padding: 28px 0 16px;
  font-size: 0.65rem;
  color: #C0C5CE;
  font-family: 'Space Mono', monospace;
}

.no-data {
  text-align: center;
  padding: 16px;
  color: var(--grey);
  font-size: 0.8rem;
  font-style: italic;
}

.toast {
  position: fixed;
  bottom: 30px;
  left: 50%;
  transform: translateX(-50%) translateY(20px);
  background: var(--dark);
  color: #fff;
  padding: 10px 22px;
  border-radius: 10px;
  font-family: 'Space Mono', monospace;
  font-size: 0.8rem;
  font-weight: 700;
  z-index: 1000;
  opacity: 0;
  transition: all 0.3s ease;
  pointer-events: none;
}
.toast.show { opacity: 1; transform: translateX(-50%) translateY(0); }
</style>
</head>
<body>

<div class="header">
  <h1>🍕 Ore Pizzeria</h1>
  <p>Traccia le tue ore · dati salvati sul dispositivo</p>
</div>

<div class="rate-bar">
  <label>Paga oraria</label>
  <span class="euro-sign">€</span>
  <input type="number" id="rateInput" step="0.5" min="0" max="100" inputmode="decimal" placeholder="0.00">
</div>

<div class="month-nav">
  <button onclick="changeMonth(-1)">◀</button>
  <div class="month-title" id="monthTitle"></div>
  <button onclick="changeMonth(1)">▶</button>
</div>

<div class="cal-grid" id="calGrid"></div>

<div class="entry-panel" id="entryPanel">
  <div class="entry-title" id="entryTitle"></div>
  <div class="input-row">
    <div class="input-group">
      <label>Ore</label>
      <div class="stepper">
        <button onclick="step('hours',-1)">−</button>
        <div class="stepper-val" id="hoursVal">0</div>
        <button onclick="step('hours',1)">+</button>
      </div>
    </div>
    <div class="input-group">
      <label>Minuti</label>
      <div class="stepper">
        <button onclick="step('mins',-5)">−</button>
        <div class="stepper-val" id="minsVal">0</div>
        <button onclick="step('mins',5)">+</button>
      </div>
    </div>
  </div>
  <button class="btn-save" onclick="saveEntry()">💾 Salva</button>
  <button class="btn-delete" id="btnDelete" onclick="deleteEntry()" style="display:none">🗑️ Rimuovi questa giornata</button>
</div>

<div class="section-title">📊 Riepilogo settimanale</div>
<div id="weekSummaries"></div>

<div class="section-title">📅 Totale mese</div>
<div class="stats-row" id="monthStats"></div>

<div class="footer">🍕 Ore Pizzeria</div>

<div class="toast" id="toast"></div>

<script>
const STORAGE_KEY = 'pizzeria_ore_data_v2';

function loadData() {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (raw) return JSON.parse(raw);
  } catch(e) {}
  return { rate: 0, entries: {} };
}
function saveData(d) { localStorage.setItem(STORAGE_KEY, JSON.stringify(d)); }

let data = loadData();
const today = new Date();
let viewYear = today.getFullYear();
let viewMonth = today.getMonth();
let selectedDate = fmtDate(today);
let inputHours = 0;
let inputMins = 0;

const MESI = ['Gennaio','Febbraio','Marzo','Aprile','Maggio','Giugno','Luglio','Agosto','Settembre','Ottobre','Novembre','Dicembre'];
const GIORNI = ['Lun','Mar','Mer','Gio','Ven','Sab','Dom'];
const GIORNI_F = ['Domenica','Lunedì','Martedì','Mercoledì','Giovedì','Venerdì','Sabato'];

function fmtDate(d) {
  return d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0');
}
function dispDate(k) { const p=k.split('-'); return p[2]+'/'+p[1]+'/'+p[0]; }
function mToHM(t) { return Math.floor(t/60)+'h '+String(t%60).padStart(2,'0')+'m'; }
function getMonday(d) {
  const dt=new Date(d); const day=dt.getDay();
  dt.setDate(dt.getDate()-((day===0?7:day)-1));
  return dt;
}

const rateInput = document.getElementById('rateInput');
rateInput.value = data.rate || '';
rateInput.addEventListener('change', () => {
  data.rate = parseFloat(rateInput.value)||0;
  saveData(data);
  render();
  showToast('Paga aggiornata');
});

function changeMonth(dir) {
  viewMonth += dir;
  if (viewMonth<0){viewMonth=11;viewYear--;}
  if (viewMonth>11){viewMonth=0;viewYear++;}
  render();
}

function step(field, delta) {
  if (field==='hours') {
    inputHours = Math.max(0,Math.min(24,inputHours+delta));
    document.getElementById('hoursVal').textContent = inputHours;
  } else {
    inputMins = Math.max(0,Math.min(55,inputMins+delta));
    document.getElementById('minsVal').textContent = inputMins;
  }
}

function saveEntry() {
  if (inputHours===0 && inputMins===0) delete data.entries[selectedDate];
  else data.entries[selectedDate] = {h:inputHours, m:inputMins};
  saveData(data); render(); showToast('Salvato ✓');
}

function deleteEntry() {
  delete data.entries[selectedDate];
  saveData(data); inputHours=0; inputMins=0; render(); showToast('Rimosso');
}

function showToast(msg) {
  const t=document.getElementById('toast'); t.textContent=msg;
  t.classList.add('show'); setTimeout(()=>t.classList.remove('show'),1500);
}

function selectDate(key) {
  selectedDate = key;
  const e = data.entries[key];
  inputHours = e?e.h:0; inputMins = e?e.m:0;
  render();
  document.getElementById('entryPanel').scrollIntoView({behavior:'smooth', block:'center'});
}

function render() {
  document.getElementById('monthTitle').textContent = MESI[viewMonth]+' '+viewYear;
  const grid = document.getElementById('calGrid');
  grid.innerHTML = '';
  GIORNI.forEach(g => { const el=document.createElement('div'); el.className='cal-head'; el.textContent=g; grid.appendChild(el); });

  const firstDay = new Date(viewYear,viewMonth,1).getDay();
  const offset = firstDay===0?6:firstDay-1;
  const dim = new Date(viewYear,viewMonth+1,0).getDate();
  const todayKey = fmtDate(today);

  for(let i=0;i<offset;i++){const el=document.createElement('div');el.className='cal-day empty';grid.appendChild(el);}

  for(let d=1;d<=dim;d++){
    const dt=new Date(viewYear,viewMonth,d);
    const key=fmtDate(dt);
    const el=document.createElement('div');
    let cls='cal-day';
    if(key===todayKey) cls+=' today';
    if(key===selectedDate) cls+=' selected';
    let dot='';
    if(data.entries[key]){
      const e=data.entries[key]; const tm=e.h*60+e.m;
      if(tm>0){cls+=' has-hours'; dot='<div class="dot">'+mToHM(tm)+'</div>';}
    }
    el.className=cls;
    el.innerHTML=d+dot;
    el.onclick=()=>selectDate(key);
    grid.appendChild(el);
  }

  // Entry panel
  const sp=selectedDate.split('-');
  const selDt=new Date(+sp[0],+sp[1]-1,+sp[2]);
  document.getElementById('entryTitle').innerHTML='✏️ <span>'+GIORNI_F[selDt.getDay()]+' '+dispDate(selectedDate)+'</span>';
  document.getElementById('hoursVal').textContent=inputHours;
  document.getElementById('minsVal').textContent=inputMins;
  document.getElementById('btnDelete').style.display=data.entries[selectedDate]?'block':'none';

  // Weekly
  const wd=document.getElementById('weekSummaries'); wd.innerHTML='';
  const seen=new Set();
  const dim2=new Date(viewYear,viewMonth+1,0).getDate();
  let hasWeekData=false;

  for(let d=1;d<=dim2;d++){
    const dt=new Date(viewYear,viewMonth,d);
    const mon=getMonday(dt);
    const mk=fmtDate(mon);
    if(seen.has(mk)) continue;
    seen.add(mk);
    const sun=new Date(mon); sun.setDate(sun.getDate()+6);
    let tm=0;
    for(let i=0;i<7;i++){
      const w=new Date(mon); w.setDate(w.getDate()+i);
      const wk=fmtDate(w);
      if(data.entries[wk]) tm+=data.entries[wk].h*60+data.entries[wk].m;
    }
    if(tm>0){
      hasWeekData=true;
      const euro=(tm/60)*(data.rate||0);
      const ms=String(mon.getDate()).padStart(2,'0')+'/'+String(mon.getMonth()+1).padStart(2,'0');
      const ss=String(sun.getDate()).padStart(2,'0')+'/'+String(sun.getMonth()+1).padStart(2,'0');
      const c=document.createElement('div'); c.className='week-card';
      c.innerHTML='<div><div class="wl">Settimana</div><div class="wh">'+ms+' → '+ss+'</div></div><div style="text-align:right"><div class="wh">'+mToHM(tm)+'</div><div class="we">€ '+euro.toFixed(2)+'</div></div>';
      wd.appendChild(c);
    }
  }
  if(!hasWeekData) wd.innerHTML='<div class="no-data">Nessuna ora registrata questo mese</div>';

  // Month stats
  let mtm=0,dw=0;
  for(let d=1;d<=dim2;d++){
    const k=fmtDate(new Date(viewYear,viewMonth,d));
    if(data.entries[k]){mtm+=data.entries[k].h*60+data.entries[k].m;dw++;}
  }
  const me=(mtm/60)*(data.rate||0);
  document.getElementById('monthStats').innerHTML=
    '<div class="stat-card"><div class="sl">Ore totali</div><div class="sv">'+mToHM(mtm)+'</div></div>'+
    '<div class="stat-card"><div class="sl">Giorni</div><div class="sv">'+dw+'</div></div>'+
    '<div class="stat-card"><div class="sl">Totale €</div><div class="sv euro">€ '+me.toFixed(2)+'</div></div>';
}

render();
</script>
</body>
</html>
""", height=1600, scrolling=True)

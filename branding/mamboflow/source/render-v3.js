const { chromium } = require('playwright'); const path=require('path');
(async()=>{const b=await chromium.launch();
const p=await b.newPage({viewport:{width:1700,height:1300}}); await p.goto('file://'+path.resolve(__dirname,'lockv3.html')); await p.evaluate(()=>document.fonts.ready); await p.waitForTimeout(400);
// metric-driven placement: mark = 1.25 x cap height, centred on the caps; endorsement under the wordmark; sparkle at the top right of Flow
const place = await p.evaluate(() => {
  const out = {};
  const capHeight = (F) => { const c=document.createElement('canvas').getContext('2d'); c.font = `500 ${F}px "Bodoni Moda"`; const m=c.measureText('M'); return {cap:m.actualBoundingBoxAscent}; };
  function layout(id, F, markLeft, top, byF, stacked) {
    const fr=document.getElementById(id); const wm=fr.querySelector('.wm'); const mk=fr.querySelector('.mark'); const by=fr.querySelector('.by'); const sp=fr.querySelector('.spark');
    wm.style.fontSize=F+'px'; wm.style.top=top+'px';
    const {cap}=capHeight(F);
    const r0=wm.getBoundingClientRect(); const f=fr.getBoundingClientRect();
    // baseline: with line-height 1, Bodoni Moda places the baseline near top + 0.80F; measure instead with a span
    const probe=document.createElement('span'); probe.textContent='M'; probe.style.cssText='display:inline-block;vertical-align:baseline;line-height:1;font:inherit'; wm.appendChild(probe);
    const pr=probe.getBoundingClientRect(); probe.remove();
    // baseline of the span box: use a zero-height inline-block aligned to baseline
    const z=document.createElement('span'); z.style.cssText='display:inline-block;width:0;height:0;vertical-align:baseline'; wm.appendChild(z); const zr=z.getBoundingClientRect(); z.remove();
    const baseline=zr.top-f.top; const capTop=baseline-cap; const capMid=baseline-cap/2;
    const markH=Math.round(cap*1.25); mk.style.height=markH+'px'; mk.style.top=Math.round(capMid-markH/2)+'px';
    const markW=markH*1.076; const gap=Math.round(cap*0.32);
    if(!stacked){ mk.style.left=markLeft+'px'; wm.style.left=Math.round(markLeft+markW+gap)+'px'; }
    else { const total=markW+gap+r0.width; const left=(f.width-total)/2; mk.style.left=Math.round(left)+'px'; wm.style.left=Math.round(left+markW+gap)+'px'; }
    const r=wm.getBoundingClientRect();
    by.style.fontSize=byF+'px'; by.style.left=Math.round(r.left-f.left+F*0.04)+'px'; by.style.top=Math.round(baseline+cap*0.42)+'px'; by.style.right='auto'; by.style.textAlign='left';
    sp.style.width=Math.round(cap*0.26)+'px'; sp.style.left=Math.round(r.right-f.left+cap*0.08)+'px'; sp.style.top=Math.round(capTop-cap*0.22)+'px';
    out[id]={cap, baseline, wmLeft:r.left-f.left, wmRight:r.right-f.left, markH};
  }
  layout('p',176,400,128,19,false); layout('r',176,400,128,19,false); layout('s',126,0,560,16,true);
  return out;
});
console.log(JSON.stringify(place));
for (const [id,t] of [['p',true],['r',false],['s',true]]) { await p.evaluate(t=>{document.body.style.background=t?'transparent':'#888'},t); const el=await p.$('#'+id); await el.screenshot({path:path.resolve(__dirname,'../lockups/v3-'+id+'.png'),omitBackground:t}); }
await b.close();})();

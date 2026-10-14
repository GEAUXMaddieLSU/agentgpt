const { chromium } = require('playwright'); const path=require('path');
(async()=>{const b=await chromium.launch();
const p=await b.newPage({viewport:{width:1700,height:1200}}); await p.goto('file://'+path.resolve(__dirname,'igcvar.html')); await p.evaluate(()=>document.fonts.ready); await p.waitForTimeout(500);
const el=await p.$('#v'); await el.screenshot({path:path.resolve(__dirname,'../board/igc-variations.png')}); await b.close(); console.log('igc variations rendered');})();

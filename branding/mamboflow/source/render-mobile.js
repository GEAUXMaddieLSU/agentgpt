const { chromium } = require('playwright'); const path=require('path');
(async()=>{const b=await chromium.launch();
const p=await b.newPage({viewport:{width:500,height:900},deviceScaleFactor:2}); await p.goto('file://'+path.resolve(__dirname,'mobile.html')); await p.evaluate(()=>document.fonts.ready); await p.waitForTimeout(500);
const el=await p.$('#m'); await el.screenshot({path:path.resolve(__dirname,'../app/mobile-welcome.png')}); await b.close(); console.log('mobile rendered');})();

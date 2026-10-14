const { chromium } = require('playwright'); const path=require('path');
(async()=>{const b=await chromium.launch();
const p=await b.newPage({viewport:{width:1700,height:1300},deviceScaleFactor:1}); await p.goto('file://'+path.resolve(__dirname,'sheet.html')); await p.evaluate(()=>document.fonts.ready); await p.waitForTimeout(600);
const el=await p.$('#sheet'); await el.screenshot({path:path.resolve(__dirname,'../board/brand-sheet.png')}); await b.close(); console.log('sheet rendered');})();

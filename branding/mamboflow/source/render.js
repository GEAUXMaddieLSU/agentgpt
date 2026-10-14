const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ deviceScaleFactor: 1, viewport: { width: 1600, height: 1200 } });
  await page.goto('file://' + path.resolve(__dirname,'assets.html'));
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(500);
  const ids = process.argv.slice(2);
  for (const id of ids) {
    const el = await page.$('#' + id);
    const transparent = ['lock-primary','lock-stacked'].includes(id);
    await page.evaluate(t => { document.body.style.background = t ? 'transparent' : '#888'; }, transparent);
    await el.screenshot({ path: `out/${id}.png`, omitBackground: transparent });
    console.log('wrote', id);
  }
  await browser.close();
})();

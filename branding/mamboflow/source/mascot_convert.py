from PIL import Image, ImageOps, ImageFilter, ImageEnhance
import numpy as np, sys
src = Image.open(sys.argv[1]).convert('RGBA')
W,H = src.size
a = np.array(src).astype(np.float32)
alpha = a[:,:,3]
rgb = a[:,:,:3]
# luminance
lum = 0.2126*rgb[:,:,0]+0.7152*rgb[:,:,1]+0.0722*rgb[:,:,2]

def save(arr_gray, name, alpha=alpha):
    g = np.clip(arr_gray,0,255).astype(np.uint8)
    out = np.dstack([g,g,g,alpha.astype(np.uint8)])
    Image.fromarray(out,'RGBA').save(f'{sys.argv[2]}/{name}.png')

# 1 ink: grayscale, contrast up, keep watercolor shading
ink = (lum-128)*1.25+128
save(ink,'mambo-ink')

# 2 classic: lift cream body to near-white, keep lines dark (S-curve)
x = lum/255.0
# strong S-curve: push >0.55 toward 1, <0.35 toward 0
classic = np.where(x>0.5, 0.5+0.5*((x-0.5)/0.5)**0.55, 0.5*((x/0.5)**1.6))
save(classic*255,'mambo-classic')

# 3 stamp: two-tone (pure black and white) with slight blur to smooth
blur = np.array(Image.fromarray(np.clip(lum,0,255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.8))).astype(np.float32)
stamp = np.where(blur>118,255,0).astype(np.float32)
save(stamp,'mambo-stamp')

# 4 spot: classic gray + collar kept in its own color (teal hue) 
import colorsys
r,g,b = rgb[:,:,0]/255, rgb[:,:,1]/255, rgb[:,:,2]/255
mx = np.max(rgb,axis=2)/255; mn = np.min(rgb,axis=2)/255
sat = np.where(mx>0, (mx-mn)/np.maximum(mx,1e-6), 0)
# hue
hsv = np.array(Image.fromarray(np.clip(rgb,0,255).astype(np.uint8)).convert('HSV')).astype(np.float32)
hue = hsv[:,:,0]/255*360
teal = (hue>150)&(hue<215)&(sat>0.18)&(alpha>40)
gold = (hue>25)&(hue<60)&(sat>0.35)&(lum>90)&(alpha>40)
g3 = np.dstack([classic*255]*3)
spot = g3.copy()
# recolor the collar to a single flat MCM accent (mustard) and the tag to ink
MUSTARD = np.array([214,160,38],dtype=np.float32)
# shade the mustard by luminance of the original teal so folds remain
shade = (lum/255.0)[...,None]
shade = np.clip((shade-0.2)/0.6,0.25,1.0)
spot[teal] = (MUSTARD*shade)[teal]
out = np.dstack([np.clip(spot,0,255).astype(np.uint8), alpha.astype(np.uint8)])
Image.fromarray(out,'RGBA').save(f'{sys.argv[2]}/mambo-spot-mustard.png')
# teal-kept variant
spot2 = g3.copy(); spot2[teal] = rgb[teal]
out = np.dstack([np.clip(spot2,0,255).astype(np.uint8), alpha.astype(np.uint8)])
Image.fromarray(out,'RGBA').save(f'{sys.argv[2]}/mambo-spot-teal.png')
print('teal px', teal.sum(), 'gold px', gold.sum())

# 5 reversed (white-on-dark): invert classic so lines are white, body dark? No: for dark grounds keep body white with black lines, add a white keyline halo.
# sticker: white keyline around silhouette
mask = Image.fromarray((alpha>30).astype(np.uint8)*255)
halo = mask.filter(ImageFilter.MaxFilter(21)).filter(ImageFilter.GaussianBlur(1))
halo_a = np.array(halo).astype(np.uint8)
base = np.dstack([np.clip(classic*255,0,255).astype(np.uint8)]*3+[alpha.astype(np.uint8)])
sticker = Image.new('RGBA',(W,H),(0,0,0,0))
white = Image.new('RGBA',(W,H),(255,255,255,255)); white.putalpha(Image.fromarray(halo_a))
sticker.alpha_composite(white); sticker.alpha_composite(Image.fromarray(base,'RGBA'))
sticker.save(f'{sys.argv[2]}/mambo-classic-sticker.png')
# contact sheet
names=['mambo-ink','mambo-classic','mambo-stamp','mambo-spot-mustard','mambo-spot-teal','mambo-classic-sticker']
sheet = Image.new('RGBA',(400*3,400*2),(251,251,248,255))
for i,n in enumerate(names):
    im = Image.open(f'{sys.argv[2]}/{n}.png').resize((400,400),Image.LANCZOS)
    bg = Image.new('RGBA',(400,400),(16,17,20,255) if i==5 else (251,251,248,255))
    bg.alpha_composite(im); sheet.paste(bg,((i%3)*400,(i//3)*400))
sheet.save(f'{sys.argv[2]}/contact-sheet.png')

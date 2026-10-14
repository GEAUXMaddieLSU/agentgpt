"""Mambo pop variants: black-and-white coat, colored collar, gold charm.
usage: python3 mascot_pop.py <color-original.png> <out-dir>"""
from PIL import Image, ImageFilter
import numpy as np, sys
src=Image.open(sys.argv[1]).convert('RGBA'); out_dir=sys.argv[2]
a=np.array(src).astype(np.float32); alpha=a[:,:,3]; rgb=a[:,:,:3]; H,W=alpha.shape
lum=0.2126*rgb[:,:,0]+0.7152*rgb[:,:,1]+0.0722*rgb[:,:,2]
x=lum/255.0
classic=np.where(x>0.5, 0.5+0.5*(np.clip((x-0.5)/0.5,0,1))**0.55, 0.5*((np.clip(x,0,1)/0.5)**1.6))*255
hsv=np.array(Image.fromarray(np.clip(rgb,0,255).astype(np.uint8)).convert('HSV')).astype(np.float32)
hue=hsv[:,:,0]/255*360; sat=hsv[:,:,1]/255
band=np.zeros((H,W),bool); band[530:760,300:930]=True   # collar strap and buckle (1254 px original)
tagr=np.zeros((H,W),bool); tagr[690:850,440:650]=True   # hanging charm
teal=(hue>150)&(hue<215)&(sat>0.18)&(alpha>40)&band
gold=(hue>25)&(hue<60)&(sat>0.35)&(lum>90)&(alpha>40)&(band|tagr)
def soft(m):
    return np.array(Image.fromarray((m*255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(1.2))).astype(np.float32)/255
tm=soft(teal)[...,None]; gm=soft(gold)[...,None]
base=np.dstack([classic]*3)
l=lum/255.0; ref=np.percentile(lum[teal],75)/255.0; s=np.clip(l/ref,0.35,1.15)[...,None]
def shade_to(t): return np.clip(np.array(t,dtype=np.float32)*s,0,255)
goldrgb=np.clip((rgb-lum[...,None])*1.35+lum[...,None]*1.02,0,255)
variants={'teal':np.clip((rgb-lum[...,None])*1.3+lum[...,None],0,255),'pink':shade_to((217,75,128)),'mustard':shade_to((226,176,58)),'red':shade_to((226,86,63))}
ys,xs=np.where(alpha>30); x0,x1,y0,y1=max(xs.min()-20,0),min(xs.max()+20,W),max(ys.min()-20,0),min(ys.max()+20,H)
for name,col in variants.items():
    out=base*(1-tm)+col*tm; out=out*(1-gm)+goldrgb*gm
    im=Image.fromarray(np.dstack([np.clip(out,0,255).astype(np.uint8),alpha.astype(np.uint8)]),'RGBA').crop((x0,y0,x1,y1))
    im.save(f'{out_dir}/mambo-pop-{name}.png',optimize=True)
    mask=Image.fromarray((np.array(im)[:,:,3]>30).astype(np.uint8)*255); halo=mask.filter(ImageFilter.MaxFilter(21)).filter(ImageFilter.GaussianBlur(1))
    st=Image.new('RGBA',im.size,(0,0,0,0)); white=Image.new('RGBA',im.size,(255,255,255,255)); white.putalpha(halo); st.alpha_composite(white); st.alpha_composite(im)
    st.save(f'{out_dir}/mambo-pop-{name}-sticker.png',optimize=True)
    print(name,'ok')

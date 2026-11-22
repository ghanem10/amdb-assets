import sys
from PIL import Image
ts=sys.argv[1].split(','); out=sys.argv[2]
ims=[Image.open(f'/home/claude/amdb/reel3/still_{float(t)}.jpg').resize((360,640)) for t in ts]
cols=4; rows=(len(ims)+3)//4
W=Image.new('RGB',(360*cols,640*rows))
for i,im in enumerate(ims): W.paste(im,((i%cols)*360,(i//cols)*640))
W.save(out)

import sys
from PIL import Image
ts=sys.argv[1].split(','); out=sys.argv[2]
ims=[Image.open(f'/home/claude/amdb/reel2/still_{float(t)}.jpg').resize((405,720)) for t in ts]
cols=4; rows=(len(ims)+3)//4
W=Image.new('RGB',(405*cols,720*rows))
for i,im in enumerate(ims): W.paste(im,((i%cols)*405,(i//cols)*720))
W.save(out)

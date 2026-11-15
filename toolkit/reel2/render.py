import sys, subprocess, pathlib
sys.path.insert(0,'/home/claude/amdb')
from lux import FONTS
from playwright.sync_api import sync_playwright
R=pathlib.Path('/home/claude/amdb/reel2')
html=(R/'reel.html').read_text(encoding='utf-8').replace('/*FONTS*/',FONTS).replace('LOGO','file:///home/claude/amdb/logo_round.png')
(R/'_built.html').write_text(html,encoding='utf-8')
FPS=30
CUTS=[0,4.5,8.1,16.3,23.0,26.45,31.8,37.5]
def scene(pg,name,a,b):
    tmp=R/f'_tmp_{name}.mp4'; out=R/f'scene_{name}.mp4'
    ff=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-f','image2pipe','-framerate',str(FPS),'-c:v','mjpeg','-i','-',
        '-c:v','libx264','-preset','veryfast','-crf','18','-pix_fmt','yuv420p','-r',str(FPS),str(tmp)],stdin=subprocess.PIPE)
    n0=round(a*FPS); n1=round(b*FPS)
    for i in range(n0,n1):
        pg.evaluate(f'setTime({i/FPS})')
        ff.stdin.write(pg.screenshot(type='jpeg',quality=92))
    ff.stdin.close(); assert ff.wait()==0; tmp.rename(out)
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome')
    pg=b.new_page(viewport={'width':1080,'height':1920})
    pg.goto(f"file://{R/'_built.html'}"); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(600)
    mode=sys.argv[1]
    if mode=='stills':
        ts=[float(x) for x in sys.argv[2].split(',')]
        for t in ts:
            pg.evaluate(f'setTime({t})'); pg.screenshot(path=str(R/f'still_{t}.jpg'),type='jpeg',quality=85)
    else:
        only=[int(x) for x in sys.argv[2].split(',')] if len(sys.argv)>2 else range(len(CUTS)-1)
        for i in only: scene(pg,f'{i:02d}',CUTS[i],CUTS[i+1])
    b.close()

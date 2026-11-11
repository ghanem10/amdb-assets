import sys, subprocess, pathlib
sys.path.insert(0,'/home/claude/amdb')
from lux import FONTS
from playwright.sync_api import sync_playwright
R=pathlib.Path('/home/claude/amdb/reel')
html=(R/'reel.html').read_text(encoding='utf-8').replace('/*FONTS*/',FONTS).replace('LOGO','file:///home/claude/amdb/logo_round.png')
(R/'_built.html').write_text(html,encoding='utf-8')
FPS=30
def scene(name,a,b,stills=None):
    tmp=R/f'_tmp_{name}.mp4'; out=R/f'scene_{name}.mp4'
    ff=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-f','image2pipe','-framerate',str(FPS),'-c:v','mjpeg','-i','-',
        '-c:v','libx264','-preset','veryfast','-crf','18','-pix_fmt','yuv420p','-r',str(FPS),str(tmp)],stdin=subprocess.PIPE)
    n=round((b-a)*FPS)
    for i in range(n):
        t=a+i/FPS
        pg.evaluate(f'setTime({t})')
        ff.stdin.write(pg.screenshot(type='jpeg',quality=92))
    ff.stdin.close(); assert ff.wait()==0; tmp.rename(out)
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome')
    pg=b.new_page(viewport={'width':1080,'height':1920})
    pg.goto(f"file://{R/'_built.html'}"); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(500)
    mode=sys.argv[1]
    if mode=='stills':
        for t in [1.5,3.6,6.5,12.0,15.5,18.2,19.3,22.5,30.5,35.5,38.5]:
            pg.evaluate(f'setTime({t})'); pg.screenshot(path=str(R/f'still_{t}.jpg'),type='jpeg',quality=80)
    else:
        cuts=[0,4.55,9.05,16.0,19.5,25.75,31.95,36.3,40.5]
        only=[int(x) for x in sys.argv[2].split(',')] if len(sys.argv)>2 else range(len(cuts)-1)
        for i in only: scene(f'{i:02d}',cuts[i],cuts[i+1])
    b.close()

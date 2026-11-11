import numpy as np, wave
SR=48000; D=40.5; N=int(SR*D); t=np.arange(N)/SR
def hz(m): return 440*2**((m-69)/12)
chords=[[57,64,67,71,72],[53,60,64,67,69],[48,55,64,67,71],[55,62,67,69,74]]*2
L=D/len(chords); pad=np.zeros(N)
for i,ch in enumerate(chords):
    s=i*L-1.0; e=(i+1)*L+1.0
    env=np.clip((t-s)/1.4,0,1)*np.clip((e-t)/1.4,0,1); env=env*env*(3-2*env)
    if env.max()==0: continue
    for k,m in enumerate(ch):
        f=hz(m); amp=.11/(1+k*.25)
        pad+=env*amp*(np.sin(2*np.pi*f*t)+.5*np.sin(2*np.pi*f*1.003*t+1)+.25*np.sin(2*np.pi*f*2*t+2)*.5)
    root=hz(ch[0]-12); pad+=env*.10*np.sin(2*np.pi*root*t)
# slow tremolo-free swell + gentle lowpass (one-pole)
y=np.zeros_like(pad); a=.08
for _ in range(2):
    acc=0.0; out=np.empty_like(pad)
    for j in range(0,N):
        acc+=a*(pad[j]-acc); out[j]=acc
    pad=out
# soft bell plucks on scene changes
cuts=[4.55,9.05,16.0,19.5,25.75,31.95,36.3]
bell=np.zeros(N)
for c,m in zip(cuts,[76,79,74,81,76,79,84]):
    i0=int(c*SR); n=int(2.5*SR); tt=np.arange(n)/SR
    b=np.exp(-tt*2.2)*(np.sin(2*np.pi*hz(m)*tt)+.3*np.sin(2*np.pi*hz(m)*2.01*tt))*.06
    bell[i0:i0+n]+=b[:max(0,min(n,N-i0))]
# whoosh: band noise swell ending at cut
rng=np.random.default_rng(1); wh=np.zeros(N)
for c in cuts:
    n=int(.6*SR); i1=int(c*SR); i0=i1-n
    nz=rng.standard_normal(n); acc=0; o=np.empty(n)
    for j in range(n):
        k=.02+.25*(j/n); acc+=k*(nz[j]-acc); o[j]=acc
    wh[i0:i1]+=o*(np.linspace(0,1,n)**2)*.05
mix=pad+bell+wh
fade=np.clip((D-t)/2.5,0,1)*np.clip(t/1.0,0,1); mix*=fade
mix/=np.abs(mix).max()*1.12
st=np.stack([mix,np.roll(mix,int(.012*SR))],1)
w=wave.open('music.wav','wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
w.writeframes((st*32767).astype(np.int16).tobytes()); w.close()

import json,os,sys,urllib.request,urllib.error,random
VAL=(0,100,320,330,500,900,0)
PST=(0,0,0,0,0,0,0,0,5,10,10,-20,-20,10,10,5,5,-5,-10,0,0,-10,-5,5,0,0,0,20,20,0,0,0,5,5,10,25,25,10,5,5,10,10,20,30,30,20,10,10,50,50,50,50,50,50,50,50,0,0,0,0,0,0,0,0,-50,-40,-30,-30,-30,-30,-40,-50,-40,-20,0,0,0,0,-20,-40,-30,5,10,15,15,10,5,-30,-30,0,15,20,20,15,0,-30,-30,5,15,20,20,15,5,-30,-30,0,10,15,15,10,0,-30,-40,-20,0,5,5,0,-20,-40,-50,-40,-30,-30,-30,-30,-40,-50,-20,-10,-10,-10,-10,-10,-10,-20,-10,5,0,0,0,0,5,-10,-10,10,10,10,10,10,10,-10,-10,0,10,10,10,10,0,-10,-10,5,5,10,10,5,5,-10,-10,0,5,10,10,5,0,-10,-10,0,0,0,0,0,0,-10,-20,-10,-10,-10,-10,-10,-10,-20,0,0,0,5,5,0,0,0,-5,0,0,0,0,0,0,-5,-5,0,0,0,0,0,0,-5,-5,0,0,0,0,0,0,-5,-5,0,0,0,0,0,0,-5,-5,0,0,0,0,0,0,-5,5,10,10,10,10,10,10,5,0,0,0,0,0,0,0,0,-20,-10,-10,-5,-5,-10,-10,-20,-10,0,5,0,0,0,5,-10,-10,5,5,5,5,5,5,-10,0,0,5,5,5,5,0,-5,-5,0,5,5,5,5,0,-5,-10,0,5,5,5,5,0,-10,-10,0,0,0,0,0,0,-10,-20,-10,-10,-5,-5,-10,-10,-20,20,30,10,0,0,10,30,20,20,20,0,0,0,0,20,20,-10,-20,-20,-20,-20,-20,-20,-10,-20,-30,-30,-40,-40,-30,-30,-20,-30,-40,-40,-50,-50,-40,-40,-30,-30,-40,-40,-50,-50,-40,-40,-30,-30,-40,-40,-50,-50,-40,-40,-30,-30,-40,-40,-50,-50,-40,-40,-30)
N=(-33,-31,-18,-14,14,18,31,33)
K=(-17,-16,-15,-1,1,15,16,17)
Q=[r*16+f for r in range(8) for f in range(8)]
CM=[15]*128
CM[0]=13;CM[7]=14;CM[112]=7;CM[119]=11;CM[4]=12;CM[116]=3
random.seed(0x9E3779B97F4A7C15)
Z=[random.getrandbits(64) for _ in range(1689)]
E=[0]*1664
for i in range(6):
 for q in Q:
  r=q>>4;f=q&7
  E[(i+7)*128+q]=VAL[i+1]+PST[i*64+r*8+f]
  E[(5-i)*128+q]=-(VAL[i+1]+PST[i*64+(7-r)*8+f])
B=[0]*128;KS=[0,0];SD=0;CR=0;EP=-1;HM=0;KY=0;RP={};ST=[];ND=0;NPC=[0,0]
LIM=110000
KL=[0]*128
HS=[0]*1664
TK=[0]*131072;TM=[0]*131072;TS=[0]*131072;TD=[-1]*131072;TF=[0]*131072
class AB(Exception):pass
def A(s,c):
 if c==0:
  if not (s-15&0x88) and B[s-15]==1:return 1
  if not (s-17&0x88) and B[s-17]==1:return 1
 else:
  if not (s+15&0x88) and B[s+15]==-1:return 1
  if not (s+17&0x88) and B[s+17]==-1:return 1
 g=1 if c==0 else -1
 for d in N:
  t=s+d
  if not (t&0x88) and B[t]==2*g:return 1
 for d in K:
  t=s+d
  if not (t&0x88) and B[t]==6*g:return 1
 for d in (-16,-1,1,16):
  t=s+d
  while not (t&0x88):
   v=B[t]
   if v:
    if v==4*g or v==5*g:return 1
    break
   t+=d
 for d in (-17,-15,15,17):
  t=s+d
  while not (t&0x88):
   v=B[t]
   if v:
    if v==3*g or v==5*g:return 1
    break
   t+=d
 return 0
def G(c):
 ms=[];w=SD==0
 for q in Q:
  p=B[q]
  if not p or (p>0)!=w:continue
  a=abs(p)
  if a==1:
   d=16 if w else -16;r=q>>4;t=q+d
   if not (t&0x88) and not B[t]:
    prm=(r==6 and w) or (r==1 and not w)
    if prm:
     for pr in (5,4,3,2):ms.append(q|(t<<7)|(pr<<14))
    elif not c:
     ms.append(q|(t<<7))
     if (r==1 and w) or (r==6 and not w):
      t2=q+2*d
      if not B[t2]:ms.append(q|(t2<<7))
   for dd in (d-1,d+1):
    t=q+dd
    if t&0x88:continue
    v=B[t]
    if v and (v>0)!=w and abs(v)!=6:
     prm=(r==6 and w) or (r==1 and not w)
     if prm:
      for pr in (5,4,3,2):ms.append(q|(t<<7)|(pr<<14))
     else:ms.append(q|(t<<7))
    elif not v and t==EP:ms.append(q|(t<<7))
  elif a==2:
   for dd in N:
    t=q+dd
    if t&0x88:continue
    v=B[t]
    if not v:
     if not c:ms.append(q|(t<<7))
    elif (v>0)!=w and abs(v)!=6:ms.append(q|(t<<7))
  elif a==6:
   for dd in K:
    t=q+dd
    if t&0x88:continue
    v=B[t]
    if not v:
     if not c:ms.append(q|(t<<7))
    elif (v>0)!=w and abs(v)!=6:ms.append(q|(t<<7))
   if not c:
    if w:
     if CR&1 and not B[5] and not B[6] and B[7]==4 and not A(4,1) and not A(5,1) and not A(6,1):ms.append(4|(6<<7))
     if CR&2 and not B[3] and not B[2] and not B[1] and B[0]==4 and not A(4,1) and not A(3,1) and not A(2,1):ms.append(4|(2<<7))
    else:
     if CR&4 and not B[117] and not B[118] and B[119]==-4 and not A(116,0) and not A(117,0) and not A(118,0):ms.append(116|(118<<7))
     if CR&8 and not B[115] and not B[114] and not B[113] and B[112]==-4 and not A(116,0) and not A(115,0) and not A(114,0):ms.append(116|(114<<7))
  else:
   ds=(-16,-1,1,16) if a==4 else (-17,-15,15,17) if a==3 else (-17,-16,-15,-1,1,15,16,17)
   for dd in ds:
    t=q+dd
    while not (t&0x88):
     v=B[t]
     if not v:
      if not c:ms.append(q|(t<<7))
     else:
      if (v>0)!=w and abs(v)!=6:ms.append(q|(t<<7))
      break
     t+=dd
 return ms
def MK(m):
 global SD,CR,EP,HM,KY
 f=m&127;t=(m>>7)&127;pr=m>>14
 pc=B[f];cp=B[t];cq=t
 if abs(pc)==1 and t==EP and not cp:
  cq=t-16 if SD==0 else t+16;cp=B[cq]
 rf=-1;rt=-1
 if abs(pc)==6 and abs(t-f)==2:
  if t>f:rf,rt=(7,5) if SD==0 else (119,117)
  else:rf,rt=(0,3) if SD==0 else (112,115)
 ST.append((m,pc,cp,cq,CR,EP,HM,KY,rf,rt))
 KY^=Z[(pc+6)*128+f]
 if cp:KY^=Z[(cp+6)*128+cq]
 if EP>=0:KY^=Z[1681+(EP&7)]
 KY^=Z[1665+CR];KY^=Z[1664]
 B[f]=0
 if cp:B[cq]=0
 if rf>=0:
  B[rt]=B[rf];B[rf]=0
  KY^=Z[(B[rt]+6)*128+rf]^Z[(B[rt]+6)*128+rt]
 np=(pr if SD==0 else -pr) if pr else pc
 B[t]=np
 KY^=Z[(np+6)*128+t]
 if abs(pc)==6:KS[SD]=t
 CR&=CM[f]&CM[t]
 KY^=Z[1665+CR]
 if abs(pc)==1 and abs(t-f)==32:
  EP=f+16 if SD==0 else f-16;KY^=Z[1681+(EP&7)]
 else:EP=-1
 HM=0 if abs(pc)==1 or cp else HM+1
 if cp and abs(cp) not in (1,6):NPC[1-SD]-=1
 if pr:NPC[SD]+=1
 SD^=1
 RP[KY]=RP.get(KY,0)+1
 if A(KS[1-SD],SD):
  UN();return 0
 return 1
def UN():
 global SD,CR,EP,HM,KY
 m,pc,cp,cq,cr,ep,hm,ky,rf,rt=ST.pop()
 RP[KY]-=1
 if m<0:
  SD^=1;CR,EP,HM,KY=cr,ep,hm,ky;return
 f=m&127;t=(m>>7)&127
 if abs(pc)==6:KS[1-SD]=f
 if rf>=0:B[rf]=B[rt];B[rt]=0
 B[f]=pc;B[t]=0
 if cp:B[cq]=cp
 if cp and abs(cp) not in (1,6):NPC[SD]+=1
 if m>>14:NPC[1-SD]-=1
 SD^=1;CR,EP,HM,KY=cr,ep,hm,ky
def NM():
 global SD,EP,HM,KY
 ST.append((-1,0,0,0,CR,EP,HM,KY,-1,-1))
 if EP>=0:KY^=Z[1681+(EP&7)];EP=-1
 KY^=Z[1664];SD^=1;HM+=1
 RP[KY]=RP.get(KY,0)+1
def NU():UN()
def V():
 s=0
 for q in Q:
  p=B[q]
  if p:s+=E[(p+6)*128+q]
 return s if SD==0 else -s
def J(a,b,y):
 global ND
 ND+=1
 if ND>LIM:raise AB
 if RP.get(KY,0)>2 or HM>=100:return 0
 ck=A(KS[SD],1-SD)
 if not ck:
  sp=V()
  if sp>=b:return b
  if sp>a:a=sp
  ms=G(1)
 else:ms=G(0)
 ol=[]
 for m in ms:
  f=m&127;t=(m>>7)&127;pc=B[f];pr=m>>14
  v=B[t]
  if not v and abs(pc)==1 and t==EP:v=-1 if SD==0 else 1
  sc=VAL[abs(v)]*32-VAL[abs(pc)]//8+(VAL[pr] if pr else 0) if v else (VAL[pr] if pr else 0)
  ol.append((sc,m))
 ol.sort(reverse=True)
 lg=0
 for sc,m in ol:
  f=m&127;t=(m>>7)&127;pc=B[f];pr=m>>14
  v=B[t]
  if not v and abs(pc)==1 and t==EP:v=-1 if SD==0 else 1
  if not ck and v and not pr and sp+VAL[abs(v)]+200<a:continue
  if not MK(m):continue
  lg+=1
  s=-J(-b,-a,y+1)
  UN()
  if s>a:a=s
  if a>=b:return a
 if ck and not lg:return -1000000+y
 return a
def F(a,b,d,y,n):
 global ND
 ND+=1
 if ND>LIM:raise AB
 if RP.get(KY,0)>2 or HM>=100:return 0
 if d<=0:return J(a,b,y)
 i=KY&131071;ttm=0
 if TK[i]==KY and TD[i]>=d:
  s=TS[i]
  if s>900000:s-=y
  elif s<-900000:s+=y
  fl=TF[i]
  if fl==0:return s
  if fl==1 and s>=b:return s
  if fl==2 and s<=a:return s
  ttm=TM[i]
 ck=A(KS[SD],1-SD)
 if d>=3 and not ck and n and NPC[SD]>0:
  NM()
  s=-F(-b,-b+1,d-3,y+1,0)
  NU()
  if s>=b:return b
 ms=G(0)
 ol=[]
 for m in ms:
  f=m&127;t=(m>>7)&127;pc=B[f];pr=m>>14
  if m==ttm:sc=1<<22
  else:
   v=B[t]
   if not v and abs(pc)==1 and t==EP:v=-1 if SD==0 else 1
   if v:sc=(1<<21)+VAL[abs(v)]*32-VAL[abs(pc)]//8+(VAL[pr] if pr else 0)
   elif pr:sc=(1<<20)+VAL[pr]
   elif m==KL[2*y]:sc=(1<<19)+1000
   elif m==KL[2*y+1]:sc=1<<19
   else:sc=HS[(pc+6)*128+t]
  ol.append((sc,m))
 ol.sort(reverse=True)
 best=-2000000;bm=0;a0=a;lg=0;fi=1
 for j in range(len(ol)):
  sc,m=ol[j]
  f=m&127;t=(m>>7)&127;pc=B[f];pr=m>>14
  v=B[t]
  if not v and abs(pc)==1 and t==EP:v=-1 if SD==0 else 1
  isq=not v and not pr
  if not MK(m):continue
  lg+=1
  if fi:s=-F(-b,-a,d-1,y+1,1);fi=0
  else:
   s=-F(-a-1,-a,d-1,y+1,1)
   if a<s<b:s=-F(-b,-a,d-1,y+1,1)
  UN()
  if s>best:best=s;bm=m
  if s>a:a=s
  if a>=b:
   if isq:
    if KL[2*y]!=m:KL[2*y+1]=KL[2*y];KL[2*y]=m
    HS[(pc+6)*128+t]+=d*d
   break
 if not lg:return -1000000+y if ck else 0
 s2=best+y if best>900000 else best-y if best<-900000 else best
 TK[i]=KY;TM[i]=bm;TS[i]=s2;TD[i]=d
 TF[i]=2 if best<=a0 else 1 if best>=b else 0
 return best
def R():
 global ND
 ND=0
 ms=G(0)
 lm=[]
 for m in ms:
  if MK(m):lm.append(m);UN()
 if not lm:return 0,-2000000
 sc={m:0 for m in lm}
 bm=lm[0];bs=-2000000
 try:
  for d in range(1,64):
   lm.sort(key=lambda m:-sc[m])
   a=-2000000
   for m in lm:
    MK(m)
    try:s=-F(-2000000,-a,d-1,1,1)
    except AB:UN();raise
    UN()
    sc[m]=s
    if s>a:a=s
   bm=max(lm,key=lambda m:sc[m]);bs=sc[bm]
   if bs>=1000000-64:break
 except AB:pass
 return bm,bs
def KC():
 k=0
 for q in Q:
  p=B[q]
  if p:k^=Z[(p+6)*128+q]
 if SD:k^=Z[1664]
 k^=Z[1665+CR]
 if EP>=0:k^=Z[1681+(EP&7)]
 return k
def Y():
 global B,KS,SD,CR,EP,HM,KY,RP,ST,NPC
 B=[0]*128
 bk=(4,2,3,5,6,3,2,4)
 for f in range(8):
  B[f]=bk[f];B[16+f]=1;B[96+f]=-1;B[112+f]=-bk[f]
 KS=[4,116];SD=0;CR=15;EP=-1;HM=0;NPC=[7,7]
 KY=KC();RP={KY:1};ST=[]
U=os.environ.get('MAKEFUN_ENV_URL') or ''
def post(p,b):
 r=urllib.request.Request(U+p,data=json.dumps(b).encode(),headers={'content-type':'application/json'})
 try:
  with urllib.request.urlopen(r) as x:return json.load(x)
 except urllib.error.HTTPError as e:sys.exit(p+': HTTP '+str(e.code))
def uci(m):
 f=m&127;t=(m>>7)&127;pr=m>>14
 s='abcdefgh'[f&7]+str((f>>4)+1)+'abcdefgh'[t&7]+str((t>>4)+1)
 return s+('nbrq'[pr-2] if pr else '')
def pu(u):
 f='abcdefgh'.index(u[0])+(int(u[1])-1)*16
 t='abcdefgh'.index(u[2])+(int(u[3])-1)*16
 pr='nbrq'.index(u[4])+2 if len(u)==5 else 0
 return f|(t<<7)|(pr<<14)
if __name__=='__main__':
 if not U:sys.exit('MAKEFUN_ENV_URL is not set')
 while True:
  g=post('/game',{})
  if g['status']=='done':break
  while g['status']=='your_move':
   Y()
   for u in g['moves']:MK(pu(u))
   m,s=R()
   if s<-1500:
    post('/resign',{'game':g['game']});break
   g=post('/move',{'game':g['game'],'move':uci(m)})

#to renew the route of openvpn 
import os,glob
routefile="routes.txt"
if os.path.exists(routefile):
    os.remove(routefile)
##since chnroutes is too large, i choose the bestroutetb which is a node based tools from https://github.com/ashi009/bestroutetb
##just put this file into the location of ovpn config files
print  "getting route config file..."
os.popen("bestroutetb --route.vpn=us -p openvpn -o "+routefile)
print  "getting route config file end."
f=open(routefile)
route=f.read()
f.close()
files=glob.glob("*.ovpn")
for fname in files :
    f=open(fname, 'r') 
    print fname
    content=[]
    for l in f:
        if l.strip().split(" ")[0]!="route":
            content.append(l);
    f.close()
    open(fname,"w").write("".join(content))
    open(fname,"a").write("\r\n"+route)
os.remove(routefile) 
    


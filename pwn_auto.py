#coding:utf-8
import os
import sys
import random
import time
def creatflag():
	random.seed(time.time())
	fl='flag{'
	for j in range(32):
		fl=fl+chr(random.randint(0,25)+ord('a'))
	fl=fl+'}'
	return fl
print(sys.path[0])
po=open(sys.path[0]+'/port')
port=int(po.readline(),10)
print port
po.close()
PWN_path=sys.path[0]+'/pwn/'
pwn_names=[name for name in os.listdir(PWN_path)]
flag=""
print pwn_names
for i in pwn_names:
	port=port+1
	os.system("mkdir "+sys.path[0]+'/'+i)
	flag=creatflag()
	print flag
	#fd = open(sys.path[0]+'/'+i+'/'+'flag', mode="w")
	#fd.write(str(flag))
	os.system("echo "+flag+" > "+sys.path[0]+'/'+str(i)+'/'+'flag')
	fd.close()
	os.system("cp "+sys.path[0]+'/pwn/'+i+' '+sys.path[0]+'/'+i+'/'+'pwn')
	os.system("cp "+sys.path[0]+'/docker/ctf.xinetd'+' '+sys.path[0]+'/'+i+'/ctf.xinetd')
	os.system("cp "+sys.path[0]+'/docker/Dockerfile'+' '+sys.path[0]+'/'+i+'/Dockerfile')
	os.system("cd "+sys.path[0]+'/'+str(i)+'/'+' '+'&& '+"docker build -t "+str(i)+'auto .')
	os.system("cd "+sys.path[0]+'/'+str(i)+'/'+' '+'&& '+"docker run -p "+str(port)+':8888 -v /data:/data -d '+i+'auto')
	print i+' '+'port:'+str(port)
	ag=open(sys.path[0]+'/flag',mode="a")
	ag.write(i+' '+'port:'+str(port)+'flag: '+flag +' \n')
	os.system("mkdir "+sys.path[0]+'/output/'+i)
	os.system("cp "+sys.path[0]+'/pwn/'+i+'  '+sys.path[0]+'/output/'+i)
	wenjian=open(sys.path[0]+'/output/'+i+'/meta.txt',mode="w")
	wenjian.write('<message>'+'nc '+'www.hutc.xyz :'+str(port)+' \n'+'<flag>'+flag)
po=po=open(sys.path[0]+'/port',"w")
po.write(str(port))


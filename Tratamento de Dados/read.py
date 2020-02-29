import matplotlib.pyplot as plt
import numpy as np
import os


doc = open("trajetoria_bola"".dat","r")
doc = doc.readlines()
docp = ""
docl = []
x =[]
y =[]
t =[]



for i in range(len(doc)):
    docp+=doc[i]
    
for i in range(len(doc)):
    docl.append(doc[i].replace('\n','').replace(' ','').split('\t'))
    
for i in range(len(docl)):
    for d in range(len(docl[i])):
        docl[i][d] = docl[i][d].replace(',','.')
docl.pop(-1)
docl.pop(-1)

c = 1

dt = open('t.dat','w')#Criando os arquivos para cada dado.
dx = open('x.dat','w')
dy = open('y.dat','w')
print(doc[c][0])
while c<len(docl):
    t.append(docl[c][0])
    x.append(docl[c][1])
    y.append(docl[c][2])
    dt.write(docl[c][0]+'\n')#Escrevendo a linha especifica no arquivo.
    dx.write(docl[c][1]+'\n')
    dy.write(docl[c][2]+'\n')
    c+=1
dt.close()#Fechando arquivo.
dx.close()
dy.close()    
#dx = np.array(range(len(t)))*10

#dy = np.array(range(len(y)))*10

#plt.plot(t, x,'go')   #usar essa parte pra projetar o eixo x em relação ao tempo/s
#plt.plot(t,x,'k:',color='red')

#plt.plot(t,y,'r^')     #usar essa parte pra projetar o eixo y em relação ao tempo/s
#plt.plot(t,y,'k--',color='blue')

#plt.grid(True)
#plt.title('Grafico de movimentação trajetória da bola')
#plt.xlabel('tempo/s')
#plt.ylabel('eixo x') #utilizar essa pro x

#plt.xlabel('tempo/s')#utilizar essa pro y
#plt.ylabel('eixo y')


#plt.show()




     
    
# 4,46	8,457	4,550 // 4,54	8,510	4,550
# 5,68	8,895	4,272 // 5,76	8,895	4,232

#ALGORITMO DE TREINAMENTO - REDE ADALINE

import numpy as np 

#DADOS DE ENTRADA DA AMOSTRA DE TREINAMENTO

x1=np.array([[-1,-1,-1,-1],[0.1, 0.3, 0.6, 0.5],[0.4,0.7,0.9,0.7],[0.7,0.2,0.8,0.1]])

#DADOS DE SAÍDA PARA A AMOSTRA DE TREINAMENTO
d=np.array([[1, -1, -1, 1]])

#INICIALIZAÇÃO DOS PESOS

w2=np.array([0.5, 0.2, 0.3, 0.4])

#TAXA DE APRENDIZAGEM
ef=0.7

#Erro quadrático médio
Eqm=0
Eqma=1
elim=0.001
e=np.absolute(Eqma-Eqm)

# INICIALIZAÇÃO DO NÚMERO DE ÉPOCAS E DO ERRO
ep=0

# LOOP DE APRENDIZAGEM

while (True):
    
 for i in range(0,4):
     
 #POTENCIAL DE ATIVAÇÃO POR AMOSTRA DE TREINAMENTO E ERRO QUADRÁTICO MÉDIO
    
     x2=x1[:,i]
     x3=x2[:,np.newaxis]
     
     u=np.dot(w2,x3)
     erro=d[0,i]-u  
          
     Eqm=Eqm+np.square(erro)
     p=len(x1)
     Eqm=Eqm/p
     e=np.absolute(Eqma-Eqm)  
     
 # ATUALIZAÇÃO DO ERRO POR AMOSTRA
 
     if i==0:
         aux1=erro*x2
     if i==1:
         aux2=erro*x2
     if i==2:
         aux3=erro*x2
     if i==3:
         aux4=erro*x2

 # ALGORÍTMO DE APRENDIZAGEM
    
 while (e>elim): 
     
    aux_t=aux1+aux2+aux3+aux4
    w2=w2-ef*aux_t    
       
    x3=x2[:,np.newaxis]
    u=np.dot(w2,x3)
       
    erro=d[0,i]-u
    Eqma=Eqm+np.square(erro)
    Eqma=Eqma/p
    e=np.absolute(Eqma-Eqm)
    Eqm=Eqma

    ep=ep+1

    print("EPOCAS:",ep)
               
   
 break        


#ALGORITMO DE OPERAÇÃO - REDE ADALINE

# AMOSTRA A SER CLASSIFICADA

amostra=np.array([[-1, 0.5, 0.7, 0.1]])
amostra2=amostra[0]
amostra3=amostra2[:,np.newaxis]

# CALCULO DO POTENCIAL DE ATIVAÇÃO
 
u2=np.dot(w2,amostra3)

# FUNÇÃO SINAL - DEGRAU BIPOLAR
    
if u2 < 0:
      y=-1
if u2==0:
      y=0       
if u2 > 0:
     y=1
     
# CLASSIFICAÇÃO FINAL DA AMOSTRA
        
if y==-1:
   print("AMOSTRA PERTENCE A CLASSE A ")
if y==1:
  print("AMOSTRA PERTENCE A CLASSE B")


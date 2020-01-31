#bin/usr

import decimal
from decimal import Decimal
import random
import os
import timeit
import time
import csv
import pickle
import pandas
import numpy as np
from sklearn import preprocessing
import matplotlib.pyplot as plt


#key generation for K(m=14)
m=7
y=1000
n=1011
A =41
tau =[]# 1st componeent
for i  in range (0,m):
      tau.append([random.uniform(1,1000),random.uniform(1000,2000),random.uniform(2000,3000)])

Theta = [] #2nd component
Theta.append(random.uniform(1,500))
Theta.append(random.uniform(2500,2000))
Theta.append(1)
Phi=[]#3rd component
for i in range(0,3):
      r=[]
      Phi.append([])
      for j in range (0,m):
            r.append(random.uniform(1,100))
      Phi[i].append(tau[0][0]*tau[0][2]*Theta[i] + tau[0][1]*r[m-1] + tau[0][0]*(r[0] - r[m-2]))
      for k in range(1,m-1):
            Phi[i].append(tau[k][0]*tau[k][2]*Theta[i] + tau[k][1]*r[m-1] + tau[k][0]*(r[k]-r[k-1]))

      Phi[i].append( (tau[m-1][0] + tau[m-1][1] + tau[m-1][2]) * r[m-1])


#Encryption
ru1 = random.uniform(5000,10000)
ru2 = random.uniform(10000,15000) 
def Enc(Phi,v,ru1,ru2):
      ru3 = v - ru1*Theta[0] - ru2*Theta[1]
      E=[]
      for i in range (0,m):
            E.append(ru1*Phi[0][i] + ru2*Phi[1][i] + ru3*Phi[2][i])
      return E
      

#Decryption
def Dec(E,tau):
      T=0
      c= 0
      for i in range(0,m-1):
            T += tau[i][2]
      S = E[m-1]/float(tau[m-1][0] + tau[m-1][1] + tau[m-1][2])
      for i  in range (0,m-1):
            c += (E[i] - S*float(tau[i][1]))/float(tau[i][0])

      c = c/float(T)
      c = int(round(c))
      return c


# main data owner function
def data_owner(file_obj):
    data = pandas.read_csv("20 Percent Training Set.csv")
    data['duration'] = preprocessing.scale(data['duration'])
    #data['protocol_type'] = preprocessing.scale(data['protocol_type'])
    #data['service'] = preprocessing.scale(data['service'])
    #data['flag'] = preprocessing.scale(data['flag'])
    data['src_bytes'] = preprocessing.scale(data['src_bytes'])
    data['dst_bytes'] = preprocessing.scale(data['dst_bytes'])
    data['land'] = preprocessing.scale(data['land'])
    data['wrong_fragment'] = preprocessing.scale(data['wrong_fragment'])
    data['urgent'] = preprocessing.scale(data['urgent'])
    data['hot'] = preprocessing.scale(data['hot'])
    data['num_failed_logins'] = preprocessing.scale(data['num_failed_logins'])
    data['logged_in'] = preprocessing.scale(data['logged_in'])
    data['num_compromised'] = preprocessing.scale(data['num_compromised'])
    data['root_shell'] = preprocessing.scale(data['root_shell'])
    data['su_attempted'] = preprocessing.scale(data['su_attempted'])
    data['num_root'] = preprocessing.scale(data['num_root'])
    data['num_file_creations'] = preprocessing.scale(data['num_file_creations'])
    data['num_shells'] = preprocessing.scale(data['num_shells'])
    data['num_access_files'] = preprocessing.scale(data['num_access_files'])
    data['num_outbound_cmds'] = preprocessing.scale(data['num_outbound_cmds'])
    data['is_host_login'] = preprocessing.scale(data['is_host_login'])
    data['is_guest_login'] = preprocessing.scale(data['is_guest_login'])
    data['count'] = preprocessing.scale(data['count'])
    data['srv_count'] = preprocessing.scale(data['srv_count'])
    data['serror_rate'] = preprocessing.scale(data['serror_rate'])
    data['srv_serror_rate'] = preprocessing.scale(data['srv_serror_rate'])
    data['rerror_rate'] = preprocessing.scale(data['rerror_rate'])
    data['srv_rerror_rate'] = preprocessing.scale(data['srv_rerror_rate'])
    data['same_srv_rate'] = preprocessing.scale(data['same_srv_rate'])
    data['diff_srv_rate'] = preprocessing.scale(data['diff_srv_rate'])
    data['srv_diff_host_rate'] = preprocessing.scale(data['srv_diff_host_rate'])
    data['dst_host_count'] = preprocessing.scale(data['dst_host_count'])
    data['dst_host_srv_count'] = preprocessing.scale(data['dst_host_srv_count'])
    data['dst_host_same_srv_rate'] = preprocessing.scale(data['dst_host_same_srv_rate'])
    data['dst_host_diff_srv_rate'] = preprocessing.scale(data['dst_host_diff_srv_rate'])
    data['dst_host_same_src_port_rate'] = preprocessing.scale(data['dst_host_same_src_port_rate'])
    data['dst_host_srv_diff_host_rate'] = preprocessing.scale(data['dst_host_srv_diff_host_rate'])
    data['dst_host_serror_rate'] = preprocessing.scale(data['dst_host_serror_rate'])
    data['dst_host_srv_serror_rate'] = preprocessing.scale(data['dst_host_srv_serror_rate'])
    data['dst_host_rerror_rate'] = preprocessing.scale(data['dst_host_rerror_rate'])
    data['dst_host_srv_rerror_rate'] = preprocessing.scale(data['dst_host_srv_rerror_rate'])
    reader = csv.reader(file_obj, delimiter=',')
    data_list = list(reader)
    f = open("output.csv", "w", newline = "")
    writer = csv.writer(f)
    d1 = dict()
    count1=0
    d2 = dict()
    count2=0
    d3 = dict()
    count3=0
    n = len(data_list)
    A = len(data_list[0])-2
    eds = []
    udm = [[[0 for k in range(A)] for j in range(4)] for i in range(n-1)]
    for line in data_list[1:]:
        line.pop()
        line.pop()
        line_d = list(line)
        line[0] = float(line[0])
        line_d[0] = float(line[0])
        line_d[0] =Enc(Phi,line_d[0],ru1,ru2)
        for i in range (4,41):
              line[i] = float(line[i])
              line_d[i] = float(line[i])
              line_d[i] = Enc(Phi,line_d[i],ru1,ru2)
        if line[1] in list(d1.keys()):
              line[1] = d1[line[1] ]
              line_d[1] = line[1]
              line_d[1] = Enc(Phi,line_d[1],ru1,ru2)
        else:
              d1[line[1]] = count1
              line[1] = count1
              line_d[1] = Enc(Phi,count1,ru1,ru2)              
              count1 = count1  + 1
        if line[2] in list(d2.keys()):
              line[2] = d2[line[2] ]
              line_d[2] = line[2]
              line_d[2] = Enc(Phi,line_d[2],ru1,ru2)
        else:
              d2[line[2]] = count2
              line[2] = count2
              line_d[2] = Enc(Phi,count2,ru1,ru2)
              count2 = count2  + 1
        if line[3] in list(d3.keys()):
              line[3] = d3[line[3] ]
              line_d[3] = line[3]
              line_d[3] = Enc(Phi,line_d[3],ru1,ru2)
        else:
              d3[line[3]] = count3
              line[3] = count3
              line_d[3] = Enc(Phi,count3,ru1,ru2)
              count3 = count3  + 1
        eds.append(line_d)
        writer.writerow(line)
    with open('eds.pkl', 'wb') as f:
           pickle.dump(eds, f)#saving encrypted dataset for access by the the third party
    for i in range(1,n):
          for j in range(4):
                for k in range(A):
                      udm[i-1][j][k] = data_list[i][k] - data_list[j+1][k]#createing the udm
    with open('udm.pkl', 'wb') as f:
           pickle.dump(udm, f)#saving udm for access by the the third party      


if __name__ == "__main__":
      #with open("20 Percent Training Set.csv") as f_obj:
          #data_owner(f_obj)
      sm = [[0 for k in range(A)] for j in range(4)]
      dec = 1
      print("update UDM?")
      dec = int(input())
      while(dec==1):
            with open('sm.pkl', 'rb') as b:
                  esm = pickle.load(b)
            with open('udm.pkl', 'rb') as v:
                  udm = pickle.load(v)
            for z in range(4):
                  for q in range(A):
                        sm[z][q] = Dec(esm[z][q],tau)
            for z in range(4):
                  print(sm[z])
            for w in range(n):
                  for z in range(4):
                        for q in range(A):
                              udm[w][z][q] += sm[z][q]
            print("added")
            with open('udm.pkl', 'wb') as f:
                  pickle.dump(udm, f)
            print("UDM upadted")
            print("update UDM?")
            dec = int(input())
      with open('clusters.pkl', 'rb') as b:
            C = pickle.load(b)
      print(len(C[0]))
      print(len(C[1]))
      print(len(C[2]))
      print(len(C[3]))
      colors = 10*["r", "g", "c", "b", "k"]
      with open("20 Percent Training Set.csv") as file_obj:
            reader = csv.reader(file_obj, delimiter=',')
            data_list = list(reader)
      d1 = dict()
      count1=0
      d2 = dict()
      count2=0
      d3 = dict()
      count3=0
      for line in data_list[1:]:
            line[4] = float(line[4])
            if line[1] in list(d1.keys()):
                  line[1] = d1[line[1] ]+ random.uniform(-0.1,0.1)
            else:
                  d1[line[1]] = count1
                  line[1] = count1+ random.uniform(-0.1,0.1)            
                  count1 = count1  + 1
            if line[2] in list(d2.keys()):
                  line[2] = d2[line[2] ] + random.uniform(-0.1,0.1)
            else:
                  d2[line[2]] = count2
                  line[2] = count2+ random.uniform(-0.1,0.1)         
                  count2 = count2 + 1
            if line[3] in list(d3.keys()):
                  line[3] = d3[line[3] ]+ random.uniform(-0.1,0.1)
            else:
                  d3[line[3]] = count3
                  line[3] = count3 + random.uniform(-0.1,0.1)           
                  count3 = count3  + 1            
            if line[41] == "normal":
                  line[41] = 1
            if line[41] == "back":
                  line[41] = 7
            if line[41] == "land":
                  line[41] = 7.5
            if line[41] == "neptune":
                  line[41] = 8
            if line[41] == "pod":
                  line[41] = 8.5
            if line[41] == "smurf":
                  line[41] = 9
            if line[41] == "teardrop":
                  line[41] = 9.5
            if line[41] == "buffer_overflow":
                  line[41] = 16
            if line[41] == "perl":
                  line[41] = 16.5
            if line[41] == "rootkit":
                  line[41] = 17
            if line[41] == "loadmodule":
                  line[41] = 17.5
            if line[41] == "ftp_write":
                  line[41] = 24
            if line[41] == "guess_passwd":
                  line[41] = 24.5
            if line[41] == "spy":
                  line[41] = 25
            if line[41] == "warezclient":
                  line[41] = 25.5
            if line[41] == "warezmaster":
                  line[41] = 25.5
            if line[41] == "imap":
                  line[41] = 26
            if line[41] == "phf":
                  line[41] = 26
            if line[41] == "multihop":
                  line[41] = 26.5
            if line[41] == "ipsweep":
                  line[41] = 30
            if line[41] == "nmap":
                  line[41] = 30.5
            if line[41] == "portsweep":
                  line[41] = 31
            if line[41] == "satan":
                  line[41] = 31.5
            
      for i in range (1,2001):
            cul =0
            for p in range(4):
                  if i in C[p]:
                        cul = p
                        break                        
            plt.scatter(data_list[i][0], data_list[i][41], color = colors[cul],s = 30)
      plt.show()

            


      

                 

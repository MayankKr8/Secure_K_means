import csv
import pickle
import sys
import copy
 #shift matrix

k =4 #number of clusters
n =1011
m =7
A= 41

with open('eds.pkl', 'rb') as f:
      eds = pickle.load(f)
with open('udm.pkl', 'rb') as g:
      udm = pickle.load(g)
C = []
B = []
Cent_t = []
sm =[]

def cal_sim(i,j):
      ans = 0
      for l in range(41):
            ans += (udm[i][j][l])*(udm[i][j][l])    
      return ans

def pop_clusters(x):
      global C,B
      for i in range(x,len(eds)):
            min_sim = sys.maxsize
            c =0
            for j in range(k):
                  if i>j:
                        sim = cal_sim(i,j)
                  else:
                        sim =  cal_sim(j,i)                  
                  if sim<min_sim :
                        min_sim =sim
                        c = j
            C[c].append(eds[i])
            B[c].append(i)
      print(len(C[0]))
      print(len(C[1]))
      print(len(C[2]))
      print(len(C[3]))

def cal_centroids():
      global Cent_t
      for  p in range(k):
            for j in range (A):
                  for l in range (m):
                        Cent_t[p][j][l] = 0
                        for q in range(len(C[p])):
                              Cent_t[p][j][l] += C[p][q][j][l]
                        Cent_t[p][j][l] = Cent_t[p][j][l]/len(C[p])
                              
      
def third_party():
      global C,B, Cent_t,s,udm
      flag =0
      Cent = []
      for i in range(k):
            C.append([eds[k]])
            B.append([i])
            Cent.append(eds[k])
      for o in range(len(C)):
            Cent_t.append([[0 for c1 in range(len(C[0][0][0]))] for c2 in range(len(C[0][0]))])          
      pop_clusters(k)
      cal_centroids()
      for w in range(k):
            sm.append([[0 for z in range(m)] for x in range(A)])
      print("sm created")
      count =0
      while(flag==0 and count<10):
            count +=1
            for z in range(k):
                  for x in range(A):
                        for v in range(m):
                              sm[z][x][v] = float(Cent_t[z][x][v]) - float(Cent[z][x][v])                                    
            print("sm updated")
            with open('sm.pkl', 'wb') as f:
                  pickle.dump(sm, f)
            a = 0
            while(a==0):
                  print("UDM updated? ")
                  a = input()            
            with open('udm.pkl', 'rb') as g:
                  udm = pickle.load(g)
            C[0] =[]
            C[1] = [] 
            C[2] =[]
            C[3] = []
            B[0] =[]
            B[1] = [] 
            B[2] =[]
            B[3] = []
            pop_clusters(0)
            Cent =[[[x for x in b] for b in r] for r in Cent_t]
            cal_centroids()
            print(Cent[0][0])
            print(Cent_t[0][0])
            if Cent == Cent_t:
                  flag=1
            #for z in range(k):
                  #for x in range(A):
                        #for v in range(m):
                              #if abs(float(Cent_t[z][x][v]) - float(Cent[z][x][v]))>10:
                                    #flag=0
                                    #break
                              #else:
                                    #flag =1
      with open('clusters.pkl', 'wb') as f:
            pickle.dump(B, f)
            
            

if __name__ == "__main__":
          third_party()

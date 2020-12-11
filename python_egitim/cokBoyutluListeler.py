# %% 2 boytulu liste
#25.11.2020 Edirne'nin Kurtuluşu
liste=[[1,2,3],[4,5,6],[7,8,9]]

for i in liste:
    print(i)
# %% 
import random
l=[]
for i in range(10):
    l.append(random.randint(1,30))

print(l)

# %% manuel liste
nl = [1,2,3]
cbl = [[1,4],[2,5],[3,6,7]]
print(cbl[2])
print(cbl[2][0])
cbl[2][0]=333
print(cbl[2][0])




# %%
cbl = [[1,4],[2,5],[3,6,7]]
# for e1 in cbl:
#     print(e1)

# for e1 in cbl:
#     for e2 in e1:
#        print(e2,end=" ")
#     print()
# cbl deki çift ve tek olanların farkını bul
tt=0
ct=0
for e1 in cbl:
    for e2 in e1:
        if e2%2==0:
            ct+=e2
        else:
            tt+=e2

print(ct-tt)
# %% liste fonksiyonları var
# dir komutu tiplerin fonksiyonlarını listeler

print(dir(list))

# %% append listenin sonuna eleman ekler

lm = []

for r in range(10):
    lm.append(r)
print(lm)
# clear liste elemanlaırnı yok eder
lm.clear()
print(lm)
# %% copy sadece değerlerin 
# kopyalanmasını sağlar
a=5
b=a
b=8
print(a,b)
l1=[1,2,3]
l2=l1.copy()
print(l1,l2,sep="@")
l2[0]=333
print(l1,l2,sep="@")
print("l1 id=",id(l1))
print("l2 id=",id(l2))
# %% index bir elemanın listededeki index
# değerini döndürür

l4=[10,20,50,55,7,78,[20,32]]

print(l4.index(20))
print(l4.index(7))
print(l4.index([20,32]))
if 38 in l4:
    print(l4.index(38))
else:
    print(38,"yok")
# %% 
# count', 'index', 
# 'insert', 'pop', 
# 'remove', 'reverse', 'sort'

print(dir(list))
# %% count parametre/argüman olarak girilen
# değerin listede kaç adet olduğunun sonucunu
# döndürür
l4=[10,20,50,55,7,78,[20,32,20]]

print(l4.count(10))
print(l4.count(100))
print(l4.count(20))
print(l4[6].count(20))




# %% sayısal 6/49
import random

# for i in range(6):
#     print(random.randint(1,49))

l=[]
while len(l)<6:
    tut=random.randint(1,49)
    if tut not in l:
        l.append(tut)
print(l)

l.append("3.4")
# sort komutu listeyi küçükten büyüğe sıralar
#sırlanacak eleman türleri aynı olmalı
l.sort()
print("sıralı liste a_z",l)
l.reverse()
print("ters sıralı liste z_a",l)

# %% remove bir dğeri listeden siler. 
# soldan sağa ratladığı ilk değeri siler
# silinecek değer yoksa hata verir.

l=[1,2,3,2]
l.remove(22)
print(l)



# %% insert istenen bir indise eleman ekler
# son idnisten büyükse en sona ekler

l=[1,2,3]
l.insert(0,333)
print(l)
l.insert(0,222)
print(l)
l.insert(0,111)
print(l)
l.insert(2,1.8)
print(l)

# %% pop komutu argüman almaz ise 
# en son elamanın döndürür ve 
# elemanı listeden siler


l=[1,2,3,4]
print(l)
print(l.pop())
print(l)
print(l.pop())
print(l)
# %% list comprehension 

sifirListesi=[0 for i in range(100)]

print(sifirListesi)
birdenYuze =[i for i in range(1,101)]
print(birdenYuze)
kareler=[i*i for i in range(1,9)]
print(kareler)

# %% yukarıdaki satırların aynısı
l=[]
for i in range(100):
    l.append(0)
l=[]
for i in range(1,101):
    l.append(i)
l=[]
for i in range(1,9):
    l.append(i*i)

#%%
# elimizde 100 elemanlı bir sayı listesi olsun 
# bu sayı listesindeki çift ve tek sayıları
# ayrı ayrı liselere aktaralım
import random

listem = [random.randint(1,1001) for i in range(100)]
print(listem)
ciftSayilar = [i for i in listem if i%2==0]
tekSayilar = [i for i in listem if i%2==1]
print("çift sayılar:\n",ciftSayilar)
print("tek sayılar:\n",tekSayilar)

# %% 
import random

listem = [random.randint(1,1001) for i in range(100)]
print(listem)

# listemdeki 500 den küçük sayıları başka bir listeye 
# ekleyin
kucuk500=[i for i in listem if i<500]
print("500den büyük sayılar\n",kucuk500)
# %% iki boyutlu liste oluşturma
import random
cbl1=[[t for t in range(3)]for i in range(4)]
print("cbl1\n",cbl1)
cbl2=[[-1 for t in range(3)]for i in range(4)]
print("cbl2\n",cbl2)
cbl3=[[random.randint(1,9) for t in range(3)]for i in range(4)]
print("cbl3\n",cbl3)
cbl4=[[3*i+1+t for t in range(3)]for i in range(3)]
print("cbl4\n",cbl4)

# %%

# %% fonksiyonlar

# bir iş yapanlar
print("merhaba")

# sonuç döndürenler
a=input("sayı gir:")
print(input("giriş:"))
# %% ilk fonsiyon

#fonksiyon 2 kısımdan oluşur.
# tanım(definition) 
# çağırma-gerçekleme(call-invoke)

def ilkFonksiyon():
    print("merhaba dünya")

ilkFonksiyon()

# %% argüman veya parametre

def selam_ver(isim):
    print("merhaba",isim)

selam_ver("hasan")
ad="pınar"
selam_ver(ad)

# %% birden fazla argüman kullanımı

def dortgen_alani(kk,uk):
    print("alan=",kk*uk)

dortgen_alani(20,30)
# %% örnek
# ad ve soyad argumanları
# alıp ekrana merhaba ad soyad
# merhaba hasan can

def selam_ver2(ad,soyad,yas):
    print("merhaba",ad,soyad,"yaş=",yas)

selam_ver2("hasan","can",13)

# bu argüman kullanımına konumsal yol 
# (positional way)
# %% anahtar kelime kullanımı (keywords way)
def selam_ver3(ad,soyad,yas):
    print("merhaba",ad,soyad,"yaş=",yas)

selam_ver3(yas=13,ad="hasan",soyad="can")

# %% karışık(mixing) paramtere kullanımı

def hesapla(a,b,c,d):
    sonuc = a+b*c/d
    print("sonuç=",sonuc,"|",a,b,c,d)

hesapla(1,2,10,2)#konuma bağlı
hesapla(a=10,d=8,b=20,c=3)#anahtar kelime yolu 
hesapla(1,5,d=3,c=10)#karışık kullanım
# karışık kullanımda
# ilk önce konuma bağlı argümanlar yazılır en son
# anahtar kelimeye bağlı argümanlar yazılır.
#hesapla(c=8,1,2,d=5)#hata
# hesapla(1,2,d=5,b=8) # hata
print("merhaba","nasılsın?",sep="½",end="@")
print()
print("merhaba","nasılsın?",end="½",sep="@")

# %% geriye değer döndürme return

def daire_alani(r):
    alan=3*r*r
    return alan#return 3*r*r

print("alan=",daire_alani(5))

# %% bir listeyi parametre olarak alıp liste
# elemanlarının toplamını bulsun ve 
# o sonucu gerei döndürsün
def liste_toplami(lst:list):
    t=0
    for eleman in lst:
        t+=eleman#t=t+eleman
    return t
    print("selam")

h=[1,2,30,52]
sonuc = liste_toplami(h)
print(sonuc)
# %% artık yıl mı?

# 00 ile biten yıllarda 400'e kalansız bölünenler
# bunun dışındaki yıllarda ise 4'e kalansız bölünenler
# artık yıldır
def artikYilMi(yil:int):#isLeapYear
    if yil%100==0 and yil%400==0:
        return True
    elif yil%4==0 and not(yil%100==0):
        return True
    else:
        return False

print(artikYilMi(2000))#True
print(artikYilMi(1700))#False
print(artikYilMi(2104))#True
print(artikYilMi(2001))#False
# %% asallık testi

# %% varsayılan değer deafault
# soldan sağa varsayılan değer ,
# verilen argümandan sonra her argümana 
# varsayılan değer verilmelidir.

def ucgenMi(a,b,c):
    # donus= a+b>c and a+c>b and b+c>a
    # return donus
    return a+b>c and a+c>b and b+c>a

print(ucgenMi(1,4,5))
print(ucgenMi(3,4,5))
print(ucgenMi(10,4,5))
print(ucgenMi(8,10,5))

# %% heron formülü

def ucgen_alaini(a,b,c):
    if ucgenMi(a,b,c):        
        s=(a+b+c)/2
        alan=(s*(s-a)*(s-b)*(s-c))**0.5
        return alan
    else:
        return "üçgen değil"
print(ucgen_alaini(8,10,5))
print(ucgen_alaini(1,4,5))
# %% fibonacci değerini hesaplasın
# formülsel yaklaşım
# iteratif yaklaşım

def fib(adim:int):
    if adim<=0:
        return None
    elif adim<3:
        return 1
    else:
        f1=f2=1
        for _ in range(3,adim+1):
            f1,f2=f2,f1+f2
        return f2
    
print(fib(1000))



# %% özyinelemeli (recursive-recursion)
def fibr(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fibr(n - 1) + fibr(n - 2)

print(fibr(34))
# %% gauss 1-n arası ardışık sayıların toplamı

def gauss1(sonSayi:int):
    toplam=(sonSayi*(sonSayi+1))/2
    return toplam
son=int(input("sayı gir:"))
print(gauss1(son))
print(gauss1(20))
print(gauss1(999999999))


# %% iteratif yol

def gauss2(sonSayi:int):
    toplam=0
    for i in range(1,sonSayi+1):
        toplam=toplam+i
    return toplam
son=int(input("sayı gir:"))
print(gauss2(son))
print(gauss2(200000))
print(gauss2(999999999))
# %%
for i in range(99999999):
    pass
print("çıktım")


# %% özyinelemeli(recusrive-recursion)

def fib1(adim):
    if adim<1:
        return None
    if adim<3:
        return 1 
    f1=1
    f2=1
    for _ in range(3,adim+1):
        f1,f2=f2,f1+f2
    
    return f2
print(fib1(5))
print(fib1(8))
print(fib1(50))
print(fib1(1000))



# %% özyinelemeli

def fib2(adim):
    if adim<1:
        return None
    if adim<3:
        return 1 
    
    return fib2(adim-1) + fib2(adim-2)

print(fib2(5))
print(fib2(8))
print(fib2(50))

# %%

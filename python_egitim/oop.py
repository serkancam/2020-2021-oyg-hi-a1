#%% ilk sınıf

#sınıf tanımı
class IlkSinif():
    pass

o1 = IlkSinif()# bu işlem sınıfın yapıcı methodunu çalıştırır.
o2 = IlkSinif()
# %%

class IlkSinif():
    def __init__(self,ad):
        self.isim=ad
        print("yapıcı çalıştı. merhaba",self.isim)

o1 = IlkSinif("kayra")# bu işlem sınıfın yapıcı methodunu çalıştırır.
o2 = IlkSinif("mert")
print(o1.isim)
# %% insan sınıfı
# boyu kilosu adı (özellikleri)
# yemek yesin ve kilo alsın
# spor yapsın kilo versin
# bki değerini hesaplasın

class Insan():
    def __init__(self,ad="-",kl=1.0,by=1.0):#yapıcı method(constructor)
        self.adi=ad
        self.kilo=kl
        self.boy=by
        
    def yemek_ye(self,miktar):
        self.kilo+=miktar#self.kilo=self.kilo++miktar
    def zayifla(self,k):
        self.kilo-=k
    
    def bki_hesapla(self):
        return self.kilo/(self.boy**2)

    # def __del__(self):
    #     print(self.adi,"silindi")


i1 = Insan()
print(i1.adi,i1.kilo,i1.boy)
i2 = Insan(ad="hasan")
print(i2.adi,i2.kilo,i2.boy)
i3 = Insan(ad="serkan",by=1.74,kl=79)
print(i3.adi,i3.kilo,i3.boy)
i3.adi="muhittin"
print(i3.adi)
i1.yemek_ye(3)
print(i1.kilo)
print(i3.bki_hesapla())
i3.zayifla(5)
print(i3.kilo)
print(i3.bki_hesapla())

# del i3
# %% veri gizleme/kapsülleme (encapsulation)
# public nesneden erişilebilir
# private sadece sınıf içinden erişilebilir.
class Hayvan:
    def __init__(self,r,kl,by):
        self.__kilo=kl#private
        self.__boy=by#private
        self.renk=r#public
    # get ve set methodları
    def setKilo(self,k):
        if k>0:
            self.__kilo=k        
    
    def getKilo(self):
        return self.__kilo
    def setBoy(self,b):
        if k>0:
            self.__boy=b        
    
    def getBoy(self):
        return self.__boy
  


h1=Hayvan("sarı",10,.2)#init methodu var yapıcı method
h2=Hayvan("kırmızı",10,.2)#init methodu var yapıcı method
h3=Hayvan("turuncu",10,.2)#init methodu var yapıcı method
print(h1.renk)
print(h2.getBoy())
print(h3.getKilo())

h1.setKilo(-5)
print(h1.getKilo())
# %% miras kavramı
# public olan özellik ve davranışlar miras verilir.
# private olanlar miras verilmez
class Hayvan:
    def __init__(self):
        print("hayvan yapıcı method")
        self.isim="Hayvan"
        self.__miras="miras alamazsın"
    def beslen(self):
        print(self.isim," besleniyor.")
    def hareket_et(self):
        print(self.isim," hareket ediyor.")
    def ses_cikar(self):
        print("Hayvan sınıfı ses çıkar mehodu")

class Kedi(Hayvan):
    def __init__(self,ad):
        # super().__init__()
        print("kedi yapıcım method")
        self.isim=ad
    def beslen(self):#method ezme yani ata sınftaki method ezilir.
        print("ben ata sınıftan geen methodu ezdim")
    def ses_cikar(self):
        print("miyav")

class Kopek(Hayvan):
    def __init__(self,ad):
        # super().__init__()
        print("Köpek yapıcım method")
        self.isim=ad
    def beslen(self):
        print("ben ata sınıftan geen methodu ezdim")
    def ses_cikar(self):
        print("hav hav")   
class Kus(Hayvan):
    pass
kd1 = Kedi("tekir")
kp1= Kopek("karabaş")
ks1 = Kus()

#çok biçimlilik
kd1.ses_cikar()
kp1.ses_cikar()

# %%
#soyutlama
l=[]
def ses_cikar(nesne):
    if  isinstance(nesne,Hayvan) :
        nesne.ses_cikar()

ses_cikar(kd1)
ses_cikar(kp1)
ses_cikar(ks1)
ses_cikar(l)

# %% # %%
# hayali araba

# arabanın özellikler
# marka, model yılı, renk, kaç km de
# arabanın davranışları
# git(km) bu değer sürekli kaçkm de değişkenine eklensin
#arabayı_boya(renk)
#model yılı private olsun 

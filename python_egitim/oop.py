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
# %%

def hizli_siralama(dizim):
    if len(dizim)<2:
        return dizim
    else:
        pivot = dizim[0]
        sol = [deger for deger in dizim[1:] if deger<=pivot]
        sag = [deger for deger in dizim[1:] if deger>pivot]
        return hizli_siralama(sol) + [pivot] + hizli_siralama(sag)

def en_kucuk_bul(dizim):
    enKucukDeger=dizim[0]
    enKucukYeri = 0
    for i in range(1,len(dizim)):
        if dizim[i]<enKucukDeger:
            enKucukDeger=dizim[i]
            enKucukYeri=i
    return enKucukYeri
  
def selection_sort(dizims):


    sirali_dizi=[]
    for i in range(len(dizims)):
        enKucukYeri = en_kucuk_bul(dizims)
        # sed = dizims.pop(enKucukYeri)
        # sirali_dizi.append(sed)
        sirali_dizi.append(dizims.pop(enKucukYeri))
    
    return sirali_dizi


import random
from datetime import  datetime

# simdi = datetime.now()
listem = [random.randint(1,1_000_000_000) for _ in range(2_000_000)]

hsl =listem.copy()
ssl = listem.copy()
# bitti = datetime.now()

# print(bitti-simdi)
# print("selection sort başla")
# ssBasla=datetime.now()
# ssSirali= selection_sort(ssl)
# ssBitis=datetime.now()
# print("selection sort süresi:\n",ssBitis-ssBasla)

print("python sortbaşla:")

psBasla=datetime.now()
listem.sort()
psBitis=datetime.now()
print("pyton liste sıralam:",psBitis-psBasla)

print("quick sort başla")
qsBasla=datetime.now()
qsSirali=hizli_siralama(hsl)
qsBitis=datetime.now()
print("Hızlı sıralama süresi:\n",qsBitis-qsBasla)


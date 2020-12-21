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

test=[16,8,25,30,12,26,7,45,9,10]
print("sırasız:\n",test)
sirali= selection_sort(test)
print("sıralı:\n",sirali)
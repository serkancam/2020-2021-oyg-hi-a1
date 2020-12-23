def hizli_siralama(dizim):
    if len(dizim)<2:
        return dizim
    else:
        pivot = dizim[0]
        sol = [deger for deger in dizim[1:] if deger<=pivot]
        sag = [deger for deger in dizim[1:] if deger>pivot]
        return hizli_siralama(sol) + [pivot] + hizli_siralama(sag)




test=[16,8,25,30,12,26,7,45,9,10]
print("sırasız:\n",test)
sirali= hizli_siralama(test)
print("sıralı:\n",sirali)
#%%
import pandas as pd
import numpy as np
from scipy import stats

veri=pd.read_csv("kalp_rahatsizligi.csv")

veri.head(3)
veri.tail(4)
#%%
veri.info()
veri.describe()


# %% serum kolestrol merkezi ölçütler

kolestrol_ortl = veri["serum_kolestrol"].mean()
kolestrol_ortn =veri.serum_kolestrol.median()
kolestrol_mod=stats.mode(veri["serum_kolestrol"])

print("serum kolestrol verisinin ortlaması=",kolestrol_ortl,"ortancası=",kolestrol_ortn,"ve en çok tekrar eden değeri=",kolestrol_mod[0])


# %% yaş verisi için
print("yaş ortalaması=",veri["yas"].mean())
print("yaş ortancası=",veri["yas"].median())


# %% dağılım ölçütleri
kolestrol_min=veri["serum_kolestrol"].min()
kolestrol_max=veri["serum_kolestrol"].max()
kolestrol_var=veri["serum_kolestrol"].var()
kolestrol_std=veri["serum_kolestrol"].std()

print("serum kolestrol aralığı:",kolestrol_max-kolestrol_min)
print("serumm kolsetrol varyansı:",kolestrol_var)
print("serumm kolsetrol standart sapması:",kolestrol_std)

# %% filtrleme
# sadece kadınların değerlerini
veri_kadin=veri[veri["cinsiyet"]=="kadin"]
veri_kadin

# %% filtreleme 
# 57 yaşından büyük erkeklerin verileri
veri_erkek=veri[(veri["cinsiyet"]=="erkek")&(veri["yas"]>57.0)]
veri_erkek

# %%

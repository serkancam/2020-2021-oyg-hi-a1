# %% kütüphaneler ve veri seti
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

veri = pd.read_csv("kalp_rahatsizligi.csv")
# print(veri.head(4))
veri.head(4)
# %%
veri.info()
# %% yaş histogramı
sns.histplot(data=veri, x="yas", bins=20)
plt.xlabel("yaş")
plt.ylabel("Adet")
plt.title("Yaş hverisi histogramı")
plt.xticks(np.arange(20, 90, step=10))
plt.show()

# %% yaş histogramı talasemiye göre
sns.histplot(data=veri, x="yas", hue="talasemi", element="step")
plt.xlabel("yaş")
plt.ylabel("Adet")
plt.title("Yaş verisi histogramı")
plt.show()

# %% yaş histogramını kalp rahatsızlığı sütununu ayırıcı olarak kullanıp grafik oluşturunuz.
sns.histplot(data=veri, x="yas", hue="kalp_rahatsizligi",
             element="step", palette="BuPu")
plt.xlabel("yaş")
plt.ylabel("Adet")
plt.title("Yaş verisi histogramı")
plt.show()
# %% saçılım grafiği:(scatterpolt)
# Saçılım diyagramı, iki farklı değişkenin arasındaki ilişkiyi belirlemek için kullanılır. Aralarındaki ilişkinin sebebi görülemese de, ilgili iki değişkenin arasında direkt olarak bir ilişki bulunup bulunmadığı ve bu ilişkinin ne derece güçlü olduğu görülebilir.
# %% kolestrol değeri ile en yüksek kalp hızı arasındaki saçılım grafiği
sns.scatterplot(data=veri, x="serum_kolestrol",
                y="en_yuksek_kalp_hizi", hue="cinsiyet")
plt.show()
# %% bu veriler arasındaki ilişkiyi göreceğiz
sns.regplot(data=veri, x="serum_kolestrol", y="en_yuksek_kalp_hizi")
plt.show()
# %%
sns.regplot(data=veri, x="yas", y="en_yuksek_kalp_hizi",)
plt.show()
# %% çizgi grafiği sayısal verilerin ilişkisini göstermek için veya genelde zamana bağlı depğişim için çizilir.
# yaş ve en yüksek kalp hızı ç.izgi grafiği

sns.lineplot(data=veri, x="yas", y="en_yuksek_kalp_hizi",
             hue="kalp_rahatsizligi")
plt.show()
# %% sütun/çubuk grafiği: kategorik verilerin görselleştirilmesinde sıklıkla kullanılır.

# cinsşyete göre kalp rahatsızlığın dağılımı
sns.countplot(data=veri, x="cinsiyet", hue="kalp_rahatsizligi")
plt.show()


# %% göğüs ağrısı tipinin kalp rahatsızlığına göre dağılımı
sns.countplot(data=veri, x="gogus_agrisi_tipi", hue="kalp_rahatsizligi")
plt.show()

# %%
sns.catplot(data=veri, x="gogus_agrisi_tipi",
            hue="kalp_rahatsizligi", col="aclik_kan_sekeri", kind="count")

plt.show()
# %%#Kutu grafiği(boxplot)
# sayısal verilerin temel istatistik bilgisini görselleştirmek için kullanılan grafik türüdür.
# serum_kolestrol verisinin kutu grafiği
sns.boxplot(data=veri, x="serum_kolestrol")
plt.show()
# %% en yüksek kalp hızı kutu grafiği
sns.boxplot(data=veri, y="en_yuksek_kalp_hizi")
plt.show()

# %%yas verisi
sns.boxplot(data=veri, y="yas")
plt.show()
# %% hareketsiz kan basını cinsiyete göre
sns.boxplot(data=veri, y="hareketsiz_kan_basinci", x="cinsiyet")
plt.show()

# %%
veri.describe()
# veri["serum_kolestrol"]
kolestrol_q1 = veri["serum_kolestrol"].describe()[4]
kolestrol_q3 = veri["serum_kolestrol"].describe()[6]
iqr_kolestrol = kolestrol_q3-kolestrol_q1
k_as = kolestrol_q1-1.5*iqr_kolestrol
k_us = kolestrol_q3+1.5*iqr_kolestrol
print(iqr_kolestrol)
print(f"kolestrol alt sınır={k_as}\nkolestrol üst sınır={k_us}")
# %% serum kolestrol için ayrık verileri ekrana yazdıralım
aykiri=veri[veri["serum_kolestrol"]>k_us]
aykiri=veri[veri["serum_kolestrol"]<k_as]
aykiri=veri[(veri["serum_kolestrol"]<k_as) | (veri["serum_kolestrol"]>k_us) ]
aykiri

# %% ısı grafiği(heatmap)
veri.corr()
sns.heatmap(data=veri.corr(),annot=True,linewidths=0.5,fmt="0.1f")

# %%

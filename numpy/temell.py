#%%
import numpy as np

listem = [1,2,3,[3,5]]

nd1 = np.array(listem)

print(nd1)
print(type(nd1))#ndarray  n dim , n değişken dimension
print(nd1.size)
print(nd1.shape)
print(np.__version__)

# %% boyut arttırark gidelim 0-d 

nd2 = np.array(2)
print(nd2.size)
print(nd2.shape)
print(nd2.dtype)



# %% 1-d 
nd3 = np.array([2,2])
print(nd3.size)
print(nd3.shape)
print(nd3.dtype)

# %% 2-d
l2 = [[32,12,3,8],[1,2,3,4]]
nd4 = np.array(l2)
print(nd4.size)
print(nd4.shape)
print(nd4.dtype)
print(nd4[0:,0:2])


# %% 3-d

image = np.random.randint(0,255,size=(300,300,3),dtype=np.uint8)
print(image.size)
print(image.shape)
print(image.dtype)

listem = [[[[1,2]]]]
nd5 =np.array(listem)
print(nd5.shape)


# %% deneme 

# %%

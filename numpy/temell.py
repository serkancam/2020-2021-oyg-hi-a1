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
import numpy as np
nd2 = np.array(2)
print(nd2.size)
print(nd2.shape)
print(nd2.dtype)
print(nd2.ndim)



# %% 1-d 
nd3 = np.array([2,2],dtype=np.float32)
print(nd3.size)
print(nd3.shape)
print(nd3.dtype)
print(nd3.ndim)

# %% 2-d
l2 = [[32,12,3,8],[1,2,3,4]]
nd4 = np.array(l2)
print(nd4.size)
print(nd4.shape)
print(nd4.dtype)
print(nd4[0:,0:2])


# %% 3-d
import cv2
import numpy as np
image = np.random.randint(0,255,size=(300,300),dtype=np.uint8)

image[0:101,:]=0
print(image.size)
print(image.shape)
print(image.ndim)
print(image.dtype)
cv2.imshow("test",image)
cv2.waitKey(0)
# listem = [[[[1,2]]]]
# nd5 =np.array(listem)
# print(nd5.shape)
# deepfake ses, görüntü ve beste konuşma.


# %% ndarray nup dizisi
import numpy as np
for i in range(0,34,3):
    print(i,end=" ")

print("")
nd0 = np.arange(0,34,3)
print(nd0)
print(nd0[1])
print(nd0[-3:])
print(nd0[3:])
print(nd0[3:-1])
print(nd0[3:-5])
print(nd0[::1])
print(nd0[::2])
print(nd0[::-1])
print(nd0.size)
nd0.shape=(2,6)
print(nd0)
nd0.shape=(3,2,2)
print(nd0)
print(nd0[0,0,1])
print(nd0[1,1,1])
# %% şekli düzgün olmak nedir
test =  np.array([[1,2,3],[5,6,7,8]])
print(test.size)
print(test.shape)
print(test.ndim)
print(test.dtype)
print(test[0,1])




# %% linspace/2-D slice

ndl0=np.linspace(1,20,20,dtype=np.uint8)#size=20
# print(ndl0)
ndl0.shape=(4,5)#nd10=np.reshape(ndl0,(4,5))
print(ndl0)
print(ndl0.ndim,"boyutlu")
print("\n",ndl0[0])#0. satır
print("\n",ndl0[0,:])#0. satır
print("\n",ndl0[1:3,:])#1. ve 2. satr
print("\n",ndl0[:,1])#1. sütun
print("\n",ndl0[:,3:])#son 2 sütun
print("\n",ndl0[:,-2:])#son 2 sütun
print("\n",ndl0[1:3,2:4])#8-9-13-14
# %%

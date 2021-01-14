
import zipfile
import io


data = zipfile.ZipFile('pandas-tigres.zip','r')
data.extractall()

#Hacer gráficas de pixeles

#Se instala cv2
#(C:\Users\Mozart\Anaconda3) C:\Users\Mozart>pip install opencv-python
#https://pypi.org/project/opencv-python/

import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

#ruta_tigres= "C:\Users\Mozart\Mozart\JupyterMoz\tigres"
ruta_tigres= "tigres"
tigres_training= []
#definir tamaño imagen
img_size=80

#trabajar sobre las imagenes de una carpeta
for img in os.listdir(ruta_tigres):
    #Se lee la imagen
    img= cv2.imread(os.path.join(ruta_tigres, img))
    img_gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img_gray_resize= cv2.resize(img_gray, (img_size, img_size))
    #img_gray_resize = cv2.re
    tigres_training.append([img_gray_resize])
    print(len(tigres_training))
    plt.figure()
    #plt.imshow(np.squeeze(img_gray_resize))
    plt.imshow(img_gray_resize)
    plt.colorbar()
    plt.grid(False)
    plt.show()

print(len(tigres_training))
print(type(tigres_training))
#print(tigres_training.shape)
print(tigres_training)

#Para ver una imagen
plt.figure()
plt.imshow(np.squeeze(tigres_training[2]))
#plt.imshow((tigres_training[2]))
plt.colorbar()
plt.grid(False)
plt.show()

#graficar imagenes pandas

ruta_pandas= "pandas"
pandas_training= []
#definir tamaño imagen
img_size=80

#trabajar sobre las imagenes de una carpeta
for img in os.listdir(ruta_pandas):
    #Se lee la imagen
    img= cv2.imread(os.path.join(ruta_pandas, img))
    img_gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img_gray_resizePandas= cv2.resize(img_gray, (img_size, img_size))
    #img_gray_resize = cv2.re
    pandas_training.append([img_gray_resizePandas])
    print(len(pandas_training))
    plt.figure()
    #plt.imshow(np.squeeze(img_gray_resize))
    plt.imshow(img_gray_resizePandas)
    plt.colorbar()
    plt.grid(False)
    #plt.show()

print(len(pandas_training))
print(type(pandas_training))
#print(tigres_training.shape)
print(pandas_training)

#Para ver una imagen
plt.figure()
plt.imshow(np.squeeze(pandas_training[2]))
#plt.imshow((tigres_training[2]))
plt.colorbar()
plt.grid(False)
plt.show()

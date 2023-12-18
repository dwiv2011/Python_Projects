import numpy as np
from PIL import Image

data =np.zeros((5,4,3),dtype=np.uint8)
print(data)

#data[row,column]
data[0:3,0:4]=[255,255,0]
img=Image.fromarray(data,'RGB')
img.save("canvas.png")
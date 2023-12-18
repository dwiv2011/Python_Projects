import numpy as np
from PIL import Image


class Canvas:
    def __init__(self,length, width,color):
        self.length=length
        self.width=width
        self.color=color
        self.data=np.zeros((self.length,self.width,3),dtype=np.uint8)
        self.data[:]=self.color

    def make(self):
        img=Image.fromarray(self.data,mode='RGB')
        img.save("can.png")

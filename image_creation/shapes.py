class Rectangle:

    def __init__(self,x_co, y_co,Rlength,Rwidth,color):
        self.Rlength=Rlength
        self.Rwidth=Rwidth
        self.color=color
        self.x_co=x_co
        self.y_co=y_co

    def draw(self,canvas):
        canvas.data[self.x_co:self.x_co+self.Rlength,self.y_co:self.y_co+self.Rwidth] =self.color


class Square:

    def __init__(self,x_co, y_co,side,color):
        self.side=side
        self.color=color
        self.x_co=x_co
        self.y_co=y_co

    def draw(self,canvas):
        canvas.data[self.x_co:self.x_co + self.side, self.y_co:self.y_co + self.side] = self.color

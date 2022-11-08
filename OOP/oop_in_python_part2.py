import math
class RectangularCoordinates:
    def __init__(self,x,y,a,b):
        self.x=x
        self.y=y
        self.a=a
        self.b=b
    def return_tuple(self):
        return (self.x,self.y)
    def is_it_ontheaxis(self):
        if self.x==0 or self.y==0:
            print ("It's on the axis")
        else:
            print("It's not on the axis")
            if (self.x>0 and self.y>0):
                print("but it's in Q1")
            elif (self.x>0 and self.y<0):
                print("but it's in Q2")
            elif (self.x<0 and self.y<0):
                print("but it's in Q3")
            else:
                print("but it's in Q4")
    def distance_from_axis(self):
        print("The x axis distance is: ",self.x)
        print("The y axis distance is: ",self.y)
    def distance_from_origin(self):
        return (self.x**2+self.y**2)**0.5
    def middle_point(self):
        return ((self.x+self.a)/2,(self.y+self.b))
    def distance_between_two_point(self):
        m=((self.a)-(self.x))**2
        n=((self.b)-(self.y))**2
        return ((m+n)**0.5)
    def deg_from_x_axis(self):
        return math.atan(abs(self.y)/abs(self.x))
setofpoint=RectangularCoordinates(1,2,3,4)
setofpoint.is_it_ontheaxis()

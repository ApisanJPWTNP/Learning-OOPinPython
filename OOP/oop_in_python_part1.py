# OOP Object-oriented programming (การเขียนโปรเเกรมเชิงวัตถุ)
# 1. อ่านง่าย ใช้ซํ้า
# 2. เอาไว้สําหรับข้อมูลที่มีคุณสมบัติเหมือนกัน (ยานพาหนะ)
# 3. ทําให้เข้าใจ python มากขึ้น

#intro
'''
# object of class
# 7 (class int),True (class bool),"Prayut" (class string)
# print(isinstance(7,int))#check ว่า 7 เป็น object ของ class int หรือไม่
# print(type(7))

# ways of naming things in programming
# snake_case -> do_math_homework
# camelCase -> doMathHomework
# PasCal -> DomathHomework

#Declarations
class Student:
    pass

vetit=Student
print(type(vetit))

#Property (คุณสมบัติ,ทรัพย์สิน)
class Student:
    age=16

vetit=Student
print(vetit.age)

class Student:
    age=16 #static property
    def multiply(): #static method
        return 2*2
vetit=Student
print(vetit.multiply())
'''
'''
#real 
class Student:
    def __init__(self,birth_year,height,weight):
        self.age=2022-birth_year
        self.height=height
        self.bmi=weight/(height/100)**2

vetit=Student(2000,175,70)
cesar=Student(2005,172,69)
print(cesar.age,cesar.bmi)
'''


class triangle:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def calculate_peri(self):
        return self.a+self.b+self.c
    def calculate_area(self):
        s=(self.a+self.b+self.c)/2
        return (s*(s-self.a)*(s-self.b)*(s-self.c))**0.5
    def is_it_right(self):
        num=[self.a,self.b,self.c]
        num=num.sort()
        if self.a**2+self.b**2==self.c**2:
            return True
        else:
            return False

my_triangle=triangle(3,4,5)
print(my_triangle.calculate_peri())
print(my_triangle.calculate_area())
print(my_triangle.is_it_right())

class car:
    def __init__(self,brand,model,year,max_speed):
        self.brand=brand
        self.model=model
        self.year=year
        self.max_speed=max_speed
    def info(self):
        return (self.brand,self.model,self.year,self.max_speed)
    def car_age(self):
        return 2022-self.year
    def get_mpersec_maxspeed(self):
        return self.max_speed*5/18
lambo=car("Lamborghini","Aventador",2000,250)
print(lambo.info())
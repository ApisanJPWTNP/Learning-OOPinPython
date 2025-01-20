class Person: #base class/parent class
    def __init__(self,name,surname,birth_year,height,weight):
        self.name = name
        self.age = surname
        self.age = 2022-birth_year
        self.height = height
        self.bmi = weight/(height/100)**2
    def greeting(self):
        print(self.name + " " + self.surname)

class Student(Person):#child class
    def __init__(self,name,surname,birth_year,height,weight,score):
        super().__init__(name,surname,birth_year,height,weight)
        self.score=score
    def is_pass_exam(self):
        if self.score >= 50:
            return True
        else:
            return False

cesar=Student("Apisan","Jongpermwattanapol",2005,172,68,100)
print(cesar.bmi)
print(cesar.is_pass_exam())

#multiply inherihance is also available 
# class E(a,b):
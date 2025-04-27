class Student:
    def __init__ (self, name, grade):
        self.__name = name
        self.grade = grade
        
    def print(self):
        return self.name + " " + self.grade
    
#tao doi tuong 
student1 = Student('Ha', '11')
print(student1.grade) 
class Student:
    def __init__(self,name:str,chinese:int,english:int,math:int):
        #實體的attribute
        self.name = name
        self.chinese = chinese
        self.english = english
        self.math = math 

    #實體方法method
    def total(self)->int:
        return self.chinese + self.english + self.math
    #property
    @property
    def average(self)->float:
        return self.total()/3.0
    
    def __repr__(self):
        return f'我是student的實體,我的name是:{self.name}'
import random  
def get_student(n:str)->Student:
    ch=random.randint(50,100)
    en=random.randint(50,100)
    ma=random.randint(50,100)
    return Student(name=n,chinese=ch,english=en,math=ma)
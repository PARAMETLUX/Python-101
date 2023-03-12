class factory:
    #Attribute
    factoryname = 'VICTUS'
    
    #Constructor
    def __init__(self, department='Python programming'):
        print('show this word when I build Instance')
        self.subject = department
    
    #Method
    def hello(self):
        print('Hello everybody')
        
    def Proof(self):
        print(f'Find and proof the problem when PD not production {self.subject}')
        
class Operator(factory):
    #Attribute
    def __init__(self, fullname, section, workday, subject):
        super().__init__(subject)
        self.fullname = fullname
        self.section = section
        self.workday = workday
        
    #Method
    def attandance(self):
        if self.subject >= 25:
            print(f'very good op {self.subject} A')
        elif self.workday >= 20:
            print(f'good op {self.subject} B')
        elif self.workday >= 15:
            print(f'very bad {self.subject} C')
        else:
            print(f'Warning {self.subject} come to HR')
    
#Instance
#factory1 = factory('ENGINEERING')
#print(f'Name of factory : {factory1.factoryname}')
#factory1.hello()
#factory1.Proof()
print('------------------------------------')
operator01 = Operator('PARAMET','Engineering', 25, 25)
print(f'Name of factory {operator01.factoryname}')
print(f'Name of operator {operator01.fullname}')
print(f'section is {operator01.section}')
print(f'working day is {operator01.workday}')
operator01.attandance()

print('------------------------------------')
operator02 = Operator('somchai','Engineering', 20, 20)
print(f'Name of factory {operator02.factoryname}')
print(f'Name of operator {operator02.fullname}')
print(f'section is {operator02.section}')
print(f'working day is {operator02.workday}')
operator02.attandance()

print('------------------------------------')
operator03 = Operator('mongkol','Engineering', 15, 15)
print(f'Name of factory {operator03.factoryname}')
print(f'Name of operator {operator03.fullname}')
print(f'section is {operator03.section}')
print(f'working day is {operator03.workday}')
operator03.attandance()
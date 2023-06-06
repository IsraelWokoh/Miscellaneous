class Parent():
    def __init__(s, dad, mum):
        s.dad = dad
        s.mum = mum
    
    def showMessage(s):
        print('Hello World')

    def getParents(s):
        return f'Parents are {s.dad} and {s.mum}'

class Child(Parent):
    def __init__(s, name, dad, mum, age):
        s.age = age
        s.name = name
        super().__init__(dad, mum)
        
    def showMessage2(s):
        return 'Hello Again'
    def getFamilyDetails(s):
        print(super().getParents())
        print(f'The child is called {s.name}')

child1 = Child('Karl', 'Clarke', 'Lois', 17)
child1.getParents()
child1.getFamilyDetails()


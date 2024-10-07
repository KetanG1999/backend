class Arithmatic:
    def __init__(self,value):
        self._value =value

    @property
    def value(self):
        print('To retrive the value\'_value\'')
        return self._value
    @value.setter
    def value(self,value):
        print('setting the value'+str(value))
        self._value = value
    @value.deleter
    def value(self):   
        print('delete the value')  

A1 = Arithmatic(12)
print(A1.value)

A1.value = 'ketan'
print(A1.value)
del A1.value
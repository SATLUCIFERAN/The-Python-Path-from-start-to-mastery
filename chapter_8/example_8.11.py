
class Meta(type):
    def __new__(cls, name, bases, dct):
        dct['created_by'] = 'Meta'
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=Meta):
    pass

print(MyClass.created_by)  

# Meta

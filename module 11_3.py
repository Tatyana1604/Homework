class Man:
    def __init__(self, name=None):
        if name:
            self.name = name
        else:
            self.name = 'Макс'

    def hello(self):
        print('Я здесь', self.name)

    def go(self, x=5, y=20):
        print('перемещение', x, y)


man = Man()


def some_function(param, param_2='n/a'):
    print('my params is', param, param_2)




def introspection(obj):
    objDict = {}
    objDict.setdefault('type', type(obj))
    attributes = dir(obj)
    obj_atr = []
    obj_met = []
    for method in attributes:
        if callable(getattr(obj, method)):
            obj_met.append(method)
        else:
            obj_atr.append(method)
    objDict.setdefault('attributes', obj_atr)
    objDict.setdefault('methods', obj_met)
    try:
        if obj.__module__:
            objDict.setdefault('module', obj.__module__)
        if obj.__name__:
            objDict.setdefault('name', obj.__name__)
    except AttributeError:
        return objDict
    return objDict


number_info = introspection(42)
print(number_info)

number_info = introspection('red')
print(number_info)
number_info = introspection(man)
print(number_info)


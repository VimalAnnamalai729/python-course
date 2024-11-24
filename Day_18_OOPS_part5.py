def add(*args):
    print('METHOD 1')
    print(sum(args))

# add(5, 5)
# add(5, 6, 7)


# access specifiers
name = 'vimal' # public
_name = 'vimal' # protected
__name =  'vimal' # private

# Bank scenario
__pin_number = '4567'


# Swiggy scenario

__card_details = '8929r2390899348'


def method_name():  # public
    pass

def _method_name(): # protected
    pass

def __method_name(): # private
    pass


class Bank:
    def __init__(self, name):
        self._server_ip = '10.0.1.1'
        self.name = name
        self.__password = '2346'

    def method1(self):
        print('public method')
        self.__method3()

    def _method2(self):
        print('protected method')

    def __method3(self):
        print('private method')


obj = Bank('vimal')
# print(obj._server_ip) # get
# obj._server_ip = '10.0.1.2'
# del obj._server_ip
print(obj.name)
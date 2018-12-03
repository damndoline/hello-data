class testclass:

    def __init__(self, x):
        self.x = x
        print('instantiated with ' + str(self.x))

    def say_hi(self):
        print('hi! new fucking PR')

    def get_x(self):
        return self.x


tmp = testclass(17)
tmp.say_hi()
print('x is ' + str(tmp.get_x()))
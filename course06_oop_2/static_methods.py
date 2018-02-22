class MathObject(object):
    value = 2

    def __init__(self, i):
        self.i = i

    @staticmethod
    def count():
        return 'some'

    # @staticmethod
    # def count_2(v):
    #     return 7 - 5 / 6 + v


t = MathObject(10)
print(MathObject.value)
print(MathObject.count())

print(t.count())
class Calculator:
    left = 2
    right = 1
    @classmethod
    def sum(cls):
         return cls.left + cls.right
    @classmethod
    def substract(cls):
        return cls.left - cls.right


print(Calculator.sum())
print(Calculator.substract())

# 여러개의 상태를 유지해야 하는 경우 생기는 문제들
# Calculator.left = 3
# Calculator.right = 2
# print(Calculator.sum())
# print(Calculator.substract())
# Calculator.left = 2
# Calculator.right = 1
# print(Calculator.sum())
# print(Calculator.substract())
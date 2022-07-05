class Calculator:
    left = 0
    right = 0
    def sum(self):
        return self.left + self.right
    def substract(self):
        return self.left - self.right

# c21, c32는 인스턴스 
# Calculator는 클래스
c21 = Calculator()
c21.left = 2
c21.right = 1

c32 = Calculator()
c32.left = 3
c32.right = 2

print('c21.sum()', c21.sum())
print('c32.sum()', c32.sum())

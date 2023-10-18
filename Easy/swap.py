class Swap(object):
    def solution1(self, x, y):
        print(f'from x = {x}, y = {y}', end=' ')
        x, y = y, x
        print(f'to x = {x}, y = {y}')
    
    def solution2(self, x, y):
        print(f'from x = {x}, y = {y}', end=' ')
        z = x
        x = y
        y = z
        print(f'to x = {x}, y = {y}')
        
    def solution3(self, x, y):
        print(f'from x = {x}, y = {y}', end=' ')
        x = x + y
        y = x - y
        x = x - y
        print(f'to x = {x}, y = {y}')
        
    def solution4(self, x, y):
        print(f'from x = {x}, y = {y}', end=' ')
        x = x * y 
        y = x / y
        x = x / y
        print(f'to x = {int(x)}, y = {int(y)}')
    
    def solution5(self, x, y):
        print(f'from x = {x}, y = {y}', end=' ')
        x = x ^ y
        y = x ^ y 
        x = x ^ y 
        print(f'to x = {x}, y = {y}')

Swap().solution1(3,4)
Swap().solution2(3,4)
Swap().solution3(3,4)
Swap().solution4(3,4)
Swap().solution5(3,4)
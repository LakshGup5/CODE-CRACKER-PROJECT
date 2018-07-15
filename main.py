import random   
import time 
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print('Welcome to Code Cracker')
lives = 126        
def even(num):
        if num % 2 == 0:
                return True
        else:
                return False
                
def countEven(password):
        isEven = 0
        for x in password:
                if even(int(x)):
                        isEven += 1
        return isEven
        
        
def Sum(password):
        _sum_ = 0
        for x in password:
                _sum_ += int(x)
        return _sum_
        
def product(password):
        producty = 1
        for x in password:
                producty *= int(x)
        return producty  
     
integer = random.randint(3, 5)
chars= "1234567890"
password = random.sample(chars, integer)
#function to calculate sum
lives = factorial(integer)
_sum_ = Sum(password)
print('loding...')
time.sleep(random.randint(0, 5))
password = ''.join(password)
print("CODE GENARATED")
print('It is', integer ,'numbers long.')
print('The sum is', _sum_, '.')
producty = product(password)
print('The product is', producty, '.')
isEven = countEven(password)
print('The number of even numbers is', isEven, '.')
print('The first number is', int(password[0], '.'))
print('The last number is', int(password[-1], '.'))
isOdd = integer - isEven
print('The number of odd numbers is', isOdd, '.')
print('The highest number is', str(max(password)), '.')
print('The lowest number is', str(min(password)), '.')
print('You have', lives, 'lives.')
while lives > 0:
        answer = input('What is your password?')
        if answer == password:
                        print('OMG, you got it ')
                        print('The password was', password, '.')
                        break
        if answer != password:
                lives -= 1
                print('You have', lives, 'lives.')
                print('BOO')
                if lives <= 1:
                        print ('GAME OVER!!!!!')
                        break

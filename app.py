A = int(input(">>> Value 'A'= "))
n = int(input(">>> Value 'n'= "))
x = pow(A,1/n)
iteration_count = 0
print('initial position = ', round(x,4))

while 1:
    x_1 = (1/n)*((n-1)*x+A/pow(x,n-1))
    
    if round(x,4) == round(x_1,4):
        iteration_count += 1
        break
   
    iteration_count += 1
    x = x_1

print('The', n, 'th root of', A, 'is', round(x_1,4),
'\niteration count =', iteration_count,)
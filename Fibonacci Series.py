a = 0
b = 1
n = int(input('Enter number of element in Fibonacci Series:  '))
print("Fibonacci Series : ", end =' ' )
print(a, b, end=' ')
i = 0
while(i<(n-2)) :
    c = a + b
    a, b = b, c
    print( c, end=' ')
    i += 1

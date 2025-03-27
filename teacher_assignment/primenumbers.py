def is_prime_number(n):
    if n<=1:
        return 'b'
    
    for i in range(2,n//2+1):
        if n%i == 0:
            return 'b'
    return 'a'
num1= int(input())
num2= int(input())
print("list of prime numbers")
for i in range(num1,num2+1):
    isPrime = is_prime_number(i)
    if isPrime=='a':
        print(f'{i} ')
is_prime_number(i)

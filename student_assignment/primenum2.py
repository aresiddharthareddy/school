def is_prime(num):
    if num<2:
        return False
    for i in range(2,num//2+1):
        if num%i==0:
            return False
    return True
num1=int(input("enter start number: "))
num2=int(input("enter end number: "))

def list_of_prime(num1,num2):
    print("list of prime numbers: ")
    for i in range(num1,num2+1):
        if is_prime(i):
            print(i, end=' ')
    print()
list_of_prime(num1,num2)


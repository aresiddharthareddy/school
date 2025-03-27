number = list(map(int,input().split(' ')))
max_number=int(input("Till: "))
def multiplication(max_number, number):
    for i in range(1,max_number+1):
        print(number,'*',i,'=',number*i)
for i in number:
    multiplication(max_number, i)
    print()
    print()


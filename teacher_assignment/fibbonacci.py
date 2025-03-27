max_num=int(input("How many numbers do you want for fibonacci: "))
def fib_sum(max_num):
    number_1=int(input("Enter a number: "))
    number_2= int(input("Enter another number: "))
    numbers=[number_1,number_2]
    for i in range(2,max_num):
        number_3= number_1+number_2
        number_1=number_2
        number_2=number_3
        numbers.append(number_3)
    print(numbers)
fib_sum(max_num)


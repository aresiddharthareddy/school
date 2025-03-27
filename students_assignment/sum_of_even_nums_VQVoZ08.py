numbers=list(map(int,input().split(',')))
def sum_of_even(numbers):
    sum=0
    for i in numbers:
        if i%2==0:
          print(i,'i')
          sum+=i
    return sum
summ=sum_of_even(numbers)
print(summ)
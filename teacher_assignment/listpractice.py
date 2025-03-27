inpuString=input()
inpuString = inpuString.replace("2","24")
list1 = list(inpuString.split(' '))
list2 = list(map(int,input().split(',')))

print(list2)

print(list1)
def generate_comma_separated_values(list1):
    string1 =""
    for i in list1:
        string1=string1 + i
        string1 = string1 + ","
    return string1[0:len(string1)-1]
a = generate_comma_separated_values(list1)
# a = a.replace('2','25')
print(a)
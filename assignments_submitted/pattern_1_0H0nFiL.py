number_of_rows_1 = int(input("Enter No.of Rows for pattern1: "))
number_of_rows_2 = int(input("Enter No.of Rows for pattern2: "))
number_of_rows_3 = int(input("Enter No.of Rows for pattern3: "))
number_of_rows_4 = int(input("Enter No.of Rows for pattern4: "))
number_of_rows_5 = int(input("Enter No.of Rows for pattern5: "))
def pattern1(number_of_rows):
    for i in range(1,number_of_rows+1):
        for j in range(number_of_rows):
            print("*", end="")
        print()
pattern1(number_of_rows_1)

def pattern2(number_of_rows):
    for i in range(1,number_of_rows+1):
        for j in range(i):
            print("*",end='')
        print()
pattern2(number_of_rows_2)

def pattern3(number_of_rows):
    for i in range(1, number_of_rows+1):
        for j in range(1, i+1):
            print(j, end='')
        print()
pattern3(number_of_rows_5)

def pattern4(number_of_rows):
    for i in range(1,number_of_rows+1):
        for j in range(1,i+2):
            print(i,end='')
        print()
pattern4(number_of_rows_4)

def pattern5(number_of_rows):
    for i in range(number_of_rows,0,-1):
        for j in range(i):
            print("*",end='')
        print()
pattern5(number_of_rows_3)
#!/usr/bin/python3


""" Function to get the Integer as the input from the User and find the factors of that number """


def fact_func():
    num = int(input("Enter integer:"))
    print(num)
    fact_list =[]
    
    for i in range(1,num+1):
        if num % i == 0:
            fact_list.append(i)
    return fact_list


""" Driver Function """


if __name__ == "__main__":
    pos = int(input("Enter position:"))
    print(pos)
    new_list = fact_func()
    enum_list = list(enumerate(new_list,start=1))
    #print(enum_list)
    for i,val in enum_list:
        if i == pos:
            print("The value is",val)
        else: 
            continue

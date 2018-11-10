def lcmOfTwoNos(a,b):
    '''
    This function finds the LCM of two numbers and returns the value of this LCM to the
    the calling section of the program
    
    '''
    num1_MultipleList = []
    num2_MultipleList = []
    commonMultipleList = []

    for i in range(1,b+1):
        num1_MultipleList.append(a*i)

    for j in range(1,a+1):
        num2_MultipleList.append(b*j)

    for num1Each in num1_MultipleList:
        for num2Each in num2_MultipleList:
            if num1Each == num2Each:
                commonMultipleList.append(num1Each)
    return commonMultipleList[0]


  # it takes finite number of numbers as input and returns the LCM of those numbers
print("For how many numbers you want to find the LCM: ")  # User prompt for number of numbers for which LCM need to be found                                                       
N = int(input())    
num_list = []
for count in range(0,N):
    print('Enter Number-{}: '.format(count+1))  # User-input for the numbers
    num_list.append(int(input()))

num_list.sort()  # Sorts the list of user input numbers into ascending order

for k in range(len(num_list)):  #Take 2 nos. starting from the list start to the end of list
    if k!=(len(num_list)-1):   # condition to check that the end of list is not reached
        Lowest_Common_Multiple = lcmOfTwoNos(num_list[k],num_list[k+1]) #uses function lcmOfTwoNos(a,b) to compute LCM of two numbers
    else:   # If it is last list element, it takes the last element and the first elment to find the LCM of those 2 numbers
        Lowest_Common_Multiple = lcmOfTwoNos(num_list[0],num_list[k])

print('The Lowest Common Multiple of the given numbers is : {}'.format(Lowest_Common_Multiple)) # The last value of the LCM is printed to the user











            





























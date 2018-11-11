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

# Below while loop iterates each time with two numbers each time and
# every next iteration it replaces one of the number with the lcm from the
# previous iteration

k=0
num2 = num_list[k+1]
while (k<N): 
    num1 = num_list[k]
    lcm_temp = lcmOfTwoNos(num1,num2)
    num2 = lcm_temp
    k += 1

print('The Lowest Common Multiple of the given numbers is : {}'.format(lcm_temp)) # The last value of the LCM is printed to the user











            





























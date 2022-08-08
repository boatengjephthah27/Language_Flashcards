


from audioop import reverse


def return_number(number):
    num = []
    nums = ' '
    [num.insert(0,values) for values in str(number)]
    for values in num:
        nums += values
    # number.reverse
    return nums
        
    

print(return_number(123456789))      

number = int(input("Enter the integer number: "))  
  
# Initiate value to null  
revs_number = 0  
  
# reverse the integer number using the while loop  
  
while (number > 0):  
    # Logic  
    remainder = number % 10  
    print(remainder)
    revs_number = (revs_number * 10) + remainder  
    print(revs_number)
    number = number // 10  
  
# Display the result  
# print("The reverse number is : {}".format(revs_number)) 
#Name:Aastha Giri
#Student ID:0957366
#Due Date: October 29th 2019
#MSITM 6341

#Problem of the day 1
 
number_list = [2,3,4,5,6,7,8,9,10,11,21,23,34,55,67,67,89]

current_largest = 0

for num in number_list:
    if num > current_largest:
        current_largest = num
print("The largest no. is: ", current_largest)


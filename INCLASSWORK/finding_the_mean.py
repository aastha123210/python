#find the mean of a list of numbers

#Mean = Sum of the total numbers divided by how many numbers there are

def mean(list_of_numbers):

    total = sum(list_of_numbers)
    count = len(list_of_numbers)
    return total / count

test_numbers = [5,32,8,19,24,42]

print(mean(test_numbers))

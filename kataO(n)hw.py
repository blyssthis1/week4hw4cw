#Question #1
# Given a month as an integer from 1 to 12, return to which quarter of the year it belongs as an integer number.

# For example: month 2 (February), is part of the first quarter; month 6 (June), is part of the second quarter; and month 11 (November), is part of the fourth quarter.

# Constraint:

1 <= month <= 12

#O(n) O(1)
def quarter_of(month):
    Q1 = 1
    Q2 = 2 
    if month <= 3:
        return 1
    elif month >3 and month <=6:
        return 2
    elif month >6 and month <= 9:
        return 3
    elif month >9 and month <= 12:
        return 4

print(quarter_of(7))



# What if we need the length of the words separated by a space to be added at the end of that same word and have it returned as an array?

# Example(Input --> Output)

# "apple ban" --> ["apple 5", "ban 3"]
# "you will win" -->["you 3", "will 4", "win 3"]
# Your task is to write a function that takes a String and returns an Array/list with the length of each word added to each element .

#O(2N) drop coefficient so its O(N) bc its looping.
def add_length(str_):
    #O(N)
    lst = str_.split()
    print(lst)
    #O(N)
    for i in range(len(lst)):
        lst[i] = lst[i] +" " + str(len(lst[i]))
    return lst


        
        
        
print(add_length("Hello win"))





#Complete the solution so that it reverses the string passed into it.

# 'world'  =>  'dlrow'
# 'word'   =>  'drow'

# Answer:
#O(N) bc touches every element.

def solution(string):
    return string[::-1]
    
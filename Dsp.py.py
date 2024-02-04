 # program to Add two number
num1=6
num2=3
sum=num1+num2
print(sum)

#  Maximum of two numberin python
num1=55
num2=10
print(max(num1,num2))

 # python program for factorial of a number
def factorial(n):
    res = 1
    for i in range(2, n+1):
        res *= i
    return res
num = 5
print("Factorial of", num, "is", factorial(num))

# python program for simple interest
def simple_interest (p,t,r):
    print('the principal is',p)
    print('the time period is',t)
    print('the rate of interest is',r)

    si = (p * t * r)/100

    print('The Simple Interest is', si)
    return si
simple_interest(8,6,8)

# python program for compound interest
def compound_interest (principal, rate, time):
    Amount = principal * (pow((1+rate/100),time))
    CI = Amount - principal
    print("Compound interest is", CI)
compound_interest(10000,10,25)

# python program to check Armstrong Number
def power(x,y):
    if y ==0:
        return 1
    if y % 2==0:
        return power(x,y //2) * power(x,y //2)
    return x * power(x,y //2) * power(x,y //2)
def order (x):
    n = 0
    while (x != 0):
        n=n+1
        x=x // 10

    return n

def isArmstrong(x):
    n=order(x)
    temp=x
    sum1=0

    while (temp != 0):
        r= temp %10
        sum1 = sum1+power(r,n)
        temp =temp // 10

    return(sum1==x)
x=153
print(isArmstrong(x))
x=1253
print(isArmstrong(x))       

#python program to find area of a circle
def findArea (r):
    PI = 3.142
    return PI * (r*r);
print("Area is %.6f" % findArea(5));

#python program to print all Prime number in an interval
def prime (x,y):
    prime_list = []
    for i in range(x,y):
        if i ==0 or i ==1:
            continue
        else:
            for j in range(2,int(i/2)+1):
                if i % j ==0:
                    break
            else:
                prime_list.append(i)
    return prime_list
x=2
y=7
i =prime(x,y)
if len(i) ==0:
    print("There are no prime numbers in this range")
else:
    print("The prime numbers in this range are: ",i)    

# Python program to check whether a number is Prime or not
num = 29

num = int( input("Enter a number: "))

flag = False

if num == 1:
    print(num, "is not a prime number")
elif num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break

    if flag:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")

#Python Program for n-th Fibonacci number
def fibonacci(n):
    if n <= 0:
        return "Invalid input. Please enter a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
n = int(input("Enter a positive integer (n): "))
result = fibonacci(n)
print(f"The {n}-th Fibonacci number is: {result}")

#Python Program for How to check if a given number is Fibonacci number?
import math

def is_perfect_square(num):
    sqrt_num = int(math.sqrt(num))
    return num == sqrt_num * sqrt_num

def is_fibonacci(num):
    if num < 0:
        return False
    return is_perfect_square(5 * num * num + 4) or is_perfect_square(5 * num * num - 4)

num = int(input("Enter a number to check if it's a Fibonacci number: "))
if is_fibonacci(num):
    print(f"{num} is a Fibonacci number.")
else:
    print(f"{num} is not a Fibonacci number.")


#    Python Program for n\’th multiple of a number in Fibonacci Series
def find_nth_multiple_of_number(n, number):
    if n <= 0:
        return "Invalid input. Please enter a positive integer for n."
    
    fib_sequence = [0, 1]
    count = 2

    while True:
        next_term = fib_sequence[-1] + fib_sequence[-2]
        if next_term % number == 0:
            count += 1
            if count == n:
                return next_term
        fib_sequence.append(next_term)
n = int(input("Enter a positive integer (n): "))
number = int(input("Enter the number to find its multiples in the Fibonacci series: "))

result = find_nth_multiple_of_number(n, number)
print(f"The {n}-th multiple of {number} in the Fibonacci series is: {result}")

#Program to print ASCII Value of a character
char = input("Enter a character: ")

ascii_value = ord(char)

print(f"The ASCII value of '{char}' is: {ascii_value}")


#Python Program for Sum of squares of first n natural numbers
def sum_of_squares(n):
    if n <= 0:
        return "Invalid input. Please enter a positive integer for n."
    
    return sum(i**2 for i in range(1, n+1))

n = int(input("Enter a positive integer (n): "))
result = sum_of_squares(n)
print(f"The sum of squares of the first {n} natural numbers is: {result}")


#Python Program for cube sum of first n natural numbers
def cube_sum(n):
    if n <= 0:
        return "Invalid input. Please enter a positive integer for n."
    
    return sum(i**3 for i in range(1, n+1))

n = int(input("Enter a positive integer (n): "))
result = cube_sum(n)
print(f"The cube sum of the first {n} natural numbers is: {result}")


#Python Program to find sum of array

def find_sum(arr):
    return sum(arr)

array = [1, 2, 3, 4, 5]
print("Sum of array:", find_sum(array))


#Python Program to find largest element in an array
def find_largest_element(arr):
    return max(arr)

array = [12, 45, 23, 78, 56]
print("Largest element:", find_largest_element(array))

#Python Program for array rotation
def rotate_array(arr, k):
    return arr[k:] + arr[:k]

# Example usage
array = [1, 2, 3, 4, 5]
rotation_amount = 2
print("Rotated array:", rotate_array(array, rotation_amount))


#Python Program for Reversal algorithm for array rotation
def reverse_array(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rotate_array_reversal(arr, k):
    n = len(arr)
    k = k % n
    reverse_array(arr, 0, n - 1)
    reverse_array(arr, 0, k - 1)
    reverse_array(arr, k, n - 1)

array = [1, 2, 3, 4, 5]
rotation_amount = 2
rotate_array_reversal(array, rotation_amount)
print("Rotated array:", array)

#Python Program to Split the array and add the first part to the end
def split_and_add(arr, k):
    return arr[k:] + arr[:k]

array = [1, 2, 3, 4, 5]
split_position = 2
print("Modified array:", split_and_add(array, split_position))

#Python Program for Find reminder of array multiplication divided by n
def array_remainder(arr, n):
    result = 1
    for num in arr:
        result = (result * num) % n
    return result

array = [2, 3, 4]
n = 5
print("Remainder of array multiplication divided by", n, "is:", array_remainder(array, n))


#Python Program to check if given array is Monotonic
def is_monotonic(arr):
    increasing = decreasing = True

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            decreasing = False
        elif arr[i] < arr[i - 1]:
            increasing = False

    return increasing or decreasing

array1 = [1, 2, 3, 4, 5]
array2 = [5, 4, 3, 2, 1]
array3 = [1, 2, 2, 3, 4]

print("Is array1 monotonic?", is_monotonic(array1))
print("Is array2 monotonic?", is_monotonic(array2))
print("Is array3 monotonic?", is_monotonic(array3))

#Python program to interchange first and last elements in a list
def interchange_first_last(lst):
    if len(lst) >= 2:
        lst[0], lst[-1] = lst[-1], lst[0]
    return lst

original_list = [1, 2, 3, 4, 5]
interchanged_list = interchange_first_last(original_list)

print("Original List:", original_list)
print("Interchanged List:", interchanged_list)


#Python program to swap two elements in a list
def swapPositions(list, pos1, pos2):
     
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list
 
List = [23, 65, 19, 90]
pos1, pos2  = 1, 3
 
print(swapPositions(List, pos1-1, pos2-1))


#Python | Ways to find length of list
li = [10, 20, 30]
n = len(li)
print("The length of list is: ", n)

#Python | Ways to check if element exists in list
lst=[ 1, 6, 3, 5, 3, 4 ] 
i=7
if i in lst: 
    print("exist") 
else: 
    print("not exist")

#Different ways to clear a list in Python
my_list = [1, 2, 3, 4, 5]
my_list.clear()
print("Cleared list using clear():", my_list)

my_list = [1, 2, 3, 4, 5]
my_list = []
print("Cleared list by assigning an empty list:", my_list)

#Python | Reversing a List
def reverse_list(lst):
    return lst[::-1]

original_list = [1, 2, 3, 4, 5]
reversed_list = reverse_list(original_list)
print("Original List:", original_list)
print("Reversed List:", reversed_list)

#Python program to find sum of elements in list
def sum_of_elements(lst):
    return sum(lst)

my_list = [1, 2, 3, 4, 5]
print("Sum of elements in the list:", sum_of_elements(my_list))

#Python | Multiply all numbers in the list
def multiply_elements(lst):
    result = 1
    for num in lst:
        result *= num
    return result

my_list = [1, 2, 3, 4, 5]
print("Product of elements in the list:", multiply_elements(my_list))

#Python program to find smallest number in a list
def find_smallest(lst):
    return min(lst)

my_list = [5, 2, 8, 1, 3]
print("Smallest number in the list:", find_smallest(my_list))

#Python program to find largest number in a list
def find_largest(lst):
    return max(lst)

my_list = [5, 2, 8, 1, 3]
print("Largest number in the list:", find_largest(my_list))

#Python program to find second largest number in a list
def find_second_largest(lst):
    unique_sorted = sorted(set(lst), reverse=True)
    if len(unique_sorted) > 1:
        return unique_sorted[1]
    else:
        return "List doesn't have a second largest element."

my_list = [5, 2, 8, 1, 3]
print("Second largest number in the list:", find_second_largest(my_list))

#Python program to find N largest elements from a list
def find_n_largest(lst, n):
    sorted_list = sorted(lst, reverse=True)
    return sorted_list[:n]

my_list = [5, 2, 8, 1, 3, 9, 7]
n_largest = 3
print(f"{n_largest} largest elements in the list:", find_n_largest(my_list, n_largest))

#Python program to print even numbers in a list
def print_even_numbers(lst):
    even_numbers = [num for num in lst if num % 2 == 0]
    return even_numbers

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Even numbers in the list:", print_even_numbers(my_list))

#Python program to print odd numbers in a List
def print_odd_numbers(lst):
    odd_numbers = [num for num in lst if num % 2 != 0]
    return odd_numbers

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Odd numbers in the list:", print_odd_numbers(my_list))

#Python program to print all even numbers in a range
def print_even_numbers_in_range(start, end):
    even_numbers = [num for num in range(start, end + 1) if num % 2 == 0]
    return even_numbers

start_range = 1
end_range = 10
print(f"All even numbers in the range ({start_range}, {end_range}):", print_even_numbers_in_range(start_range, end_range))

#Python program to print all odd numbers in a range
def print_odd_numbers_in_range(start, end):
    odd_numbers = [num for num in range(start, end + 1) if num % 2 != 0]
    return odd_numbers

start_range = 1
end_range = 10
print(f"All odd numbers in the range ({start_range}, {end_range}):", print_odd_numbers_in_range(start_range, end_range))

#Python program to print positive numbers in a list
def print_positive_numbers(lst):
    positive_numbers = [num for num in lst if num > 0]
    return positive_numbers

my_list = [-1, 2, -3, 4, -5, 6]
print("Positive numbers in the list:", print_positive_numbers(my_list))

#Python program to print negative numbers in a list
def print_negative_numbers(lst):
    negative_numbers = [num for num in lst if num < 0]
    return negative_numbers

my_list = [-1, 2, -3, 4, -5, 6]
print("Negative numbers in the list:", print_negative_numbers(my_list))

#Python program to print all positive numbers in a range
def print_positive_numbers_in_range(start, end):
    positive_numbers = [num for num in range(start, end + 1) if num > 0]
    return positive_numbers
start_range = -5
end_range = 5
print(f"All positive numbers in the range ({start_range}, {end_range}):", print_positive_numbers_in_range(start_range, end_range))

#Python program to print all negative numbers in a range
def print_negative_numbers_in_range(start, end):
    negative_numbers = [num for num in range(start, end + 1) if num < 0]
    return negative_numbers
start_range = -5
end_range = 5
print(f"All negative numbers in the range ({start_range}, {end_range}):", print_negative_numbers_in_range(start_range, end_range))

#Remove multiple elements from a list in Python
def remove_elements(lst, elements_to_remove):
    return [elem for elem in lst if elem not in elements_to_remove]

original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
elements_to_remove = [2, 4, 6]

new_list = remove_elements(original_list, elements_to_remove)
print("Original List:", original_list)
print("List after removing elements:", new_list)

#Python – Remove empty List from List
def remove_empty_lists(lst):
    return [sublist for sublist in lst if sublist]

original_list = [1, [], 3, [], 5, 6, [], 8]
new_list = remove_empty_lists(original_list)
print("Original List:", original_list)
print("List after removing empty lists:", new_list)

#Python | Cloning or Copying a list
original_list = [1, 2, 3, 4, 5]
cloned_list = original_list[:]

original_list = [1, 2, 3, 4, 5]
cloned_list = list(original_list)

print("Original List:", original_list)
print("Cloned List:", cloned_list)

#Python | Count occurrences of an element in a list
def count_occurrences(lst, element):
    return lst.count(element)

my_list = [1, 2, 3, 4, 2, 5, 2]
element_to_count = 2
print(f"Occurrences of {element_to_count} in the list:", count_occurrences(my_list, element_to_count))

#Python | Remove empty tuples from a list
def remove_empty_tuples(lst):
    return [item for item in lst if item]

original_list = [(1, 2), (), (3, 4), (), (5, 6)]
new_list = remove_empty_tuples(original_list)
print("Original List:", original_list)
print("List after removing empty tuples:", new_list)

#Python | Program to print duplicates from a list of integers
def find_duplicates(lst):
    seen = set()
    duplicates = set()
    for num in lst:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)

my_list = [1, 2, 3, 2, 4, 5, 1, 6]
print("Duplicates in the list:", find_duplicates(my_list))

#Python program to find Cumulative sum of a list
def cumulative_sum(lst):
    cum_sum = [sum(lst[:i + 1]) for i in range(len(lst))]
    return cum_sum

my_list = [1, 2, 3, 4, 5]
print("Cumulative sum of the list:", cumulative_sum(my_list))

#Python | Sum of number digits in List
def sum_of_digits_in_list(lst):
    total_sum = 0
    for num in lst:
        # Convert the number to a string to iterate through its digits
        num_str = str(num)
        # Sum the digits of the number
        digit_sum = sum(int(digit) for digit in num_str)
        total_sum += digit_sum
    return total_sum

my_list = [123, 45, 678, 9]
print("Sum of digits in the list:", sum_of_digits_in_list(my_list))

#Break a list into chunks of size N in Python
def chunk_list(lst, chunk_size):
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
chunk_size = 3
print(f"List after breaking into chunks of size {chunk_size}:", chunk_list(my_list, chunk_size))

#Python | Sort the values of first list using second list
def sort_list_using_another(list1, list2):
    zipped_lists = zip(list2, list1)
    sorted_lists = sorted(zipped_lists)
    sorted_list1 = [element[1] for element in sorted_lists]
    return sorted_list1

list1 = ['apple', 'banana', 'orange']
list2 = [3, 1, 2]
print("List1 sorted using List2:", sort_list_using_another(list1, list2))


#Matrix Programs:

#Python program to add two Matrices
def add_matrices(mat1, mat2):
    result = [[mat1[i][j] + mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))]
    return result

matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
result_matrix = add_matrices(matrix1, matrix2)
print("Matrix 1:")
print(matrix1)
print("Matrix 2:")
print(matrix2)
print("Sum of Matrices:")
print(result_matrix)

#Python program to multiply two matrices
def multiply_matrices(mat1, mat2):
    result = [[sum(mat1[i][k] * mat2[k][j] for k in range(len(mat2))) for j in range(len(mat2[0]))] for i in range(len(mat1))]
    return result

matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
result_matrix = multiply_matrices(matrix1, matrix2)
print("Matrix 1:")
print(matrix1)
print("Matrix 2:")
print(matrix2)
print("Product of Matrices:")
print(result_matrix)

#Python program for Matrix Product
def matrix_product(mat1, mat2):
    result = [[sum(mat1[i][k] * mat2[k][j] for k in range(len(mat2))) for j in range(len(mat2[0]))] for i in range(len(mat1))]
    return result

matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
result_matrix = matrix_product(matrix1, matrix2)

print("Matrix 1:")
for row in matrix1:
    print(row)

print("\nMatrix 2:")
for row in matrix2:
    print(row)

print("\nMatrix Product:")
for row in result_matrix:
    print(row)

#Adding and Subtracting Matrices in Python
def add_matrices(mat1, mat2):
    result = [[mat1[i][j] + mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))]
    return result

def subtract_matrices(mat1, mat2):
    result = [[mat1[i][j] - mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))]
    return result

matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

# Addition
sum_matrix = add_matrices(matrix1, matrix2)
print("Matrix 1:")
for row in matrix1:
    print(row)

print("\nMatrix 2:")
for row in matrix2:
    print(row)

print("\nMatrix Sum:")
for row in sum_matrix:
    print(row)

# Subtraction
difference_matrix = subtract_matrices(matrix1, matrix2)
print("\nMatrix Difference:")
for row in difference_matrix:
    print(row)

#Transpose a matrix in Single line in Python
def transpose_matrix(mat):
    return [list(row) for row in zip(*mat)]

original_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed_matrix = transpose_matrix(original_matrix)

print("Original Matrix:")
for row in original_matrix:
    print(row)

print("\nTransposed Matrix:")
for row in transposed_matrix:
    print(row)

#Python | Matrix creation of n*n
def create_matrix(n):
    return [[0 for _ in range(n)] for _ in range(n)]

n = 3
new_matrix = create_matrix(n)
print(f"Matrix of size {n}*{n} created:")
print(new_matrix)

#Python | Get Kth Column of Matrix
def get_kth_column(mat, k):
    return [row[k] for row in mat]

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
k = 1
column_k = get_kth_column(matrix, k)
print(f"{k}th Column of Matrix:")
print(column_k)

#Python – Vertical Concatenation in Matrix
def vertical_concatenation(mat1, mat2):
    return mat1 + mat2

matrix1 = [[1, 2, 3], [4, 5, 6]]
matrix2 = [[7, 8, 9], [10, 11, 12]]
result_matrix = vertical_concatenation(matrix1, matrix2)
print("Matrix 1:")
print(matrix1)
print("Matrix 2:")
print(matrix2)
print("Vertical Concatenation:")
print(result_matrix)

#String Programs:
#Python program to check if a string is palindrome or not
def is_palindrome(string):
    return string == string[::-1]

my_string = "radar"
if is_palindrome(my_string):
    print(f"{my_string} is a palindrome.")
else:
    print(f"{my_string} is not a palindrome.")

#Python program to check whether the string is Symmetrical or Palindrome
def is_symmetrical(string):
    return string == string[::-1]

my_string = "madam"
if is_symmetrical(my_string):
    print(f"{my_string} is both symmetrical and a palindrome.")
else:
    print(f"{my_string} is not symmetrical or a palindrome.")

#Reverse words in a given String in Python
def reverse_words(string):
    words = string.split()
    reversed_words = ' '.join(reversed(words))
    return reversed_words

my_string = "Hello World"
reversed_string = reverse_words(my_string)
print("Original String:", my_string)
print("Reversed Words:", reversed_string)

#Ways to remove i’th character from string in Python
def remove_ith_character(string, i):
    return string[:i] + string[i+1:]

my_string = "david"
i_to_remove = 3
modified_string = remove_ith_character(my_string, i_to_remove)
print("Original String:", my_string)
print(f"String after removing {i_to_remove}th character:", modified_string)

#Python | Check if a Substring is Present in a Given String
def is_substring_present(string, substring):
    return substring in string

main_string = "Python is awesome"
substring_to_check = "is"
if is_substring_present(main_string, substring_to_check):
    print(f"{substring_to_check} is present in the string.")
else:
    print(f"{substring_to_check} is not present in the string.")

#Python – Words Frequency in String Shorthands
from collections import Counter

def words_frequency(string):
    return Counter(string.split())

my_string = "Python is Pythonic and awesome. Python programming is fun."
frequency_dict = words_frequency(my_string)
print("Word Frequency in the String:")
print(frequency_dict)

#Python – Convert Snake case to Pascal case
def snake_to_pascal(string):
    words = string.split('_')
    pascal_case = ''.join(word.capitalize() for word in words)
    return pascal_case

snake_case_string = "this is my python program"
pascal_case_string = snake_to_pascal(snake_case_string)
print("Snake Case:", snake_case_string)
print("Pascal Case:", pascal_case_string)

#Find length of a string in python (4 ways)
# Method 1: Using len() function
my_string = "Hello World"
length_method1 = len(my_string)

# Method 2: Using loop
length_method2 = 0
for char in my_string:
    length_method2 += 1

# Method 3: Using list comprehension
length_method3 = sum(1 for char in my_string)

# Method 4: Using while loop
length_method4 = 0
iterator = iter(my_string)
while True:
    try:
        next(iterator)
        length_method4 += 1
    except StopIteration:
        break

print("Length using len():", length_method1)
print("Length using loop:", length_method2)
print("Length using list comprehension:", length_method3)
print("Length using while loop:", length_method4)

#Python program to print even length words in a string
def even_length_words(string):
    words = string.split()
    even_length_words_list = [word for word in words if len(word) % 2 == 0]
    return even_length_words_list

my_string = "Python is a powerful programming language"
even_length_words_list = even_length_words(my_string)
print("Original String:", my_string)
print("Even Length Words:", even_length_words_list)

#	Python program to accept the strings which contains all vowels
def contains_all_vowels(string):
    vowels = set("aeiou")
    return set(string.lower()) >= vowels

my_string = "AEIOU are vowels"
if contains_all_vowels(my_string):
    print(f"{my_string} contains all vowels.")
else:
    print(f"{my_string} does not contain all vowels.")

#Python | Count the Number of matching characters in a pair of string
def count_matching_characters(str1, str2):
    return sum(ch1 == ch2 for ch1, ch2 in zip(str1, str2))

string1 = "hello"
string2 = "hola"
matching_count = count_matching_characters(string1, string2)
print(f"Number of matching characters between '{string1}' and '{string2}': {matching_count}")

# Remove all duplicates from a given string in Python
def remove_duplicates(string):
    return ''.join(sorted(set(string), key=string.index))

my_string = "programming"
without_duplicates = remove_duplicates(my_string)
print("Original String:", my_string)
print("String without duplicates:", without_duplicates)

# 	Python – Least Frequent Character in String
from collections import Counter

def least_frequent_character(string):
    char_count = Counter(string)
    least_frequent = min(char_count, key=char_count.get)
    return least_frequent

my_string = "programming"
least_freq_char = least_frequent_character(my_string)
print("Original String:", my_string)
print("Least Frequent Character:", least_freq_char)

#     Python | Maximum frequency character in String
from collections import Counter

def max_frequency_character(string):
    char_count = Counter(string)
    max_frequency_char = max(char_count, key=char_count.get)
    return max_frequency_char

my_string = "programming"
max_freq_char = max_frequency_character(my_string)
print("Original String:", my_string)
print("Maximum Frequency Character:", max_freq_char)

# 	Python | Program to check if a string contains any special character
def contains_special_character(string):
    special_characters = set("!@#$%^&*()-_+=[]{}|;:'\",.<>?/")
    return any(char in special_characters for char in string)

my_string = "Hello! How are you?"
if contains_special_character(my_string):
    print(f"{my_string} contains special characters.")
else:
    print(f"{my_string} does not contain any special characters.")

# 	Generating random strings until a given string is generated
import random
import string

def generate_random_string(length):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def generate_until_match(target_string):
    generated_string = ""
    while generated_string != target_string:
        generated_string = generate_random_string(len(target_string))
    return generated_string

target_string = "hello"
random_string = generate_until_match(target_string)
print(f"Random string matching '{target_string}': {random_string}")

# 	Find words which are greater than given length k
def words_greater_than_length(string, k):
    words = string.split()
    return [word for word in words if len(word) > k]

my_string = "Python program for finding words greater than length k"
k_value = 4
long_words = words_greater_than_length(my_string, k_value)
print(f"Words greater than length {k_value}:", long_words)

# 	Python program for removing i-th character from a string
def remove_ith_character(string, i):
    return string[:i] + string[i+1:]

my_string = "example"
i_to_remove = 3
modified_string = remove_ith_character(my_string, i_to_remove)
print("Original String:", my_string)
print(f"String after removing {i_to_remove}th character:", modified_string)

# 	Python program to split and join a string
def split_and_join(string):
    words = string.split()
    joined_string = '-'.join(words)
    return joined_string

my_string = "Split and Join"
modified_string = split_and_join(my_string)
print("Original String:", my_string)
print("Modified String:", modified_string)

# 	Python | Check if a given string is binary string or not
def is_binary_string(string):
    return all(char in '01' for char in string)

binary_string = "101010"
if is_binary_string(binary_string):
    print(f"{binary_string} is a binary string.")
else:
    print(f"{binary_string} is not a binary string.")

# Python program to find uncommon words from two Strings
def uncommon_words(str1, str2):
    set1 = set(str1.split())
    set2 = set(str2.split())
    uncommon = set1.symmetric_difference(set2)
    return list(uncommon)

string1 = "Python is great"
string2 = "Java is also great"
uncommon_words_list = uncommon_words(string1, string2)
print("Uncommon Words:", uncommon_words_list)

# Python – Replace duplicate Occurrence in String
def replace_duplicate_occurrence(string):
    seen = set()
    result = []
    for char in string:
        if char in seen:
            result.append('$')
        else:
            result.append(char)
            seen.add(char)
    return ''.join(result)

my_string = "programming"
modified_string = replace_duplicate_occurrence(my_string)
print("Original String:", my_string)
print("String with duplicate occurrences replaced:", modified_string)

# Python – Replace multiple words with K
def replace_multiple_words(string, words_to_replace, k):
    for word in words_to_replace:
        string = string.replace(word, k)
    return string

my_string = "Replace apple with orange and banana with mango"
words_to_replace = ["apple", "banana"]
replacement_word = "fruit"
modified_string = replace_multiple_words(my_string, words_to_replace, replacement_word)
print("Original String:", my_string)
print("Modified String:", modified_string)

# Python | Permutation of a given string using inbuilt function
from itertools import permutations

def string_permutations(string):
    perms = [''.join(p) for p in permutations(string)]
    return perms

my_string = "abc"
permutations_list = string_permutations(my_string)
print("Original String:", my_string)
print("Permutations:", permutations_list)

# Python | Check for URL in a String
import re

def contains_url(string):
    url_pattern = re.compile(r'https?://\S+')
    return bool(url_pattern.search(string))

my_string = "Visit https://www.example.com for more information."
if contains_url(my_string):
    print(f"{my_string} contains a URL.")
else:
    print(f"{my_string} does not contain a URL.")

# Execute a String of Code in Python
def execute_code(code_string):
    exec(code_string)

code_to_execute = 'print("Hello, World!")'
execute_code(code_to_execute)

# String slicing in Python to rotate a string
def rotate_string(string, k):
    rotated_string = string[k:] + string[:k]
    return rotated_string

my_string = "abcdef"
rotation_count = 2
rotated_string = rotate_string(my_string, rotation_count)
print("Original String:", my_string)
print(f"String rotated by {rotation_count} positions:", rotated_string)

# String slicing in Python to check if a string can become empty by recursive deletion
def is_empty_by_recursive_deletion(string):
    while '()' in string or '[]' in string or '{}' in string:
        string = string.replace('()', '').replace('[]', '').replace('{}', '')
    return not string

my_string = "{[()]}[{}]"
if is_empty_by_recursive_deletion(my_string):
    print(f"{my_string} can become empty by recursive deletion.")
else:
    print(f"{my_string} cannot become empty by recursive deletion.")

# Python Counter| Find all duplicate characters in string
from collections import Counter

def duplicate_characters(string):
    char_count = Counter(string)
    duplicates = [char for char, count in char_count.items() if count > 1]
    return duplicates

my_string = "programming"
duplicates_list = duplicate_characters(my_string)
print("Original String:", my_string)
print("Duplicate Characters:", duplicates_list)

# Python – Replace all occurrences of a substring in a string
def replace_all_occurrences(string, old_substring, new_substring):
    return string.replace(old_substring, new_substring)

my_string = "Replace all occurrences of 'apple' with 'orange' and 'banana' with 'mango'"
old_substring = "apple"
new_substring = "orange"
modified_string = replace_all_occurrences(my_string, old_substring, new_substring)
print("Original String:", my_string)
print("Modified String:", modified_string)

#Dictionary Programs:
# Python – Extract Unique values dictionary values
def extract_unique_values(dictionary):
    unique_values = set(value for values_list in dictionary.values() for value in values_list)
    return list(unique_values)

my_dict = {'a': [1, 2, 3], 'b': [2, 3, 4], 'c': [3, 4, 5]}
unique_values_list = extract_unique_values(my_dict)
print("Original Dictionary:")
print(my_dict)
print("Unique Values List:")
print(unique_values_list)

# Python program to find the sum of all items in a dictionary
def sum_of_items(dictionary):
    return sum(value for values_list in dictionary.values() for value in values_list)

my_dict = {'a': [1, 2, 3], 'b': [2, 3, 4], 'c': [3, 4, 5]}
total_sum = sum_of_items(my_dict)
print("Original Dictionary:")
print(my_dict)
print("Sum of all items:", total_sum)

# Python | Ways to remove a key from dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
key_to_remove = 'b'
del my_dict[key_to_remove]
print("Dictionary after removing key using del:", my_dict)

my_dict = {'a': 1, 'b': 2, 'c': 3}
key_to_remove = 'b'
my_dict.pop(key_to_remove, None)
print("Dictionary after removing key using pop():", my_dict)

# Ways to sort list of dictionaries by values in Python – Using itemgetter
from operator import itemgetter

list_of_dicts = [{'name': 'David', 'age': 25}, {'name': 'Roshinta', 'age':20}, {'name': 'Mini', 'age': 20}]
sorted_list = sorted(list_of_dicts, key=itemgetter('age'))
print("Original List of Dictionaries:")
print(list_of_dicts)
print("Sorted List of Dictionaries by age:")
print(sorted_list)

# Ways to sort list of dictionaries by values in Python – Using lambda function
list_of_dicts = [{'name': 'David', 'age': 25}, {'name': 'Minku', 'age': 20}, {'name': 'Mini', 'age': 20}]
sorted_list = sorted(list_of_dicts, key=lambda x: x['age'])
print("Original List of Dictionaries:")
print(list_of_dicts)
print("Sorted List of Dictionaries by age:")
print(sorted_list)

# Python | Merging two Dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged_dict = {**dict1, **dict2}
print("Dictionary 1:", dict1)
print("Dictionary 2:", dict2)
print("Merged Dictionary:", merged_dict)

# Python – Convert key-values list to flat dictionary
key_values_list = [('a', 1), ('b', 2), ('c', 3)]
flat_dict = dict(key_values_list)
print("Key-Values List:")
print(key_values_list)
print("Flat Dictionary:")
print(flat_dict)

# Python – Insertion at the beginning in OrderedDict
from collections import OrderedDict

ordered_dict = OrderedDict([('a', 1), ('b', 2)])
ordered_dict.update({'c': 3})
ordered_dict.move_to_end('c', last=False)
print("Original OrderedDict:")
print(ordered_dict)

# Python | Check order of character in string using OrderedDict( )
from collections import OrderedDict

def check_order(string, pattern):
    pattern_dict = OrderedDict.fromkeys(pattern)
    pattern_length = len(pattern)
    current_index = 0

    for char in string:
        if char == pattern[current_index]:
            current_index += 1
            if current_index == pattern_length:
                return True

    return False

my_string = "Hello, World!"
search_pattern = "Wor"
if check_order(my_string, search_pattern):
    print(f"The characters in '{search_pattern}' appear in order in the string.")
else:
    print(f"The characters in '{search_pattern}' do not appear in order in the string.")

# Dictionary and counter in Python to find winner of election
from collections import Counter

def election_winner(votes):
    vote_count = Counter(votes)
    winner = max(vote_count, key=vote_count.get)
    return winner

election_votes = ['David', 'Minku', 'Mini', 'Minku', 'David', 'Minku', 'Mini', 'Minku', 'David']
winner_candidate = election_winner(election_votes)
print("Election Votes:")
print(election_votes)
print("Winner of the Election:", winner_candidate)

# Python – Append Dictionary Keys and Values ( In order ) in dictionary
def append_keys_and_values(dict1, dict2):
    result_dict = {}
    keys = list(dict1.keys()) + list(dict2.keys())
    values = list(dict1.values()) + list(dict2.values())
    result_dict.update(zip(keys, values))
    return result_dict

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
appended_dict = append_keys_and_values(dict1, dict2)
print("Dictionary 1:", dict1)
print("Dictionary 2:", dict2)
print("Appended Dictionary:", appended_dict)

# Python | Sort Python Dictionaries by Key or Value
my_dict = {'b': 2, 'a': 1, 'c': 3}
sorted_by_key = dict(sorted(my_dict.items()))
sorted_by_value = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Original Dictionary:")
print(my_dict)
print("Sorted by Key:")
print(sorted_by_key)
print("Sorted by Value:")
print(sorted_by_value)

# Python – Sort Dictionary key and values List
my_dict = {'b': [2, 1, 3], 'a': [1, 2, 3], 'c': [3, 2, 1]}
sorted_dict = {key: sorted(values) for key, values in my_dict.items()}
print("Original Dictionary:")
print(my_dict)
print("Sorted Dictionary:")
print(sorted_dict)

# Handling missing keys in Python dictionaries
my_dict = {'a': 1, 'b': 2, 'c': 3}

key_to_check = 'b'
value = my_dict.get(key_to_check, "Key not found")
print(f"Value for key '{key_to_check}': {value}")

key_to_check = 'd'
try:
    value = my_dict[key_to_check]
except KeyError:
    value = "Key not found"
print(f"Value for key '{key_to_check}': {value}")

# Python dictionary with keys having multiple inputs
def create_multi_input_dict(keys, values):
    result_dict = {}
    for key, value in zip(keys, values):
        if key in result_dict:
            result_dict[key].append(value)
        else:
            result_dict[key] = [value]
    return result_dict

keys_list = ['a', 'b', 'a', 'c', 'b']
values_list = [1, 2, 3, 4, 5]
multi_input_dict = create_multi_input_dict(keys_list, values_list)
print("Keys List:", keys_list)
print("Values List:", values_list)
print("Multi-Input Dictionary:")
print(multi_input_dict)

# Print anagrams together in Python using List and Dictionary
def group_anagrams(words_list):
    anagram_dict = {}
    for word in words_list:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(word)
        else:
            anagram_dict[sorted_word] = [word]
    return list(anagram_dict.values())

words_list = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
grouped_anagrams = group_anagrams(words_list)
print("Original List of Words:")
print(words_list)
print("Anagrams Grouped Together:")
print(grouped_anagrams)

# K’th Non-repeating Character in Python using List Comprehension and OrderedDict
from collections import Counter, OrderedDict

def kth_non_repeating_char(string, k):
    char_count = Counter(string)
    non_repeating_chars = [char for char, count in char_count.items() if count == 1]
    ordered_dict = OrderedDict.fromkeys(non_repeating_chars)
    return list(ordered_dict.keys())[k - 1] if k <= len(non_repeating_chars) else None

my_string = "Davidnag"
k_value = 3
kth_non_repeating = kth_non_repeating_char(my_string, k_value)
print(f"{k_value}th Non-repeating Character in '{my_string}': {kth_non_repeating}")

# Check if binary representations of two numbers are anagram
def are_binary_anagrams(num1, num2):
    bin1 = bin(num1)[2:]
    bin2 = bin(num2)[2:]
    return sorted(bin1) == sorted(bin2)

number1 = 10
number2 = 5
if are_binary_anagrams(number1, number2):
    print(f"The binary representations of {number1} and {number2} are anagrams.")
else:
    print(f"The binary representations of {number1} and {number2} are not anagrams.")

# Python Counter to find the size of largest subset of anagram words
from collections import Counter

def size_of_largest_anagram_subset(words_list):
    anagram_counter = Counter(tuple(sorted(word)) for word in words_list)
    largest_subset_size = max(anagram_counter.values(), default=0)
    return largest_subset_size

words_list = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
largest_subset_size = size_of_largest_anagram_subset(words_list)

print("Original List of Words:")
print(words_list)
print("Size of the Largest Anagram Subset:", largest_subset_size)

# Python | Remove all duplicates words from a given sentence
def remove_duplicates_from_sentence(sentence):
    words = sentence.split()
    unique_words = set(words)
    result_sentence = ' '.join(unique_words)
    return result_sentence

input_sentence = "Python is great and Python is versatile"
output_sentence = remove_duplicates_from_sentence(input_sentence)

print("Original Sentence:")
print(input_sentence)
print("Sentence after removing duplicate words:")
print(output_sentence)

# Python Dictionary to find mirror characters in a string
def find_mirror_characters(s):
    mirror_dict = {'A': 'A', 'B': 'D', 'C': ' ', 'D': 'B', 'E': ' ', 'F': ' ', 'G': ' ', 'H': 'H', 'I': 'I', 'J': 'L', 'K': ' ', 'L': 'J', 'M': 'M', 'N': ' ', 'O': 'O', 'P': 'Q', 'Q': 'P', 'R': ' ', 'S': ' ', 'T': 'T', 'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y', 'Z': 'Z'}
    mirror_chars = [mirror_dict.get(char, '') for char in s[::-1]]
    return ''.join(mirror_chars)

input_str = "MIRROR"
result = find_mirror_characters(input_str)
print(f"Original: {input_str}, Mirror: {result}")

# Counting the frequencies in a list using dictionary in Python
from collections import Counter

my_list = [1, 2, 3, 1, 2, 3, 4, 5, 1]
freq_dict = Counter(my_list)

print("Frequency Dictionary:", freq_dict)

# Python | Convert a list of Tuples into Dictionary
list_of_tuples = [("a", 1), ("b", 2), ("c", 3)]
dict_from_tuples = dict(list_of_tuples)

print("Dictionary from Tuples:", dict_from_tuples)

# Python counter and dictionary intersection example (Make a string using deletion and rearrangement)
from collections import Counter

def can_make_string(s1, s2):
    counter_s1 = Counter(s1)
    counter_s2 = Counter(s2)

    return all(counter_s1[char] >= counter_s2[char] for char in counter_s2)

str1 = "xyz"
str2 = "xyyzyx"
result = can_make_string(str1, str2)
print(f"Can make string: {result}")

# Python dictionary, set and counter to check if frequencies can become same
from collections import Counter

def same_frequencies(s):
    char_freq = Counter(s)
    freq_set = set(char_freq.values())

    return len(freq_set) == 1

input_str = "aabcc"
result = same_frequencies(input_str)
print(f"Can have same frequencies: {result}")



# Possible Words using given characters in Python
from itertools import permutations

def possible_words(characters):
    perms = [''.join(p) for p in permutations(characters)]
    return perms

input_chars = "abc"
result = possible_words(input_chars)
print("Possible Words:", result)

# Python – Keys associated with Values in Dictionary
my_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 2}

def keys_for_value(my_dict, value):
    keys = [key for key, val in my_dict.items() if val == value]
    return keys

target_value = 2
result = keys_for_value(my_dict, target_value)
print(f"Keys associated with value {target_value}: {result}")

#Tuple Programs:
#Python program to Find the size of a Tuple
my_tuple = (1, 2, 3, 'a', 'b', 'c')
tuple_size = len(my_tuple)
print("Size of the Tuple:", tuple_size)

#Python – Maximum and Minimum K elements in Tuple
my_tuple = (10, 5, 8, 20, 3)
k = 2

max_k_elements = tuple(sorted(my_tuple, reverse=True)[:k])
min_k_elements = tuple(sorted(my_tuple)[:k])

print(f"Maximum {k} elements: {max_k_elements}")
print(f"Minimum {k} elements: {min_k_elements}")

# Create a list of tuples from given list having number and its cube in each tuple
original_list = [1, 2, 3, 4, 5]
tuple_list = [(num, num ** 3) for num in original_list]

print("List of Tuples:", tuple_list)


# Python – Closest Pair to Kth index element in Tuple
my_tuple = (10, 20, 15, 25, 30)
k = 2

closest_pair = min(my_tuple, key=lambda x: abs(x - my_tuple[k]))
print(f"Closest pair to Kth index element ({k}): {closest_pair}")

# Python – Join Tuples if similar initial element
tuple_list = [(1, 'a'), (1, 'b'), (2, 'c'), (2, 'd')]

result_dict = {}
for t in tuple_list:
    result_dict.setdefault(t[0], []).append(t[1])

result_tuples = [(key, tuple(values)) for key, values in result_dict.items()]

print("Joined Tuples:", result_tuples)

# Python – Extract digits from Tuple list
tuple_list = [(123, 'abc'), (456, 'def'), (789, 'ghi')]

extracted_digits = [int(''.join(filter(str.isdigit, str(t[0])))) for t in tuple_list]

print("Extracted Digits:", extracted_digits)

# Python – All pair combinations of 2 tuples
tuple1 = (1, 2)
tuple2 = ('a', 'b')

pair_combinations = [(x, y) for x in tuple1 for y in tuple2]

print("All Pair Combinations:", pair_combinations)

# Python – Remove Tuples of Length K
k = 2
tuple_list = [(1, 2), (3, 4), ('a', 'b'), ('c', 'd')]

filtered_tuples = [t for t in tuple_list if len(t) != k]

print("Filtered Tuples:", filtered_tuples)

# Sort a list of tuples by second Item
tuple_list = [(3, 5), (1, 2), (4, 1), (2, 8)]

sorted_tuples = sorted(tuple_list, key=lambda x: x[1])

print("Sorted Tuples:", sorted_tuples)

# Python program to Order Tuples using external List
tuple_list = [(3, 'c'), (1, 'a'), (4, 'd'), (2, 'b')]
order_list = [2, 0, 3, 1]

ordered_tuples = [tuple_list[i] for i in order_list]

print("Ordered Tuples:", ordered_tuples)

# Python – Flatten tuple of List to tuple
nested_tuple = ((1, 2), [3, 4], (5, 6))

flattened_tuple = tuple(item for sublist in nested_tuple for item in (sublist if isinstance(sublist, tuple) else [sublist]))

print("Flattened Tuple:", flattened_tuple)

# Python – Convert Nested Tuple to 
nested_tuple = ((1, 2), (3, 4), (5, 6))

converted_tuple = tuple(item for sublist in nested_tuple for item in sublist)

print("Converted Tuple:", converted_tuple)


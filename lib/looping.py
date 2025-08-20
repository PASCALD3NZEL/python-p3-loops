#!/usr/bin/env python3

def happy_new_year():
    """
    Prints a countdown from 10 to 1, followed by "Happy New Year!"
    """
    for i in range(10, 0, -1):
        print(i)
    print("Happy New Year!")

def square_integers(int_list):
    """
    Takes a list of integers and returns a list of their squares.
    Works with both positive and negative integers.
    """
    return [i**2 for i in int_list]

def fizzbuzz():
    """
    Prints numbers from 1 to 100, but:
    - For multiples of 3, print "Fizz" instead of the number
    - For multiples of 5, print "Buzz" instead of the number
    - For multiples of both 3 and 5, print "FizzBuzz" instead of the number
    """
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
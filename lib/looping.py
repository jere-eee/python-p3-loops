#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    num = 10
    while num > 0:
        print(num)
        num -= 1
    print("Happy New Year!")

def square_integers(int_list):
    # code goes here!
    return [nu**2 for nu in int_list]

def fizzbuzz():
    # code goes here!
    num = 1
    while num < 101:
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0 and num % 5 != 0:
            print("Fizz")
        elif num % 3 != 0 and num % 5 == 0:
            print("Buzz")
        else:
            print(num)
        num += 1

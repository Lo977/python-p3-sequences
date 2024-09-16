#!/usr/bin/env python3

def print_fibonacci(length):
    fib_num = [0,1]
    while len(fib_num)<length:
        fib_num.append(fib_num[-1]+fib_num[-2])
    print(fib_num[:length])
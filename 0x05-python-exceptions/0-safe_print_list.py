#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    try:
        counter = 0
        for i in range(0, x):
            print(f"{my_list[i]}", end="")
            count += 1
        print()
        return counter
    except (TypeError, IndexError):
        print()
        return counter

import numpy as np
# import torch
# import conda
import sys


def print_hi():

    str_1 = input("Enter your input: ")
    split_str = list(str_1)
    str_2 = ""
    for s in split_str:
        if s == "b":
            str_2 += "U"
            print("U")
        elif s == "r":
            str_2 += "R"
            print("R")
        elif s == "w":
            str_2 += "F"
            print("F")
        elif s == "g":
            str_2 += "D"
            print("D")
        elif s == "o":
            str_2 += "L"
            print("L")
        elif s == "y":
            str_2 += "B"
            print("B")
        else:
            print(" ")

    print("result :", str_2)  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


#!/usr/bin/env python3
# Created By: Minab Berhane
# Date: Oct 11, 2022
# This program tells you what type of integer you put in


def main():
    # User input
    print("welcome to my number assigner")
    user_input = int(input("please input an integer: "))

    # Number assigner
    if user_input > 0:
        print("{} is a positive number".format(user_input))
    elif user_input < 0:
        print("{} is a negative number".format(user_input))
    else:
        print("{} is 0".format(user_input))


if __name__ == "__main__":
    main()
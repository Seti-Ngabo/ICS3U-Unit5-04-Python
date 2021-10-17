#!/usr/bin/env python3

# Created by: Seti Ngabo
# Created on: Sept 2021
# This program calculates the volume of a cylinder
#   with user input

import math


def cylinder_volume(radius, height):
    # this function checks the volume

    # process
    volume = math.pi * radius ** 2 * height

    return volume


def main():
    # this function prints the final answer

    # input
    radius_from_user_str = input("Enter the radius of the cylinder (cm): ")
    height_from_user_str = input("Enter the height of the cylinder (cm): ")
    print("")

    try:
        radius_from_user_int = int(radius_from_user_str)
        height_from_user_int = int(height_from_user_str)

        # call function
        answer = cylinder_volume(radius_from_user_int, height_from_user_int)

        # output
        print(
            "The volume of a cylinder with a radius of {0}cm and the height of {1}cm is {2}cm³.".format(
                radius_from_user_int, height_from_user_int, answer
            )
        )

    except Exception:
        print("Invalid input, try again.")
    print("\nDone.")


if __name__ == "__main__":
    main()

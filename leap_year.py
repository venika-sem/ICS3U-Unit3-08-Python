#!/usr/bin/env python3

# Created by: Venika Sem
# Created on: Nov 2022
# This program checks if the year is a leap year


def main():
    # this function checks if the year is a leap year

    # input
    year_as_string = input("Please enter the year: ")
    print("")

    # process & output
    try:
        year_as_number = int(year_as_string)
        if year_as_number > 0:
            if year_as_number % 4 == 0:
                if year_as_number % 100 == 0:
                    if year_as_number % 400 == 0:
                        print("The year {0} is a leap year.".format(year_as_number))
                    else:
                        print("The year {0} is a common year.".format(year_as_number))
                else:
                    print("The year {0} is a leap year.".format(year_as_number))
            else:
                print("The year {0} is a common year.".format(year_as_number))
        else:
            print("\n{} is not in the common era.".format(year_as_number))
    except ValueError:
        print("{0} is not a valid input".format(year_as_string))
    finally:
        print("Done.")


if __name__ == "__main__":
    main()

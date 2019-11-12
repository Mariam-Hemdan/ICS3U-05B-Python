#!/usr/bin/env python3

# Created by : Mariam Hemdan
# Created on : November 2019
# This program using a nested loop


def main():
    # this program uses a nested loop

    counter1 = 0
    counter2 = 0

    # process & output
    for counter1 in range(100):
        for counter2 in range(100):
            if (counter1+counter2 == 60 and counter1-counter2 == 14):
                print("(a+b=60 and a-b=14) a={0} and b={1}".
                      format(counter1, counter2))


if __name__ == "__main__":
    main()

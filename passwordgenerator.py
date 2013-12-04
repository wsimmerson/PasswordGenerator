#!/usr/bin/python3

import random
import argparse

__author__ = "Wayne Simmerson"
__email__ = "wsimmerson@gmail.com"

def characters():
    """
        Generates list of required characters
    """

    letter = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
    sc = "! @ # $ % ^ & * ( ) _ - + = ? : ;".split()


    chars = []
    chars.append(random.choice(letter))
    chars.append(random.choice(letter).upper())
    chars.append(str(random.randint(0,9)))
    chars.append(random.choice(sc))

    return chars

def newpassword(length=8):
    """
        Generates and returns a strong password
    """

    word = characters()

    while len(word) < length:
        word.append(random.choice(characters()))

    random.shuffle(word)
    return "".join(word)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--number", dest='number', type=int, default=1, help='Specify number of passwords to generate <default 1>')
    parser.add_argument("-l", "--length", type=int, default=8, help='Specify Password Length <default 8>')

    args = parser.parse_args()

    for n in range(args.number):
        print(newpassword(args.length))

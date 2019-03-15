# -*- coding: utf-8 -*-


def changeNumber(vector):
    vector[vector.__len__() - 1] = 300


def add_number(v):
    return v + 1


if __name__ == "__main__":
    # Python does not have variable in the box sense of the word
    # only named references for objects
    a = 1234
    print(id(a))

    b = 5678
    print(id(b))

    b = a  # Python does not copy an object by value
    print(id(b))

    print(a is b)
    print(a == b)
    print(id(a) == id(b))

    r = [1, 2, 3]
    print(r)

    s = r
    print(s)

    s[1] = 42

    print("{0}\n{1}".format(s, r))
    changeNumber(s)
    print(r)

    c = [3]
    d = [3]

    print("{0}\n{1}".format(c == d, c is d))  # Object equality vs object identity

    e = 10
    print("{0}\t{1}\t{2}".format(e, add_number(e), e))

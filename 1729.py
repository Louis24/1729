#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @Time    : 2021/3/4 16:49
#  @Author  : Louis Li
#  @Email   : vortex750@hotmail.com


import math


def isSqr(n):
    x = int((math.sqrt(n)))
    return x * x == n


def main():
    i = 1

    while True:
        print(i)
        n = 1729 * i * i + 1
        if isSqr(n):
            print(i, n)
            return
        else:
            i += 1


if __name__ == "__main__":
    main()

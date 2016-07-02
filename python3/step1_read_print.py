#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import mal_readline
import printer
import reader
from mal_types import *


def READ(s: str) -> MalType:
    try:
        obj = reader.read_str(s)
    except ValueError as e:
        print('error', e)
        return None
    else:
        return obj


def EVAL(obj: MalType) -> MalType:
    return obj


def PRINT(obj: MalType) -> str:
    return printer.pr_str(obj, print_readably=False)


def rep(s: str) -> str:
    return PRINT(EVAL(READ(s)))


def main():
    try:
        while True:
            s = mal_readline.readline('user> ')
            print(rep(s))
    except (KeyboardInterrupt, EOFError):
        pass


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import mal_readline
import printer
import reader
from mal_types import *


def READ(s: str) -> MalType:
    return reader.read_str(s)


def EVAL(ast: MalType) -> MalType:
    return ast


def PRINT(exp: MalType) -> str:
    return printer.pr_str(exp, print_readably=True)


def rep(s: str) -> str:
    return PRINT(EVAL(READ(s)))


def main():
    while True:
        try:
            print(rep(mal_readline.readline('user> ')))
        except (KeyboardInterrupt, EOFError):
            break
        except Exception as e:
            print('Error: ', e)


if __name__ == '__main__':
    main()

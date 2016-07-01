#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import mal_readline


def READ(s: str) -> str:
    return s


def EVAL(s: str) -> str:
    return s


def PRINT(s: str) -> str:
    return s


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

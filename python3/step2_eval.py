#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import operator as op

import mal_readline
import printer
import reader
from mal_types import *


def READ(s: str) -> MalType:
    return reader.read_str(s)


def eval_ast(ast: MalType, env: dict):
    if isinstance(ast, MalSymbol):
        try:
            return env[ast]
        except KeyError as e:
            raise KeyError('Symbol {} not found in environment.'.format(ast))
    elif isinstance(ast, MalList):
        return MalList(EVAL(child, env) for child in ast)
    else:
        return ast


def EVAL(ast: MalType, env: dict = None) -> MalType:
    if isinstance(ast, MalList):
        if len(ast) == 0:  # an empty list
            return ast
        else:  # a list
            f, *args = eval_ast(ast, env)
            return f(*args)
    if isinstance(ast, MalVector):
        return MalVector(EVAL(member, env) for member in ast)
    if not isinstance(ast, MalList):  # not a list
        return eval_ast(ast, env)


def PRINT(exp: MalType) -> str:
    return printer.pr_str(exp, print_readably=True)


repl_env = {
    '+': op.add,
    '-': op.sub,
    '*': op.mul,
    '/': op.floordiv,
}


def rep(s: str) -> str:
    return PRINT(
        EVAL(
            READ(s),
            env=repl_env
        )
    )


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

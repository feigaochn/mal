#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from mal_types import *
import logging


def pr_str(ast: MalType, print_readably=False) -> str:
    """Take a mal data structure and return a string representation of it.
    """
    # logging.critical("(type: {}; value: {})".format(type(obj), str(obj)))
    if isinstance(ast, MalList):
        s = '(' + ' '.join(map(pr_str, ast)) + ')'
    elif isinstance(ast, MalVector):
        s = '[' + ' '.join(map(pr_str, ast)) + ']'
    elif isinstance(ast, MalHashmap):
        s = '{' + ' '.join(map(pr_str, ast)) + '}'

    elif isinstance(ast, MalNumber):
        s = str(ast)
    elif isinstance(ast, MalSymbol):
        s = ast
    else:
        s = str(ast)

    # if print_readably:
    #     s = s.replace('"', '\\"')
    #     s = s.replace('\n', '\\n"')
    #     s = s.replace('\\', '\\\\')

    return s

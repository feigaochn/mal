#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from mal_types import *


def pr_str(ast: MalType, print_readably=False) -> str:
    """Take a mal data structure and return a string representation of it.
    """
    # logging.critical("(type: {}; value: {})".format(type(obj), str(obj)))
    if isinstance(ast, MalList):
        s = '(' + ' '.join(
            pr_str(c, print_readably=print_readably) for c in ast) + ')'
    elif isinstance(ast, MalVector):
        s = '[' + ' '.join(
            pr_str(c, print_readably=print_readably) for c in ast) + ']'
    elif isinstance(ast, MalHashmap):
        s = '{' + ' '.join(
            pr_str(c, print_readably=print_readably) for c in ast) + '}'

    elif isinstance(ast, MalFunction):
        s = str(ast)
    elif isinstance(ast, MalNumber):
        s = str(ast)
    elif isinstance(ast, MalSymbol):
        s = str(ast)
    elif isinstance(ast, MalKeyword):
        s = str(ast)
    elif ast == nil:
        s = str(nil)
    elif isinstance(ast, MalString):
        s = str(ast)
        if print_readably:
            s = s.replace('\\', '\\\\')
            s = s.replace('\n', '\\n')
            s = s.replace('"', '\\"')
            s = '"' + s + '"'
    else:
        s = str(ast)

    return s

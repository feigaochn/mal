#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import functools
import operator as op

import printer
from mal_types import *


def _chain(rtype, fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        return rtype(fn(*args, **kwargs))

    return wrapper


ns = {
    '+': _chain(MalNumber, op.add),
    '-': _chain(MalNumber, op.sub),
    '*': _chain(MalNumber, op.mul),
    '/': _chain(MalNumber, op.floordiv),

    # call pr_str on the first parameter with print_readably set to true,
    # prints the result to the screen and then return nil.
    # 'prn': (lambda ast: printer.pr_str(ast, print_readably=True) or nil),

    # take the parameters and return them as a list.
    'list': (lambda *args: MalList(args)),

    # return true if the first parameter is a list, false otherwise.
    'list?': _chain(MalBool, lambda p: isinstance(p, MalList)),

    # treat the first parameter as a list and return true if the list is empty
    # and false if it contains any elements.
    'empty?': _chain(MalBool, lambda p: isinstance(p, (MalList, MalVector))
                                        and len(p) == 0),

    # treat the first parameter as a list and return the number of elements
    # that it contains.
    'count': _chain(MalNumber,
                    lambda p: len(p)
                    if isinstance(p, (MalList, MalVector))
                    else 0),

    'nil': nil,

    # compare the first two parameters and return true if they are the same
    # type and contain the same value. In the case of equal length lists,
    # each element of the list should be compared for equality and if they are
    # the same return true, otherwise false.
    '=': _chain(MalBool, op.eq),
    # '=': lambda a, b: MalBool(type(a) == type(b) and op.eq(a, b)),

    # <, <=, >, and >=:
    # treat the first two parameters as numbers and do the corresponding numeric
    # comparison, returning either true or false.
    '<': _chain(MalBool, op.lt),
    '<=': _chain(MalBool, op.le),
    '>': _chain(MalBool, op.gt),
    '>=': _chain(MalBool, op.ge),

    # string functions
    'pr-str': lambda *args: MalString(
        " ".join(printer.pr_str(arg, print_readably=True)
                 for arg in args)),
    'str': lambda *args: MalString(
        "".join(printer.pr_str(arg, print_readably=False)
                for arg in args)),
    'prn': lambda *args: print(
        MalString(" ".join(printer.pr_str(arg, print_readably=True)
                           for arg in args))) or nil,
    'println': lambda *args: print(
        " ".join(printer.pr_str(arg, print_readably=False)
                 for arg in args)) or nil,
}

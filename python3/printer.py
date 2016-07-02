#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from mal_types import *
import logging


def pr_str(obj: MalType, print_readably=False) -> str:
    """Take a mal data structure and return a string representation of it.
    """
    # logging.critical("(type: {}; value: {})".format(type(obj), str(obj)))
    if isinstance(obj, MalNumber):
        s = str(obj)
    elif isinstance(obj, MalList):
        s = '(' + ' '.join(map(pr_str, obj)) + ')'
    elif isinstance(obj, MalVector):
        s = '[' + ' '.join(map(pr_str, obj)) + ']'
    elif isinstance(obj, MalSymbol):
        s = obj
    else:
        s = str(obj)

    if print_readably:
        s = s.replace('"', '\\"')
        s = s.replace('\n', '\\n"')
        s = s.replace('\\', '\\\\')

    return s

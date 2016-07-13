#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from functools import partial
from typing import List

from mal_types import *

Token = str


class Reader:
    """a simple stateful object stores the tokens and a position."""

    def __init__(self, tokens):
        """
        :type tokens: List[Token]
        """
        self.tokens = tokens
        self.position = 0

    def next(self) -> Token:
        """Returns the token at the current position and increments the
        position.
        """
        value = self.peek()
        self.position += 1
        return value

    def peek(self) -> Token:
        """Returns the token at the current position.
        """
        try:
            token = self.tokens[self.position]
        except IndexError:
            raise IndexError('No more tokens')
        else:
            return token


def read_str(line_str: str) -> MalType:
    """Convert string to an MAL data structure."""
    tokens = tokenizer(line_str)
    reader = Reader(tokens)
    return read_form(reader)


def tokenizer(s):
    """Takes a single string and return a list of all the tokens (strings)
    in it.
    """
    mal_pattern = re.compile(r"""
    [\s,]*      # matches whitespaces or commas. this is not captured
    (~@        # captures special two-characters
    | [\[\]{}()'`~\^@]        # any special single character
    | "(?:\\.|[^\\"])*"      # starts capturing at a double-quote and strops
                            # at next double-quote unless it was proceeded
                            # by a backslash in which case it includes it
                            # until next double-quote
    | ;.*        # any sequence of characters starting with ;
    | [^\s\[\]{}('"`,;)]*    # a sequence of zero or more non special characters
    )""", re.VERBOSE)
    return re.findall(mal_pattern, s)


def read_form(reader):
    """Peek at the first token in the Reader object and switch on the first
    character of that token.

    :type reader: Reader
    :return: a mal data type
    :rtype: MalType
    """
    token = reader.peek()
    # TODO: handle more types to pass the test

    if token == '':
        pass
    elif token == "'":  # quote
        reader.next()
        return MalList([MalSymbol('quote'), read_form(reader)])
    elif token == "`":  # quasi-quote
        reader.next()
        return MalList([MalSymbol('quasiquote'), read_form(reader)])
    elif token == "~":  # unquote
        reader.next()
        return MalList([MalSymbol('unquote'), read_form(reader)])
    elif token == "~@":  # splice-unquote
        reader.next()
        return MalList([MalSymbol('splice-unquote'), read_form(reader)])
    elif token == '@':  # deref
        reader.next()
        return MalList([MalSymbol('deref'), read_form(reader)])
    elif token == '^':  # with-meta
        reader.next()
        val1 = read_form(reader)
        val2 = read_form(reader)
        return MalList([MalSymbol('with-meta'), val2, val1])

    elif token == '(':
        return read_list(reader)
    elif token == '[':
        return read_vector(reader)
    elif token == '{':
        return read_hashmap(reader)

    else:
        return read_atom(reader)


def read_array(reader: Reader, result_type: MalArray,
               ending: str) -> MalArray:
    """Read array-like data: list, vector, hashmap, etc."""
    results = result_type()
    reader.next()
    while True:
        token = reader.peek()
        if token == '':  # EOF
            raise ValueError('illegal string')
        elif token[0] == ending:
            reader.next()
            return results
        else:
            results.append(read_form(reader))


read_list = partial(read_array, result_type=MalList, ending=')')
read_list.__doc__ = """Returns a list of values."""

read_vector = partial(read_array, result_type=MalVector, ending=']')
read_vector.__doc__ = """Returns a vector of values."""

read_hashmap = partial(read_array, result_type=MalHashmap, ending='}')


def read_atom(reader: Reader) -> MalType:
    """Look at the contents of the token and return the appropriate scalar
    (simple/single) data type value.
    """
    token = reader.next()
    # Number type
    try:
        return MalNumber(token)
    except ValueError:
        pass

    if token[0] == token[-1] == '"':
        s = token[1:-1]
        s = s.replace('\\"', '"')
        s = s.replace('\\n', '\n')
        s = s.replace('\\\\', '\\')
        return MalString(s)

    elif token == 'nil':
        return nil
    elif token == 'true':
        return MalBool(True)
    elif token == 'false':
        return MalBool(False)
    elif token[0] == ':':
        return MalKeyword(token)

    # catch all as Symbol type
    return MalSymbol(token)

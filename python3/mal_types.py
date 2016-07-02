#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import typing



class MalType:
    pass


class MalList(MalType, list):
    pass


class MalNumber(MalType, int):
    pass


class MalString(MalType, str):
    pass


class MalSymbol(MalType, str):
    pass


class MalVector(MalType, list):
    pass


class MalHashmap(MalType, list):
    pass


MalArray = typing.TypeVar('MalArray', MalList, MalVector, MalHashmap)
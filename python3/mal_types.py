#!/usr/bin/env python3
# -*- coding: utf-8 -*-


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
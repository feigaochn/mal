#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from mal_types import MalList


class Env(dict):
    def __init__(self, *args, **kwargs):
        self._outer = kwargs.pop('outer', None)
        binds = kwargs.pop('binds', [])
        exprs = kwargs.pop('exprs', [])
        # if binds and exprs:
        for i, b in enumerate(binds):
            if b == '&':
                self.set(binds[i+1], MalList(exprs[i:]))
                break
            else:
                self.set(b, exprs[i])
        super().__init__(*args, **kwargs)

    def find(self, key):
        """Find the environment that contains the key."""
        if key in self:
            return self
        elif self._outer is not None:
            return self._outer.find(key)
        else:
            return None

    def get(self, key, **kwargs):
        """Get the value for key in current and outer environments."""
        env = self.find(key)
        if env:
            return env[key]
        else:
            raise KeyError(
                "Key '{}' not found in any environments.".format(key))

    def set(self, key, value):
        self[key] = value
        return value

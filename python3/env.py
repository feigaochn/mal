#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import operator as op


class Env2:
    def __init__(self, outer=None):
        """
        :type outer: [Env, None]
        """
        self.data = dict()
        self.outer = outer
        self._set_default()

    def find(self, k):
        if k in self.data:
            return self
        elif self.outer is not None:
            return self.outer.get(k)
        else:
            return None

    def get(self, k):
        env = self.find(k)
        if env:
            return env.data[k]
        else:
            raise KeyError("'{}' not found".format(k))

    def set(self, key, val):
        self.data[key] = val

    def _set_default(self):
        self.data.update(
            {
                '+': op.add,
                '-': op.sub,
                '*': op.mul,
                '/': op.floordiv,
            }
        )


class Env(dict):
    def __init__(self, *args, **kwargs):
        self._outer = kwargs.pop('outer', None)
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
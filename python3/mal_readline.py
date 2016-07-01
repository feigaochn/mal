#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
readline support:

Ref: https://pymotw.com/2/readline/
"""

import os
import readline as py_readline

CUR_DIR = os.path.abspath(os.path.curdir)
READLINE_HISTORY = os.path.join(CUR_DIR, '.history')

if not os.path.exists(READLINE_HISTORY):
    open(READLINE_HISTORY, 'w').close()


class HistoryCompleter:
    def __init__(self):
        self.matches = []

    def complete(self, text, state):
        resp = None
        if state == 0:
            hist = [py_readline.get_history_item(i + 1)
                    for i in range(py_readline.get_current_history_length())]
            if text:
                self.matches = sorted(h for h in hist if h and h.startswith(text))
            else:
                self.matches = []
        try:
            resp = self.matches[state]
        except IndexError:
            resp = None
        return resp


py_readline.set_completer(HistoryCompleter().complete)
py_readline.parse_and_bind('tab: complete')
py_readline.set_history_length(128)


def readline(prompt=''):
    py_readline.read_history_file(READLINE_HISTORY)
    s = input(prompt)
    py_readline.write_history_file(READLINE_HISTORY)
    return s

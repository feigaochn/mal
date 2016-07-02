#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from invoke import task

import reader


@task
def token(ctx, s):
    print(reader.tokenizer(s))

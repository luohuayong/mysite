#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Leo on 2017/10/28

"""
代码说明：
"""

# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)

if __name__ == '__main__':
    pass
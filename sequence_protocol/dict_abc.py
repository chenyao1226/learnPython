#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/3 13:32
# @Author  : ChenYao
# @File    : dict_abc.py

from collections.abc import Mapping, MutableMapping

a = {}

print(isinstance(a, MutableMapping))

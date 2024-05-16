#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from OSS import Oss
from utils.decorators import async_task


@async_task
def oss_task(key, obj):
    oss = Oss()
    oss.put_object(key, obj)
    path = oss.get_url(key)
    print(path)

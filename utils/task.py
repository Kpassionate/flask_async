#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from utils.decorators import async_task


@async_task
def oss_task(key, obj):
    # oss = Oss()
    # oss.put_object(key, obj)
    import time
    time.sleep(3)
    a = 1 / 0
    # raise Exception('oss_task complate!')


#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import functools
import traceback

from utils.thread_util import global_thread_pool


def callback(*args, **kwargs):
    def inner_callback(task):
        e = task.exception()
        if not e:
            return
        # 可以获取错误 简版\详细 信息（日志记录 可自行选择使用）
        print(f"后台上传OSS数据异常--{kwargs}:\n" + str(e))
        traceback_info = traceback.format_exc()
        print(f"后台上传OSS数据异常--{kwargs}:\n" + traceback_info)

    return inner_callback


def async_task(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        global_thread_pool.executor.submit(func, *args, **kwargs).add_done_callback(callback(*args, **kwargs))

    return wrapper

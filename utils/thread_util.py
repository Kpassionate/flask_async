#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from concurrent.futures.thread import ThreadPoolExecutor


class ThreadPool(object):
    def __init__(self):
        # 线程池
        self.executor = ThreadPoolExecutor(10)
        # 用于存储每个项目批量任务的期程
        self.future_dict = {}

    def __del__(self):
        self.executor.shutdown()


# 主线程中的全局线程池
global_thread_pool = ThreadPool()

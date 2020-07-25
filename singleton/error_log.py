# -*- coding: utf-8 -*-
"""
Author:duan
Date: 2020/7/26 1:59
"""

from singleton import sf_logger

if __name__ == '__main__':

    try:
        a = 1 / 0
    except:
        sf_logger.error("something wnt wrong")

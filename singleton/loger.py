# -*- coding: utf-8 -*-
"""
Author:duan
Date: 2020/7/26 1:50
"""


def critical(msg):
    with open('debug.log', "a") as log_file:
        log_file.write("[CRITICAL] {0}\n".format(msg))


def error(msg):
    with open('debug.log', "a") as log_file:
        log_file.write("[ERROR] {0}\n".format(msg))


def warn(msg):
    with open('debug.log', "a") as log_file:
        log_file.write("[WARN] {0}\n".format(msg))


def info(msg):
    with open('debug.log', "a") as log_file:
        log_file.write("[INFO] {0}\n".format(msg))


def debug(msg):
    with open('debug.log', "a") as log_file:
        log_file.write("[DEBUG] {0}\n".format(msg))

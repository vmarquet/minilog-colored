#!/usr/bin/env python3
# coding: utf-8

# usage:
# from minilog import info, success, warning, error
# print(warn("You cannot fight here. This is the war room."))

def info(s):
    return "\033[34m[i] %s\033[0m" % s

def success(s):
    return "\033[32m[+] %s\033[0m" % s

def warning(s):
    return "\033[33m[-] %s\033[0m" % s

def error(s):
    return "\033[31m[-] %s\033[0m" % s


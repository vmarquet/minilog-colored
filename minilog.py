#!/usr/bin/env python3
# coding: utf-8

# usage:

# from minilog import blue, green, yellow, red
# print(green("Update successful."))

# from minilog import info, success, warn, error
# print(warn("You cannot fight here. This is the war room."))


########################################
#                colors                #
########################################

def blue(s):
    return "\033[34m%s\033[0m" % s

def green(s):
    return "\033[32m%s\033[0m" % s

def yellow(s):
    return "\033[33m%s\033[0m" % s

def red(s):
    return "\033[31m%s\033[0m" % s


########################################
#           log formatting             #
########################################

def info(s):
    return blue("[i] %s" % s)

def success(s):
    return green("[+] %s" % s)

def warn(s):
    return yellow("[-] %s" % s)

def error(s):
    return red("[-] %s" % s)


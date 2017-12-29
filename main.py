#! /usr/bin/env/ python3
# coding: utf-8

"""
===== main.py =====

A module to colors the output of the logging module

"""

import colors as clr     #colors is a module available on https://github.com/LopsemPyier/colors.
import logging as lg

def debugLevel():    #To display debug's logging's messages
    lg.basicConfig(level=lg.DEBUG)

def critical(msg):     #Print a critical's logging message with white text on red background.
    clr.crit()
    lg.critical(msg)
    clr.reset()

def info(msg):     #Print a information's logging message with blue text.
    clr.blue()
    lg.info(msg)
    clr.reset()

def warning(msg):     #Print a warning's logging message with yellow text.
    clr.yellow()
    lg.warning(msg)
    clr.reset()

def error(msg):     #Print a error's logging message with red text.
    clr.red()
    lg.error(msg)
    clr.reset()

def debug(msg):     #Print a debug's logging message with green text.
    clr.green()
    lg.debug(msg)
    clr.reset()

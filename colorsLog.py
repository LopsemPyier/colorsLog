#! /usr/bin/env python3
# coding: utf-8

import colors as clr
import logging as lg
import time
import datetime as dt
import re
import os

global path, level
path = ""
level = 5


def strf(te, ti = None):
	if ti:
		date = time.strftime(te, ti)
	else :
		date = time.strftime(te)

	monthsNum = {}

	for i in range(1,13):
		if re.search("^[0-9]$", str(i)):
			ie = re.sub("(?P<t>[0-9])", "0\g<t>", str(i))
		else :
			ie = str(i)
		monthsNum[ie] = dt.date(2008, i, 1).strftime('%B')
	
	for i, j in monthsNum.items():
		date = date.replace(j, i)
	return date

def initLogs(localPath="", lev=5):
	global path, level
	level = lev
	reset()
	try :
		os.mkdir(localPath + "/logs")
	except FileExistsError :
		pass
	timeStart = time.localtime()
	path = localPath + strf("/logs/%d%B%Y_%H%M%S.log", timeStart)
	with open(path, "a") as f:
		f.write("Logs' file. Create on the {}.\n==================================================\n[{t}] % : Begin.\n[{t}] % : Program had started running.\n".format(time.strftime("%A %d %B %Y %H:%M:%S", timeStart), t = strf("%d/%B/%Y at %Hh %M:%S")))
	
	return path

def debug(msg):
        clr.green()
        lg.debug(msg)
        clr.reset()
        if level >= 5:
                with open(path, "a") as f:
                        f.write("[{}] & : (DEBUG:root:) {}\n".format(strf("%d/%B/%Y at %Hh %M:%S"), msg))

def info(msg):
        clr.blue()
        lg.info(msg)
        clr.reset()
        if level >= 4:
                with open(path, "a") as f:
                        f.write("[{}] & : (INFO:root:) {}\n".format(strf("%d/%B/%Y at %Hh %M:%S"), msg))

def warning(msg):
        clr.yellow()
        lg.warning(msg)
        clr.reset()
        if level >= 3:
                with open(path, "a") as f:
                        f.write("[{}] & : (WARNING:root:) {}\n".format(strf("%d/%B/%Y at %Hh %M:%S"), msg))

def error(msg):
        clr.red()
        lg.error(msg)
        clr.reset()
        if level >= 2:
                with open(path, "a") as f:
                        f.write("[{}] & : (ERROR:root:) {}\n".format(strf("%d/%B/%Y at %Hh %M:%S"), msg))

def critical(msg):
        clr.crit()
        lg.critical(msg)
        clr.reset()
        if level >= 1:
                with open(path, "a") as f:
                        f.write("[{}] & : (CRITICAL:root:) {}\n".format(strf("%d/%B/%Y at %Hh %M:%S"), msg))

def log(msg):
	with open(path, "a") as f:
		f.write("[{}] @ : {}\n".format(strf("%d/%B/%Y at %Hh %M:%S"), msg))

def debugLevel():
        lg.basicConfig(level=lg.DEBUG)

def reset():
        clr.reset()

def end():
	with open(path, "a") as f:
		f.write("[{t}] % : Program had stoped.\n[{t}] % : End.\n==================================================\n\n".format(t = strf("%d/%B/%Y at %Hh %M:%S")))
	

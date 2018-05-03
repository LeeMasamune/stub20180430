#!/usr/bin/env python3
# -*- coding: utf_8 -*-

import random
import time

import math
tau = math.pi * 2.0

import pigpio
pi = pigpio.pi()

def QC(x):
	if (x < 0):
		x = 0
	if (x > 1):
		x = 1
	d = x * tau
	z = math.cos(d)
	return (1 - z) * 0.5

def QCR(x):
	if (x < 0):
		x = 0
	if (x > 1):
		x = 1
	x = x * 0.5
	d = x * tau
	z = math.cos(d)
	return (1 - z) * 0.5

# unused
def QCF(x):
	if (x < 0):
		x = 0
	if (x > 1):
		x = 1
	x = (x * 0.5) + 0.5
	d = x * tau
	z = math.cos(d)
	return (1 - z) * 0.5	

def LPR(min, max, msecs_timeout_q):
	start = time.time()
	while True:
		current = time.time()
		msecs_diff = (current - start) * 1000
		if msecs_diff > msecs_timeout_q :
			break
		else: 
			plot_x = msecs_diff / msecs_timeout_q
			plot_y = 0
			plot_y = QCR(plot_x)
			val = min + ((max - min) * plot_y)
			#print(math.ceil(val))
			pi.set_PWM_dutycycle(17, val)

# unused
def LPF(min, max, msecs_timeout_q):
	start = time.time()
	while True:
		current = time.time()
		msecs_diff = (current - start) * 1000
		if msecs_diff > msecs_timeout_q :
			break
		else: 
			plot_x = msecs_diff / msecs_timeout_q
			plot_y = 0
			plot_y = QCF(plot_x)
			val = min + ((max - min) * plot_y)
			#print(math.ceil(val))
			pi.set_PWM_dutycycle(17, val)

# (co)sine loop
def LP(min, max, msecs_timeout_q):
	while True:
		start = time.time()
		while True:
			current = time.time()
			msecs_diff = (current - start) * 1000
			if msecs_diff > msecs_timeout_q :
				break
			else: 
				plot_x = msecs_diff / msecs_timeout_q
				plot_y = 0
				plot_y = QC(plot_x)
				val = min + ((max - min) * plot_y)
				#print(math.ceil(val))
				pi.set_PWM_dutycycle(17, val)

pwm_min = 48
pwm_max = 255

msecs_timeout = 5000

LPR(0, pwm_min, msecs_timeout * 0.5)
LP(pwm_min, pwm_max, msecs_timeout)

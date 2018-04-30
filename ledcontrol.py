#!/usr/bin/env python3
# -*- coding: utf_8 -*-

import math
import random
import time

def Q1(x):
	if (x < 0):
		x = 0
	if (x > 1):
		x = 1
	return math.sqrt(1 - (x ** 2))

def Q2(x):
	if (x < 0):
		x = 0
	if (x > 1):
		x = 1
	return math.sqrt((2 * x) - (x ** 2))

def Q3(x):
	if (x < 0):
		x = 0
	if (x > 1):
		x = 1
	return 1 - math.sqrt((2 * x) - (x ** 2))

def Q4(x):
	if (x < 0):
		x = 0
	if (x > 1):
		x = 1
	return 1 - math.sqrt(1 - (x ** 2))

pwm_min = 64
pwm_max = 255
pwm_mid = (pwm_min + pwm_max) / 2
pwm_val = 0

msecs_timeout = 1000 #* random.random()

state = 4
state_table = { 4 : 2, 2 : 1, 1 : 3, 3 : 4 }

plot_x = 0
plot_y = 0

while True:
	start = time.time()
	msecs_timeout_q = (msecs_timeout / 4) #* random.random()
	while True:
		current = time.time()
		msecs_diff = (current - start) * 1000
		if msecs_diff > msecs_timeout_q :
			state = state_table[state]
			break
		else: 
			plot_x = msecs_diff / msecs_timeout_q
			plot_y = 0
			if state == 4 :
				plot_y = Q4(plot_x)
				pwm_val = pwm_min + ((pwm_mid - pwm_min) * plot_y)
			elif state == 2 :
				plot_y = Q2(plot_x)
				pwm_val = pwm_mid + ((pwm_max - pwm_mid) * plot_y)
			elif state == 1 :
				plot_y = Q1(plot_x)
				pwm_val = pwm_mid + ((pwm_max - pwm_mid) * plot_y)
			elif state == 3 :
				plot_y = Q3(plot_x)
				pwm_val = pwm_min + ((pwm_mid - pwm_min) * plot_y)
			print(math.ceil(pwm_val))

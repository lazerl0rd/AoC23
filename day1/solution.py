#! /usr/bin/env python

import regex as re

with open("input.txt") as file:
	firstNum = r"^([^0-9]*)([0-9]{1})"
	lastNum =  r"([0-9]{1})([^0-9]*)$"
	total = 0

	for line in file:
		value = int(re.search(firstNum, line).group(2) + re.search(lastNum, line).group(1))
		total += value

	print(total)

with open("input.txt") as file:
	firstNum = r"(?<!([0-9]|(one|two|three|four|five|six|seven|eight|nine)))([0-9]|(one|two|three|four|five|six|seven|eight|nine)){1}"
	lastNum =  r"([0-9]|(one|two|three|four|five|six|seven|eight|nine)){1}(?!([0-9]|(one|two|three|four|five|six|seven|eight|nine)))"
	numdict = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
	total = 0

	for line in file:
		i = re.search(firstNum, line).group(3)
		j = re.search(lastNum, line, flags=re.REVERSE).group(1)

		try:
			int(i)
		except ValueError:
			i = numdict[i]

		try:
			int(j)
		except ValueError:
			j = numdict[j]

		value = int(i + j)
		total += value

	print(total)
 
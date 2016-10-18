#!/usr/bin/env python3

import time

def main():
	buf = []
	start = time.clock()
	for i in range(100000000):
		buf.append(i)
	end = time.clock()
	print(end - start)

if __name__ == '__main__':
	main()

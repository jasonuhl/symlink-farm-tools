#!/usr/bin/env python

import os

def medium_host(medium):
	idx = medium.find(':')
	if idx == -1:
		return False
	return medium[:idx]

def medium_path(medium):
	idx = medium.find(':')
	if idx == -1:
		return medium
	return medium[idx+1:]

def spawn(cmd):
	print cmd
	os.system(cmd)

def do_local_rsync(left, right):
	spawn('rsync -av --delete '+left+'/ '+right)

def do_remote_rsync(host, left, right):
	spawn('ssh '+host+' rsync -av --delete '+left+'/ '+right)

def rsync(left, right):
	lhost, rhost = map(medium_host, (left, right))
	if lhost and rhost:
		left = medium_path(left)
		if lhost == rhost:
			right = medium_path(right)
		do_remote_rsync(lhost, left, right)
	else:
		do_local_rsync(left, right)

def main():
	for line in file('mediatab'):
		left, right = line.split()
		rsync(left, right)

if __name__ == '__main__':
	main()

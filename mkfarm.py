#!/usr/bin/env python

import os

media = {}

def assimilate_object(root, m, x):
	if not root.has_key(x):
		root[x] = os.path.join(m, x)
		return

	newm = os.path.join(m, x)
	if not isinstance(root[x], dict):
		oldm = root[x]
		root[x] = {}
		assimilate_medium(root[x], oldm)
	assimilate_medium(root[x], newm)


def assimilate_medium(root, m):
	for x in os.listdir(m):
		assimilate_object(root, m, x)

def excrete_farm(root):
	for x in root:
		if isinstance(root[x], dict):
			os.mkdir(x)
			os.chdir(x)
			excrete_farm(root[x])
			os.chdir('..')
		else:
			os.symlink(root[x], x)

def sshfsify(s):
	i = s.find(':')
	if i == -1:
		return s
	return os.getenv('HOME') + '/mnt/' + s[:i] + s[i+1:]

def main():
	for line in file('mediatab'):
		m = sshfsify(line.split()[0])
		assimilate_medium(media, m)
	os.mkdir('farm')
	os.chdir('farm')
	excrete_farm(media)

if __name__ == '__main__':
	main()

# -*- coding: utf-8 -*-
from sys import modules
from importlib.machinery import (
	SourceFileLoader,
	SourcelessFileLoader,
)
from os.path import isdir

__all__ = (
	'ImportModulePath'
)

def ImportModule(name, path):
	mo = SourceFileLoader(
		name, 
		'{}/__init__.py'.format(path) if isdir(path) else path
	).load_module()
	modules[name] = mo
	return

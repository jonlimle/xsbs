from ConfigParser import ConfigParser
import os, sys

plugins = []
paths = [os.curdir]
config_filename = 'plugin.conf'

class Plugin:
	def __init__(self, path, config_path):
		conf = ConfigParser()
		conf.read(config_path)
		self.initmodule = conf.get('Plugin', 'module')
		if conf.has_option('Plugin', 'enable'):
			self.isenabled = 'yes' == conf.get('Plugin', 'enable')
		else:
			self.isenabled = False
		if self.initmodule and self.isenabled:
			__import__(os.path.basename(path) + '.' + self.initmodule)

def loadPlugins():
	del plugins[:]
	print 'Loading plugins...'
	for path in paths:
		files = os.listdir(path)
		for file in files:
			dirpath = path + '/' + file
			config_path = dirpath + '/' + config_filename
			if os.path.isdir(dirpath) and os.path.exists(config_path):
				plugins.append(Plugin(dirpath, config_path))


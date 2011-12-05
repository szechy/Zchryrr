from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm

env.hosts = ['10.0.1.23']

zchryrr_directory = "/Users/zachorr/Developer/Python/zchryrr/"

def test_local():
	with settings(warn_only=True):
		local("cd " + zchryrr_directory)
		result_local = local("python zchryrr.py --test", capture=True)
		if result.failed:
			abort("Local testing failed!")

def test_remote():
	sudo(local("scp -r " + zchryrr_directory + " zachorr@" + env.hosts[0] + ":/home/zachorr"))
	#run("cd /home/zachorr/zchryrr/")
	#result = run("python zchryrr.py --test", capture=True)
	#if result.failed:
	#	abort("Local testing failed!")
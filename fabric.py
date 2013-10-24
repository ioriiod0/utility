from fabric.api import env,run,cd
from fabric.operations import put

env.hosts = ["10.0.2.%d" % i for i in range(5,225) ]
env.password = "Dev@Thinputer"
env.user = "root"
env.warn_only = True

def upload():
        put('/home/thin/thinclient-edu-2.1-20131024.i686.rpm','/home/thin')


def update():
        remote_dir = '/home/thin'
        with cd(remote_dir):
                run('rpm -Uvh *.rpm')

def upload_and_update():
        upload()
        update()

def info():
        run('rpm -qi thinclient')
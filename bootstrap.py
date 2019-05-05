#!/usr/bin/python3
"""
For running inside of chromebook debian which starts with python
"""
import subprocess
import os
import collections
import sys

packages = [
    { "package" : 'emacs-nox', "filename": "/usr/bin/emacs"    },
    { "package" : 'apt-utils', "filename": "/usr/bin/apt-extracttemplates"    },
    { "package" : 'ansible', "filename": "/usr/bin/ansible"    },
    { "package" : 'packer', "filename": "/usr/bin/packer"    },
    { "package" : 'golang-go', "filename": "/usr/bin/go"    },
    
]

pkgs =  [
        'libtruffle-java',
        'python3-pip',
]

pkgs.extend("""strace lsof mlocate""".split(" "))

for pkg in pkgs:
    packages.append({
        'package': pkg,
        'filename' : '/fsd/fsdfsd'
    })
    
go_packages = [
    
]
Package = collections.namedtuple("Package",'package filename')

def run(cmd):
    with open('var/log/boostrap.log', 'wb') as f:
        print("execute", *cmd)
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        for line in iter(process.stdout.readline, b''):
            print(str(line))
            #sys.stdout.write(str(line))
            f.write(line)

run("dpkg --configure -a".split(" "))

for x in (Package(**x) for x in packages):
    if not os.path.exists(x.filename):
        print ("package", x.package)
        cmd = ['apt','install',"-y", x.package]
        run(cmd)

        run(['dpkg', '-L', x.package])

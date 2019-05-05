import subprocess

conf = { 'user.email' : "jmikedupont2@gmail.com",
         'user.name' : "James Michael DuPont",
}
for k in conf:
  cmd = ["git", "config", "--global", k, k[v], ]
  subprocess.call(cmd, shell=True)
  

import sys
import subprocess

# getting the second arg from sys.arg since 1st arg is the name of file!
commit_msg = f'git commit -m "{list(sys.argv)[1]}"'

lst = ["git add .", commit_msg, "git push"]

for i in lst:
    print('ran:', i)
    subprocess.run(f"{i}")

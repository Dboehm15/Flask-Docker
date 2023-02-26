import os
import sys
from test.testEnv import runDocker
from test.testEnv import killDocker

try:
    if sys.argv[1] == "start":
        runDocker()
    elif sys.argv[1] == "stop":
        killDocker()
    elif sys.argv[1] == "ps":
        bashCommand = 'docker ps'
        os.system(bashCommand)
    else:
        print("Acceptable arguments are start, stop, and ps.")
        print('"start" will boot up the app in a container.')
        print('"stop" will kill the container.')
        print('"ps" Runs docker ps.')
except Exception as e:
    if str(e) == "list index out of range":
        print("You didn't run the script with an argument.")
        print("Acceptable arguments are start, stop, and ps.")
        print('"start" will boot up the app in a container.')
        print('"stop" will kill the container.')
        print('"ps" Runs docker ps.')
    else:
        print(e)

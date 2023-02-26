import os
import time


def runDocker():
    bashCommand1 = 'docker build -t python-val .'
    os.system(bashCommand1)
    bashCommand2 = 'docker run --name python-val -d -p 80:80 python-val'
    os.system(bashCommand2)
    time.sleep(1.0)


def killDocker():
    bashCommand1 = 'docker kill python-val'
    os.system(bashCommand1)
    bashCommand2 = 'docker rm python-val'
    os.system(bashCommand2)


# TODO right now this only returns something if the test fails. Make it return true/false and then create an html
#  page with a report of pass/fail tests
def checkResult(test, result):
    if result:
        return result
    else:
        print(test)

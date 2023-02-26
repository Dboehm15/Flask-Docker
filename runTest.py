from test.docker import dockerTest
from test.testEnv import *

# Run the app in a container
runDocker()

# Run the tests
try:
    checkResult("Docker build works", dockerTest())
except Exception as e:
    print(e)

# kill and delete the container
killDocker()

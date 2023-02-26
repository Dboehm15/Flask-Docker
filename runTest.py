from test.docker import dockerTest
from test.testEnv import *
from test.blizzard import *

# Run the app in a container
runDocker()

# Run the tests
try:
    checkResult("Docker build works", dockerTest())
    test_getSeason()
except Exception as e:
    print(e)

# kill and delete the container
killDocker()

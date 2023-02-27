from test.docker import dockerTest
from test.testEnv import *
from test.blizzard import *

# Run the app in a container
runDocker()
fail = False

# Run the tests
try:
    dockerTest()
    test_getSeason()
except Exception as e:
    print(e)
    fail = True

# kill and delete the container
killDocker()

if not fail:
    print("Pass")

from sensor.exception import SensorException
from sensor.logger import logging

import sys
import os

def test_Exception():
    logging.info("Testing the custom exception")
    try:
        a=1/0
    except Exception as e:
        raise SensorException(e,sys)



if __name__ == "__main__":
    try:
        test_Exception()
    except Exception as e:
        print(e)

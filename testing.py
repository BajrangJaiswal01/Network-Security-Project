import sys 
import os 
from networksecurity.exception.exception import NetworkSecurityException 
from networksecurity.logging.logger import logging 


if __name__ == '__main__':
    try:
        logging.info("Testing started")

        result = 10 / 0
        print("the result will not printed",result)

    except Exception as e:
        logging.error("An error occurred")
        raise NetworkSecurityException(e, sys)
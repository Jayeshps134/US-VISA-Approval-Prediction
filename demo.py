from us_visa.logger import logging
import sys
from us_visa.exception import USvisaException

logging.info("enter try-catch block")
try:
    a=2/0
    logging.info("divisible by 0")
except Exception as e:
    #raise USvisaException(e, sys)
    logging.error(USvisaException(e, sys))
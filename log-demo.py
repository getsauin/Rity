# logging & debugging

# logging is used to track event that occur when a program is running. 
# print(), logging are two ways to track event.

# logging is a module in python
# different log level i.e. DEBUG, INFO, WARNING, ERROR, CRITICAL
# DEBUG - detailed info, useful for debuggging
# INFO - Confirmation that things has worked / or any normal information to be logged 
# WARNING - Something unexpected has happend i.e. exception
# ERROR - some problem has been encountered that prevented program to perform any intented action
# CRITICAL - something unexpected happend like program crashed


import logging

# setting log level
#logging.basicConfig(level=logging.ERROR)

# logging into a file
# logging.basicConfig(level=logging.INFO, 
#                     filename='log.txt',
#                     filemode='w')

# logging into a file with custom log formal
logging.basicConfig(level=logging.INFO,
                    filemode='w',
                    filename='log.txt',
                    format='%(asctime)s - %(levelname)s - %(message)s')

logging.critical("This is log level...")
logging.warning("This is warning log line ...")
logging.error("This is error log level ...")

logging.info("This is info log level ...")
logging.debug("This is debug log level ...")
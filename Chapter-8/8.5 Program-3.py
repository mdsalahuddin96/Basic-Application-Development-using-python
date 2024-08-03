import logging

# Create and configure logger using the basicConfig() function
logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

# Creating an object of the logging
logger = logging.getLogger()

# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

# Test messages
logger.debug("This is a harmless debug Message")
logger.info("This is just an information")
logger.warning("It is a Warning. Please make changes")
logger.error("You are trying to divide by zero")
logger.critical("Internet is down")

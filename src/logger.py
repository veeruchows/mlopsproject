import logging
import os
from datetime import datetime

# Create log file name with timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Set up logging configuration
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,  # Change to DEBUG to capture all logs
)

if __name__ == '__main__':
    logging.info('logging has started')  # This should log if everything is correct
    logging.debug('This is a debug message')  # This should now appear if level is DEBUG
    logging.warning('This is a warning message')  # Warnings should appear
    logging.error('This is an error message')  # Errors should appear

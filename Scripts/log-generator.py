#Import the library
import logging
import random
import time
import datetime
import sys

# Setting up the variables for log generation (it determine how the log will be generated)
LOG_FILE = "random_app.log"
LOG_LEVELS = [logging.INFO, logging.WARNING, logging.ERROR]
USER_IDS = [f"user_{i:04d}" for i in range(10, 20)]
ACTIONS = ["login", "logout", "view_page", "purchase","data_fetch"]
INTERVAL_SECONDS = 0.5 

# Configure the logger
logging.basicConfig(
    filename=LOG_FILE,
    filemode='a', 
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

def generate_random_log():
    """Generates and writes a single random log entry."""
    #Choosing Random value for user_id, action, and status
    user_id = random.choice(USER_IDS)
    action = random.choice(ACTIONS)
    status = random.choice(["success", "failure", "delayed"])
    
    # Determine the log level based on the status
    if status == "failure":
        level = logging.ERROR
    elif status == "delayed":
        level = logging.WARNING
    else:
        level = logging.INFO
        
    #the log message format
    message = f"user_id={user_id}-Action={action}-status={status}"
    
    # Write the log message
    logger.log(level, message)

def main():
    print(f"--- Starting random log generation to {LOG_FILE} ---")
    print("Press Ctrl+C to stop.")
    
    try:
       #Generate the log for the amount that be determined (it can be any number)
       for _ in range(100):
            generate_random_log()
            time.sleep(INTERVAL_SECONDS)
    #because it run in terminal so if the user want to stop the log generation they can press Ctrl+C and it will stop the log generation
    except KeyboardInterrupt:
        print("\n--- Log generation stopped ---")

if __name__ == "__main__":
    main()




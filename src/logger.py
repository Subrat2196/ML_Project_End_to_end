import logging 
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


'''
Let's go through the provided code step by step to understand what it does, particularly focusing on setting up logging in Python.

1. Importing Required Modules

import logging
import os
from datetime import datetime

logging: This module is used to track events that happen when some software runs. Logging is important for tracking issues, debugging,
and monitoring the behavior of an application.
os: This module provides a way of using operating system-dependent functionality like reading or writing to the file system.
datetime: This module supplies classes for manipulating dates and times. Here, it's used to generate a timestamp for the log file name.

2. Creating the Log File Name

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

Purpose: This line creates a string representing the log file name.
datetime.now().strftime('%m_%d_%Y_%H_%M_%S'): This part of the code generates a string with the current date and time, 
formatted as month_day_year_hour_minute_second. Example output: 08_26_2024_15_30_45.
Result: The log file name will be something like 08_26_2024_15_30_45.log, ensuring that each log file is uniquely named based on 
the timestamp when it was created.

3. Creating the Log Directory Path

logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

Purpose: This line creates the full path for where the log file will be stored.
os.getcwd(): This function returns the current working directory (the directory where the script is being executed).
os.path.join: This function is used to construct a full path by joining parts of the path together. Here, it's joining the current 
working directory (os.getcwd()), the logs directory, and the log file name.
Result: The full path might look something like /path/to/your/project/logs/08_26_2024_15_30_45.log.

4. Creating the Log Directory

os.makedirs(logs_path, exist_ok=True)

Purpose: This line creates the logs directory (and any necessary parent directories) if it does not already exist.
os.makedirs: This function is used to create directories recursively. If the directory already exists, it does nothing.
exist_ok=True: This parameter prevents an error from being raised if the directory already exists.

5. Setting the Log File Path

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

Purpose: This line just reaffirms the path to the log file by joining the logs_path and the LOG_FILE name.
Result: LOG_FILE_PATH will store the full path where the log file will be saved, 
although this is somewhat redundant as logs_path already includes the file name.]

6. Configuring the Logging System

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

Purpose: This block sets up the logging configuration, specifying how and where logs should be written.

Parameters:

filename=LOG_FILE_PATH: Specifies the file where logs will be written. This is the path we constructed earlier.
format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s":
%(asctime)s: Inserts the timestamp of when the log entry was created.
%(lineno)d: Inserts the line number in the source code where the log entry was created.
%(name)s: Inserts the name of the logger that created the log entry.
%(levelname)s: Inserts the severity level of the log entry (e.g., INFO, ERROR).
%(message)s: Inserts the actual log message.
level=logging.INFO: Sets the logging level to INFO, meaning that only messages at this level or higher (e.g., WARNING, ERROR, CRITICAL) will be logged.
Flow Summary:
Log File Creation:

A unique log file name is generated based on the current date and time.
A directory named logs is created in the current working directory, if it doesn't already exist.
Logging Configuration:

The logging system is configured to write log messages to the generated log file.
The log messages will include detailed information, such as the time of logging, the line number in the source code, the logger's name, the severity level, and the actual log message.
Usage:
Once this setup is complete, throughout your code, you can add logging statements like:

logging.info("This is an info message")
logging.error("This is an error message")
These messages will be saved to the log file in the logs directory, helping you track the behavior of your application over time.

The if __name__ == "__main__": Part

Purpose: This line checks if you're running the Python file directly. If you are, then it will run the code inside this block.

When does it run?

If you run the file directly: For example, if you run python myfile.py, the code inside this block will run.
If you import the file into another file: For example, import myfile, the code inside this block won't run.
The logging.info("logging has started") Part
Purpose: This line simply adds a message saying "logging has started" to your log file. This helps you track when your program
starts running.
Why is this useful?
Control: It lets you write code that only runs when you directly execute the file, and doesn't run if the file is used somewhere
 else as a module.
Logging: It helps you keep a record of important events in your program, like when it starts.
In summary:
When you run your Python file directly, this setup logs a message saying your program has started. If someone else uses your code 
by importing it, that logging message won't run automatically.

'''
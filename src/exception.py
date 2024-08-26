import sys   # sys library provides various functions and variables that are used to manipulate different parts of the python runtime env.
def error_message_detail(error,error_detail:sys):   #whenever any exception is raised , this custom exception is invoked,error onject is first parameter , error detail is the second parameter that we will get from sys
    _,_,exc_tb=error_detail.exc_info() # exc_info() gives tuple of 3 values(Type of exception,value of exception and traceback object exc_tb)
    file_name=exc_tb.tb_frame.f_code.co_filename # exc_tb(trace_back object) contains info about stack frames , here inside stack frames from the code areas we are collecting file name
    error_message="Error occured in python script name [{0}] line number [{1} error message[{2}]]".format(file_name,exc_tb.tb_lineno,str(error))
    return error_message
    '''
    Flow of the error_message_detail Function:
    Purpose: This function is designed to create a detailed error message that includes the name of the script, 
    the line number where the error occurred, and the error message itself.

    Parameters:

    error: This is the exception object that was raised. It contains information about the specific error.
    error_detail: This is typically the sys module, which is used to retrieve detailed error information.
    error_detail.exc_info():
    This function returns a tuple containing three elements:
    The type of exception.
    The exception value (the error message).
    The traceback object (exc_tb), which contains information about the call stack at the point where the exception occurred.
    The function only stores the third element (exc_tb) because the file name and line number of the error can be extracted from it.
    '''

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super.__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message
    
    '''
    Flow of the CustomException Class:
    Purpose: This class extends Python's built-in Exception class to create a custom exception that provides more detailed error messages.
    The custom exception captures additional details about the error, such as the specific location (file name and line number) 
    where it occurred.

    __init__ Method:
    Parameters:
    error_message: This is the error message that will be passed to the base Exception class.
    error_detail: This is the sys module passed to the error_message_detail function to extract detailed information about the exception.
    
    Calling the Parent Class Constructor:
    super().__init__(error_message)
    This line calls the constructor of the Exception class with the error_message. This ensures that the custom exception 
    still behaves like a standard Python exception.

    Storing the Detailed Error Message:
    self.error_message = error_message_detail(error_message, error_detail=error_detail)
    This line calls the error_message_detail function to generate the detailed error message (including the file name and line number)
    and stores it in the self.error_message attribute.
    '''
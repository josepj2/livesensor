import sys
import os


def error_message_detail(error, error_detail:sys)-> str:
    _,_,exc_tb = sys.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename  
    error_message = "Error occured in the python script name [{0}]" \
    "on line number [{1}] error message [{2}]".format(filename, exc_tb.tb_lineno, str(error))
    return error_message

class SensorException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)

        self.error_message_detail = error_message_detail(error_message, error_detail=error_detail)                                                  
    def __str__(self):
        return self.error_message_detail
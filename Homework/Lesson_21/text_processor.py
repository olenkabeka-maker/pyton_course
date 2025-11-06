# Task_3 
"""Create a simple function, which performs any logic of your choice with text data, which it obtains from a file object, 
passed to this function. Create a test case for this function using pytest library. Create pytest fixture, which uses your 
implementation of the context manager to return a file object, which could be used inside your function"""

def process_text(file_obj):                        # ф-ія, яка читає текст із файла, рахує кільк. слів, повертає кільк. слів у ньому
    text = file_obj.read()
    words = text.split()
    return len(words)
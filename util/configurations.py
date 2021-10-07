import configparser
from pathlib import Path
import os

#https://stackoverflow.com/questions/56739921/python-not-able-to-read-properties-from-property-file
# using classes
class Configurations:
    """
    [use the constructor to start reading the file]
    """
    def __init__(self):
        self.config = configparser.ConfigParser()
        file_path = 'C:/Users/qtvo9/PycharmProjects/PythonSeleniumFramework/util/config.ini'
        print('configuration ini file path ' + file_path)
        self.config.read(file_path)

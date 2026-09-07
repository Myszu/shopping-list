import socket
from configparser import ConfigParser, ExtendedInterpolation, NoSectionError
cfg = ConfigParser(interpolation=ExtendedInterpolation(), allow_no_value=True)

from modules.initializer import config_file

config_file()
    
DEBUGGING_SOCKET = socket.gethostname()
DEBUGGING_PORT = 8080

import socket
from configparser import ConfigParser, ExtendedInterpolation, NoSectionError
cfg = ConfigParser(interpolation=ExtendedInterpolation(), allow_no_value=True)

cfg.read("./modules/config.cfg")

try:
    DEBUGGING = cfg.getboolean("Main", "debugging")
except NoSectionError:
    print("No config file found. Creating one.")
    debug = input("Do you want this to be a protyping session? (y/N)")
    debug = True if debug in ('y', 'Y') else False
    with open("./modules/config.cfg", "w", encoding="utf-8") as file:
        template = f"""[Main]
debugging = {debug}
"""
        file.write(template)
    cfg.read("./modules/config.cfg")
    DEBUGGING = cfg.getboolean("Main", "debugging")
    
DEBUGGING_SOCKET = socket.gethostname()
DEBUGGING_PORT = 8080
SSL_CERT = None
SSL_KEY = None
PORT = 80 if not SSL_CERT else 443

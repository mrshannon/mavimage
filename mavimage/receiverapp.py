
'''
ReceiverApp class to be inherited by App class
Attributes:
    mavlink:MavLinkConnection
    developer:Developer
    logger:Logger
'''

class ReceiverApp:

    def __init__(self, mavlink, developer, logger):
        # mavlink:MavLinkConnection, developer:Developer, logger:Logger
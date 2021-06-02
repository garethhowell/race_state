"""Factory class to create the appropriate race"""

import logging

from race_state.wec_race import WECRace

class RaceFactory:
    """Factory class to create the appropriate race"""


    def __init__(self):

        self.log = logging.getLogger("race_state")
        self.log.debug("Entering RaceFactory")

    def create(self, race_type):
        """Instantiate the appropriate race 
            depending on supplied race_type argument"""

        self.log.debug("Creating race of type %s", race_type)
        return globals()[race_type]()

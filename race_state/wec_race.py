"""WECRace Class."""

import json
import logging

import requests

from .race import Race

class WECRace(Race):
    """Class that will get the state of the currently-running WEC race."""


    def __init__(self) -> None:
        self.log =logging.getLogger("race_state")
        self.raceURL = "https://storage.googleapis.com/fiawec-prod/assets/live/WEC/__data.json"

    def fetchState(self, currentState: str) -> str:
        """Fetch the latest race data from `raceURL`
        convert to our required form and return the state"""

        # Mapping of WEC_specific race states to the vocabulary 
        # recognised by Home Assistant
        raceStates = {
            "ns": "Not Started",
            "green": "Green Flag",
            "yellow": "Yellow Flag",
            "full-yellow": "FCY",
            "safety-car": "Safety Car",
            "red": "Red Flag",
            "Chk": "Checkered"
        }
        self.log.debug("raceStates = %s", raceStates)

        # Fetch json data stream from WEC timing site
        response = requests.get(url=self.raceURL,timeout=5)

        # Only process if we get a good return
        if response.status_code == 200 or response.status_code == 201:
            data = json.loads(response.text)
            wecRaceState = data['params']['racestate']
            self.log.debug("wecRaceState = %s", wecRaceState)

            raceState = raceStates[wecRaceState]
            self.log.debug("raceState = %s", raceState)
            return raceState
        # Otherwise, just send back the current state.
        else:
            return currentState




"""WEC Race."""

# Standard libraries
import io, os, sys, glob, time
import logging
import requests
import json



class WECRace():
    """Class that will get the state of the currently-running WEC race
    and use the returned state to update a `select` switch 
    in the defined instance of Home Assistant.
    """
    
    # The url from which we can get the live timing data


    def __init__(self) -> None:
        
        self.log = logging.getLogger("race-state")
        self.raceURL = "https://storage.googleapis.com/fiawec-prod/assets/live/WEC/__data.json"

    def fetchState(self, currentState) -> str:
        """Fetch the latest race data from `raceURL`
        convert to our required form and return the state"""

        # Mapping of WEC_specific race states to the vocabulary 
        #  recognised by Home Assistant
        raceStates = {
            "green": "Green Flag",
            "yellow": "Yellow Flag",
            "full-yellow": "FCY",
            "safety-car": "Safety Car",
            "red": "Red Flag",
            "Chk": "Checkered"
        }

        self.log.debug("raceStates = %s", raceStates)

        # Fetch json data stream from WEC timing site
        response = requests.get(
                                url=self.raceURL,
                                timeout=5)

        # Only process if we get a good return
        if response.status_code == 200 or response.status_code == 201:
            data = json.loads(response.text)
            wecRaceState = data['params']['racestate']
            self.log.debug("wecRaceState = %s", wecRaceState)
        
            raceState = raceStates[wecRaceState]
            self.log.debug("raceState = %s", raceState)
            return raceState
        else:
            return currentState




"""Main module."""
# Standard libraries
import io, os, sys, glob, time
import logging

class WECRaceState():
    """Class that will get the state of the currently-running WEC race
    and use the returned state to update a `select` switch 
    in the defined instance of Home Assistant.
    """

    def __init__(self, raceURL, hassioIP, hassioUsername, hassioPassword, hassioSelect) -> None:
        
        self.raceURL = raceURL
        self.hassioIP = hassioIP
        self.hassioUsername = hassioUsername
        self.hassioPassword = hassioPassword
        self.hassioSelect = hassioSelect

    def fetchRaceState() -> state:
        """Fetch the latest race data from `raceURL` and convert to our required form"""
        pass

    def updateHassio(newState):
        """Update the pre-defined HA `select`"""
        pass

def main(raceURL, hassioIP, hassioUsername, hassioPassword, hassioSelect):
    currentState = "Not Started"
    race = WECRaceState(raceURL, hassioIP, hassioUsername, hassioPassword, hassioSelect)
    while currentState != "Checkered":
        tmpState = race.fetchRaceState()
        if tmpState != currentState:
            race.updateHassio(tmpState)
            currentState = tmpState
        sleep(10)
    


    while 




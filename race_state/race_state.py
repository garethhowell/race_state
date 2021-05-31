"""Main module."""
# Standard libraries
import io, os, sys, glob, time
import logging

class WECRace():
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

    def fetchState() -> str:
        """Fetch the latest race data from `raceURL`
        convert to our required form and return the state"""
        pass

    def updateHassio(newState):
        """Update the pre-defined HA `select`"""
        pass

def main(raceURL, hassioIP, hassioUsername, hassioPassword, hassioSelect):
    currentState = "Not Started"
    race = WECRace(raceURL, hassioIP, hassioUsername, hassioPassword, hassioSelect)
    while (currentState != "Checkered"):
        tmpState = race.fetchState()
        if tmpState != currentState:
            race.updateHassio(tmpState)
            currentState = tmpState
        sleep(10)




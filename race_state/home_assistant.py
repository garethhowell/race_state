# Standard libraries
import io, os, sys, glob, time
import logging

import requests

class Auth():
    """Interface to Home Assistant"""

    def __init__(self, host: str, accessToken: str):
        self.host = host
        self.accessToken = accessToken
        self.log = logging.getLogger("race-state")

    def updateEntity(self, entity, newState) -> requests.Response:
        """Update an entity in HA"""
        
        return requests.request(
            "put", 
            f"{self.host}/{entity}", 
            newState, 
            headers={}, 
            timeout=5
        )
        

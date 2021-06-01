"""HAAuth Class."""

import logging

import requests


class HAAuth:
    """Class to create authenticated requests to Home Assistant."""

    def __init__(self, host: str, accessToken: str, entity: str):
        """Initialise the authentication object."""

        self.path = f"{host}/api/services/input_select/select_option"
        self.entity = entity
        self.log = logging.getLogger("race_state")
        self.log.debug("self.path = %s", self.path)
        self.accessToken = accessToken

    def update(self, update: str) -> requests.Response:
        """Update the Home Assistant entity"""
        
        #Insert the access token into the request header.
        headers = {}
        headers["Authorization"] = f"Bearer {self.accessToken}"
        self.log.debug("Headers = %s", headers)

        #Set up the request's payload
        payload = {}
        payload['entity_id'] = self.entity
        payload['option'] = update
        self.log.debug("JSON payload = %s", payload)
        
        return requests.post(
            url=self.path, json=payload, headers=headers
        )        

"""Console script for race_state."""

import argparse
import logging
import logging.config
import sys
import time

from race_state import HAAuth, WECRace

def main():
    """Console script for race_state."""

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--host', help='The IP address (or DNS name) of the Home Assistant instance', default='')
    parser.add_argument('-a', '--access_token', help='The required access token', default='')
    parser.add_argument('-e', '--entity', help='The path to the entity to update', default='')
    parser.add_argument('-d', '--debug', help='The degree of debug logging you wish for', default='warn')
    args = parser.parse_args()

     # Initialise logging.
    logging.basicConfig(level = {'info':logging.INFO, 'debug':logging.DEBUG}[args.debug])
    log = logging.getLogger("race_state")
    log.setLevel({'error': logging.ERROR, 'warning': logging.WARNING, 'info':logging.INFO, 'debug':logging.DEBUG}[args.debug])
    
    log.debug(args)

    log.info("race_state started")
    
    # Initialisation.
    currentState = "Not Started"
    race = WECRace()
    ha = HAAuth(args.host, args.access_token, args.entity)
    ha.update("Not Started")
    
    #Check the race state every 10s and update Home Assistant if it has changed.
    while currentState != "Checkered":
        tmpState = race.fetchState(currentState)
        log.debug("Returned tmpState = %s", tmpState)
        if tmpState != currentState:
            #Update Home Assistant entity.
            update = { "select_option": tmpState }
            resp = ha.update(tmpState)
            #Check if the update succeeded.
            if resp.status_code == 200 or resp.status_code == 201:
                #If so, update current state.
                currentState = tmpState
            else:
                #Otherwise ignore, we'll try again the next time around.
                log.warning("Updating of Home Assistant failed with response code %i", resp.status_code)
        time.sleep(10)
    log.info("The race is over - exiting")
    return 0
    


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover

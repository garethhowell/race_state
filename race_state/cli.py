"""Console script for race_state."""

import argparse
import logging
import logging.config
from race_state.race_factory import RaceFactory
import sys
import time

from race_state.ha_auth import HAAuth

def main():
    """Console script for race_state."""

    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--race', choices=['WEC'],
                        help='The type of race you want to follow', default='WEC')
    parser.add_argument('-i', '--host',
                        help='The IP address (or DNS name) of the Home Assistant instance',
                        required=True)
    parser.add_argument('-a', '--access_token', help='The required access token',
                        required=True)
    parser.add_argument('-e', '--entity', help='The path to the entity to update',
                        required=True)
    parser.add_argument('-d', '--debug',
                        choices=['warning', 'debug', 'info', 'error', 'critical'], 
                        help='The degree of debug logging you wish for',
                        default='info')
    args = parser.parse_args()

     # Initialise logging.
    logging.basicConfig(level={'info': logging.INFO, 'warning': logging.WARNING, 
                            'error': logging.ERROR, 'critical':logging.CRITICAL,
                            'debug': logging.DEBUG}[args.debug])
    log = logging.getLogger("race_state")
    log.setLevel({'error': logging.ERROR, 'warning': logging.WARNING,
                    'info': logging.INFO, 'debug': logging.DEBUG}[args.debug])

    log.debug(args)

    log.info("race_state started")

    # Initialisation.
    race_types = {'WEC': 'WECRace'}
    currentState = "Not Started"

    # Instantiate the correct race_type
    log.debug("race = %s", args.race)
    race_type = race_types[args.race]
    log.debug("race_type = %s", race_type)
    raceObj = RaceFactory()
    race = raceObj.create(race_type)

    ha = HAAuth(args.host, args.access_token, args.entity)
    ha.update("Not Started")

    # Check the race state every 10s and update Home Assistant if it has changed.
    while currentState != "Checkered":
        tmpState = race.fetchState(currentState)
        log.debug("Returned tmpState = %s", tmpState)
        if tmpState != currentState:
            log.info("Race State changed from %s to %s.",
                    currentState, tmpState)
            # Update Home Assistant entity.

            resp = ha.update(tmpState)
            # Check if the update succeeded.
            if resp.status_code == 200 or resp.status_code == 201:
                # If so, update current state.
                currentState = tmpState
            else:
                # Otherwise ignore, we'll try again the next time around.
                log.warning(
                    "Updating of Home Assistant failed with response code %i",
                    resp.status_code)
        time.sleep(1)
    log.info("The race is over (was it good?) - exiting")
    return 0

if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover

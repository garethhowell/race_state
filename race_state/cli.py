"""Console script for race_state."""
import argparse
import sys
import time
import logging, logging.config

from race_state import WECRace, Auth


def main():
    """Console script for race_state."""
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--host', help='The IP address of the Home Assistant instance', default='')
    parser.add_argument('-a', '--access_token', help='The required access token', default='')
    parser.add_argument('-e', '--entity', help='The path to the entity to update', default='')
    parser.add_argument('-d', '--debug', help='The degree of debug loggin you wish for', default='info')
    parser.add_argument('_', nargs='*')
    args = parser.parse_args()


    # Initialise logging
    logging.basicConfig(level = {'info':logging.INFO, 'debug':logging.DEBUG}[args.debug])
    log = logging.getLogger("race_state")
    log.setLevel({'info':logging.INFO, 'debug':logging.DEBUG}[args.debug])
    log.info("race_state started")
    log.debug(args)

    currentState = "Not Started"

    race = WECRace()

    ha = Auth(args.host, args.access_token)
    
    while currentState != "Checkered":
        tmpState = race.fetchState(currentState)
        log.debug("returned tmpState = %s", tmpState)
        if tmpState != currentState:
            resp = ha.updateEntity(args.entity, tmpState)
            if resp.status_code == 200 or 201:
                currentState = tmpState
            else:
                log.warn("Updating of Home Assistant failed with response code %i", resp.status_code)
        time.sleep(1)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover

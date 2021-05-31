"""Console script for race_state."""
import argparse
import sys
import logging, logging.config

from .race_state import WECRace


def main():
    """Console script for race_state."""
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--race_URL', help='The URL from where we can fetch race data', default='')
    parser.add_argument('-i', '--hassio_ip', help='The IP address of the Home Assistant instance', default='')
    parser.add_argument('-u', '--username', help='The username to access HA', default='')
    parser.add_argument('-p', '--password', help='The user\'s password', default='')
    parser.add_argument('-s', '--select', help='The name of entity to update', default='')
    parser.add_argument('-d', '--debug', help='The degree of debug loggin you wish for', default='info')
    parser.add_argument('_', nargs='*')
    args = parser.parse_args()


    # Initialise logging
    logging.basicConfig(level = {'info':logging.INFO, 'debug':logging.DEBUG}[args.debug])
    log = logging.getLogger("race_state")
    log.setLevel({'info':logging.INFO, 'debug':logging.DEBUG}[args.debug])
    log.info("race_state started")
    log.debug(args)

    raceURL = args.race_URL
    hassioIP = args.hassio_ip
    hassioUsername = args.username
    hassioPassword = args.password
    hassioSelect = args.select

    currentState = "Not Started"

    race = WECRace(raceURL, hassioIP, hassioUsername, hassioPassword, hassioSelect)
    
    while currentState != "Checkered":
        tmpState = race.fetchRaceState()
        if tmpState != currentState:
            race.updateHassio(tmpState)
            currentState = tmpState
        sleep(10)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover

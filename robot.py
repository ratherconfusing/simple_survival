#!/usr/bin/env python
"""File: robot.py"""

import time
import logging

class Robot():
    def __init__(self, name='Karel'):
        # Logging
        logging.basicConfig()
        self.logger = logging.getLogger(name)

        # Robot variables
        self.name = name
        self.logger.setLevel(logging.DEBUG)
        self.battery_level = 100
        self.state = 0

    def run(self, time_step=1):
        while True:
            time.sleep(time_step)

            # Deplete battery a bit
            self.battery_level -= 5
            if self.battery_level < 0:
                self.battery_level = 0

            self.logger.info(f'Time has progressed... Robot {self.name} has battery level {self.battery_level}..')

            # Check battery depletion
            if self.battery_level == 0:
                self.logger.error(f'Robot {self.name} has ran out of juice! Game over!')
                break

if __name__=='__main__':
    robot = Robot()
    robot.run()

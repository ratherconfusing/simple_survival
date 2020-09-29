#!/usr/bin/env python
"""File: robot.py"""

import time
import random
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
        self.age = 0

    def run(self, time_step=1, charge_chance_threshold=0.5):
        """ Runs the robot until battery is depleted
        Robot has a chance to charge the battery each step
        
        Arguments:
        time_step -- time step of the simulation
        charge_chance_threshold -- Threshold for charge <0, 1>, if chance is > this parameter, robot will charge
        """

        self.logger.info(f'Simulation has started! Robot {self.name} - battery level {self.battery_level}, age: {self.age}')

        while True:
            time.sleep(time_step)

            # Deplete battery a bit
            self.battery_level -= 5
            if self.battery_level < 0:
                self.battery_level = 0

            self.logger.info(f'Time has progressed... Robot {self.name} - battery level {self.battery_level}, age: {self.age}')

            # Check battery depletion
            if self.battery_level == 0:
                self.logger.error(f'Robot {self.name} has ran out of juice! Game over! Total lifespan: {self.age}')
                break

            # Try to survive. If charge attempt is > charge_chance_threshold, charge by 10
            charge_chance = random.random()
            if charge_chance > charge_chance_threshold:
                self.battery_level += 10
                if self.battery_level > 100:
                    self.battery_level = 100
                self.logger.info(f'Robot had luck! ({charge_chance} > {charge_chance_threshold}), luck charged battery by 10, new level: {self.battery_level}')
            else:
                self.logger.info('Robot did not have luck, no charge this time..')

            # Robot ages as he lives inside simulation
            self.age += 1


if __name__=='__main__':
    robot = Robot()
    robot.run(time_step=0.01)

# -*- coding: utf-8 -*-
import serial, serial.tools.list_ports
import subprocess
import logging
import time
import importlib
import os
import sys
import argparse
try:
    import ConfigParser as configparser
except:
    # Python 3  
    import configparser
from events import *

def alert(title, msg):
    rc = subprocess.call(["/usr/bin/notify-send", title, msg])
    return rc

class Distractinator:
    def __init__(self):
        # Parse the command line options!
        desc = "The Distractinator(TM) notifier!"
        parser = argparse.ArgumentParser(description=desc)
        parser.add_argument('--log', help='Absolute path to the desired log. (/path/to/file.log)', type=str, required=False)
        args = parser.parse_args()

        # Set up logging!
        self.log = self.createlogger(args.log)
        self.log.info('notifier started.')

        # Find and parse the config file!
        self.config = self.config_file(print_err_msg=True)
        self.default_alert = self.use_default_alert()
        
        # Find and import the custom actions file!
        try:
            # Let's go find your custom file
            self.usermodule = self.customcode()
        except IOError:
            # I could not find the file you specified :(
            log.error("I could not find the custom actions file in the location you specified. :(")
            sys.exit(2) 

        # Find and assign the correct port!
        self.p = self.autoconnect() # Won't you join me on the perennial quest?

    def createlogger(self, logfile_location=None):
        logger = logging.getLogger()

        if logfile_location is None:
            handler = logging.StreamHandler()
        else:
            handler = logging.FileHandler(logfile_location)

        formatter = logging.Formatter('[%(asctime)s] %(levelname)-8s %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.DEBUG)
        return logger

    def config_file(self, print_err_msg=False):
        config_location = os.path.join(os.path.expanduser('~'), '.distractinator.conf')
        if not os.path.exists(config_location):
            if print_err_msg:
                self.log.info('No config file found at {}.'.format(config_location))
            return None

        try:
            cfg = configparser.ConfigParser()
            cfg.read(config_location)
            return cfg
        except:
            self.log.error('Config file at {} could not be read.'.format(config_location))
            sys.exit(2)
    
    def use_default_alert(self):
        """ 
        Use the default alert unless the user specifies otherwise
        explicitly in the config file.
        """
        try:
            return self.config_file(print_err_msg=False).getboolean('notifier', 'use_default_alert_function')
        except:
            return True

    def customcode(self):
        if self.config_file(print_err_msg=False):

            try:
                path_to_custom_events = self.config_file().get('notifier', 'custom_script')
                self.log.info('Looking for custom script file at {}...'.format(path_to_custom_events))
            except configparser.NoOptionError:
                self.log.info('custom_script variable not set in config file.') 
                return False

            if os.path.exists(path_to_custom_events):
                self.log.info("SUCCESS: Found custom script file at {}.".format(path_to_custom_events))
            else:
                self.log.error("Could not find a file named {}.".format(path_to_custom_events))
                raise IOError

            containing_dir = os.path.split(path_to_custom_events)[0]
            sys.path.append(containing_dir) 
            return importlib.import_module('notifieractions')
        return False

    def identify_board(self, p):
        if p.description == 'Adafruit' and p.manufacturer == 'Flora':
            return True
        return False

    def autoconnect(self):
        self.log.info('Attempting to find + connect to USB device...')

        device_not_found = True

        while device_not_found:
            known_ports = list(serial.tools.list_ports.comports())
            for p in known_ports:
                if self.identify_board(p):
                    self.log.info('Found device at address: {}'.format(p.device))
                    device_not_found = False
            time.sleep(1)

        return serial.Serial(p.device, 9600, timeout=10)

    def get_alert_title(self):
        try:
            return self.config_file().get('notifier', 'alert_title')
        except:
            return None

    def get_alert_msg(self):
        try:
            return self.config_file().get('notifier', 'alert_msg')
        except:
            return None
    
    def alert(self, title=None, msg=None):
        if self.use_default_alert():
            if self.get_alert_title() is None:
                title = "Pay Attention!"
            if self.get_alert_msg() is None:
                msg = "Someone wants to speak with you."

            rc = alert(title, msg)
            if rc == 0:
                self.log.info('/usr/bin/notify received return code 0')
            else:
                self.log.error('/usr/bin/notify received return code {}'.format(rc))

    def run(self, port=None):
        if port is None:
            port = self.p

        while True:
            try:
                serialMsg = port.readline().strip()
            except serial.serialutil.SerialException:
                self.log.error('USB disconnected.')
                on_disconnect(usermodule=self.usermodule, log=self.log)

                port = self.autoconnect()
                on_connect(usermodule=self.usermodule, log=self.log)

                serialMsg = port.readline().strip()

            if serialMsg in ('a_recvd', b'a_recvd'): # A Button
                self.log.info('Received {} from serial.'.format(serialMsg.strip()))
                run_action_a(usermodule=self.usermodule, log=self.log)

            if serialMsg in ('b_recvd', b'b_recvd'): # B Button
                self.log.info('Received {} from serial.'.format(serialMsg.strip()))
                run_action_b(usermodule=self.usermodule, log=self.log)

            if serialMsg in ('c_recvd', b'c_recvd'): # C Button
                self.log.info('Received {} from serial.'.format(serialMsg.strip()))
                run_action_c(usermodule=self.usermodule, log=self.log)

            if serialMsg in ('d_recvd', b'd_recvd'): # D Button
                self.log.info('Received {} from serial.'.format(serialMsg.strip()))
                self.alert()
                run_action_d(usermodule=self.usermodule, log=self.log)

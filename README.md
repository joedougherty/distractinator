# DISTRACTINATOR: The customizable, open source cubicle doorbell #

## Installation ##
    pip install distractinator

OR

    git clone <this repo>
    cd distractinator
    python setup.py install


## SETUP ##
    
Config file. Not strictly necessary, but strongly encouraged.
You will need one in order to customize events.

### Specifying a logfile: ###
By default, the log messages will print to stdout. You can specify a logfile location with the --log argument.

`notify --log /path/to/notifier.log`

This is especially helpful when running as a background process, or under the supervision of a separate process.

## HOW TO RUN ##
`notify` works best when it runs any time your machine is on. Here are two strategies for running it without too much hassle on Ubuntu.
    
Add an entry to Startup Applications:

`/usr/local/bin/notify --log /path/to/notifier.log`

Run it under Supervisord

`pip install supervisor`

Example stanza for supervisord.conf:

    [program:notifier]
    command=/usr/local/bin/notify
    autostart=True
    autorestart=unexpected
    user=joe ; Replace with your user
    exitcodes=0,2
    redirect_stderr=True
    stdout_logfile=/path/to/notifier.log

## CUSTOM EVENTS ##

customevents.py
---------------
You should use one!

You'll need to get a config file set up first. After doing so, set the `custom_script` variable. 

Make sure it's the full, absolute path to your customevents.py file.


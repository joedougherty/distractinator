# DISTRACTINATOR: The customizable, open source cubicle doorbell #

## Installation ##
    pip install distractinator

**Note**: You may need to `sudo pip install` as this will attempt to write to `/usr/local/bin/`

## SETUP ##

`distractd`

You will be walked through a few steps to ensure the script can communicate with your receiver. The setup process will also copy an example config file to your home directory, at `~/.distractinator.conf`.

### If You Encounter a Permissions Issue During setup ###
The default permissions on the device may not allow for reading and writing. If the setup process asks you to check the permissions on the device, try the following:


    $ sudo usermod -aG dialout $USER
    $ newgrp dialout

After these commands have been run, call `distractd` once again.

### Specifying a logfile: ###
By default, the log messages will print to stdout. You can specify a logfile location with the --log argument.

`distractd --log /path/to/distractd.log`

This is especially helpful when running as a background process, or under the supervision of a separate process.

## HOW TO RUN ##
`distractd` works best when it runs any time your machine is on. Here are a few strategies for running it without too much hassle on Ubuntu.

### Use a systemd unit file

Any systemd unit file placed in `~/.config/systemd/user/` can be managed by with normal user privileges. For example:

```
$ cat ~/.config/systemd/user/distractd.service
[Unit]
Description=Distractinator Service Daemon

[Service]
ExecStart=/usr/bin/python %h/.local/bin/distractd

[Install]
WantedBy=default.target
```

Then to start:

```
systemctl --user start distractd.service
```

The above path to the `distractd` script in the `ExecStart` line assumes the package was installed with the `--user` flag. Update accordingly if you installed `distractinator` system-wide.

### Add an entry to Startup Applications

`/usr/local/bin/distractd --log /path/to/distractd.log`

### Run it under Supervisord

`pip install supervisor`

Example stanza for supervisord.conf:

    [program:distractd]
    command=/usr/local/bin/distractd
    autostart=True
    autorestart=unexpected
    user=joe ; Replace with your user
    exitcodes=0,2
    redirect_stderr=True
    stdout_logfile=/path/to/distractd.log

## CUSTOM EVENTS ##

customevents.py
---------------
You should use one!

This repository comes with an example **customevents.py** file. Find its path on your system with:

    distractd --example_custom_code

* Copy that file to your desired location
* Uncomment the `custom_script` variable in your config file
* Point it to the absolute path of your customevents.py file

You will need to restart `distractd` to pick up changes to customevents.py.


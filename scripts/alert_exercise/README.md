# Alerting Exercise

This little project helps us alert people when machines at specific IP addresses are unresponsive.

The `test.txt` file is a list of IP addresses being monitored.

The `test.csv` file is an address book of people responsible for each IP and their email address.

The `test.sh` file is a bash script that takes `test.txt` as standard input and echos IP addresses that are unresponsive.

The `test.py` file is a python script that takes the unresponsive IPs produced with `test.sh` and alerts the person responsible.

The `alert.sh` file is a bash script that automates the process of alerting. Calling this one command combines `test.sh` and `test.py`.

## To run:
Simply run `./alert.sh` to see output for various unresponsive IPs.

## What about emailing?
See [this neat tutorial](http://naelshiab.com/tutorial-send-email-python/) about how to use python's `smtplib` to automate emails. You can also check my [secret santa project](https://github.com/chuckinator0/Projects/tree/master/secretSanta) to see email automation in action.


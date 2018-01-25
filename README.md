# USP Agent

A Python implementation of a CoAP/STOMP USP Agent (for the USP
protocol as defined by the Broadband Forum).

# Install

First, ensure you have Python 3 and the Python package manager `pip`
installed.  If you don't have `pip` installed already, download and
run the following script to install it:

https://bootstrap.pypa.io/get-pip.py

Next, run `make` to install the required Python packages via `pip`
(you may need to run this as root or using sudo) and then run `make
database` to initialize the database files under
`database/<client-type>.db`.

# Usage

```
$ python3 -m agent.main -h
usage: main.py [-h] [-c] [--coap-port [COAP_PORT]] [--intf [INTF]]
               [-t [CLIENT_TYPE]] [--version]

optional arguments:
  -h, --help            show this help message and exit
  -c, --coap            use the CoAP Binding instead of the STOMP Binding
  --coap-port [COAP_PORT]
                        specify the CoAP Port to listen on
  --intf [INTF]         specify the network interface to use
  -t [CLIENT_TYPE], --client-type [CLIENT_TYPE]
                        specify the type of client (e.g. test, camera, motion)
  --version             show the version of this tool
```

Use the `-t <client-type>` option to specify which client type and
thus which database to use.  For example, if you specify `-t test` the
agent will use the database file `database/test.db`.  Use the `-c` or
`--coap` options to make the agent use CoAP instead of the default
STOMP.

# Advanced

Run `make database` to reinitialize the database files by copying the
stock versions `database/<client-type>-db.json` to their live versions
`database/<client-type>.db`.

Run `make schema` if you need to regenerate the Protobuf classes for
USP records/messages.  Note that regenerating the Protobuf classes
requires `protoc` be somewhere in your `PATH`.  If you don't already
have it, download and install the latest Protobuf release from:

https://github.com/google/protobuf/releases/latest

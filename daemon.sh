#!/bin/sh

CMD=start

MTP=stomp
PIDFILE=/tmp/usp-agent-python.pid
DATABASE=daemon

CONTROLLER_ID=132543
CONTROLLER_IP=6.0.0.2
CONTROLLER_PATH=/queue/132543
CONTROLLER_PORT=61613

AGENT_GW=202.254.1.1
AGENT_ID=345231
AGENT_INTERFACE=eth2
AGENT_IP=202.254.1.18
AGENT_PASSWORD=guest
AGENT_PATH=/foo/bar
AGENT_PLEN=24
AGENT_PORT=61613
AGENT_USERNAME=guest

usage()
{
    echo "usage: $name [options...] [start|stop]" 2>&1
    echo "Run a USP agent simulator.  If no command is given, defaults to 'start'." 2>&1
    echo "" 2>&1
    echo "-controller-id STR           Value to use as controller ID, defaults to $CONTROLLER_ID" 2>&1
    echo "-controller-ip IP            IPv4 or IPv6 address to use as controller IP, defaults to $CONTROLLER_IP" 2>&1
    echo "-controller-path STR         Value to use as controller path, defaults to $CONTROLLER_PATH" 2>&1
    echo "-controller-port NUM         Value to use as controller port, defaults to $CONTROLLER_PORT" 2>&1
    echo "-database STR                Value to use for the agent's database file, defaults to $DATABASE" 2>&1
    echo "-gw IP                       IPv4 or IPv6 address to use as agent's default gateway, defaults to $AGENT_GW" 2>&1
    echo "-h, -help                    Display this usage text and exit" 2>&1
    echo "-id STR                      Value to use as agent ID, defaults to $AGENT_ID" 2>&1
    echo "-interface IFNAME            Value to use as agent's interface, defaults to $AGENT_INTERFACE" 2>&1
    echo "-ip IP                       IPv4 or IPv6 address to use as agent IP, defaults to $AGENT_IP" 2>&1
    echo "-password STR                Value to use as agent's password, defaults to $AGENT_PASSWORD" 2>&1
    echo "-path STR                    Value to use as agent's path, defaults to $AGENT_PATH" 2>&1
    echo "-plen NUM                    Value to use as agent's prefix-length, defaults to $AGENT_PLEN" 2>&1
    echo "-username STR                Value to use as agent's username, defaults to $AGENT_USERNAME" 2>&1
}

while [ x$1 != x ]; do
    case "$1" in
        -controller-id)   shift; CONTROLLER_ID=$1;   shift ;;
        -controller-ip)   shift; CONTROLLER_IP=$1;   shift ;;
        -controller-path) shift; CONTROLLER_PATH=$1; shift ;;
        -controller-port) shift; CONTROLLER_PORT=$1; shift ;;
        -gw)              shift; AGENT_GW=$1;        shift ;;
        -h)               usage; exit 1 ;;
        -help)            usage; exit 1 ;;
        -id)              shift; AGENT_ID=$1;        shift ;;
        -interface)       shift; AGENT_INTERFACE=$1; shift ;;
        -ip)              shift; AGENT_IP=$1;        shift ;;
        -mtp)             shift; MTP=$1;             shift ;;
        -password)        shift; AGENT_PASSWORD=$1;  shift ;;
        -path)            shift; AGENT_PATH=$1;      shift ;;
        -pidfile)         shift; PIDFILE=$1;         shift ;;
        -plen)            shift; AGENT_PLEN=$1;      shift ;;
        -port)            shift; AGENT_PORT=$1;      shift ;;
        -username)        shift; AGENT_USERNAME=$1;  shift ;;
        *)
            if [ x$1 == xstart -o x$1 == xstop ];
            then
                CMD=$1
                break
            fi

            usage
            exit 1
            ;;
    esac
done

if [ x$CMD == xstop ];
then
    if [ -e $PIDFILE ];
    then
        pid=`cat $PIDFILE`
        if [ x$pid != x ];
        then
            echo "Killing $pid"
            kill $pid
            if [ $? -ne 0 ]; then
                exit 1
            fi
        fi
    fi
    exit
fi

cd `dirname $0`

ip addr add $AGENT_IP/$AGENT_PLEN dev $AGENT_INTERFACE
ip route add $CONTROLLER_IP via $AGENT_GW dev $AGENT_INTERFACE

trap ctrl_c INT
trap ctrl_c TERM

cleanup() {
    ip route del $CONTROLLER_IP via $AGENT_GW dev $AGENT_INTERFACE
    ip addr del $AGENT_IP/$AGENT_PLEN dev $AGENT_INTERFACE
}

ctrl_c() {
    echo "\ncontrol-c-handler called, exiting"
    cleanup
    exit
}

cp database/${DATABASE}-db.json database/${DATABASE}.db

sed -i -e "s!__CONTROLLER_ID__!$CONTROLLER_ID!g" database/${DATABASE}.db
sed -i -e "s!__CONTROLLER_IP__!$CONTROLLER_IP!g" database/${DATABASE}.db
sed -i -e "s!__CONTROLLER_PORT__!$CONTROLLER_PORT!g" database/${DATABASE}.db
sed -i -e "s!__CONTROLLER_PATH__!$CONTROLLER_PATH!g" database/${DATABASE}.db
sed -i -e "s!__AGENT_ID__!$AGENT_ID!g" database/${DATABASE}.db
sed -i -e "s!__AGENT_IP__!$AGENT_IP!g" database/${DATABASE}.db
sed -i -e "s!__AGENT_PLEN__!$AGENT_PLEN!g" database/${DATABASE}.db
sed -i -e "s!__AGENT_PORT__!$AGENT_PORT!g" database/${DATABASE}.db
sed -i -e "s!__AGENT_GW__!$AGENT_GW!g" database/${DATABASE}.db
sed -i -e "s!__AGENT_PATH__!$AGENT_PATH!g" database/${DATABASE}.db
sed -i -e "s!__AGENT_INTERFACE__!$AGENT_INTERFACE!g" database/${DATABASE}.db
sed -i -e "s!__AGENT_USERNAME__!$AGENT_USERNAME!g" database/${DATABASE}.db
sed -i -e "s!__AGENT_PASSWORD__!$AGENT_PASSWORD!g" database/${DATABASE}.db

if [ x$MTP == xstomp ];
then
    python3 -m agent.main -t $DATABASE --intf $AGENT_INTERFACE &
else
    python3 -m agent.main -t $DATABASE --intf $AGENT_INTERFACE --coap &
fi

echo $! > $PIDFILE
wait $!

echo "exiting"
cleanup

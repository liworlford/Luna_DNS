if pgrep -x "dnsmasq" > /dev/null
then
    echo "dnsmasq is running"
    python3 major.py
else
    echo "dnsmasq is not running"
    python3 d.py
    python3 major.py
fi

#!/bin/bash
if systemctl start dnsmasq 2>/dev/null; then
    echo "dnsmasq started successfully."
    python3 major.py
else
    echo "Failed to start dnsmasq. It may not be installed."
    python3 d.py
    python3 major.py
fi

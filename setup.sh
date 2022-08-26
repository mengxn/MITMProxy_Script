#!/bin/bash

# download proxy.py
curl https://raw.githubusercontent.com/mengxn/MITMProxy_Script/master/proxy.py -o ~/.mitmproxy/proxy.py -s
# download keys.yaml
curl https://raw.githubusercontent.com/mengxn/MITMProxy_Script/master/keys.yaml -o ~/.mitmproxy/keys.yaml -s

echo done
wget --no-check-certificate -O dnsmasq_sniproxy.sh https://raw.githubusercontent.com/myxuchangbin/dnsmasq_sniproxy_install/master/dnsmasq_sniproxy.sh && bash dnsmasq_sniproxy.sh -f
wget -O nf https://github.com/sjlleo/netflix-verify/releases/download/v3.1.0/nf_linux_amd64 && chmod +x nf && ./nf
curl -L -o check.sh https://raw.githubusercontent.com/WolfordLi/nfdns/main/check.sh
curl -L -o main.py https://raw.githubusercontent.com/WolfordLi/nfdns/main/main.py
curl -L -o pause.py https://raw.githubusercontent.com/WolfordLi/nfdns/main/pause.py
curl -L -o continue.py https://raw.githubusercontent.com/WolfordLi/nfdns/main/continue.py
python3 main.py

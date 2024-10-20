wget --no-check-certificate -O dnsmasq_sniproxy.sh https://raw.githubusercontent.com/myxuchangbin/dnsmasq_sniproxy_install/master/dnsmasq_sniproxy.sh && bash dnsmasq_sniproxy.sh -f
wget -O nf https://github.com/sjlleo/netflix-verify/releases/download/v3.1.0/nf_linux_amd64 && chmod +x nf && ./nf
curl -L -o check.sh https://raw.githubusercontent.com/liworlford/Luna_DNS/refs/heads/main/check.sh
curl -L -o major.py https://raw.githubusercontent.com/liworlford/Luna_DNS/refs/heads/main/major.py
curl -L -o d.sh https://raw.githubusercontent.com/liworlford/Luna_DNS/refs/heads/main/d.sh
curl -L -o d.py https://raw.githubusercontent.com/liworlford/Luna_DNS/refs/heads/main/d.py
if systemctl start dnsmasq 2>/dev/null; then
    echo "dnsmasq started successfully."
    echo "请注意 如果不是初次安装或更新 只是更改地区解锁 请运行python3 major.py节约时间"
    python3 major.py
else
    echo "Failed to start dnsmasq. It may not be installed."
    python3 d.py
    echo "dnsmasq started successfully."
    echo "更新脚本请运行bash install.sh"
    echo "更改地区请运行python3 major.py"
    python3 major.py
fi

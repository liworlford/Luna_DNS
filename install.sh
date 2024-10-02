wget --no-check-certificate -O dnsmasq_sniproxy.sh https://raw.githubusercontent.com/myxuchangbin/dnsmasq_sniproxy_install/master/dnsmasq_sniproxy.sh && bash dnsmasq_sniproxy.sh -f
wget -O nf https://github.com/sjlleo/netflix-verify/releases/download/v3.1.0/nf_linux_amd64 && chmod +x nf && ./nf
curl -L -o check.sh https://raw.githubusercontent.com/liworlford/Luna_DNS/refs/heads/main/check.sh
curl -L -o major.py https://raw.githubusercontent.com/liworlford/Luna_DNS/refs/heads/main/major.py
curl -L -o d.sh https://raw.githubusercontent.com/liworlford/Luna_DNS/refs/heads/main/d.sh

# 检查 dnsmasq 是否正在运行
if pgrep -x "dnsmasq" > /dev/null
then
    echo "dnsmasq is running"
else
    echo "dnsmasq is not running"
    bash d.sh
fi

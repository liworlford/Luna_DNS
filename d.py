import os
os.system('echo 1.1.1.1 | bash dnsmasq_sniproxy.sh -id')
os.system("rm -rf /etc/resolv.conf && echo 'nameserver 8.8.4.4'>/etc/resolv.conf")

import os
import subprocess
#调试中
import requests
import re

#0可以 1不行
#service_id的格式是region_service


def get_uuid():
    if not os.path.exists('uuid.txt'):
        uuid = input("请输入您的UUID: ")
        with open('uuid.txt', 'w') as f:
            f.write(uuid)
    else:
        with open('uuid.txt', 'r') as f:
            uuid = f.read().strip()
    return uuid

def get_region():
    print("请选择地区代码:")
    print("日本 -- JP")
    print("香港 -- HK")
    print("新加坡 -- SG")
    print("台湾 -- TW")
    print("美国 -- US")
    region = input("请输入地区代码: ")
    return region

def get_service():
    print("请选择媒体服务代码:")
    print("NF+PV+HAMI+BAHAMUT+GPT+Crunchyroll -- ALL")
    print("Netflix -- NF")
    print("PrimeVideo -- PV")
    print("HAMI -- HAMI")
    print("ChatGPT -- GPT")
    print("Crunchyroll -- CR")
    print("动画疯 -- BAHAMUT")
    service = input("请输入媒体代码: ")
    return service

def send_request(uuid, region):
    url = f"http://38.207.160.142:8080?uuid={uuid}&region={region}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get('value')
    else:
        print("请求失败:", response.json())
        return None

def change_all(ipv4_address, file_path='/etc/dnsmasq.d/custom_netflix.conf'):
    with open(file_path, 'r') as file:
        lines = file.readlines()
# 用于匹配IPv4地址的正则表达式
    ipv4_pattern = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')
    with open(file_path, 'w') as file:
        for line in lines:
            if 'address' in line:
                # 替换匹配行中的IPv4地址为新的IP地址
                line = ipv4_pattern.sub(ipv4_address, line)
            file.write(line)
    os.system('systemctl stop dnsmasq')
    os.system('systemctl start dnsmasq')

def change_proxy(services, ip, file_path='/etc/dnsmasq.d/custom_netflix.conf'):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # 用于匹配IPv4地址的正则表达式
    ipv4_pattern = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')

    # 修改文件内容
    with open(file_path, 'w') as file:
        for line in lines:
            for service in services:
                if service in line:
                    # 替换匹配行中的IPv4地址为新的IP地址
                    line = ipv4_pattern.sub(ip, line)
                    break
            file.write(line)
    os.system('systemctl stop dnsmasq')
    os.system('systemctl start dnsmasq')
    print("change_work_done")

# 调用示例
service_domain_map = {
    'ALL': ['address'],
    'NF': ['netflix.com', 'netflix.net', 'nflximg.com', 'nflximg.net', 'nflxvideo.net', 'nflxso.net', 'nflxext.com'],
    'HAMI': ['hinet.net'],
    'BAHAMUT': ['gamer.com.tw', 'bahamut.com'],
    'GPT': ['openai.com'],
    'PV': ['amazonprimevideo.cn', 'amazonprimevideo.com.cn', 'mazonprimevideos.com', 'amazonvideo.cc', 'media-amazon.com', 'prime-video.com', 'primevideo.cc', 'primevideo.com', 'primevideo.info', 'primevideo.org', 'primevideo.tv', 'pv-cdn.net'],
    'CR': ['crunchyroll.com']
}

nf_region_map = {
    "JP": "日本",
    "HK": "香港",
    "SG": "新加坡",
    "TW": "台湾",
    "US": "美国",
}
##############################################################

#必须将两个变量的赋值写在词典模块前面 不是调用前 不然报错


# 验证示例
#media_list = service_domain_map["NF"]
#dns_ip = "192.168.1.1"  # 示例IP地址
#change_proxy(media_list, dns_ip)
#check_point = service_big_test_map[service][0]

#print(check_point)
######################################3

def nf_test():
    result = os.popen("./nf")
    result = result.read()
    return result
def big_test():
    process = subprocess.Popen(
        'echo 1 | bash check.sh -M 4',
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    stdout, stderr = process.communicate()
    output = stdout
    return output

def find_in_big_test_result(checkpoint,test_result):
    if checkpoint in test_result:
        return 0
    else:
        return 1

def find_in_nf_test(nf_region):
    for _ in range(10):
        result = os.popen("./nf")
        result = result.read()
        print(result)
        if "您的出口IP完整解锁Netflix，支持非自制剧的观看" in result and f"所识别的IP地域信息：{nf_region}" in result:
            print("done")
            return 0

def together(region,service):
    return f"{region}_{service}"


def main():
    uuid = get_uuid()
    region = get_region()
    service = get_service()
    print(service)

    if service == "ALL":
        while True:
            service = 'NF'
            service_id = together(region, service)
            print(service_id)
            print("NF+PV+HAMI+BAHAMUT+GPT+Crunchyroll")
            proxy_ip = send_request(uuid, service_id)
            print("requested")
            if proxy_ip is None:
                print("Failed to get proxy IP. Exiting.")
                break

            change_all(proxy_ip)
            os.system("rm -rf /etc/resolv.conf && echo 'nameserver 127.0.0.1'>/etc/resolv.conf")
            nf_region = nf_region_map.get(region, 'luna')
            result = find_in_nf_test(nf_region)
            if result == 0:
                break
    if service == "NF":
        while True:
            service = 'NF'
            service_id = together(region, service)
            print(service_id)
            print("NF+PV+HAMI+BAHAMUT+GPT+Crunchyroll")
            proxy_ip = send_request(uuid, service_id)
            print("requested")
            if proxy_ip is None:
                print("Failed to get proxy IP. Exiting.")
                break

            change_all(proxy_ip)
            os.system("rm -rf /etc/resolv.conf && echo 'nameserver 127.0.0.1'>/etc/resolv.conf")
            nf_region = nf_region_map.get(region, 'luna')
            result = find_in_nf_test(nf_region)
            if result == 0:
                break
    else:
        while True:
            service_id = together(region, service)
            proxy_ip = send_request(uuid, service_id)
            if proxy_ip is None:
                print("Failed to get proxy IP. Exiting.")
                break
            service_list = service_domain_map[service]
            print(proxy_ip)
            change_proxy(service_list, proxy_ip)
            os.system("rm -rf /etc/resolv.conf && echo 'nameserver 127.0.0.1'>/etc/resolv.conf")
            result = big_test()
            print(result)
            service_big_test_checkpoint_map = {
                'HAMI': ['Hami Video:\t\t\t\t[32mYes[0m'],
                'BAHAMUT': ['Bahamut Anime:\t\t\t\t[32mYes ('],
                'GPT': ['ChatGPT:\t\t\t\t[32mYes[0m'],
                'PV': [f"Amazon Prime Video:\t\t\t[32mYes (Region: {region})[0m"],
                'CR': ['Crunchyroll:\t\t\t\t[32mYes[0m']
            }
            check_point = service_big_test_checkpoint_map[service][0]
            print(check_point)
            if find_in_big_test_result(check_point, result) == 0:
                break

    print('work_done')
    print(proxy_ip)


if __name__ == "__main__":
    main()

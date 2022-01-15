import json
import requests
import os

# From Env

bearer = os.getenv('BEARER_CF')
dns_record = os.getenv('DNS_RECORD_CF')
zone = os.getenv('ZONE_ID_CF')

my_ip = requests.get("https://checkip.amazonaws.com/").text


if my_ip:
    # Getting the Dns Record ID

    dnsrecordid = requests.get(f"https://api.cloudflare.com/client/v4/zones/{zone}/dns_records?type=A&name={dns_record}", 
    headers={
     "Authorization": f'Bearer {bearer}',
     'Content-Type': 'application/json'
    }).text
    record_in_json = json.loads(dnsrecordid)
    dns_record_id = (record_in_json["result"][0]["id"])

    # Updating the DNS
    print(f"Current IP Address is: {my_ip}")
    update_dns = requests.put(f'https://api.cloudflare.com/client/v4/zones/{zone}/dns_records/{dns_record_id}', headers={
        "Authorization": f'Bearer {bearer}',
        'Content-Type': 'application/json'
    }, json={
        "type": "A",
        "name": "ssh.linuxadmin.cloud",
        "content": f"{my_ip}"
    }).text
    result_in_json = json.loads(update_dns)
    if (result_in_json["success"]) == True or (result_in_json["success"]) == 'True':
        print(f"The ip was changed to: {my_ip}")
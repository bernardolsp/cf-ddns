# CF-DDNS
Easy and safe way to use Cloudflare as an Dynamic DNS.

In this setup, you shall just pass some enviroment variables:

    bearer = os.getenv('BEARER_CF')
    dns_record = os.getenv('DNS_RECORD_CF')
    zone = os.getenv('ZONE_ID_CF')

All of which can be find in **Cloudflare's Dash page**.

After that - just set this file in a cronjob :-) 


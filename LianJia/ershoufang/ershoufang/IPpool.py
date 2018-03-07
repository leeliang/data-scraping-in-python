import requests
import json
import random
#
class GetIP(object):
    def getRandomIp(self):
        r = requests.get('http://0.0.0.0:8000')
        pool = json.loads(r.text)
        ip = random.choice(pool)
        proxies={'http':'http://%s:%s'%(ip[0],ip[1]),'https':'http://%s:%s'%(ip[0],ip[1])}
        ip_check = self.checkIp(proxies)
        if ip_check:
            return proxies['http']
        else:
            return self.getRandomIp()
    def checkIp(self, proxies):
        try:
            url = "http://www.baidu.com"
            res = requests.get(url, proxies=proxies,timeout=1.0)
            if res.status_code >=200 and res.status_code <=300:
                print "Effective IP"
                return True
            else:
                print ("Invaild IP")
                self.delectIP(proxies)
                return False
        except Exception as e:
            print ("Invaild IP")
            self.delectIP(proxies)
            return False
    def delectIP(self,proxies):
        url = '0.0.0.1:8000/delete?ip=' + proxies['http'].split("//")[1]
        r = requests.get(url)
##
if __name__ == "__main__":
    get_IP = GetIP()
    get_IP.getRandomIp()  
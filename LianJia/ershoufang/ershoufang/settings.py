# -*- coding: utf-8 -*-

# Scrapy settings for ershoufang project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'ershoufang'

SPIDER_MODULES = ['ershoufang.spiders']
NEWSPIDER_MODULE = 'ershoufang.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'ershoufang (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'ershoufang.middlewares.ErshoufangSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'scrapy.downloadermiddleware.useragent.UserAgentMiddleware': None,
   'ershoufang.middlewares.MyUserAgentMiddleware': 400,
   #'ershoufang.middlewares.ProxyMiddleware': 543,
   #'ershoufang.middlewares.ProxyPool': 543,
   #'scrapy.downloadermiddlewares.retry.RetryMiddleware': 560,
   #'scrapy.contrib.downloadermiddleware.downloadtimeout.DownloadTimeoutMiddleware': 350,
}
#RETRY_TIMES = 20
#DOWNLOAD_TIMEOUT = 10

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'ershoufang.pipelines.ErshoufangPipeline': 300,
}
MONGO_URI = 'mongodb://localhost:27017'
MONGO_DB = "lianjia"
# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
MY_USER_AGENT = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    ]
PROXIES = [u'http://122.72.18.35:80',
 u'http://124.165.252.72:8081',
 u'http://124.165.252.72:8080',
 u'http://124.165.252.72:9999',
 u'http://111.62.251.68:80',
 u'http://111.62.251.68:8080',
 u'http://42.245.252.36:80',
 u'http://122.72.18.61:80',
 u'http://122.72.18.60:80',
 u'http://112.5.56.108:3128',
 u'http://122.72.108.53:80',
 u'http://210.202.37.54:3128',
 u'http://121.248.112.20:3128',
 u'http://219.135.164.245:3128',
 u'http://113.207.44.70:3128',
 u'http://183.62.196.10:3128',
 u'http://119.36.92.46:80',
 u'http://120.77.223.86:3128',
 u'http://121.43.178.58:3128',
 u'http://61.4.184.180:3128',
 u'http://119.36.92.42:80',
 u'http://120.198.224.106:8080',
 u'http://123.130.243.84:82',
 u'http://122.228.25.97:8101',
 u'http://60.249.19.50:8080',
 u'http://120.198.224.103:8080',
 u'http://120.198.224.109:8080',
 u'http://114.115.140.25:3128',
 u'http://116.11.254.37:80',
 u'http://124.133.230.254:80',
 u'http://139.224.24.26:8888',
 u'http://112.13.93.43:8088',
 u'http://112.74.94.142:3128',
 u'http://101.53.101.172:9999',
 u'http://118.119.168.172:9999',
 u'http://61.155.164.106:3128',
 u'http://180.250.74.210:8080',
 u'http://60.169.19.66:9000',
 u'http://114.251.228.124:3128',
 u'http://171.37.176.140:9797',
 u'http://61.163.39.70:9999',
 u'http://118.193.107.104:80',
 u'http://106.14.51.145:8118',
 u'http://119.90.63.3:3128',
 u'http://116.199.2.208:82',
 u'http://116.199.115.78:82',
 u'http://202.202.90.20:8080',
 u'http://61.187.251.235:80',
 u'http://183.30.197.74:9797',
 u'http://116.199.2.210:82',
 u'http://106.39.179.9:80',
 u'http://218.29.236.50:3128',
 u'http://202.85.213.219:3128',
 u'http://60.13.74.168:80',
 u'http://101.200.89.170:8888',
 u'http://122.224.227.202:3128',
 u'http://218.26.217.77:3128',
 u'http://218.22.7.62:53281',
 u'http://115.213.60.99:53281',
 u'http://183.184.194.15:9797',
 u'http://59.110.236.204:3128',
 u'http://222.222.169.60:53281',
 u'http://218.56.132.157:8080',
 u'http://36.250.94.162:3128',
 u'http://182.254.247.171:9000',
 u'http://118.193.107.37:80',
 u'http://61.163.139.241:9797',
 u'http://119.36.92.41:81',
 u'http://36.36.201.253:8080',
 u'http://116.199.2.209:82',
 u'http://118.193.107.178:80',
 u'http://116.199.2.196:80',
 u'http://118.193.107.195:80',
 u'http://58.56.128.84:9001',
 u'http://190.121.158.114:8080',
 u'http://118.193.107.245:80',
 u'http://175.165.90.91:80',
 u'http://27.36.116.226:3128',
 u'http://47.92.75.67:3128',
 u'http://163.125.197.19:9797',
 u'http://60.13.74.203:80',
 u'http://222.86.191.44:8080',
 u'http://121.8.170.53:9797',
 u'http://177.128.193.114:8089',
 u'http://163.125.192.21:9797',
 u'http://180.140.161.138:9797',
 u'http://171.88.52.96:9797',
 u'http://120.9.75.45:9999',
 u'http://112.114.94.17:8118',
 u'http://118.193.107.182:80',
 u'http://118.193.107.210:80',
 u'http://124.206.133.219:3128',
 u'http://101.200.55.71:8080',
 u'http://118.193.107.75:80',
 u'http://106.39.179.118:80',
 u'http://27.46.51.55:9797',
 u'http://123.7.38.31:9999',
 u'http://118.193.107.184:80',
 u'http://125.45.87.12:9999',
 u'http://190.151.10.226:8080',
 u'http://203.95.220.110:53281',
 u'http://118.193.26.18:8080',
 u'http://101.4.136.34:80',
 u'http://113.254.110.25:80',
 u'http://120.198.224.110:8080',
 u'http://117.93.82.50:8118',
 u'http://223.19.41.6:8380',
 u'http://116.30.218.76:9000',
 u'http://116.236.151.166:8080',
 u'http://118.193.107.222:80',
 u'http://222.52.142.242:8080',
 u'http://163.125.69.98:8888',
 u'http://120.198.224.7:8080',
 u'http://106.39.179.162:80',
 u'http://118.193.107.219:80',
 u'http://59.59.144.135:53281',
 u'http://118.193.107.103:80',
 u'http://118.193.107.28:80',
 u'http://118.193.107.125:80',
 u'http://118.193.107.146:80',
 u'http://27.46.74.27:9999',
 u'http://106.39.179.244:80',
 u'http://47.94.230.42:9999',
 u'http://202.69.38.82:8080',
 u'http://118.193.107.135:80',
 u'http://202.59.163.129:8080',
 u'http://118.193.107.234:80',
 u'http://118.193.107.137:80',
 u'http://61.163.137.58:9797',
 u'http://113.65.188.46:9797',
 u'http://218.56.132.158:8080',
 u'http://222.73.68.144:8090',
 u'http://58.147.174.113:8080',
 u'http://163.125.196.61:9797',
 u'http://222.169.193.162:8099',
 u'http://118.193.107.238:80',
 u'http://123.133.52.247:81',
 u'http://221.237.154.58:9999',
 u'http://120.198.224.7:80',
 u'http://159.226.249.93:8080',
 u'http://180.76.134.106:3128',
 u'http://123.163.142.221:808',
 u'http://218.29.111.106:9999',
 u'http://216.241.14.94:8080',
 u'http://43.243.207.242:8080',
 u'http://113.200.214.164:9999',
 u'http://177.128.225.193:8080',
 u'http://60.191.134.165:9999',
 u'http://106.2.6.23:3128',
 u'http://119.130.115.226:808',
 u'http://120.198.224.6:8080',
 u'http://120.198.224.6:80',
 u'http://223.19.206.178:8380',
 u'http://112.114.96.99:8118',
 u'http://218.56.0.234:3128',
 u'http://112.114.94.107:8118',
 u'http://115.183.11.158:9999',
 u'http://104.236.48.178:8080',
 u'http://118.193.107.109:80',
 u'http://113.78.90.215:9797',
 u'http://123.14.165.105:8118',
 u'http://112.114.96.48:8118',
 u'http://61.134.25.106:3128',
 u'http://61.158.187.157:8080',
 u'http://113.65.189.142:9797',
 u'http://60.194.46.119:3128',
 u'http://112.114.97.225:8118',
 u'http://222.89.112.48:53281',
 u'http://1.196.161.163:9999',
 u'http://111.62.245.189:80',
 u'http://121.40.65.178:8080',
 u'http://118.193.107.232:80',
 u'http://112.114.95.37:8118',
 u'http://112.114.94.33:8118',
 u'http://222.211.163.135:53281',
 u'http://182.88.244.248:9797',
 u'http://118.193.107.147:80',
 u'http://59.59.145.90:53281',
 u'http://119.53.112.91:9000',
 u'http://118.193.107.183:80',
 u'http://112.114.97.230:8118',
 u'http://113.78.254.84:9000',
 u'http://31.131.67.76:8080',
 u'http://221.214.110.130:8080',
 u'http://220.180.50.14:53281',
 u'http://223.96.95.229:3128',
 u'http://223.16.229.241:8080',
 u'http://101.200.45.131:3128',
 u'http://180.156.94.186:8118',
 u'http://222.76.174.120:8118',
 u'http://118.193.107.99:80',
 u'http://119.144.14.27:8118',
 u'http://218.56.132.156:8080',
 u'http://112.114.99.184:8118',
 u'http://211.143.112.138:8118',
 u'http://120.25.164.134:8118',
 u'http://27.46.38.38:9797',
 u'http://112.114.95.115:8118',
 u'http://183.196.170.247:9000',
 u'http://118.193.107.230:80',
 u'http://60.255.186.169:8888',
 u'http://171.34.197.71:3128',
 u'http://202.109.207.126:8888',
 u'http://223.223.203.30:8080',
 u'http://42.157.5.154:9999',
 u'http://61.144.105.150:9797',
 u'http://221.237.154.57:9999',
 u'http://58.51.38.122:808',
 u'http://113.83.219.206:9797',
 u'http://113.116.147.197:9000',
 u'http://200.195.141.178:8080',
 u'http://223.241.78.231:8010',
 u'http://223.241.78.71:8010',
 u'http://36.55.230.154:3128',
 u'http://60.184.181.116:8118',
 u'http://221.10.159.234:1337',
 u'http://59.41.202.117:53281',
 u'http://118.193.107.64:80',
 u'http://110.73.34.161:8123',
 u'http://60.174.233.154:9999',
 u'http://221.178.251.168:3128',
 u'http://221.224.132.174:53281',
 u'http://122.237.106.156:80',
 u'http://113.65.161.64:9797',
 u'http://89.191.131.243:8080',
 u'http://222.217.19.248:8080',
 u'http://222.92.141.250:80']

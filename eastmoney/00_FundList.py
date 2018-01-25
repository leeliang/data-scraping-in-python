
# coding: utf-8
import requests
import re
from bs4 import BeautifulSoup
# Set Default Encoding
import sys
stdout = sys.stdout
reload(sys)
sys.setdefaultencoding('utf-8')
sys.stdout = stdout

def getHTMLText(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.content
    except Exception as e:
        print "Failed to open url: {}".format(e)
        return None


def getFundList(url):
    html = getHTMLText(url)
    soup = BeautifulSoup(html,'html.parser',from_encoding='gb18030')
    uls = soup.find_all('ul', attrs={'class':'num_right'})
    fund_list = []
    for ul in uls:
        for li in ul.find_all('li'):
            a_href = li.find_all('a')
            if len(a_href) > 1:
                info = a_href[0]
                code = re.findall(r'\d+',info.text)[0]
                url = info.attrs['href']
                name_start_n = info.text.find(ur'）')+1
                name = info.text.decode('utf-8')[name_start_n:].encode('utf-8')
                fund_list.append([code,name,url])
    return fund_list




def writeToCsv(file_name, text=[]):
    with open(file_name,'wb') as f:
        for item in text:
            line = ','.join(item) + '\n'
            f.write(line.encode('utf-8'))



if __name__ == '__main__':
	url = 'http://fund.eastmoney.com/allfund.html#0'
	fund_list = getFundList(url)
	writeToCsv('FundList.csv',fund_list)


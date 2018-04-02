
# coding: utf-8
import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
import time
import os 
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

def getFundNAV(code):
    # get total records count
    base_url = 'http://fund.eastmoney.com/f10/F10DataApi.aspx?type=lsjz&page=1&'
    url = base_url + 'code=' + code + '&PER=1' 
    html = getHTMLText(url)
    records = str(html.split('records:')[1].split(',')[0])
    # Net Asset Value of funds
    if records == '0':
        return None
    else:
        url = base_url + 'code=' + code + '&PER=' + records
        html = getHTMLText(url)
        soup = BeautifulSoup(html,'html.parser')
        trs = soup.findAll('tr')
        pattern = re.compile('<td.*?>(.*?)</td>',re.S)
        result = []
        for tr in trs[1:]:
            td = tr.findAll('td')
            nav = re.findall(pattern,str(td))
            result.append(nav[:4])
        return result 
        

def writeToCsv(file_name, text=[]):
    with open(file_name,'wb') as f:
        for item in text:
            line = ','.join(item) + '\n'
            f.write(line.encode('utf-8'))



# read fund list

if __name__ == '__main__':
    #fund_list = pd.read_csv('FundList.csv',header=None,names=['code','name','url'],dtype={'code':str})


    i = 0
    codes = ['160212']
    #for code in fund_list.code:
    for code in codes:
        try:
            csv_name = code+'.csv'
            # file_path = os.path.join(os.getcwd(),csv_name)
            # if os.path.exists(file_path):
            #     print file_path
            #     i = i + 1
            #     continue 
            print code
            result = getFundNAV(code)
            writeToCsv(csv_name,result)
            print "Finished fund: %s" % code
        except Exception as e:
            print time.strftime('[%Y-%m-%d %H:%M:%S]', time.localtime(time.time()))
            print "Failed to get the %s data" % code



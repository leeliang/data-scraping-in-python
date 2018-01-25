
# coding: utf-8
import requests
import re
from bs4 import BeautifulSoup
import pandas as pd 
import os
# Set Default Encoding
import sys
stdout = sys.stdout
reload(sys)
sys.setdefaultencoding('utf-8')
sys.stdout = stdout
#
def getHTMLText(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.content
    except Exception as e:
        print "Failed to open url: {}".format(e)
        return None


# def getFundInfo(code):
#     url = 'http://fund.eastmoney.com/f10/jbgk_'+code+'.html'
#     html = getHTMLText(url)
#     soup = BeautifulSoup(html,'html.parser')
#     tabels = soup.find_all('table',attrs={'class':'info w790'})
#     tds = tabels[0].find_all('td')
#     fund_name = tds[0].string
#     fund_type = tds[3].string
#     fund_start_t = '-'.join(re.findall('\d+',tds[4].string))
#     if tds[10].string == None:
#     	fund_manager = 'No_Manager'
#     else:
#     	fund_manager = tds[10].string
#     fund_company = tds[8].string
#     return [code,fund_name,fund_type,fund_start_t,fund_manager,fund_company]

def getFundInfo(code):
    url = 'http://fund.eastmoney.com/'+code+'.html'
    html = getHTMLText(url)
    soup = BeautifulSoup(html,'html.parser')
    div = soup.find_all('div',attrs={'class':'infoOfFund'})
    a_href = div[-1].find_all('a')
    fund_type = a_href[0].string
    fund_manager = a_href[2].string
    fund_company = a_href[3].string
    return [code,fund_type,fund_manager,fund_company]


def writeToCsv(file_name, text=[]):
    with open(file_name,'ab') as f:
        for item in text:
            line = ','.join(item) + '\n'
            f.write(line.encode('utf-8'))

##

if __name__ == '__main__':
#
    #codes = ['000001','000002']
    file_path_failed = os.path.join(os.getcwd(), 'FailedCodes.txt')
    if os.path.exists(file_path_failed):
        codes = pd.read_table('FailedCodes.txt')
    else:
        fund_list = pd.read_csv('FundList.csv',header=None,names=['code','name','url'],dtype={'code':str})
        codes = fund_list.code
    funds_info = []
    failed_codes = []
    finish_codes = []
    # fundInfo.csv
    file_path_fund = os.path.join(os.getcwd(), 'FundInfo.csv')
    if os.path.exists(file_path_fund):
	    finish = pd.read_csv('FundInfo.csv',header=None,names=['code','type','manager','company'],dtype={'code':str})
	    finish_codes = list(finish.code)
	    #print finish_codes
# 
    for code in codes:
        try:
    	    if code in finish_codes:
    		    continue 
    	    else:
    		    fund_info = getFundInfo(code)
    		#print fund_info
    		#funds_info.append(fund_info)
    		    writeToCsv('FundInfo.csv',[fund_info])
    		    print "%s Done" % code
        except Exception as e: 
        #failed_codes.append(code) 
            print "Failed to get the %s information" %code,e 
            writeToCsv('FailedCodes.txt',[[code]]) 
    #writeToCsv('FundInfo.csv',funds_info) 
    #writeToCsv('FailedCodes.txt',failed_codes)


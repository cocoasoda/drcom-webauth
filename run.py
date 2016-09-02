#!/usr/bin/env python
import urllib
import urllib2
#深大某宿舍区样例
conf = {
    'account': 'YOUR_ACCOUNT',
    'passwd': 'YOUR_PASSWORD',
    'url': 'http://172.30.255.2/a30.htm'
}
form = {
    'DDDDD': conf['account'],
    'upass': conf['passwd'],
    '0MKKey': '%B5%C7%A1%A1%C2%BC'
}
#url, 0MKKey 请自行抓包 

data = urllib.urlencode(form)
req = urllib2.Request(conf['url'], data)
res = urllib2.urlopen(req)

from urllib import request
from urllib.parse import urlencode
import re
from os import system
from time import sleep
import sys
import random
import http.cookiejar
import concurrent.futures
import socket
la5dhar = '\033[92m'
system("clear")
la7mar  = '\033[91m'
green = '\033[92m'
labyadh = '\033[00m'
headers = {'user-agent': 'Moozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}
domain = ['co.in','co.uk','in','pk','co.pk','co.org','org','com','uk','bd','net','ac', 'ad', 'ae', 'af', 'ag', 'ai', 'al', 'am', 'an', 'ao',
                        'aq', 'ar', 'as', 'at', 'au', 'aw', 'ax', 'az', 'ba', 'bb',
                        'bd', 'be', 'bf', 'bg', 'bh', 'bi', 'bj', 'bm', 'bn', 'bo',
                        'br', 'bs', 'bt', 'bv', 'bw', 'by', 'bz', 'ca', 'cc', 'cd',
                        'cf', 'cg', 'ch', 'ci', 'ck', 'cl', 'cm', 'cn', 'co', 'cr',
                        'cu', 'cv', 'cx', 'cy', 'cz', 'de', 'dj', 'dk', 'dm', 'do',
                        'dz', 'ec', 'ee', 'eg', 'eh', 'er', 'es', 'et', 'eu', 'fi',
                        'fj', 'fk', 'fm', 'fo', 'fr', 'ga', 'gb', 'gd', 'ge', 'gf',
                        'gg', 'gh', 'gi', 'gl', 'gm', 'gn', 'gp', 'gq', 'gr', 'gs',
                        'gt', 'gu', 'gw', 'gy', 'hk', 'hm', 'hn', 'hr', 'ht', 'hu',
                        'id', 'ie', 'il', 'im', 'in', 'io', 'iq', 'is', 'it',
                        'je', 'jm', 'jo', 'jp', 'ke', 'kg', 'kh', 'ki', 'km', 'kn',
                        'kp', 'kr', 'kw', 'ky', 'kz', 'la', 'lb', 'lc', 'li', 'lk',
                        'lr', 'ls', 'lt', 'lu', 'lv', 'ly', 'ma', 'mc', 'md', 'me',
                        'mg', 'mh', 'mk', 'ml', 'mm', 'mn', 'mo', 'mp', 'mq', 'mr',
                        'ms', 'mt', 'mu', 'mv', 'mw', 'mx', 'my', 'mz', 'na', 'nc',
                        'ne', 'nf', 'ng', 'ni', 'nl', 'no', 'np', 'nr', 'nu', 'nz',
                        'om', 'pa', 'pe', 'pf', 'pg', 'ph', 'pk', 'pl', 'pm', 'pn',
                        'pr', 'ps', 'pt', 'pw', 'py', 'qa', 're', 'ro', 'rs', 'ru',
                        'rw', 'sa', 'sb', 'sc', 'sd', 'se', 'sg', 'sh', 'si', 'sj',
                        'sk', 'sl', 'sm', 'sn', 'so', 'sr', 'st', 'su', 'sv', 'sy',
                        'sz', 'tc', 'td', 'tf', 'tg', 'th', 'tj', 'tk', 'tl', 'tm',
                        'tn', 'to', 'tp', 'tr', 'tt', 'tv', 'tw', 'tz', 'ua', 'ug',
                        'uk', 'um', 'us', 'uy', 'uz', 'va', 'vc', 've', 'vg', 'vi',
                        'vn', 'vu', 'wf', 'ws', 'ye', 'yt', 'za', 'zm', 'zw', 'com',
                        'net', 'org', 'biz', 'gov', 'mil', 'edu', 'info', 'int', 'tel']

def bing(dork):
	okkk = dork
	first = 0
	try:
		for i in range(int(page1)):
			first = first+50
			params = {'q': okkk, 'count': '1000','first':first}
			get = urlencode(params)
			url = "http://www.bing.com/search?"+get
			url = request.Request(url,None,headers=headers)
			result = request.urlopen(url,timeout=10)
			result = result.read().decode('utf-8')
			patern = r'<h2><a href="(.*?)"'
			ok = re.findall(patern,result)
			for i in ok:
				i = i.replace("<strong>","")
				i = i.replace("</strong>","")
				i = i.replace("http://","")
				i = i.replace("https://","")
				i = i.replace("www.","")
				i = i.split("/")
				i = i[0]
				check(i)
				#ip(i)						
	except Exception as e:
		print(e)
		bing(dork)
def check(url):
	pdf = ".pdf"
	string = "." in url
	try:
		file = open(filename,"r").read()
	except:
		open(filename,"w")
		file = open(filename,"r").read()
	if url in file or pdf in url or string == False:
			print(la7mar+" [+] Already Exists: "+url+labyadh)
	else:
		file = open(filename,"a")
		file.write(url+"\n")
		file.close()
		print(la5dhar+" [+] Added: "+url+labyadh)
try:
	dorks = "dork.txt"
	page1 = 500
	filename = "list.txt"
	dork = open(dorks,"r").read().splitlines()
except Exception as e:
	print(e)
	exit()
try:
	with concurrent.futures.ThreadPoolExecutor(200) as executor:
		executor.map(bing,dork)
except Exception as e:
	print(e)

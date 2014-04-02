#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: rtseng
# @Date:   2014-03-12 14:14:13
# @Last Modified by:   rtseng
# @Last Modified time: 2014-04-02 12:04:38

import urllib.request
import json
from bs4 import BeautifulSoup
import requests

def BSPaser(req):
	print(req)
	soup = BeautifulSoup(req.read().decode("utf8"))

	webtext = soup.get_text().strip().split()

	print(soup.head.title)
	print(webtext)


def WebRequest(url):
	payload = {
		'Host':'cois.moi.gov.tw',
		'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
		'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		'Accept-Language':'zh-tw,zh;q=0.8,en-us;q=0.5,en;q=0.3',
		'Accept-Encoding':'gzip, deflate',
		'Connection':'keep-alive',
		'Referer':'http://cois.moi.gov.tw/moiweb/web/frmHome.aspx',
		'Cache-Control':'max-age=0'
	}
	getValue = {
		'__EVENTTARGET' : '',
		'__EVENTARGUMENT' : '',
		'GSSintDateType' : '2',
		'GSSCalSaturdayColor' : 'Black',
		'GSSCalSundayColor' : 'Black',
		'GSStxtToday' : '2014/04/02',
		'__VIEWSTATE' : 'dDwtMTMxMTQ0ODc5NDt0PDtsPGk8NT47PjtsPHQ8O2w8aTwxPjtpPDQ+O2k8Nj47aTw4PjtpPDEyPjtpPDE0PjtpPDE2Pjs+O2w8dDw7bDxpPDE+O2k8Mz47PjtsPHQ8cDxwPGw8VGV4dDs+O2w8MTAz5bm0MDPmnIgxN+aXpSAg5pif5pyf5LiAOz4+Oz47Oz47dDw7bDxpPDE+Oz47bDx0PHA8cDxsPFRleHQ7PjtsPHwmbmJzcFw75oKo5piv56ysXDxpbWcgaGVpZ2h0PScyMCcgc3JjPScuLi9pbWcvMS5naWYnIGFsdD0nMScgd2lkdGg9JzE1JyBhbGlnbj0nYWJzTWlkZGxlJ1w+XDxpbWcgaGVpZ2h0PScyMCcgc3JjPScuLi9pbWcvMy5naWYnIGFsdD0nMycgd2lkdGg9JzE1JyBhbGlnbj0nYWJzTWlkZGxlJ1w+XDxpbWcgaGVpZ2h0PScyMCcgc3JjPScuLi9pbWcvMC5naWYnIGFsdD0nMCcgd2lkdGg9JzE1JyBhbGlnbj0nYWJzTWlkZGxlJ1w+XDxpbWcgaGVpZ2h0PScyMCcgc3JjPScuLi9pbWcvNS5naWYnIGFsdD0nNScgd2lkdGg9JzE1JyBhbGlnbj0nYWJzTWlkZGxlJ1w+XDxpbWcgaGVpZ2h0PScyMCcgc3JjPScuLi9pbWcvMC5naWYnIGFsdD0nMCcgd2lkdGg9JzE1JyBhbGlnbj0nYWJzTWlkZGxlJ1w+XDxpbWcgaGVpZ2h0PScyMCcgc3JjPScuLi9pbWcvNi5naWYnIGFsdD0nNicgd2lkdGg9JzE1JyBhbGlnbj0nYWJzTWlkZGxlJ1w+XDxpbWcgaGVpZ2h0PScyMCcgc3JjPScuLi9pbWcvMy5naWYnIGFsdD0nMycgd2lkdGg9JzE1JyBhbGlnbj0nYWJzTWlkZGxlJ1w+5L2NJm5ic3BcO+ioquWuoiZuYnNwXDt8Jm5ic3BcOzs+Pjs+Ozs+Oz4+Oz4+O3Q8O2w8aTwxPjs+O2w8dDxwPHA8bDxUZXh0Oz47bDxcPHRyXD5cPHRkXD4NClw8dGFibGUgc3VtbWFyeT0n5o6S54mI55SoJyB3aWR0aD0nMTAwJScgYm9yZGVyPScwJyBjZWxscGFkZGluZz0nMCcgY2VsbHNwYWNpbmc9JzAnXD4NClw8dHJcPlw8dGRcPlw8aW1nIGFsdD0nJyBzcmM9Jy4uL2ltZy9sZWZ0X21lbnVfYjAxLmdpZicgd2lkdGg9JzYnIGhlaWdodD0nMjQnXD5cPC90ZFw+DQpcPHRkIHdpZHRoPScxMDAlJyBhbGlnbj0nY2VudGVyJyBub3dyYXAgYmFja2dyb3VuZD0nLi4vaW1nL2xlZnRfbWVudV9iMDIuZ2lmJyBjbGFzcz0nbV90aXRsZWZvbnRfMDInXD7pl5zmlrzmiJHlgJFcPC90ZFw+XDx0ZFw+XDxpbWcgYWx0PScnIHNyYz0nLi4vaW1nL2xlZnRfbWVudV9iMDMuZ2lmJyB3aWR0aD0nNicgaGVpZ2h0PScyNCdcPlw8L3RkXD5cPC90clw+XDwvdGFibGVcPlw8L3RkXD5cPC90clw+DQpcPHRyXD5cPHRkXD5cPHRhYmxlIHN1bW1hcnk9J+aOkueJiOeUqCcgd2lkdGg9JzEwMCUnIGJvcmRlcj0nMCcgY2VsbHBhZGRpbmc9JzAnIGNlbGxzcGFjaW5nPScyJyBcPlw8dHJcPlw8dGRcPiZuYnNwXDtcPC90ZFw+DQpcPHRkIHdpZHRoPScxMDAlJyBhbGlnbj0nY2VudGVyJyBub3dyYXAgY2xhc3M9J21fdGRjb2xvcl8wNidcPlw8YSBocmVmPSdmcm1TaW5nbGVQYWdlLmFzcHg/RnVuSUQ9ZjJhNjJlYjk1NzIyY2E0NSdcPue2suermeWwjuimvVw8L2FcPlw8L3RkXD5cPHRkXD4mbmJzcFw7XDwvdGRcPlw8L3RyXD5cPC90YWJsZVw+XDwvdGRcPlw8L3RyXD4NClw8dHJcPlw8dGRcPlw8dGFibGUgc3VtbWFyeT0n5o6S54mI55SoJyB3aWR0aD0nMTAwJScgYm9yZGVyPScwJyBjZWxscGFkZGluZz0nMCcgY2VsbHNwYWNpbmc9JzInIFw+XDx0clw+XDx0ZFw+Jm5ic3BcO1w8L3RkXD4NClw8dGQgd2lkdGg9JzEwMCUnIGFsaWduPSdjZW50ZXInIG5vd3JhcCBjbGFzcz0nbV90ZGNvbG9yXzA2J1w+XDxhIGhyZWY9J2ZybUFubm91bmNlLmFzcHg/RnVuSUQ9NTg1YzcwZjJiMzlmYTE0MSdcPuacgOaWsOWFrOWRilw8L2FcPlw8L3RkXD5cPHRkXD4mbmJzcFw7XDwvdGRcPlw8L3RyXD5cPC90YWJsZVw+XDwvdGRcPlw8L3RyXD4NClw8dHJcPlw8dGRcPlw8dGFibGUgc3VtbWFyeT0n5o6S54mI55SoJyB3aWR0aD0nMTAwJScgYm9yZGVyPScwJyBjZWxscGFkZGluZz0nMCcgY2VsbHNwYWNpbmc9JzInIFw+XDx0clw+XDx0ZFw+Jm5ic3BcO1w8L3RkXD4NClw8dGQgd2lkdGg9JzEwMCUnIGFsaWduPSdjZW50ZXInIG5vd3JhcCBjbGFzcz0nbV90ZGNvbG9yXzA2J1w+XDxhIGhyZWY9J2ZybVNpbmdsZVBhZ2UuYXNweD9GdW5JRD04ODZhMTk4MmVhNDRhMjE1J1w+55m85bGV54++5rOBXDwvYVw+XDwvdGRcPlw8dGRcPiZuYnNwXDtcPC90ZFw+XDwvdHJcPlw8L3RhYmxlXD5cPC90ZFw+XDwvdHJcPg0KXDx0clw+XDx0ZFw+XDx0YWJsZSBzdW1tYXJ5PSfmjpLniYjnlKgnIHdpZHRoPScxMDAlJyBib3JkZXI9JzAnIGNlbGxwYWRkaW5nPScwJyBjZWxsc3BhY2luZz0nMicgXD5cPHRyXD5cPHRkXD4mbmJzcFw7XDwvdGRcPg0KXDx0ZCB3aWR0aD0nMTAwJScgYWxpZ249J2NlbnRlcicgbm93cmFwIGNsYXNzPSdtX3RkY29sb3JfMDYnXD5cPGEgaHJlZj0nZnJtRm9ybS5hc3B4P0Z1bklEPWU4OWFkYjVlOGI1YjRiODEnXD7ntbHoqIjos4fmlplcPC9hXD5cPC90ZFw+XDx0ZFw+Jm5ic3BcO1w8L3RkXD5cPC90clw+XDwvdGFibGVcPlw8L3RkXD5cPC90clw+DQpcPHRyXD5cPHRkXD4NClw8dGFibGUgc3VtbWFyeT0n5o6S54mI55SoJyB3aWR0aD0nMTAwJScgYm9yZGVyPScwJyBjZWxscGFkZGluZz0nMCcgY2VsbHNwYWNpbmc9JzAnXD4NClw8dHJcPlw8dGRcPlw8aW1nIGFsdD0nJyBzcmM9Jy4uL2ltZy9sZWZ0X21lbnVfYjAxLmdpZicgd2lkdGg9JzYnIGhlaWdodD0nMjQnXD5cPC90ZFw+DQpcPHRkIHdpZHRoPScxMDAlJyBhbGlnbj0nY2VudGVyJyBub3dyYXAgYmFja2dyb3VuZD0nLi4vaW1nL2xlZnRfbWVudV9iMDIuZ2lmJyBjbGFzcz0nbV90aXRsZWZvbnRfMDInXD7npL7mnIPlnJjpq5RcPC90ZFw+XDx0ZFw+XDxpbWcgYWx0PScnIHNyYz0nLi4vaW1nL2xlZnRfbWVudV9iMDMuZ2lmJyB3aWR0aD0nNicgaGVpZ2h0PScyNCdcPlw8L3RkXD5cPC90clw+XDwvdGFibGVcPlw8L3RkXD5cPC90clw+DQpcPHRyXD5cPHRkXD5cPHRhYmxlIHN1bW1hcnk9J+aOkueJiOeUqCcgd2lkdGg9JzEwMCUnIGJvcmRlcj0nMCcgY2VsbHBhZGRpbmc9JzAnIGNlbGxzcGFjaW5nPScyJyBcPlw8dHJcPlw8dGRcPiZuYnNwXDtcPC90ZFw+DQpcPHRkIHdpZHRoPScxMDAlJyBhbGlnbj0nY2VudGVyJyBub3dyYXAgY2xhc3M9J21fdGRjb2xvcl8wNidcPlw8YSBocmVmPSdmcm1Gb3JtLmFzcHg/RnVuSUQ9MTNiMmEzNDg0ZTY2YzA1ZSdcPuekvuacg+WcmOmrlOebuOmXnOazleimj1w8L2FcPlw8L3RkXD5cPHRkXD4mbmJzcFw7XDwvdGRcPlw8L3RyXD5cPC90YWJsZVw+XDwvdGRcPlw8L3RyXD4NClw8dHJcPlw8dGRcPlw8dGFibGUgc3VtbWFyeT0n5o6S54mI55SoJyB3aWR0aD0nMTAwJScgYm9yZGVyPScwJyBjZWxscGFkZGluZz0nMCcgY2VsbHNwYWNpbmc9JzInIFw+XDx0clw+XDx0ZFw+Jm5ic3BcO1w8L3RkXD4NClw8dGQgd2lkdGg9JzEwMCUnIGFsaWduPSdjZW50ZXInIG5vd3JhcCBjbGFzcz0nbV90ZGNvbG9yXzA2J1w+XDxhIGhyZWY9J2ZybUZvcm0uYXNweD9GdW5JRD1kNTJkNGY2NmY2ZjliYzg3J1w+56S+5pyD5ZyY6auU55Sz6KuL5pu4XDwvYVw+XDwvdGRcPlw8dGRcPiZuYnNwXDtcPC90ZFw+XDwvdHJcPlw8L3RhYmxlXD5cPC90ZFw+XDwvdHJcPg0KXDx0clw+XDx0ZFw+XDx0YWJsZSBzdW1tYXJ5PSfmjpLniYjnlKgnIHdpZHRoPScxMDAlJyBib3JkZXI9JzAnIGNlbGxwYWRkaW5nPScwJyBjZWxsc3BhY2luZz0nMicgXD5cPHRyXD5cPHRkXD4mbmJzcFw7XDwvdGRcPg0KXDx0ZCB3aWR0aD0nMTAwJScgYWxpZ249J2NlbnRlcicgbm93cmFwIGNsYXNzPSdtX3RkY29sb3JfMDYnXD5cPGEgaHJlZj0nZnJtRm9ybS5hc3B4P0Z1bklEPTljZWUxMGY4ZDQ3ODFkYzEnXD7nlLPoq4vntYTnuZTlhajlnIvmgKflnJjpq5TpoIjnn6VcPC9hXD5cPC90ZFw+XDx0ZFw+Jm5ic3BcO1w8L3RkXD5cPC90clw+XDwvdGFibGVcPlw8L3RkXD5cPC90clw+DQpcPHRyXD5cPHRkXD5cPHRhYmxlIHN1bW1hcnk9J+aOkueJiOeUqCcgd2lkdGg9JzEwMCUnIGJvcmRlcj0nMCcgY2VsbHBhZGRpbmc9JzAnIGNlbGxzcGFjaW5nPScyJyBcPlw8dHJcPlw8dGRcPiZuYnNwXDtcPC90ZFw+DQpcPHRkIHdpZHRoPScxMDAlJyBhbGlnbj0nY2VudGVyJyBub3dyYXAgY2xhc3M9J21fdGRjb2xvcl8wNidcPlw8YSBocmVmPSdmcm1Gb3JtLmFzcHg/RnVuSUQ9ZTRjZGY0YzgzNGY2NmM2YydcPuWFqOWci+aAp+ekvuacg+WcmOmrlOW3peS9nOaJi+WGilw8L2FcPlw8L3RkXD5cPHRkXD4mbmJzcFw7XDwvdGRcPlw8L3RyXD5cPC90YWJsZVw+XDwvdGRcPlw8L3RyXD4NClw8dHJcPlw8dGRcPlw8dGFibGUgc3VtbWFyeT0n5o6S54mI55SoJyB3aWR0aD0nMTAwJScgYm9yZGVyPScwJyBjZWxscGFkZGluZz0nMCcgY2VsbHNwYWNpbmc9JzInIFw+XDx0clw+XDx0ZFw+Jm5ic3BcO1w8L3RkXD4NClw8dGQgd2lkdGg9JzEwMCUnIGFsaWduPSdjZW50ZXInIG5vd3JhcCBjbGFzcz0nbV90ZGNvbG9yXzA2J1w+XDxhIGhyZWY9J2ZybUZvcm0uYXNweD9GdW5JRD0wOGQ2OWVhZTI3ODU5N2MzJ1w+5bm05bqm57WQ6aSY57aT6LK755WZ55So5YW36auU6KiI55Wr5pu4XDwvYVw+XDwvdGRcPlw8dGRcPiZuYnNwXDtcPC90ZFw+XDwvdHJcPlw8L3RhYmxlXD5cPC90ZFw+XDwvdHJcPg0KXDx0clw+XDx0ZFw+XDx0YWJsZSBzdW1tYXJ5PSfmjpLniYjnlKgnIHdpZHRoPScxMDAlJyBib3JkZXI9JzAnIGNlbGxwYWRkaW5nPScwJyBjZWxsc3BhY2luZz0nMicgXD5cPHRyXD5cPHRkXD4mbmJzcFw7XDwvdGRcPg0KXDx0ZCB3aWR0aD0nMTAwJScgYWxpZ249J2NlbnRlcicgbm93cmFwIGNsYXNzPSdtX3RkY29sb3JfMDYnXD5cPGEgaHJlZj0nZnJtRm9ybS5hc3B4P0Z1bklEPWE1NmNiZGNlZmMwMDNiMTYnXD5cPC9hXD5cPC90ZFw+XDx0ZFw+Jm5ic3BcO1w8L3RkXD5cPC90clw+XDwvdGFibGVcPlw8L3RkXD5cPC90clw+DQpcPHRyXD5cPHRkXD4NClw8dGFibGUgc3VtbWFyeT0n5o6S54mI55SoJyB3aWR0aD0nMTAwJScgYm9yZGVyPScwJyBjZWxscGFkZGluZz0nMCcgY2VsbHNwYWNpbmc9JzAnXD4NClw8dHJcPlw8dGRcPlw8aW1nIGFsdD0nJyBzcmM9Jy4uL2ltZy9sZWZ0X21lbnVfYjAxLmdpZicgd2lkdGg9JzYnIGhlaWdodD0nMjQnXD5cPC90ZFw+DQpcPHRkIHdpZHRoPScxMDAlJyBhbGlnbj0nY2VudGVyJyBub3dyYXAgYmFja2dyb3VuZD0nLi4vaW1nL2xlZnRfbWVudV9iMDIuZ2lmJyBjbGFzcz0nbV90aXRsZWZvbnRfMDInXD7ogbfmpa3lnJjpq5RcPC90ZFw+XDx0ZFw+XDxpbWcgYWx0PScnIHNyYz0nLi4vaW1nL2xlZnRfbWVudV9iMDMuZ2lmJyB3aWR0aD0nNicgaGVpZ2h0PScyNCdcPlw8L3RkXD5cPC90clw+XDwvdGFibGVcPlw8L3RkXD5cPC90clw+DQpcPHRyXD5cPHRkXD5cPHRhYmxlIHN1bW1hcnk9J+aOkueJiOeUqCcgd2lkdGg9JzEwMCUnIGJvcmRlcj0nMCcgY2VsbHBhZGRpbmc9JzAnIGNlbGxzcGFjaW5nPScyJyBcPlw8dHJcPlw8dGRcPiZuYnNwXDtcPC90ZFw+DQpcPHRkIHdpZHRoPScxMDAlJyBhbGlnbj0nY2VudGVyJyBub3dyYXAgY2xhc3M9J21fdGRjb2xvcl8wNidcPlw8YSBocmVmPSdmcm1GQVEuYXNweD9jbGFzcz0xY2UyNmU3MjZmMmRmYmJmJ1w+5bi46KaL5ZWP6aGM6ZuGXDwvYVw+XDwvdGRcPlw8dGRcPiZuYnNwXDtcPC90ZFw+XDwvdHJcPlw8L3RhYmxlXD5cPC90ZFw+XDwvdHJcPg0KXDx0clw+XDx0ZFw+XDx0YWJsZSBzdW1tYXJ5PSfmjpLniYjnlKgnIHdpZHRoPScxMDAlJyBib3JkZXI9JzAnIGNlbGxwYWRkaW5nPScwJyBjZWxsc3BhY2luZz0nMicgXD5cPHRyXD5cPHRkXD4mbmJzcFw7XDwvdGRcPg0KXDx0ZCB3aWR0aD0nMTAwJScgYWxpZ249J2NlbnRlcicgbm93cmFwIGNsYXNzPSdtX3RkY29sb3JfMDYnXD5cPGEgaHJlZj0nZnJtRm9ybS5hc3B4P0Z1bklEPTZjOGFlOGFlMGRlYjJmOTQnXD7ogbfmpa3lnJjpq5Tnm7jpl5zms5Xopo9cPC9hXD5cPC90ZFw+XDx0ZFw+Jm5ic3BcO1w8L3RkXD5cPC90clw+XDwvdGFibGVcPlw8L3RkXD5cPC90clw+DQpcPHRyXD5cPHRkXD5cPHRhYmxlIHN1bW1hcnk9J+aOkueJiOeUqCcgd2lkdGg9JzEwMCUnIGJvcmRlcj0nMCcgY2VsbHBhZGRpbmc9JzAnIGNlbGxzcGFjaW5nPScyJyBcPlw8dHJcPlw8dGRcPiZuYnNwXDtcPC90ZFw+DQpcPHRkIHdpZHRoPScxMDAlJyBhbGlnbj0nY2VudGVyJyBub3dyYXAgY2xhc3M9J21fdGRjb2xvcl8wNidcPlw8YSBocmVmPSdmcm1Gb3JtLmFzcHg/RnVuSUQ9NWQyMDA0YTNkMjJmNWFmOCdcPuiBt+alreWcmOmrlOeUs+iri+abuFw8L2FcPlw8L3RkXD5cPHRkXD4mbmJzcFw7XDwvdGRcPlw8L3RyXD5cPC90YWJsZVw+XDwvdGRcPlw8L3RyXD4NClw8dHJcPlw8dGRcPlw8dGFibGUgc3VtbWFyeT0n5o6S54mI55SoJyB3aWR0aD0nMTAwJScgYm9yZGVyPScwJyBjZWxscGFkZGluZz0nMCcgY2VsbHNwYWNpbmc9JzInIFw+XDx0clw+XDx0ZFw+Jm5ic3BcO1w8L3RkXD4NClw8dGQgd2lkdGg9JzEwMCUnIGFsaWduPSdjZW50ZXInIG5vd3JhcCBjbGFzcz0nbV90ZGNvbG9yXzA2J1w+XDxhIGhyZWY9J2ZybUZvcm0uYXNweD9GdW5JRD1lYWZhODIwMTc4ZWVmN2E3J1w+55Sz6KuL57WE57mU5YWo5ZyL5oCn6IG35qWt5ZyY6auU6aCI55+lXDwvYVw+XDwvdGRcPlw8dGRcPiZuYnNwXDtcPC90ZFw+XDwvdHJcPlw8L3RhYmxlXD5cPC90ZFw+XDwvdHJcPg0KOz4+Oz47Oz47Pj47dDxwPGw8VmlzaWJsZTs+O2w8bzxmPjs+PjtsPGk8MD47aTwyPjs+O2w8dDw7bDxpPDE+O2k8OD47PjtsPHQ8QDA8cDxwPGw8QXV0b1NldFNvcnRlZEluZm87UGFnZUNvdW50O1BhZ2VTaXplO1ZpcnR1YWxJdGVtQ291bnQ7XyFEYXRhU291cmNlSXRlbUNvdW50O18hSXRlbUNvdW50O0RhdGFLZXlzOz47bDxvPHQ+O2k8MTE+O2k8MTA+O2k8MTAzPjtpPDEwMz47aTwxMD47bDxpPDE3MD47aTwxNjk+O2k8MTY4PjtpPDE2Mz47aTwxNjQ+O2k8MTY1PjtpPDE2Mj47aTwxNTk+O2k8MTU4PjtpPDE1Nz47Pjs+Pjs+O0AwPDtAMDxwPGw8SGVhZGVyVGV4dDtGb290ZXJUZXh0O0hlYWRlckltYWdlVXJsOz47bDzmqJnpoYw7XGU7XGU7Pj47Ozs7Pjs7QDA8cDxsPEhlYWRlclRleHQ7Rm9vdGVyVGV4dDtIZWFkZXJJbWFnZVVybDs+O2w85pel5pyfO1xlO1xlOz4+Ozs7Oz47Ozs7Oz47cDxsPFBhZ2VyVmlzaWJsZTtIb3Jpem9udGFsQWxpZ247UG9zaXRpb247XyFTQjs+O2w8bzx0PjtTeXN0ZW0uV2ViLlVJLldlYkNvbnRyb2xzLkhvcml6b250YWxBbGlnbiwgU3lzdGVtLldlYiwgVmVyc2lvbj0xLjAuNTAwMC4wLCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPWIwM2Y1ZjdmMTFkNTBhM2E8Q2VudGVyPjtTeXN0ZW0uV2ViLlVJLldlYkNvbnRyb2xzLlBhZ2VyUG9zaXRpb24sIFN5c3RlbS5XZWIsIFZlcnNpb249MS4wLjUwMDAuMCwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj1iMDNmNWY3ZjExZDUwYTNhPEJvdHRvbT47aTwyNTIzMTM2MD47Pj47Ozs7Ozs7Oz47bDxpPDA+Oz47bDx0PDtsPGk8Mj47aTwzPjtpPDQ+O2k8NT47aTw2PjtpPDc+O2k8OD47aTw5PjtpPDEwPjtpPDExPjs+O2w8dDxwPDtwPGw8X1NlbGVjdDtfRWRpdDtfRGVsZXRlOz47bDxfX2RvUG9zdEJhY2soJ1VjQW5ub3VuY2VMaXN0MSRjZGdBTk5fTElTVCRfY3RsMyRfY3RsMScsJycpO19fZG9Qb3N0QmFjaygnVWNBbm5vdW5jZUxpc3QxJGNkZ0FOTl9MSVNUJF9jdGwzJF9jdGwyJywnJyk7X19kb1Bvc3RCYWNrKCdVY0Fubm91bmNlTGlzdDEkY2RnQU5OX0xJU1QkX2N0bDMkX2N0bDAnLCcnKTs+Pj47bDxpPDA+O2k8MT47aTwyPjtpPDM+O2k8ND47PjtsPHQ8O2w8aTwxPjs+O2w8dDxwPHA8bDxUZXh0Oz47bDwxOz4+Oz47Oz47Pj47dDxwPHA8bDxUZXh0Oz47bDzjgJDoqIrmga/ovYnnn6XjgJHmnInpl5zlj7DngaPnhKHpmpznpJnljZTmnIPovqbnkIbjgIzkuK3oj6/msJHlnIvnrKzkuozljYHlsYblhajlnIvljYHlpKflgpHlh7rmhJvlv4Plqr3lqr3mhYjmmonnjY7pgbjmi5TmtLvli5XjgI3pgbjmi5Toh7MxMDPlubQ05pyIMTXml6XmraLvvIjpg7XmiLPngrrmhpHvvIk7Pj47Pjs7Pjt0PDtsPGk8MT47aTwzPjs+O2w8dDxwPHA8bDxUZXh0Oz47bDxcPGlucHV0IG5hbWU9J2J0blJlYWQnIGlkPSdidG5SZWFkMScgdHlwZT0nc3VibWl0JyB2YWx1ZT0nWzE3MF3plrHoroAnIC9cPlw8c2NyaXB0XD4gdHJ5IHsgZG9jdW1lbnQuYWxsWydidG5SZWFkMSddLnN0eWxlLmRpc3BsYXkgPSAnbm9uZSdcOyB9IGNhdGNoKGUpIHt9IFw8L3NjcmlwdFw+Oz4+Oz47Oz47dDxwPHA8bDxUZXh0O0NvbW1hbmROYW1lO0NhdXNlc1ZhbGlkYXRpb247PjtsPOOAkOioiuaBr+i9ieefpeOAkeaciemXnOWPsOeBo+eEoemanOekmeWNlOacg+i+pueQhuOAjOS4reiPr+awkeWci+esrOS6jOWNgeWxhuWFqOWci+WNgeWkp+WCkeWHuuaEm+W/g+WqveWqveaFiOaaieeNjumBuOaLlOa0u+WLleOAjemBuOaLlOiHszEwM+W5tDTmnIgxNeaXpeatou+8iOmDteaIs+eCuuaGke+8iTtsYnRuQU5OX1RJVExFO288Zj47Pj47Pjs7Pjs+Pjt0PHA8cDxsPFRleHQ7PjtsPDIwMTQvMDMvMTc7Pj47Pjs7Pjt0PDtsPGk8MT47PjtsPHQ8cDxwPGw8VGV4dDs+O2w8MTAzLzAzLzE3Oz4+Oz47Oz47Pj47Pj47dDxwPDtwPGw8X1NlbGVjdDtfRWRpdDtfRGVsZXRlOz47bDxfX2RvUG9zdEJhY2soJ1VjQW5ub3VuY2VMaXN0MSRjZGdBTk5fTElTVCRfY3RsNCRfY3RsMScsJycpO19fZG9Qb3N0QmFjaygnVWNBbm5vdW5jZUxpc3QxJGNkZ0FOTl9MSVNUJF9jdGw0JF9jdGwyJywnJyk7X19kb1Bvc3RCYWNrKCdVY0Fubm91bmNlTGlzdDEkY2RnQU5OX0xJU1QkX2N0bDQkX2N0bDAnLCcnKTs+Pj47bDxpPDA+O2k8MT47aTwyPjtpPDM+O2k8ND47PjtsPHQ8O2w8aTwxPjs+O2w8dDxwPHA8bDxUZXh0Oz47bDwyOz4+Oz47Oz47Pj47dDxwPHA8bDxUZXh0Oz47bDzjgJDoqIrmga/ovYnnn6XjgJHmnInpl5zmraHllpzluIzmnJvnpL7mnIPnpo/liKnln7rph5HmnIPoiIfkuK3oj6/ml6XloLHnpL7lj4rlj7DljZfluILlqaboga/liIbmnIPlkIjovqYxMDPlubTjgIzlhajlnIvpnZ7lh6Hmr43mhJvnjY7jgI3pgbjmi5Tmmqjooajmj5roh7MxMDPlubQz5pyIMTjml6XmraI7Pj47Pjs7Pjt0PDtsPGk8MT47aTwzPjs+O2w8dDxwPHA8bDxUZXh0Oz47bDxcPGlucHV0IG5hbWU9J2J0blJlYWQnIGlkPSdidG5SZWFkMicgdHlwZT0nc3VibWl0JyB2YWx1ZT0nWzE2OV3plrHoroAnIC9cPlw8c2NyaXB0XD4gdHJ5IHsgZG9jdW1lbnQuYWxsWydidG5SZWFkMiddLnN0eWxlLmRpc3BsYXkgPSAnbm9uZSdcOyB9IGNhdGNoKGUpIHt9IFw8L3NjcmlwdFw+Oz4+Oz47Oz47dDxwPHA8bDxUZXh0O0NvbW1hbmROYW1lO0NhdXNlc1ZhbGlkYXRpb247PjtsPOOAkOioiuaBr+i9ieefpeOAkeaciemXnOatoeWWnOW4jOacm+ekvuacg+emj+WIqeWfuumHkeacg+iIh+S4reiPr+aXpeWgseekvuWPiuWPsOWNl+W4guWppuiBr+WIhuacg+WQiOi+pjEwM+W5tOOAjOWFqOWci+mdnuWHoeavjeaEm+eNjuOAjemBuOaLlOaaqOihqOaPmuiHszEwM+W5tDPmnIgxOOaXpeatojtsYnRuQU5OX1RJVExFO288Zj47Pj47Pjs7Pjs+Pjt0PHA8cDxsPFRleHQ7PjtsPDIwMTQvMDMvMTA7Pj47Pjs7Pjt0PDtsPGk8MT47PjtsPHQ8cDxwPGw8VGV4dDs+O2w8MTAzLzAzLzEwOz4+Oz47Oz47Pj47Pj47dDxwPDtwPGw8X1NlbGVjdDtfRWRpdDtfRGVsZXRlOz47bDxfX2RvUG9zdEJhY2soJ1VjQW5ub3VuY2VMaXN0MSRjZGdBTk5fTElTVCRfY3RsNSRfY3RsMScsJycpO19fZG9Qb3N0QmFjaygnVWNBbm5vdW5jZUxpc3QxJGNkZ0FOTl9MSVNUJF9jdGw1JF9jdGwyJywnJyk7X19kb1Bvc3RCYWNrKCdVY0Fubm91bmNlTGlzdDEkY2RnQU5OX0xJU1QkX2N0bDUkX2N0bDAnLCcnKTs+Pj47bDxpPDA+O2k8MT47aTwyPjtpPDM+O2k8ND47PjtsPHQ8O2w8aTwxPjs+O2w8dDxwPHA8bDxUZXh0Oz47bDwzOz4+Oz47Oz47Pj47dDxwPHA8bDxUZXh0Oz47bDzpoJDlkYrkv67mraPjgIzkurrmsJHlnJjpq5TpgbjoiInnvbflhY3ovqbms5XjgI3nrKwzNeaine+8jOiri+aWvOacrOWFrOWRiuWIiueZu+WFrOWgseS5i+aXpei1tzEw5pel5YWn6Zmz6L+w5oSP6KaL5oiW5rS96Kmi5YWn5pS/6YOo5ZCI5L2c5Y+K5Lq65rCR5ZyY6auU5Y+457GM5YKZ6JmV77yI5Lit6IiI77yJ6IG35qWt5ZyY6auU56eROz4+Oz47Oz47dDw7bDxpPDE+O2k8Mz47PjtsPHQ8cDxwPGw8VGV4dDs+O2w8XDxpbnB1dCBuYW1lPSdidG5SZWFkJyBpZD0nYnRuUmVhZDMnIHR5cGU9J3N1Ym1pdCcgdmFsdWU9J1sxNjhd6Zax6K6AJyAvXD5cPHNjcmlwdFw+IHRyeSB7IGRvY3VtZW50LmFsbFsnYnRuUmVhZDMnXS5zdHlsZS5kaXNwbGF5ID0gJ25vbmUnXDsgfSBjYXRjaChlKSB7fSBcPC9zY3JpcHRcPjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDtDb21tYW5kTmFtZTtDYXVzZXNWYWxpZGF0aW9uOz47bDzpoJDlkYrkv67mraPjgIzkurrmsJHlnJjpq5TpgbjoiInnvbflhY3ovqbms5XjgI3nrKwzNeaine+8jOiri+aWvOacrOWFrOWRiuWIiueZu+WFrOWgseS5i+aXpei1tzEw5pel5YWn6Zmz6L+w5oSP6KaL5oiW5rS96Kmi5YWn5pS/6YOo5ZCI5L2c5Y+K5Lq65rCR5ZyY6auU5Y+457GM5YKZ6JmV77yI5Lit6IiI77yJ6IG35qWt5ZyY6auU56eRO2xidG5BTk5fVElUTEU7bzxmPjs+Pjs+Ozs+Oz4+O3Q8cDxwPGw8VGV4dDs+O2w8MjAxNC8wMi8yMTs+Pjs+Ozs+O3Q8O2w8aTwxPjs+O2w8dDxwPHA8bDxUZXh0Oz47bDwxMDMvMDIvMjE7Pj47Pjs7Pjs+Pjs+Pjt0PHA8O3A8bDxfU2VsZWN0O19FZGl0O19EZWxldGU7PjtsPF9fZG9Qb3N0QmFjaygnVWNBbm5vdW5jZUxpc3QxJGNkZ0FOTl9MSVNUJF9jdGw2JF9jdGwxJywnJyk7X19kb1Bvc3RCYWNrKCdVY0Fubm91bmNlTGlzdDEkY2RnQU5OX0xJU1QkX2N0bDYkX2N0bDInLCcnKTtfX2RvUG9zdEJhY2soJ1VjQW5ub3VuY2VMaXN0MSRjZGdBTk5fTElTVCRfY3RsNiRfY3RsMCcsJycpOz4+PjtsPGk8MD47aTwxPjtpPDI+O2k8Mz47aTw0Pjs+O2w8dDw7bDxpPDE+Oz47bDx0PHA8cDxsPFRleHQ7PjtsPDQ7Pj47Pjs7Pjs+Pjt0PHA8cDxsPFRleHQ7PjtsPOaciemXnOOAjOWFqOWci+aAp+ekvuacg+WPiuiBt+alreWcmOmrlOWEquiJr+W3peS9nOS6uuWToemBuOaLlOimgem7nuOAjeaaqOmZhOS7tuWEquiJr+W3peS9nOS6uuWToeaOqOiWpuihqOaWvDEwM+W5tDLmnIgxOeaXpeWPsOWFp+WcmOWtl+esrDEwMzAwODkyNzEx6Jmf5Ye95L+u5q2jOz4+Oz47Oz47dDw7bDxpPDE+O2k8Mz47PjtsPHQ8cDxwPGw8VGV4dDs+O2w8XDxpbnB1dCBuYW1lPSdidG5SZWFkJyBpZD0nYnRuUmVhZDQnIHR5cGU9J3N1Ym1pdCcgdmFsdWU9J1sxNjNd6Zax6K6AJyAvXD5cPHNjcmlwdFw+IHRyeSB7IGRvY3VtZW50LmFsbFsnYnRuUmVhZDQnXS5zdHlsZS5kaXNwbGF5ID0gJ25vbmUnXDsgfSBjYXRjaChlKSB7fSBcPC9zY3JpcHRcPjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDtDb21tYW5kTmFtZTtDYXVzZXNWYWxpZGF0aW9uOz47bDzmnInpl5zjgIzlhajlnIvmgKfnpL7mnIPlj4rogbfmpa3lnJjpq5TlhKroia/lt6XkvZzkurrlk6Hpgbjmi5TopoHpu57jgI3mmqjpmYTku7blhKroia/lt6XkvZzkurrlk6HmjqjolqbooajmlrwxMDPlubQy5pyIMTnml6Xlj7DlhaflnJjlrZfnrKwxMDMwMDg5MjcxMeiZn+WHveS/ruatoztsYnRuQU5OX1RJVExFO288Zj47Pj47Pjs7Pjs+Pjt0PHA8cDxsPFRleHQ7PjtsPDIwMTQvMDIvMTk7Pj47Pjs7Pjt0PDtsPGk8MT47PjtsPHQ8cDxwPGw8VGV4dDs+O2w8MTAzLzAyLzE5Oz4+Oz47Oz47Pj47Pj47dDxwPDtwPGw8X1NlbGVjdDtfRWRpdDtfRGVsZXRlOz47bDxfX2RvUG9zdEJhY2soJ1VjQW5ub3VuY2VMaXN0MSRjZGdBTk5fTElTVCRfY3RsNyRfY3RsMScsJycpO19fZG9Qb3N0QmFjaygnVWNBbm5vdW5jZUxpc3QxJGNkZ0FOTl9MSVNUJF9jdGw3JF9jdGwyJywnJyk7X19kb1Bvc3RCYWNrKCdVY0Fubm91bmNlTGlzdDEkY2RnQU5OX0xJU1QkX2N0bDckX2N0bDAnLCcnKTs+Pj47bDxpPDA+O2k8MT47aTwyPjtpPDM+O2k8ND47PjtsPHQ8O2w8aTwxPjs+O2w8dDxwPHA8bDxUZXh0Oz47bDw1Oz4+Oz47Oz47Pj47dDxwPHA8bDxUZXh0Oz47bDzmnInpl5zjgIzlhajlnIvmgKfnpL7mnIPlnJjpq5TnuL7mlYjoqZXpkZHopoHpu57jgI3mmqjpmYTku7blubTluqblt6XkvZzloLHlkYrooajmlrwxMDPlubQy5pyIMTnml6Xlj7DlhaflnJjlrZfnrKwxMDMwMDg5MjcxMeiZn+WHveS/ruatozs+Pjs+Ozs+O3Q8O2w8aTwxPjtpPDM+Oz47bDx0PHA8cDxsPFRleHQ7PjtsPFw8aW5wdXQgbmFtZT0nYnRuUmVhZCcgaWQ9J2J0blJlYWQ1JyB0eXBlPSdzdWJtaXQnIHZhbHVlPSdbMTY0XemWseiugCcgL1w+XDxzY3JpcHRcPiB0cnkgeyBkb2N1bWVudC5hbGxbJ2J0blJlYWQ1J10uc3R5bGUuZGlzcGxheSA9ICdub25lJ1w7IH0gY2F0Y2goZSkge30gXDwvc2NyaXB0XD47Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7Q29tbWFuZE5hbWU7Q2F1c2VzVmFsaWRhdGlvbjs+O2w85pyJ6Zec44CM5YWo5ZyL5oCn56S+5pyD5ZyY6auU57i+5pWI6KmV6ZGR6KaB6bue44CN5pqo6ZmE5Lu25bm05bqm5bel5L2c5aCx5ZGK6KGo5pa8MTAz5bm0MuaciDE55pel5Y+w5YWn5ZyY5a2X56ysMTAzMDA4OTI3MTHomZ/lh73kv67mraM7bGJ0bkFOTl9USVRMRTtvPGY+Oz4+Oz47Oz47Pj47dDxwPHA8bDxUZXh0Oz47bDwyMDE0LzAyLzE5Oz4+Oz47Oz47dDw7bDxpPDE+Oz47bDx0PHA8cDxsPFRleHQ7PjtsPDEwMy8wMi8xOTs+Pjs+Ozs+Oz4+Oz4+O3Q8cDw7cDxsPF9TZWxlY3Q7X0VkaXQ7X0RlbGV0ZTs+O2w8X19kb1Bvc3RCYWNrKCdVY0Fubm91bmNlTGlzdDEkY2RnQU5OX0xJU1QkX2N0bDgkX2N0bDEnLCcnKTtfX2RvUG9zdEJhY2soJ1VjQW5ub3VuY2VMaXN0MSRjZGdBTk5fTElTVCRfY3RsOCRfY3RsMicsJycpO19fZG9Qb3N0QmFjaygnVWNBbm5vdW5jZUxpc3QxJGNkZ0FOTl9MSVNUJF9jdGw4JF9jdGwwJywnJyk7Pj4+O2w8aTwwPjtpPDE+O2k8Mj47aTwzPjtpPDQ+Oz47bDx0PDtsPGk8MT47PjtsPHQ8cDxwPGw8VGV4dDs+O2w8Njs+Pjs+Ozs+Oz4+O3Q8cDxwPGw8VGV4dDs+O2w86L6m55CGMTAy5bm05bqm5YWo5ZyL5oCn56S+5pyD5ZyY6auU57i+5pWI6KmV6ZGR5Y+K5YSq6Imv5bel5L2c5Lq65ZOh6YG45ouU5qGIOz4+Oz47Oz47dDw7bDxpPDE+O2k8Mz47PjtsPHQ8cDxwPGw8VGV4dDs+O2w8XDxpbnB1dCBuYW1lPSdidG5SZWFkJyBpZD0nYnRuUmVhZDYnIHR5cGU9J3N1Ym1pdCcgdmFsdWU9J1sxNjVd6Zax6K6AJyAvXD5cPHNjcmlwdFw+IHRyeSB7IGRvY3VtZW50LmFsbFsnYnRuUmVhZDYnXS5zdHlsZS5kaXNwbGF5ID0gJ25vbmUnXDsgfSBjYXRjaChlKSB7fSBcPC9zY3JpcHRcPjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDtDb21tYW5kTmFtZTtDYXVzZXNWYWxpZGF0aW9uOz47bDzovqbnkIYxMDLlubTluqblhajlnIvmgKfnpL7mnIPlnJjpq5TnuL7mlYjoqZXpkZHlj4rlhKroia/lt6XkvZzkurrlk6Hpgbjmi5TmoYg7bGJ0bkFOTl9USVRMRTtvPGY+Oz4+Oz47Oz47Pj47dDxwPHA8bDxUZXh0Oz47bDwyMDE0LzAyLzE5Oz4+Oz47Oz47dDw7bDxpPDE+Oz47bDx0PHA8cDxsPFRleHQ7PjtsPDEwMy8wMi8xOTs+Pjs+Ozs+Oz4+Oz4+O3Q8cDw7cDxsPF9TZWxlY3Q7X0VkaXQ7X0RlbGV0ZTs+O2w8X19kb1Bvc3RCYWNrKCdVY0Fubm91bmNlTGlzdDEkY2RnQU5OX0xJU1QkX2N0bDkkX2N0bDEnLCcnKTtfX2RvUG9zdEJhY2soJ1VjQW5ub3VuY2VMaXN0MSRjZGdBTk5fTElTVCRfY3RsOSRfY3RsMicsJycpO19fZG9Qb3N0QmFjaygnVWNBbm5vdW5jZUxpc3QxJGNkZ0FOTl9MSVNUJF9jdGw5JF9jdGwwJywnJyk7Pj4+O2w8aTwwPjtpPDE+O2k8Mj47aTwzPjtpPDQ+Oz47bDx0PDtsPGk8MT47PjtsPHQ8cDxwPGw8VGV4dDs+O2w8Nzs+Pjs+Ozs+Oz4+O3Q8cDxwPGw8VGV4dDs+O2w86L6m55CGMTAy5bm05bqm5YWo5ZyL5oCn5Y+K6Ie654Gj5Y2A5bel5ZWG5pqo6Ieq55Sx6IG35qWt5ZyY6auU57i+5pWI6KmV6ZGR5Y+K5YSq6Imv5bel5L2c5Lq65ZOh6YG45ouU5qGIOz4+Oz47Oz47dDw7bDxpPDE+O2k8Mz47PjtsPHQ8cDxwPGw8VGV4dDs+O2w8XDxpbnB1dCBuYW1lPSdidG5SZWFkJyBpZD0nYnRuUmVhZDcnIHR5cGU9J3N1Ym1pdCcgdmFsdWU9J1sxNjJd6Zax6K6AJyAvXD5cPHNjcmlwdFw+IHRyeSB7IGRvY3VtZW50LmFsbFsnYnRuUmVhZDcnXS5zdHlsZS5kaXNwbGF5ID0gJ25vbmUnXDsgfSBjYXRjaChlKSB7fSBcPC9zY3JpcHRcPjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDtDb21tYW5kTmFtZTtDYXVzZXNWYWxpZGF0aW9uOz47bDzovqbnkIYxMDLlubTluqblhajlnIvmgKflj4roh7rngaPljYDlt6XllYbmmqjoh6rnlLHogbfmpa3lnJjpq5TnuL7mlYjoqZXpkZHlj4rlhKroia/lt6XkvZzkurrlk6Hpgbjmi5TmoYg7bGJ0bkFOTl9USVRMRTtvPGY+Oz4+Oz47Oz47Pj47dDxwPHA8bDxUZXh0Oz47bDwyMDE0LzAxLzE3Oz4+Oz47Oz47dDw7bDxpPDE+Oz47bDx0PHA8cDxsPFRleHQ7PjtsPDEwMy8wMS8xNzs+Pjs+Ozs+Oz4+Oz4+O3Q8cDw7cDxsPF9TZWxlY3Q7X0VkaXQ7X0RlbGV0ZTs+O2w8X19kb1Bvc3RCYWNrKCdVY0Fubm91bmNlTGlzdDEkY2RnQU5OX0xJU1QkX2N0bDEwJF9jdGwxJywnJyk7X19kb1Bvc3RCYWNrKCdVY0Fubm91bmNlTGlzdDEkY2RnQU5OX0xJU1QkX2N0bDEwJF9jdGwyJywnJyk7X19kb1Bvc3RCYWNrKCdVY0Fubm91bmNlTGlzdDEkY2RnQU5OX0xJU1QkX2N0bDEwJF9jdGwwJywnJyk7Pj4+O2w8aTwwPjtpPDE+O2k8Mj47aTwzPjtpPDQ+Oz47bDx0PDtsPGk8MT47PjtsPHQ8cDxwPGw8VGV4dDs+O2w8ODs+Pjs+Ozs+Oz4+O3Q8cDxwPGw8VGV4dDs+O2w85pyJ6Zec44CM5YWo5ZyL5oCn5Y+K6Ie654Gj5Y2A5bel5ZWG5pqo6Ieq55Sx6IG35qWt5ZyY6auU57i+5pWI6KmV6ZGR6KaB6bue44CN5pqo6ZmE5Lu25bm05bqm5bel5L2c5aCx5ZGK6KGo5pa8MTAy5bm0MTLmnIgzMeaXpeWFp+aOiOS4reWcmOWtl+esrDEwMjU5MzI3MjbomZ/lh73kv67mraM7Pj47Pjs7Pjt0PDtsPGk8MT47aTwzPjs+O2w8dDxwPHA8bDxUZXh0Oz47bDxcPGlucHV0IG5hbWU9J2J0blJlYWQnIGlkPSdidG5SZWFkOCcgdHlwZT0nc3VibWl0JyB2YWx1ZT0nWzE1OV3plrHoroAnIC9cPlw8c2NyaXB0XD4gdHJ5IHsgZG9jdW1lbnQuYWxsWydidG5SZWFkOCddLnN0eWxlLmRpc3BsYXkgPSAnbm9uZSdcOyB9IGNhdGNoKGUpIHt9IFw8L3NjcmlwdFw+Oz4+Oz47Oz47dDxwPHA8bDxUZXh0O0NvbW1hbmROYW1lO0NhdXNlc1ZhbGlkYXRpb247PjtsPOaciemXnOOAjOWFqOWci+aAp+WPiuiHuueBo+WNgOW3peWVhuaaqOiHqueUseiBt+alreWcmOmrlOe4vuaViOiplemRkeimgem7nuOAjeaaqOmZhOS7tuW5tOW6puW3peS9nOWgseWRiuihqOaWvDEwMuW5tDEy5pyIMzHml6XlhafmjojkuK3lnJjlrZfnrKwxMDI1OTMyNzI26Jmf5Ye95L+u5q2jO2xidG5BTk5fVElUTEU7bzxmPjs+Pjs+Ozs+Oz4+O3Q8cDxwPGw8VGV4dDs+O2w8MjAxMy8xMi8zMTs+Pjs+Ozs+O3Q8O2w8aTwxPjs+O2w8dDxwPHA8bDxUZXh0Oz47bDwxMDIvMTIvMzE7Pj47Pjs7Pjs+Pjs+Pjt0PHA8O3A8bDxfU2VsZWN0O19FZGl0O19EZWxldGU7PjtsPF9fZG9Qb3N0QmFjaygnVWNBbm5vdW5jZUxpc3QxJGNkZ0FOTl9MSVNUJF9jdGwxMSRfY3RsMScsJycpO19fZG9Qb3N0QmFjaygnVWNBbm5vdW5jZUxpc3QxJGNkZ0FOTl9MSVNUJF9jdGwxMSRfY3RsMicsJycpO19fZG9Qb3N0QmFjaygnVWNBbm5vdW5jZUxpc3QxJGNkZ0FOTl9MSVNUJF9jdGwxMSRfY3RsMCcsJycpOz4+PjtsPGk8MD47aTwxPjtpPDI+O2k8Mz47aTw0Pjs+O2w8dDw7bDxpPDE+Oz47bDx0PHA8cDxsPFRleHQ7PjtsPDk7Pj47Pjs7Pjs+Pjt0PHA8cDxsPFRleHQ7PjtsPDEwMuW5tOW6puesrOS4ieWtoyDlhafmlL/pg6gg5Li7566hIOijnOWKqeWcmOmrlOWPiuWAi+S6uue2k+iyu+Wft+ihjOaDheW9ojs+Pjs+Ozs+O3Q8O2w8aTwxPjtpPDM+Oz47bDx0PHA8cDxsPFRleHQ7PjtsPFw8aW5wdXQgbmFtZT0nYnRuUmVhZCcgaWQ9J2J0blJlYWQ5JyB0eXBlPSdzdWJtaXQnIHZhbHVlPSdbMTU4XemWseiugCcgL1w+XDxzY3JpcHRcPiB0cnkgeyBkb2N1bWVudC5hbGxbJ2J0blJlYWQ5J10uc3R5bGUuZGlzcGxheSA9ICdub25lJ1w7IH0gY2F0Y2goZSkge30gXDwvc2NyaXB0XD47Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7Q29tbWFuZE5hbWU7Q2F1c2VzVmFsaWRhdGlvbjs+O2w8MTAy5bm05bqm56ys5LiJ5a2jIOWFp+aUv+mDqCDkuLvnrqEg6KOc5Yqp5ZyY6auU5Y+K5YCL5Lq657aT6LK75Z+36KGM5oOF5b2iO2xidG5BTk5fVElUTEU7bzxmPjs+Pjs+Ozs+Oz4+O3Q8cDxwPGw8VGV4dDs+O2w8MjAxMy8xMC8yMTs+Pjs+Ozs+O3Q8O2w8aTwxPjs+O2w8dDxwPHA8bDxUZXh0Oz47bDwxMDIvMTAvMjE7Pj47Pjs7Pjs+Pjs+Pjt0PHA8O3A8bDxfU2VsZWN0O19FZGl0O19EZWxldGU7PjtsPF9fZG9Qb3N0QmFjaygnVWNBbm5vdW5jZUxpc3QxJGNkZ0FOTl9MSVNUJF9jdGwxMiRfY3RsMScsJycpO19fZG9Qb3N0QmFjaygnVWNBbm5vdW5jZUxpc3QxJGNkZ0FOTl9MSVNUJF9jdGwxMiRfY3RsMicsJycpO19fZG9Qb3N0QmFjaygnVWNBbm5vdW5jZUxpc3QxJGNkZ0FOTl9MSVNUJF9jdGwxMiRfY3RsMCcsJycpOz4+PjtsPGk8MD47aTwxPjtpPDI+O2k8Mz47aTw0Pjs+O2w8dDw7bDxpPDE+Oz47bDx0PHA8cDxsPFRleHQ7PjtsPDEwOz4+Oz47Oz47Pj47dDxwPHA8bDxUZXh0Oz47bDznpL7mnIPlnJjpq5TovqbnkIblvoDnlJ/kupLliqnkuovpoIXoq4vkvp3jgIzlhafmlL/pg6jovJTlsI7npL7mnIPlnJjpq5TlvoDnlJ/kupLliqnkuovpoIXomZXnkIbljp/liYfjgI3ovqbnkIbjgII7Pj47Pjs7Pjt0PDtsPGk8MT47aTwzPjs+O2w8dDxwPHA8bDxUZXh0Oz47bDxcPGlucHV0IG5hbWU9J2J0blJlYWQnIGlkPSdidG5SZWFkMTAnIHR5cGU9J3N1Ym1pdCcgdmFsdWU9J1sxNTdd6Zax6K6AJyAvXD5cPHNjcmlwdFw+IHRyeSB7IGRvY3VtZW50LmFsbFsnYnRuUmVhZDEwJ10uc3R5bGUuZGlzcGxheSA9ICdub25lJ1w7IH0gY2F0Y2goZSkge30gXDwvc2NyaXB0XD47Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7Q29tbWFuZE5hbWU7Q2F1c2VzVmFsaWRhdGlvbjs+O2w856S+5pyD5ZyY6auU6L6m55CG5b6A55Sf5LqS5Yqp5LqL6aCF6KuL5L6d44CM5YWn5pS/6YOo6LyU5bCO56S+5pyD5ZyY6auU5b6A55Sf5LqS5Yqp5LqL6aCF6JmV55CG5Y6f5YmH44CN6L6m55CG44CCO2xidG5BTk5fVElUTEU7bzxmPjs+Pjs+Ozs+Oz4+O3Q8cDxwPGw8VGV4dDs+O2w8MjAxMy8wNy8yMjs+Pjs+Ozs+O3Q8O2w8aTwxPjs+O2w8dDxwPHA8bDxUZXh0Oz47bDwxMDIvMDcvMjI7Pj47Pjs7Pjs+Pjs+Pjs+Pjs+Pjt0PHA8cDxsPFZpc2libGU7PjtsPG88Zj47Pj47Pjs7Pjs+Pjt0PHA8cDxsPFZpc2libGU7PjtsPG88Zj47Pj47PjtsPGk8MT47aTwzPjtpPDU+O2k8Nz47PjtsPHQ8cDxwPGw8VGV4dDs+O2w86IG35qWt5ZyY6auUOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDxcPFBcPuS/guS6uuawkeWfuuaWvOWQjOS4gOiBt+alreiAjOe1hOe5lOS5i+WcmOmrlO+8jOWFtuaAp+izqui8g+iRl+mHjee2k+a/n+WxpOmdou+8jOS9huS4jeS7peeHn+WIqeeCuuebrueahO+8jOiAjOS/guS7peS/nemanOaIkOWToeasiuebiueCuuebruaome+8jOWMheaLrOW3pealreOAgeWVhualreOAgeiHqueUseiBt+alreOAgei+suawkeOAgea8gealreOAgeWLnuW3peetieWcmOmrlOOAglw8QlJcPuKAp+mAo+e1oembu+ipse+8mjA0OS0yMzkxNDAxIOKAp+mAo+e1oeWcsOWdgO+8mjU0MCDljZfmipXnuKPkuK3oiIjmlrDmnZHlupzopb/ot683MeiZnzPmqJMgXDwvUFw+Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDznpL7mnIPlnJjpq5Q7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPFw8UFw+5L+C5Lq65rCR5Z+65pa85b+X6Laj44CB5L+h5Luw44CB5Zyw57ej5oiW6KGA57ej5LmL55u45ZCM6ICM57WE5oiQ5LmL5ZyY6auU77yM5YW25oCn6LOq6LyD6JGX6YeN56S+5pyD5bGk6Z2i77yM57SU5Lul5YCL5Lq66IiI6Laj5LmL5ru/6Laz5oiW55CG5oOz5LmL5a+m54++54K655uu55qE77yM5YyF5ous5a246KGT5paH5YyW44CB56S+5pyD5pyN5YuZ5Y+K5oWI5ZaE44CB6Yar55mC6KGb55Sf44CB5a6X5pWZ44CB6auU6IKy44CB5ZyL6Zqb44CB57aT5r+f5qWt5YuZ44CB5a6X6Kaq5pyD562J5ZyY6auU44CCXDxCUlw+4oCn6YCj57Wh6Zu76Kmx77yaMDItMjM1NjUyMDbjgIE1MjAy44CBNTE5MeKAp+mAo+e1oeWcsOWdgO+8mjEwMCDlj7DljJfluILlvpDlt57ot6816JmfIFw8L1BcPjs+Pjs+Ozs+Oz4+Oz4+O3Q8cDxwPGw8VmlzaWJsZTs+O2w8bzx0Pjs+Pjs+O2w8aTwwPjtpPDE+Oz47bDx0PDtsPGk8Mz47aTw3PjtpPDExPjtpPDE1PjtpPDI3PjtpPDMxPjtpPDM1Pjs+O2w8dDw7bDxpPDA+Oz47bDx0PHA8cDxsPE1lc3NQYXJhbTs+O2w8XGU7Pj47Pjs7Pjs+Pjt0PHQ8cDxwPGw8RGF0YVZhbHVlRmllbGQ7RGF0YVRleHRGaWVsZDs+O2w8Q09ERV9JRDtDT0RFX05BTUU7Pj47Pjt0PGk8Mz47QDxcZTvnpL7mnIPlnJjpq5Q76IG35qWt5ZyY6auUOz47QDxcZTtTO087Pj47Pjs7Pjt0PHQ8O3A8bDxpPDA+Oz47bDxwPOiri+WFiOmBuOaTh+WcmOmrlOWIhumhnjtcZT47Pj47Pjs7Pjt0PDtsPGk8MD47PjtsPHQ8cDxwPGw8TWVzc1BhcmFtOz47bDxcZTs+Pjs+Ozs+Oz4+O3Q8O2w8aTwwPjs+O2w8dDxwPHA8bDxNZXNzUGFyYW07PjtsPFxlOz4+Oz47Oz47Pj47dDw7bDxpPDA+O2k8Mj47PjtsPHQ8O2w8aTwwPjs+O2w8dDxwPHA8bDxNZXNzUGFyYW07PjtsPFxlOz4+Oz47Oz47Pj47dDw7bDxpPDA+Oz47bDx0PHA8cDxsPE1lc3NQYXJhbTs+O2w8XGU7Pj47Pjs7Pjs+Pjs+Pjt0PDtsPGk8MD47PjtsPHQ8cDxwPGw8TWVzc1BhcmFtOz47bDxcZTs+Pjs+Ozs+Oz4+Oz4+O3Q8O2w8aTwxPjs+O2w8dDxAMDw7Ozs7Ozs7Ozs7Pjs7Pjs+Pjs+Pjt0PHA8cDxsPFZpc2libGU7PjtsPG88Zj47Pj47PjtsPGk8MT47aTwzPjs+O2w8dDw7bDxpPDA+Oz47bDx0PHA8cDxsPE1lc3NQYXJhbTs+O2w8XGU7Pj47Pjs7Pjs+Pjt0PHA8O3A8bDxvbmtleXByZXNzOz47bDxqYXZhc2NyaXB0OnRoaXMuY2xpY2soKVw7Oz4+Pjs7Pjs+Pjt0PDtsPGk8MT47aTwzPjtpPDU+O2k8Nz47PjtsPHQ8O2w8aTwwPjs+O2w8dDxwPHA8bDxNZXNzUGFyYW07PjtsPOiri+i8uOWFpeW4s+iZnzs+Pjs+Ozs+Oz4+O3Q8O2w8aTwwPjs+O2w8dDxwPHA8bDxNZXNzUGFyYW07PjtsPOiri+i8uOWFpeWvhueivDs+Pjs+Ozs+Oz4+O3Q8cDw7cDxsPG9ua2V5cHJlc3M7PjtsPGphdmFzY3JpcHQ6dGhpcy5jbGljaygpXDs7Pj4+Ozs+O3Q8cDw7cDxsPG9ua2V5cHJlc3M7PjtsPGphdmFzY3JpcHQ6dGhpcy5jbGljaygpXDs7Pj4+Ozs+Oz4+O3Q8O2w8aTwxPjs+O2w8dDxwPHA8bDxUZXh0Oz47bDxcPHRhYmxlIHN1bW1hcnk9J+aOkueJiOeUqCcgd2lkdGg9JzEwMCUnIGJvcmRlcj0nMCcgY2VsbHBhZGRpbmc9JzAnIGNlbGxzcGFjaW5nPScwJ1w+XDx0ciB2YWxpZ249J3RvcCdcPlw8dGRcPlw8aW1nIGFsdD0nJyBzcmM9Jy4uL2ltZy9naWZfZGluMi5naWYnIGhzcGFjZT0nNScgdnNwYWNlPSc1J1w+XDwvdGRcPlw8dGQgd2lkdGg9JzEwMCUnXD5cPGEgaHJlZj0naHR0cDovL3d3dy5tb2kuZ292LnR3LycgY2xhc3M9J1JpZ2h0bGluaycgdGFyZ2V0PSdfYmxhbmsnXD7kuK3oj6/msJHlnIvlhafmlL/pg6jlhajnkIPos4foqIrntrJcPC9hXD5cPC90ZFw+XDwvdHJcPlw8dHIgdmFsaWduPSd0b3AnXD5cPHRkXD5cPGltZyBhbHQ9Jycgc3JjPScuLi9pbWcvZ2lmX2RpbjIuZ2lmJyBoc3BhY2U9JzUnIHZzcGFjZT0nNSdcPlw8L3RkXD5cPHRkIHdpZHRoPScxMDAlJ1w+XDxhIGhyZWY9J2h0dHA6Ly9sYXcubW9qLmdvdi50dy8jJyBjbGFzcz0nUmlnaHRsaW5rJyB0YXJnZXQ9J19ibGFuaydcPuWFqOWci+azleimj+izh+aWmeW6q1w8L2FcPlw8L3RkXD5cPC90clw+XDx0ciB2YWxpZ249J3RvcCdcPlw8dGRcPlw8aW1nIGFsdD0nJyBzcmM9Jy4uL2ltZy9naWZfZGluMi5naWYnIGhzcGFjZT0nNScgdnNwYWNlPSc1J1w+XDwvdGRcPlw8dGQgd2lkdGg9JzEwMCUnXD5cPGEgaHJlZj0naHR0cDovL3d3dy5tb2kuZ292LnR3L2RzYS8nIGNsYXNzPSdSaWdodGxpbmsnIHRhcmdldD0nX2JsYW5rJ1w+5YWn5pS/6YOo56S+5pyD5Y+4XDwvYVw+XDwvdGRcPlw8L3RyXD5cPHRyIHZhbGlnbj0ndG9wJ1w+XDx0ZFw+XDxpbWcgYWx0PScnIHNyYz0nLi4vaW1nL2dpZl9kaW4yLmdpZicgaHNwYWNlPSc1JyB2c3BhY2U9JzUnXD5cPC90ZFw+XDx0ZCB3aWR0aD0nMTAwJSdcPlw8YSBocmVmPSdodHRwOi8vY3dycC5tb2kuZ292LnR3L21haWxzLmFzcHgnIGNsYXNzPSdSaWdodGxpbmsnIHRhcmdldD0nX2JsYW5rJ1w+5oCn5Yil5bmz562J5L+h566xXDwvYVw+XDwvdGRcPlw8L3RyXD5cPHRyIHZhbGlnbj0ndG9wJ1w+XDx0ZFw+XDxpbWcgYWx0PScnIHNyYz0nLi4vaW1nL2dpZl9kaW4yLmdpZicgaHNwYWNlPSc1JyB2c3BhY2U9JzUnXD5cPC90ZFw+XDx0ZCB3aWR0aD0nMTAwJSdcPlw8YSBocmVmPSdodHRwOi8vd3d3LmNuZmkub3JnLnR3LycgY2xhc3M9J1JpZ2h0bGluaycgdGFyZ2V0PSdfYmxhbmsnXD7kuK3oj6/msJHlnIvlhajlnIvlt6Xmpa3nuL3mnINcPC9hXD5cPC90ZFw+XDwvdHJcPlw8dHIgdmFsaWduPSd0b3AnXD5cPHRkXD5cPGltZyBhbHQ9Jycgc3JjPScuLi9pbWcvZ2lmX2RpbjIuZ2lmJyBoc3BhY2U9JzUnIHZzcGFjZT0nNSdcPlw8L3RkXD5cPHRkIHdpZHRoPScxMDAlJ1w+XDxhIGhyZWY9J2h0dHA6Ly93d3cucm9jY29jLm9yZy50dy8nIGNsYXNzPSdSaWdodGxpbmsnIHRhcmdldD0nX2JsYW5rJ1w+5Lit6I+v5rCR5ZyL5YWo5ZyL5ZWG5qWt57i95pyDXDwvYVw+XDwvdGRcPlw8L3RyXD5cPHRyIHZhbGlnbj0ndG9wJ1w+XDx0ZFw+XDxpbWcgYWx0PScnIHNyYz0nLi4vaW1nL2dpZl9kaW4yLmdpZicgaHNwYWNlPSc1JyB2c3BhY2U9JzUnXD5cPC90ZFw+XDx0ZCB3aWR0aD0nMTAwJSdcPlw8YSBocmVmPSdodHRwOi8vd3d3LmNzYS5vcmcudHcvJyBjbGFzcz0nUmlnaHRsaW5rJyB0YXJnZXQ9J19ibGFuaydcPuS4reiPr+awkeWci+itieWIuOWVhualreWQjOalreWFrOacg1w8L2FcPlw8L3RkXD5cPC90clw+XDx0ciB2YWxpZ249J3RvcCdcPlw8dGRcPlw8aW1nIGFsdD0nJyBzcmM9Jy4uL2ltZy9naWZfZGluMi5naWYnIGhzcGFjZT0nNScgdnNwYWNlPSc1J1w+XDwvdGRcPlw8dGQgd2lkdGg9JzEwMCUnXD5cPGEgaHJlZj0naHR0cDovL3d3dy4yMjgub3JnLnR3LycgY2xhc3M9J1JpZ2h0bGluaycgdGFyZ2V0PSdfYmxhbmsnXD7osqHlnJjms5Xkurrkuozkuozlhavkuovku7bntIDlv7Xln7rph5HmnINcPC9hXD5cPC90ZFw+XDwvdHJcPlw8L3RhYmxlXD47Pj47Pjs7Pjs+Pjs+Pjs+PjtsPFVjQ29RdWVyeVJlc3VsdDE6cmRvU1RBVFVTX0UxO1VjQ29RdWVyeVJlc3VsdDE6cmRvU1RBVFVTX0UxO1VjQ29RdWVyeVJlc3VsdDE6cmRvU1RBVFVTX0UyO1VjQ29RdWVyeVJlc3VsdDE6cmRvU1RBVFVTX0UyO1VjQ29RdWVyeVJlc3VsdDE6cmRvU1RBVFVTX0UzO1VjTG9naW4yOmlidG5fTE9HSU47VWNMb2dpbjI6aWJ0bl9GT1JHRVQ7Pj5FEVXOs2u/OLWkVWucUFul/QTLrQ==',
		'UcCoQueryResult1:txtQ_CO_NAME:EditText' : '',
		'UcCoQueryResult1:drpQ_CO_CLASS' : '',
		'UcCoQueryResult1:drpQ_CO_TYPE' : '',
		'UcCoQueryResult1:txtQ_DIRECTOR:EditText' : '',
		'UcCoQueryResult1:STATUS' : 'rdoSTATUS_E3',
		'UcCoQueryResult1:txtQ_E_AGREE_ESTABLISH_DOC:EditText' : '',
		'UcCoQueryResult1:idpQ_LEGAL_DTE:txtPreBox:txtDate' : '',
		'UcCoQueryResult1:idpQ_LEGAL_DTE:txtPostBox:txtDate' : '',
		'UcCoQueryResult1:txtQ_ASSOCIATION_ADDR:EditText' : '',
		'UcCoQueryResult1:btnQuery' : '查詢',
		'UcCoQueryResult1:dgA_Main:_ctl5:txtPageSize' : '10',
		'UcCoQueryResult1:dgA_Main:_ctl5:drpPageCount' : '1',
		'UcLogin2:txt_E_ACCOUNT_ID:EditText' : '',
		'UcLogin2:txt_E_PASSWORD:EditText' : '',
		'UcCoQueryResult1_dgA_Main_SelectedIndex' : '-1'
	}
	headers = {'content-type': 'application/json'}

	req = requests.post(url, data=json.dumps(getValue), headers=payload)
	print(req.url)
	print(req.headers)

	print(req.text)


if __name__ == "__main__":
	#JsonData(str(243368320))
	WebRequest('http://cois.moi.gov.tw/moiweb/web/frmHome.aspx')


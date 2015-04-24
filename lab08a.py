 #################
# Simon Milburn   #
# UID: 112385125  #
# GEOG376 - 0102  #
# lab08a.py       #
# 4/23/2015       #
 #################

#dl weather data from online to .txt

import urllib

path = "/Users/smilburn/Desktop/lab08/"

#stations in towson/timonium MD
stations = ["KMDPHOEN3", "KMDTOWSO2", "KMDTOWSO3", "KMDTOWSO4", "KMDTIMON1"]
months = ['1','2','3']

#part of url that never changes
wunder = "http://www.wunderground.com/weatherstation/WXDailyHistory.asp?"

#iterating through weather stations Jan-Mar
for s in stations:
	for m in months:
		url = wunder + "ID=%s&day=25&month=%d&year=2014&dayend=24&monthend=4&yearend=2014&graphspan=custom&format=1" % (s,m)
		data = urllib.urlopen(url).read()
		out = open(path + s + '_' + m + '.txt', "w")
		out.write(data) #filling new file
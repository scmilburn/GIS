 #################
# Simon Milburn   #
# UID: 112385125  #
# GEOG376 - 0102  #
# lab08b.py       #
# 4/23/2015       #
 #################

#parser
import fileinput

path = "/Users/smilburn/Desktop/lab08/"

#stations in towson/timonium MD
stations = ["KMDPHOEN3", "KMDTOWSO2", "KMDTOWSO3", "KMDTOWSO4", "KMDTIMON1"]
months = ['1','2','3']

for s in stations:
	for m in months:
		for line in fileinput.input(path + s + '_' + m + '.txt', inplace=True)
			line.replace(texttosearch, texttoreplace, end='')

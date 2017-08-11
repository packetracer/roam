import subprocess

def detectRoam(BSSID):
	roam = False
	print "Monitoring... "
	while roam == False:
		output = subprocess.check_output("netsh wlan show interfaces")
		output = output.split('\r\n')
		for item in output:
			if ("BSSID" in item):
				curBSSID = item.split(": ")[1]
				if not (curBSSID == BSSID):
					roam = True
					print "Roam Detected\nOld BSSID: " + BSSID + "\nNew BSSID: " + curBSSID
					detectRoam(curBSSID)

def initBSSID():					
	output = subprocess.check_output("netsh wlan show interfaces")
	output = output.split('\r\n')
	for item in output:
		if ("BSSID" in item):
			BSSID = item.split(": ")[1]
			print "Current BSSID: " + BSSID
	return BSSID

BSSID = initBSSID()
detectRoam(BSSID)

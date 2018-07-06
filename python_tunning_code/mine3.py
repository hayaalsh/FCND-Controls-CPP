import fileinput
import time

rate = 0.4

def drange(start, stop, step):
    while start < stop:
            yield start
            start += step
# (1)
for kpYaw in drange(2,4,rate):
	for line in fileinput.input("./FCND-Term1-Starter-Kit/FCND-Controls/FCND-Controls-CPP/config/QuadControlParams.txt", inplace=True):
		if line.strip().startswith('kpYaw = '):
			line = 'kpYaw = %s\n' % str(kpYaw)
		print line,
	# (2)
	for kpPQRz in drange(10,20,4):
		for line in fileinput.input("./FCND-Term1-Starter-Kit/FCND-Controls/FCND-Controls-CPP/config/QuadControlParams.txt", inplace=True):
			if line.strip().startswith('kpPQR = '):
				line = 'kpPQR = 60, 50, %s\n' % str(kpPQRz)
			print line,
		print(kpYaw)
		print(kpPQRz)
		time.sleep(2.5)





import fileinput
import time

kpPosXY_min = 3.0
kpPosXY_max = 4.01

kpVelXY_min = 6.0
kpVelXY_max = 16.01

def drange(start, stop, step):
    while start < stop:
            yield start
            start += step

# (1)
for kpPosXY in drange(kpPosXY_min,kpPosXY_max,0.1):

	for line in fileinput.input("./FCND-Term1-Starter-Kit/FCND-Controls/FCND-Controls-CPP/config/QuadControlParams.txt", inplace=True):
		if line.strip().startswith('kpPosXY = '):
			line = 'kpPosXY = %s\n' % str(kpPosXY)
		print line,

	

	# (2)
	for kpVelXY in drange(kpVelXY_min,kpVelXY_max,0.1):
		if kpVelXY > 4*kpPosXY or kpVelXY < 3*kpPosXY:
			continue

		for line in fileinput.input("./FCND-Term1-Starter-Kit/FCND-Controls/FCND-Controls-CPP/config/QuadControlParams.txt", inplace=True):
			if line.strip().startswith('kpVelXY = '):
				line = 'kpVelXY = %s\n' % str(kpVelXY)
			print line,

		print(kpPosXY)
		print(kpVelXY)
		time.sleep(2.5)





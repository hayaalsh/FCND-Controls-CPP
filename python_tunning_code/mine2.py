import fileinput
import time

rate = 0.1

kpPosXY_min = 2.9
kpPosXY_max = 3.9

kpPosZ_min = 2.6
kpPosZ_max = 3.9

def drange(start, stop, step):
    while start < stop:
            yield start
            start += step

# (1)
for kpPosXY in drange(kpPosXY_min,kpPosXY_max,rate):
	kpVelXY = 3.9*kpPosXY

	for line in fileinput.input("./FCND-Term1-Starter-Kit/FCND-Controls/FCND-Controls-CPP/config/QuadControlParams.txt", inplace=True):
		if line.strip().startswith('kpPosXY = '):
			line = 'kpPosXY = %s\n' % str(kpPosXY)
		elif line.strip().startswith('kpVelXY = '):
			line = 'kpVelXY = %s\n' % str(kpVelXY)
		print line,

	# (2)
	for kpPosZ in drange(kpPosXY_min,kpPosXY_max,rate):
		kpVelZ = 3.9*kpPosZ

		for line in fileinput.input("./FCND-Term1-Starter-Kit/FCND-Controls/FCND-Controls-CPP/config/QuadControlParams.txt", inplace=True):
			if line.strip().startswith('kpPosZ = '):
				line = 'kpPosZ = %s\n' % str(kpPosZ)
			elif line.strip().startswith('kpVelZ = '):
				line = 'kpVelZ = %s\n' % str(kpVelZ)
			print line,

		print(kpPosXY)
		print(kpPosZ)
		print(kpVelXY)
		print(kpVelZ)

		time.sleep(2.5)





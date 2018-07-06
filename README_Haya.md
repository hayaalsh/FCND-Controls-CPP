# CONTROLLRES:
## Body rate control:
A proportional controller on body rates was implemented. A major faced problem was forgetting to include the moment of inertia, however, after reading the rubrics and the comments, it was added.

## Roll pitch control:
The controller was implemented using the python implementation. No major problem was faced here.

## Altitude controller:
The most tricky part here was the direction. I had to play with the signs for days until I figured it out. The integrator addition was simple and clear.

## Lateral position control:
The PD controller initially was a bit tricky and confusing especially with the false comments on the Slack community! A revision of the material clarified things up. 

## Yaw control:
The comment section contained a mistake about the functionality of fmod. Slack community clarified it.

## GenerateMotorCommands: 
This was the most confusing bit of the course. Nice documentation from one of the students clarified everything!

# OVERALL CONTROLLER & TUNING: 
The drone looks stable and performs the required task in all scenarios and can handle the non-linearities of scenario 4. For an initial tuning of kpPosXY, KpPosZ, KpVelXY, KpVelZ I followed an exhaustive search approach using a python code I wrote that can be found below:
```
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

	for line in fileinput.input("./config/QuadControlParams.txt", inplace=True):
		if line.strip().startswith('kpPosXY = '):
			line = 'kpPosXY = %s\n' % str(kpPosXY)
		elif line.strip().startswith('kpVelXY = '):
			line = 'kpVelXY = %s\n' % str(kpVelXY)
		print line,

	# (2)
	for kpPosZ in drange(kpPosZ_min,kpPosZ_max,rate):
		kpVelZ = 3.9*kpPosZ

		for line in fileinput.input("./config/QuadControlParams.txt", inplace=True):
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
```

For tuning kpYaw and kpPQRz, a similar python code was used: 
```
import fileinput
import time

rate = 0.4

def drange(start, stop, step):
    while start < stop:
            yield start
            start += step
# (1)
for kpYaw in drange(2,4,rate):
	for line in fileinput.input("./config/QuadControlParams.txt", inplace=True):
		if line.strip().startswith('kpYaw = '):
			line = 'kpYaw = %s\n' % str(kpYaw)
		print line,
	# (2)
	for kpPQRz in drange(10,20,4):
		for line in fileinput.input("./config/QuadControlParams.txt", inplace=True):
			if line.strip().startswith('kpPQR = '):
				line = 'kpPQR = 60, 50, %s\n' % str(kpPQRz)
			print line,
		print(kpYaw)
		print(kpPQRz)
		time.sleep(2.5)
```
Further manual tunings were done at each stage to achieve optimal results.


# VIDEO:
A short video of the drone in different situations can be found [here](https://drive.google.com/file/d/1w8f0rQQPTc9KFx-H51lmTkieBE3Ymobk/view?usp=sharing).
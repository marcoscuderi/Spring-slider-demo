# Spring-slider-demo

The purpose of this demo is to explore in class the basic concepts of earthquake physics.# 
At the following link it is possible to find a detailed explanation of the rationale behind this demo.
K.Linton and R. Stein 2012 SRL
https://www.seismosoc.org/Publications/SRL/SRL_83/srl_83-1_eq/

My version of the QuakeSimulator is designed to show in real time the movement of the block and record the data.
This is useful to analyze the results and build exercises for the students.
I have added a short video of a portion of one demontration I made in class (my students are italians so excuse me if you do not understand). 

# Main Components

The system is characterized by (figure 1):
1) A direct current motor (https://en.wikipedia.org/wiki/DC_motor) that I have cannibalized from an old printer that was disused.
2) A home made circuit with a potentiometer to regulate the velocity of the motor. 
If you don't have the possibility to build this circuit there are some out of shelf products that can do this for you.
Note that the circuit is not necessary, the motor can also be powered directly by direct current and it will move at a single speed. 
3) Arduino Uno board (see figure 2 for a schematic of the circuit and connection to the arduino board)
4) A potentiometer to measure displacement. (https://www.cw-industrialgroup.com/Products/Sensors/Linear-Position-Sensors-Transducers/Linear-Displacement-Sensor-SLS130)
5) A potentiometer holder. I have a friend that works at a machine shop that can easily work aluminum.
I recommend to contact a machine shop.
In the future I will make a second version that will use an ultrasonic sensor to measure displacement which doesn't need the building of a holder. Once tested I will upload the code and instructions.
6) Sand paper of different roughness
7) A block slider. I used a cube of carbonate rock, I live in the appennines and this is the most common rock. You can choose any rock (or other material) you like.
8) Springs with different stiffness. Those are very easy to find in any hardware store. 

# Codes

1) arduino_setup.ino
This is the code that must be uploaded to the Arduino Uno board to allow the readings of the potentiometer.
2) python_recording
This code should be executed in python and allows to show real time data and record the data
3) calibration 
for the ones that are not used to laboratory work, the potentiometer needs to be calibrated to converst the voltage readings in engineering units of displacement. The calibration shold be done manually and it should result in something similar as reported from the excution of this script. The slope represents the calibration number.

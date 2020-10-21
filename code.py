#disclaimer, I haven't seen the robot in action yet, so I *think*
#thats what FORWARD and REVERSE should look like, but I don't actually know - HL

#def forward():
    #left_motor.spin(FORWARD)
    #right_motor.spin(FORWARD)

#def backward():
    #left_motor.spin(REVERSE)
    #right_motor.spin(REVERSE)

#activate the left and back motors to work in the same direction
#activate the right motor to balance the motion in the opposite direction
def move_left():
    left_motor.spin(FORWARD)
    right_motor.spin(REVERSE)
    back_motor.spin(REVERSE)

#activate the right and back motors to work in the same direction
#activate the left motor to balance the motion in the opposite direction
#def move_right():
    #left_motor(REVERSE)
    #right_motor(FORWARD)
    #back_motor(FORWARD)

#"turn left" is really more like backup in the left direction, need to observe action of robot
#def turn_left():
    #left_motor.spin(REVERSE)
    #back_motor.spin(REVERSE)
    #right_motor.spin(FORWARD)
    
#"turn right" is really more like backup in the right direction, need to observe action of robot
#def turn_right():
    #left_motor.spin(FORWARD)
    #right_motor.spin(REVERSE)
    #back_motor.spin(FORWARD)

while True:
    
        axis3Value = controller_1.axis3.position();
        axis4Value = controller_1.axis4.position();

        left_motor.spin(FORWARD, (axis3Value + axis4Value * 0.666), PERCENT)
        right_motor.spin(FORWARD, (axis3Value + axis4Value * -0.666), PERCENT)
        back_motor.spin(REVERSE, (axis4Value), PERCENT)

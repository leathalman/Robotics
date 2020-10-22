#"turn left" is really more like backup in the left direction, need to observe action of robot
#def turn_left():
    #left_motor.spin(REVERSE, 100, PERCENT)
    #back_motor.spin(REVERSE, 100, PERCENT)
    #right_motor.spin(FORWARD, 100, PERCENT)
    
#"turn right" is really more like backup in the right direction, need to observe action of robot
#def turn_right():
    #left_motor.spin(FORWARD, 100, PERCENT)
    #right_motor.spin(REVERSE, 100, PERCENT)
    #back_motor.spin(FORWARD, 100, PERCENT)

while True:
        axis1Value = controller_1.axis1.position();
        axis3Value = controller_1.axis3.position();
        axis4Value = controller_1.axis4.position();

        if axis1Value < -5 :
            left_motor.spin(REVERSE, axis1Value * -1, PERCENT)
            back_motor.spin(REVERSE, axis1Value  * -1, PERCENT)
            right_motor.spin(FORWARD, axis1Value  * -1, PERCENT)
        elif axis1Value > 5 :
            left_motor.spin(FORWARD, axis1Value, PERCENT)
            right_motor.spin(REVERSE, axis1Value, PERCENT)
            back_motor.spin(FORWARD, axis1Value, PERCENT)
        else :    
            left_motor.spin(FORWARD, (axis3Value + axis4Value * 0.666), PERCENT)
            right_motor.spin(FORWARD, (axis3Value + axis4Value * -0.666), PERCENT)
            back_motor.spin(REVERSE, (axis4Value), PERCENT)
            

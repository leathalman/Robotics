#included components
#   left_motor set to "normal" on port 2
#   right_motor set to "normal" on port 11
#   back_motor set to "normal" on port 1
#   left_grab_motor set to "normal" on port 4
#   right_grab_motor set to "normal" on port 12

#All directions dictated with brain screen facing viewer (behind robot)

while True:

    #represents the right chain
    if controller_1.buttonR1.pressing() :
        right_grab_motor.spin(FORWARD, 75, PERCENT)
    elif controller_1.buttonR2.pressing() :
        right_grab_motor.spin(REVERSE, 75, PERCENT)
    else :
        right_grab_motor.stop()

    #represents the left grabber
    if controller_1.buttonL1.pressing() :
        left_grab_motor.spin(FORWARD, 100, PERCENT)
    elif controller_1.buttonL2.pressing() :
        left_grab_motor.spin(REVERSE, 100, PERCENT)
    else : 
        left_grab_motor.stop()

    #axis 1, right joystick on x-axis
    #axis 3, left joystick on y-axis
    #axis 4, left joystick on x-axis
    axis1Value = controller_1.axis1.position()
    axis3Value = controller_1.axis3.position()
    axis4Value = controller_1.axis4.position()

    #axis 1 in negative x direction (pushed to left side)
    #sensitivity deadzone for values 1...5 
    if axis1Value < -5 :
        left_motor.spin(REVERSE, axis1Value * -1, PERCENT)
        back_motor.spin(REVERSE, axis1Value  * -1, PERCENT)
        right_motor.spin(REVERSE, axis1Value  * -1, PERCENT)

    #axis 1 in positive x direction (pushed to right side)
    #sensitivity deadzone for values 1...5 
    elif axis1Value > 5 :
        left_motor.spin(FORWARD, axis1Value, PERCENT)
        right_motor.spin(FORWARD, axis1Value, PERCENT)
        back_motor.spin(FORWARD, axis1Value, PERCENT)

    #add values for axis 3 and axis 4 and multi by approx. .666
    #only move back motor when axis 4 is moved
    else :    
        left_motor.spin(FORWARD, (axis3Value + axis4Value * 0.666), PERCENT)
        right_motor.spin(REVERSE, (axis3Value + axis4Value * -0.666), PERCENT)
        back_motor.spin(REVERSE, (axis4Value), PERCENT)  

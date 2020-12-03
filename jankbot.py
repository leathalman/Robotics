#included components
#   left_motor set to "normal" on port 2
#   right_motor set to "normal" on port 11
#   back_motor set to "normal" on port 1
#   left_grab_motor set to "normal" on port 4
#   right_grab_motor set to "normal" on port 12
#   elevator_motor set to "normal" on port 5

while True:

    #on up-arrow press, spin left_grab, right_grab, and elevator motors to pull ball in
    #on down-arrow press, spin left_grab, right_grab, and elevator motors to push ball out
    if controller_1.buttonUp.pressing() :
        right_grab_motor.spin(FORWARD, 100, PERCENT)
        left_grab_motor.spin(FORWARD, 100, PERCENT)
        elevator_motor.spin(FORWARD, 100, PERCENT)
    elif controller_1.buttonDown.pressing() :
        right_grab_motor.spin(REVERSE, 100, PERCENT)
        left_grab_motor.spin(REVERSE, 100, PERCENT)
        elevator_motor.spin(REVERSE, 100, PERCENT)
    else :
        right_grab_motor.stop()
        left_grab_motor.stop()
        elevator_motor.stop()

    if controller_1.buttonLeft.pressing() :
        controller_1.screen.clear_screen()
        brain.screen.clear_row()

    #axis 1, right joystick on x-axis
    #axis 3, left joystick on y-axis
    #axis 4, left joystick on x-axis
    axis1Value = controller_1.axis1.position()
    axis3Value = controller_1.axis3.position()
    axis4Value = controller_1.axis4.position()

    #define velocity percent for L1 and R1 spins
    # spinVelocity = 75

    # #spin robot to the right
    # if controller_1.buttonR1.pressing() :
    #     left_motor.spin(REVERSE, spinVelocity, PERCENT)
    #     right_motor.spin(REVERSE, spinVelocity, PERCENT)
    #     back_motor.spin(REVERSE, spinVelocity, PERCENT)

    #     #spin robot to the left
    # elif controller_1.buttonL1.pressing() :
    #     left_motor.spin(FORWARD, spinVelocity, PERCENT)
    #     right_motor.spin(FORWARD, spinVelocity, PERCENT)
    #     back_motor.spin(FORWARD, spinVelocity, PERCENT)
        
    # else :
    #     left_motor.stop()
    #     right_motor.stop()
    #     back_motor.stop()

    #axis 1 in negative x direction (pushed to left side)
    #sensitivity deadzone for values 1...5 
    axisFactor = 0.65

    if axis1Value < -5 :
        left_motor.spin(REVERSE, axis1Value * -axisFactor, PERCENT)
        right_motor.spin(REVERSE, axis1Value  * -axisFactor, PERCENT)
        back_motor.spin(REVERSE, axis1Value  * -1, PERCENT)

        controller_1.screen.print(back_motor.velocity(PERCENT))
        brain.screen.print(back_motor.velocity(PERCENT))

    #axis 1 in positive x direction (pushed to right side)
    #sensitivity deadzone for values 1...5 
    elif axis1Value > 5 :
        left_motor.spin(FORWARD, axis1Value * axisFactor, PERCENT)
        right_motor.spin(FORWARD, axis1Value * axisFactor, PERCENT)
        back_motor.spin(FORWARD, axis1Value, PERCENT)

        controller_1.screen.print(back_motor.velocity(PERCENT))
        brain.screen.print(back_motor.velocity(PERCENT))

    #add values for axis 3 and axis 4 and multi by approx. .666
    #only move back motor when axis 4 is moved
    else :    
        left_motor.spin(FORWARD, (axis3Value + axis4Value * 0.666), PERCENT)
        right_motor.spin(REVERSE, (axis3Value + axis4Value * -0.666), PERCENT)
        back_motor.spin(REVERSE, (axis4Value), PERCENT)

        controller_1.screen.print(back_motor.velocity(PERCENT))
        brain.screen.print(back_motor.velocity(PERCENT))
        brain.screen.next_row()
    

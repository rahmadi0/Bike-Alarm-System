# Turn signals with adaptive taillights
#
# Bright  ->  dim white taillights
# Dark    ->  red taillights

from adafruit_circuitplayground.express import cpx
import time
# set initial state color to be white
cpx.pixels.fill((255, 255, 255))

# initial status for hazard light button status
b_state = cpx.button_b
hazard_signal = False

while True:
    ### HEADLIGHTS MODE###
    # if the swtich is in "on" position, CPX enters headlights mode
    if cpx.switch:
        b = cpx.button_b

        # Prepare NeoPixels for headlights mode
        if not hazard_signal:
            cpx.pixels.fill((255, 255, 255))

        ### HIGH BEAMS MECHANISM ###
        # if button A is pressed and held, brightness turns to max to "flash" headlights
        if cpx.button_a:
            cpx.pixels.brightness = 1
        else:
            cpx.pixels.brightness = 0.15

        ### TOGGLE MECHANISM ###
        # Button B changes hazard_signal between True and False
        if b != b_state:
            b_state = b
            if b_state:
                hazard_signal = not hazard_signal

        # if toggle state is on
        elif hazard_signal:
            cpx.pixels.brightness = 1
            cpx.pixels.fill((255, 0, 0))

            cpx.pixels[1] = (255, 155, 0)
            cpx.pixels[2] = (255, 155, 0)
            cpx.pixels[3] = (255, 155, 0)
            cpx.pixels[6] = (255, 155, 0)
            cpx.pixels[7] = (255, 155, 0)
            cpx.pixels[8] = (255, 155, 0)
            time.sleep(0.35) # delay between each flash

            cpx.pixels[1] = (0, 0, 0)
            cpx.pixels[2] = (0, 0, 0)
            cpx.pixels[3] = (0, 0, 0)
            cpx.pixels[6] = (0, 0, 0)
            cpx.pixels[7] = (0, 0, 0)
            cpx.pixels[8] = (0, 0, 0)
            time.sleep(0.35) # delay between each flash

    ### TAIL LIGHTS MODE ###
    # If the swtich is in "off" position, CPX enters taillights mode
    else:
        cpx.pixels.brightness = 1

        # when button B is pressed and held, right turn signals will flash red
        if cpx.button_b:
            cpx.pixels[9] = (255, 0, 0)
            cpx.pixels[8] = (255, 0, 0)
            cpx.pixels[7] = (255, 0, 0)
            time.sleep(0.35)
            cpx.pixels[9] = (0, 0, 0)
            cpx.pixels[8] = (0, 0, 0)
            cpx.pixels[7] = (0, 0, 0)
            time.sleep(0.35) # flash in increments of 0.35 seconds

        # when button A is pressed and held, left turn signals will flash red
        if cpx.button_a:
            cpx.pixels[0] = (255, 0, 0)
            cpx.pixels[1] = (255, 0, 0)
            cpx.pixels[2] = (255, 0, 0)
            time.sleep(0.35)
            cpx.pixels[0] = (0, 0, 0)
            cpx.pixels[1] = (0, 0, 0)
            cpx.pixels[2] = (0, 0, 0)
            time.sleep(0.35) # flash in increments of 0.35 seconds

        # when sensor is triggered, it will turn on the red lights which could be used for brake lights if trigered by the brake string when brake levers pulled by the rider.
        else:
            if cpx.light > 100:
                cpx.pixels.fill((255, 0, 0))
                cpx.pixels.show() # update the pixels and avoid flickering

            # when sensor is not triggered, lights will remain steady white
            else:
                cpx.pixels.fill((50, 50, 50))
                cpx.pixels.show() # update the pixels and avoid flickering

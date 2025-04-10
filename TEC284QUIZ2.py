from gpiozero import LED, Button
from time import sleep  # Make sure sleep is imported
from signal import pause

# Define LED and BUTTONS
RED_LED = LED(23)
GREEN_LED = LED(24)
BLUE_LED = LED(25)

RED_BUTTON = Button(17)
GREEN_BUTTON = Button(27)
BLUE_BUTTON = Button(22)

#Look for button state
def update_led():
    #turn on LED
    if RED_BUTTON.is_pressed:
        RED_LED.on()
    else:
        RED_LED.off()

    if GREEN_BUTTON.is_pressed:
        GREEN_LED.on()
    else:
        GREEN_LED.off()

    if BLUE_BUTTON.is_pressed:
        BLUE_LED.on()
    else:
        BLUE_LED.off()

# Check Button state
def main():
    print("Press any combination of buttons to change the RGB LED color; ctrl+c to end.")
    try:
        while True:
            update_led()
            sleep(0.1)
    except KeyboardInterrupt: #to end program
        print("\nEND")
        RED_LED.off()
        GREEN_LED.off()
        BLUE_LED.off()

if __name__ == "__main__":
    main()

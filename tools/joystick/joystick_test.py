from inputs import get_gamepad

while True:
    joystick_event = get_gamepad()[0]
    event = (joystick_event.code, joystick_event.state)
    if 'ABS_RZ' in joystick_event.code:
        print(event)

    if 'ABS_Z' in joystick_event.code:
        print(event)
    
    if 'ABS_X' in joystick_event.code:
        print(event)
    
import screen_brightness_control as sbc

current_brightness = sbc.get_brightness()
print(current_brightness)
sbc.fade_brightness(75, start=25)
monitors = sbc.list_monitors()
# print(monitors)
# sbc.set_brightness(75, display=monitors[1])
# import
from uagame import Window
from time import sleep
# create window
window = Window('Hacking', 700, 600)
window.set_font_color('green')
window.set_font_name('couriernew')
window.set_bg_color('black')
window.set_font_size(18)

# initialize variables
line_y = 0
string_height = window.get_font_height()

# display remaining attempts
window.draw_string('1 ATTEMPT(S) LEFT', 0, line_y)
window.update()
sleep(0.5)
line_y = line_y + string_height
# display password list (similar to above, copy/paste for each password)
window.draw_string('PASSWORD', 0, line_y)
window.update()
sleep(0.5)
line_y = line_y + string_height

window.draw_string('HACKING', 0, line_y)
window.update()
sleep(0.5)
line_y = line_y + string_height

window.draw_string('ADMIN', 0, line_y)
window.update()
sleep(0.5)
line_y = line_y + string_height

# prompt user for password
guess = window.input_string('ENTER A PASSWORD > ', 0, line_y)
guess = window.guess.upper

# clear window
window.clear()

# create outcome
if (guess == 'PASSWORD'):
    window.draw_string('SUCCESS!', 0, 0)
    window.update()
else:
    window.draw_string('Failure.', 0,0)
    window.update()
sleep(2)

# clear window
window.clear()

# prompt for end
window.input_string('PRESS ENTER TO QUIT', 0, 0)

# close window
window.close()


import psutil
from pyglow import PyGlow
import signal
import sys

pyglow = PyGlow()
# Set the order in which you want the lights to come one
# In this case they start in the center and spiral outwards
led_list = [6, 12, 18, 5, 11, 17, 4, 10, 16, 3, 9, 15, 2, 8, 14, 1, 7, 13]


def signal_handler(signal, frame):
        pyglow.all(0)
        pyglow.update_leds()
        sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
# Set some variables
brightness = 100
previous_value = 0
number_leds = 18

while True:
	cpu_percent = psutil.cpu_percent(interval=11)
	number_to_display = (cpu_percent / (100/number_leds))
	cpu_rounded = int(number_to_display)
	print cpu_percent
	if (cpu_rounded > 18):
		cpu_rounded = 18
	# alter brightness based on load
	if (previous_value == cpu_rounded):
		brightness += 10
		if (brightness > 255):
			brightness = 255
	else:
		brightness -= 10
		if (brightness < 10):
			brightness = 10

	previous_value = cpu_rounded
	print ("Brightness: ", brightness)

	print ('led id:', cpu_rounded)
	pyglow.all(0)
	for count in xrange(0, cpu_rounded, 1):
		#pyglow.led(count, brightness)
		pyglow.led(led_list[count], brightness)

pyglow.update_leds()


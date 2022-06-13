import time
import itertools
class TrafficLight():
	__color = [['red', 7], ['yellow', 2], ['green', 1]]
	print(__color[1][1])
	def running(self, __color):
		for light in itertools.cycle(__color):
			print(f'Traffic Light is {light[0]}')
			print(light[1])
			time.sleep(3)


lenina_mira = TrafficLight()
lenina_mira.running('yellow')


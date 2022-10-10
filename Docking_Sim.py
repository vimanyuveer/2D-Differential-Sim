import time as t
import matplotlib.pyplot as plt
# mass, velocity, accln, disp, time
# interaction force every loop
# inputs --> thrust increments -> new_accl, and continous parameters
# some step function --> steps through iterations

time = 0

class Spacecraft:
	def __init__(self, name, mass, velocity, accln, x_pos):
		self.name = name
		self.mass = mass
		self.velocity = velocity
		self.accln = accln
		self.x_pos = x_pos

	def step_Function(self):
		global time
		# MASS CONSTANT
		time_step = 0.01 
		time += time_step
		self.x_pos += self.velocity * time_step
		self.velocity += self.accln * time_step
		self.accln += time ** 2

						
	def display_Status(self):
		global time
		print("TIME     -->", time)
		print("CRAFT    -->", self.name)
		print("MASS     --> ", self.mass)
		print("VELOCITY --> ", self.velocity)
		print("ACCLRTION--> ", self.accln)
		print("POSITION --> ", self.x_pos)
		print("\n")	

chaser = Spacecraft("CHASER", 100, 10, 2, 0)

x_list = []
t_list = []

for i in range(0, 1000):
	chaser.display_Status()
	chaser.step_Function()
	
	x_list.append(chaser.x_pos)
	t_list.append(time)

plt.plot(t_list, x_list)
plt.show()
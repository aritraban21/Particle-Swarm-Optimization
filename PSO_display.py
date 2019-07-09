# Importing necessary libraries 
import pygame
import time
from random import randint
import random
import math
import numpy as np

def display(x,y):
	"""
	Function to display particles at (x,y) and target on screen
	"""
	pygame.draw.circle(screen,color_2,(point_x,point_y),4)
	pygame.draw.circle(screen,color,(x,y),2)
	pygame.display.flip()


def cost(x,y):
	"""
	Cost function that PSO minimizes(here distance between (x,y) and target point in 2D )
	"""
	return math.sqrt((((point_x - x)**2)+((point_y - y)**2)))


# PSO parameters
max_iter = 100;					# maximum iterations of PSO
num_particles = 100				# number of swarm particles used
w = 1							# Global constant
w_damp = 0.99					# Global damping factor
c1 = 1							
c2 = 2
c1_damp =0.55					# Local damping factor

point_x = random.randint(0,1000)	# target x coordinate
point_y = random.randint(0,500)		#target y coordinate
done = False
nvar = 2							#number of variables in PSO(here 2)
var_min = 0;						
var_max = 1000;


# Initializing pygame
pygame.init()
screen = pygame.display.set_mode((1000, 500))
clock = pygame.time.Clock()
color = (0,0,255)
color_2=(255,0,0)


# Start of PSO
X = np.random.randint(var_min,var_max,(num_particles,nvar))		# Randomly poaitioning 100 particles in 2D
v = np.zeros((num_particles,nvar))								# Initailizing velocty of all particles to 0
global_best = float('inf')										# Setting best cost of entire swarm as inf
particle_cost = np.zeros((num_particles,1))						# Setting best cost of each particle as 0


for i in range(num_particles):									# Setting cost of first position as best cost for each particle
	particle_cost[i] = cost(X[i,0],X[i,1])

particle_best_pos = X
particle_best_cost = particle_cost
if(global_best>particle_best_cost.min()):						# Getting the current best particle(with least cost) in entire swarm
	global_best_position = X[particle_best_cost.argmin(),:]
	global_best = particle_best_cost.min()


# PSO Loop
for i in range(1,max_iter):
	v = (w*v)+c1*((np.random.rand(num_particles,nvar))*(particle_best_pos-X))+c2*((np.random.rand(num_particles,nvar))*(global_best_position-X))
	X = X + v  													# Implementing the PSO equation
	for j in range(num_particles):
		particle_cost[j] = cost(X[j,0],X[j,1])
		if(particle_cost[j]<particle_best_cost[j]):				# Getting best cost of each particle uptil now
			particle_best_pos[j]=X[j]
			particle_best_cost[j]=particle_cost[j]
		if(global_best>particle_best_cost.min()):				# Getting best cost of entire swarm uptil now
			global_best_position = X[particle_best_cost.argmin(),:]
			global_best = particle_best_cost.min()
				#best_costs[i,1]=global_best
		display(int(X[j,0]),int(X[j,1]))
	print("Iteration {} : {}".format(i,global_best_position))	
	w = w_damp * w;												# Damping global factor
	c1 =c1_damp *c1;
	time.sleep(0.07)
	clock.tick(1000)
	screen.fill((255,255,255))
print("Completed converging at : [{},{}] ".format(point_x,point_y))
sd=input()



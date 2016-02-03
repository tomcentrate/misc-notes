from random import random

# Demonstrating Inheritance in Python
class Particle(object):

  charge = 0
  def __init__(self, x,y):
    self.x = x
    self.y = y

  def getNextPosition(list_of_particles):
    new_position_x = self.x
    new_position_y = self.y
    for particle in list_of_particles:
      if particle.x == self.x and particle.y == self.y:
        continue

      new_position = self.position(particle)
      new_position_x += new_position[x]
      new_position_y += new_position[y]

    self.x = new_position_x
    self.y = new_position_y


  def position(self, particle):
    dist = (self.x + self.y)**2 - (particle.x + particle.y)**2
    next_x = (self.x ** 2 - particle.x **2) / dist
    next_y = (self.y ** 2 - particle.y **2) / dist
    if (particle.charge == self.charge ):
      next_x = - next_x
      next_y = - next_y
    return {x: next_x, y:next_y }

class Proton(Particle):
  charge = 1

class Negatron(Particle):
  charge = -1

# Factory Pattern
class ParticleFactory(object):

  @staticmethod
  def createProtons(number):
    return ParticleFactory.createParticles(Proton, number)

  @staticmethod
  def createNegatrons(number):
    return ParticleFactory.createParticles(Negatron, number)

  @staticmethod
  def createParticles(className, number):
    particle_list = []
    for x in range(1, number+1):
      particle = className(0,0)
      particle_list.append(particle)

    return particle_list

# Basic Tree with Search using Depth-First search.
class TreeNode(object):

  def __init__(self, val):
    self.children_nodes = []
    self.value = val

  def addChild(self,node):
    self.children_nodes.append(node)

  def findVal(self,value):
    if value == self.value:
      return self

    for node in self.children_nodes:
      print "We are at Node " + str(node.value)
      if node.findVal(value) != None:
        return node

    return None

  def __repr__(self):
    return "Tree Node" + str(self.value)


NodeA = TreeNode('A')
NodeB = TreeNode('B')
NodeC = TreeNode('C')
NodeD = TreeNode('D')
NodeE = TreeNode('E')
NodeF = TreeNode('F')
NodeG = TreeNode('G')

NodeB.addChild(NodeD)
NodeB.addChild(NodeE)
NodeC.addChild(NodeF)
NodeC.addChild(NodeG)

NodeA.addChild(NodeB)
NodeA.addChild(NodeC)

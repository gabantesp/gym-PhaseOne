import pygame
import random 
import numpy as np
import os

class gridview:
  
  def __init__(self, grid_name="Grid2D", grid_file_path=None,
               grid_size=(30,30), screen_size=(600,600)):
    
    pygame.init()
    pygame.display.set_caption(grid_name)
    self.clock = pygame.time.Clock()
    self.__game_over = False
    
    """if grid_file_path is None:
      self.__grid = Grid(grid_size=grid_size)
    else:
      if not os.path.exists(grid_file_path):
        dir_path = os.path.dirname(os.path.abspath(__file__))
        rel_path = os.path.join(dir_path, "grid_samples", grid_file_path)
        if os.path.exists(rel_path):
          grid_file_path = rel_path
        else:
          raise FileExistsError("Cannot find %s." % grid_file_path)
      self.__grid = Grid(grid_cells=Grid.load_grid(grid_file_path)"""
    self.__grid = Grid(grid_size=grid_size)
    self.grid_size = self.__grid.grid_size
    
    self.screen = pygame.display.set_mode(screen_size)
    self.__screen_size = tuple(map(sum, zip(screen_size, (-1, -1))))
    
    self.__entrance = np.zeros(2, dtype=int)
    
    self.__goal = np.array(self.maze_size) - np.array((1, 1))
    
    self.__robot = self.entrance
    
    self.background = pygame.Surface(self.screen.get_size()).convert()
    self.background.fill((255, 255, 255))
    
    self.grid_layer = pygame.Surface(self.screen.get_size()).convert_alpha()
    self.grid_layer.fill((0, 0, 0, 0))
    
    self.__draw_grid()
    
    self.__draw_robot()
    
    self.__draw_entrance()
    
    self.__draw_goal()
    
  def update(self, mode="human"):
    try:
      img_output = self.__view_update(mode)
      self.__controller_update()
    except Exception as e:
      self.__game_over = True
      self.quit_game()
      raise e
    else:
      return img_output
    
  def quit_game(self):
    try:
      self.__game_over = True
      pygame.display.quit()
      pygame.quit()
    except Exception:
      pass
    
  def move_robot(self, dir):
    if dir not in self.__grid.COMPASS.keys():
      raise ValueError("dir cannot be %s. The only valid dirs are %s."
                       %(str(dir),str(self.__maze.COMPASS.keys())))
      
    if self.__maze.is_open(self.__robot, dir):
      
      self.__draw_robot(transparency = 0)
      
      self.__robot += np.array(self.__maze.COMPASS[dir])
      self.__draw_robot(transparency=255)
      
      
  def reset_robot(self):
    
    self.__draw_robot(transparency=0)
    self.__robot = np.zeros(2, dtype=int)
    self.__draw_robot(transparency=255)
    
  def __controller_update(self):
    if not self.__game_over:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.__game_over = True 
          self.quit_game()
          
  def __view_update(self, mode="human"):
    if not self.__game_over:
      self.__draw_entrance()
      self.__draw_goal()
      self.__draw_portals()
      self.__draw_robot()
      
      self.screen.blit(self.background, (0,0))
      self.screen.blit(self.maze_layer,(0,0))
      
      if mode == "human":
        pygame.display.flip()
        
      return np.flipud(np.rot90(pygame.surfarray.array3d(pygame.display.get_surface())))
    
  def __cover_walls(self):
    
    dx = x * self.CELL_W
    dy = y *self.CELL_H
    
    if not isinstance(dirs, str):
      raise TypeError("dirs must be a str")
      
    for dir in dirs:
      if dir == "S":
        line_head = (dx + 1, dy + self.Cell_H)
        line_tail = (dx + self.CELL_W -1, dy + self.CELL_H)
      elif dir == "N":
        line_head = (dx + 1, dy)
        line_tail = (dx + self.CELL_W - 1, dy)
      elif dir == "W":
        line_head = (dx, dy + 1)
        line_tail = (dx, dy + self.CELL_H - 1)
      elif dir == "E":
        line_head = (dx + self.CELL_W, dy +1)
        line_tail = line_tail = (dx + self.CELL_W, dy + self.CELL_H -1)
      else: 
        raise ValueError("The only valid directions are (N, S, E, W).")
        
      pygame.draw.line(self.maze_layer, colour, line_head, line_tail)
      
  def __draw_robot(self, colour = (o,0,150), transparency=235):
    x = int(self.__robot[0] * self.CELL_W + self.CELL_W * 0.5 + 0.5)
    y = int(self.__robot[1] * self.CELL_H + self.CELL_H * 0.5 + 0.5)
    r = int(min(self.CELL_W, self.CELL_H)/5 + 0.5)
    
    pygame.draw.circle(self.maze_layer, colour + (transparency), (x, y), r)
    
  def __draw_entrance(self, colour=(0, 0, 150), transparency=235):
    self.__colour_cell(self.entrance, colour=colour, transparency=transparency)
    
  def __draw_goal(self, colour=(150,0,0), transparency=235):
    self.__colour_cell(self.goal, colour=colour, transparency=transparency) 
    
  @property
    def maze(self):
        return self.__maze

  @property
    def robot(self):
        return self.__robot

  @property
    def entrance(self):
        return self.__entrance

  @property
    def goal(self):
        return self.__goal

  @property
    def game_over(self):
        return self.__game_over

  @property
    def SCREEN_SIZE(self):
        return tuple(self.__screen_size)

  @property
    def SCREEN_W(self):
        return int(self.SCREEN_SIZE[0])

  @property
    def SCREEN_H(self):
        return int(self.SCREEN_SIZE[1])

  @property
    def CELL_W(self):
        return float(self.SCREEN_W) / float(self.maze.MAZE_W)

  @property
    def CELL_H(self):
        return float(self.SCREEN_H) / float(self.maze.MAZE_H)
    

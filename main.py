#!/usr/bin/env python3
import os, sys
os.environ['SDL_AUDIODRIVER'] = 'dummy'
sys.path.append('./libs/')

import pygame
import numpy as np
import colorlover as cl
from collections import deque

from SimEnv import SimEnv

# Get a color scale
colors = cl.scales['12']['qual']['Set3']
for i, color in enumerate(colors):
    colors[i] = tuple(int(part) for part in color[4:-1].split(','))
colors = colors + colors + colors + colors + colors + colors + colors + colors + colors + colors + colors


if __name__ == '__main__':
    sim_env = SimEnv()

    # 1. initialize pygame
    pygame.init()
    # Define the window size
    window_size = [800, 800]
    screen = pygame.display.set_mode(window_size)
    # Define the map size
    map_size = [100, 100, 600, 600]

    pgcoor = lambda pos: (int(map_size[0] + map_size[2] * pos[0]), int(map_size[1] + map_size[3] * pos[1]))

    # Define the agent size
    agent_size = 5

    # Clear the screen
    screen.fill((255, 255, 255))

    sim_env.run_parrell()

    # 2. start simulation
    pygame_running = True
    for iter in range(1000):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame_running = False

        # sim_env.step()

        if not pygame_running:
            break

        ############ Pygame Rendering

        screen.fill((255, 255, 255))

        for pos in sim_env.agents[0].ctrllr._targ_dist.means:
            pygame.draw.circle(screen, (255, 0, 0), pgcoor(pos), 20)

        # Draw the map
        pygame.draw.rect(screen, (255, 255, 255), map_size, 2)
        # Draw the agents
        for agent_id, agent in enumerate(sim_env.agents):
            pos = agent.state[:2]
            pygame.draw.circle(screen, colors[agent_id], pgcoor(pos), agent_size)

            # Draw the path of the agent
            if len(sim_env.agent_paths[agent_id]) > 1:  # Only draw the line if there are at least two points
                pygame.draw.lines(screen, colors[agent_id], False, [pgcoor(path_pos) for path_pos in sim_env.agent_paths[agent_id]], 1)

        # Update the screen
        pygame.display.flip()

    pygame.quit()

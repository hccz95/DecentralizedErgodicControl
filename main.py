#!/usr/bin/env python3
import os
os.environ['SDL_AUDIODRIVER'] = 'dummy'

from quad_agent import Agent
from env import Map
import pygame
import numpy as np

import colorlover as cl
from collections import deque

# Get a color scale
colors = cl.scales['12']['qual']['Set3']
for i, color in enumerate(colors):
    colors[i] = tuple(int(part) for part in color[4:-1].split(','))
colors = colors + colors + colors + colors + colors + colors + colors + colors + colors + colors + colors

if __name__ == '__main__':
    agent_num = 50
    building_num = 3

    agents = [Agent('agent_' + str(i+1)) for i in range(agent_num)]
    agent_paths = [deque(maxlen=50) for _ in range(agent_num)]  # Add this line to store the paths of each agent

    map = Map(building_num)

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

    pygame_running = True
    for iter in range(1000):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame_running = False

        map.update_rendering()
        print('iter:', iter)

        for obj_id, obj in enumerate(map.objects):
            print('\t', 'obj_'+str(obj_id), ':', 'xy=', obj._p, 'wl=', obj.dim)
        print('')

        # print('\t', , ':', agent.state)
        for agent_id, agent in enumerate(agents):
            agent.step()
            print('\t', 'agent_'+str(agent_id), ':', 'xy=', agent.state[:2])
            agent_paths[agent_id].append(agent.state[:2])  # Add this line to store the current position of the agent

            # 手动发布Ck消息，不使用ros接口
            for target_id in range(len(agents)):
                if target_id == agent_id:
                    continue
                agents[target_id].ctrllr._ck_dict[agent.agent_name] = np.array(agent.ctrllr._ck_msg.ck)

        print('\n----------------------\n')

        if not pygame_running:
            break

        ############ Pygame Rendering

        screen.fill((255, 255, 255))

        for pos in agents[0].ctrllr._targ_dist.means:
            pygame.draw.circle(screen, (255, 0, 0), pgcoor(pos), 20)

        # Draw the map
        pygame.draw.rect(screen, (255, 255, 255), map_size, 2)
        # Draw the agents
        for agent_id, agent in enumerate(agents):
            pos = agent.state[:2]
            pygame.draw.circle(screen, colors[agent_id], pgcoor(pos), agent_size)

            # Draw the path of the agent
            if len(agent_paths[agent_id]) > 1:  # Only draw the line if there are at least two points
                pygame.draw.lines(screen, colors[agent_id], False, [pgcoor(path_pos) for path_pos in agent_paths[agent_id]], 1)

            # break

        # Update the screen
        pygame.display.flip()

    pygame.quit()

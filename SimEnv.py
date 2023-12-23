#!/usr/bin/env python3
import os, sys
os.environ['SDL_AUDIODRIVER'] = 'dummy'

from quad_agent import Agent
import numpy as np
from collections import deque


class SimEnv:
    def __init__(self, agent_num=15, building_num=3) -> None:
        self.agent_num = agent_num
        self.building_num = building_num

        # 使用共享内存
        from multiprocessing import Array
        self.agent_ck = [Array('d', 25) for _ in range(agent_num)]
        # self.agent_ck = [np.zeros((25, )) for _ in range(agent_num)]

        self.agents = [Agent('agent_' + str(i+1), self.agent_ck[i]) for i in range(agent_num)]
        self.agent_paths = [deque(maxlen=50) for _ in range(agent_num)]  # Add this line to store the paths of each agent
        self.iter = 0

    def step(self):
        self.iter = 0
        print('iter:', self.iter)

        # print('\t', , ':', agent.state)
        for agent_id, agent in enumerate(self.agents):
            agent.step()
            # print('\t', 'agent_'+str(agent_id), ':', 'xy=', agent.state[:2])
            self.agent_paths[agent_id].append(agent.state[:2])  # Add this line to store the current position of the agent

        print('\n----------------------\n')

    def run_parrell(self):
        from multiprocessing import Process
        procs = []
        for agent_id, agent in enumerate(self.agents):
            p = Process(target=agent.run, )
            procs.append(p)
        for p in procs:
            p.start()

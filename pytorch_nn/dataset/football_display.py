# -*- encoding: utf-8 -*-
'''
@File    :   football_display.py
@Time    :   2020/01/30 16:16:59
@Author  :   Yuan Yu
'''

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import os


class FootballDisplay:
    """Load football dataset and Display"""
    def __init__(self,
                 football_dataset,
                 img_root='/projects/research/football/dumps/img'):
        self.football_dataset = football_dataset
        self.img_root = img_root

    def show_football(self, i, time):
        """Show football_players and the ball"""
        plt.figure()
        sample = self.football_dataset[i]
        X, Y = sample['X'], sample['Y']
        players_poss, ball_pos = X[time].reshape(22,
                                                 2), Y[time][:2].reshape(2)

        plt.scatter(players_poss[:, 0],
                    players_poss[:, 1],
                    s=10,
                    marker='.',
                    c='r')
        plt.scatter(ball_pos[0], ball_pos[1], s=10, marker='*', c='blue')
        # plt.pause(0.001)  # pause a bit so that plots are updated

    def save_gifs(self, idxs, file_name='match'):
        for i in idxs:
            sample = self.football_dataset[i]
            X, Y = sample['X'], sample['Y']
            fig = plt.figure()
            ax = plt.gca()

            def init():
                players_poss, ball_pos = X[0].reshape(22,
                                                      2), Y[0][:2].reshape(2)
                scat1 = ax.scatter(players_poss[:, 0],
                                   players_poss[:, 1],
                                   s=10,
                                   marker='.',
                                   c='r',
                                   animated=True)
                scat2 = ax.scatter(ball_pos[0],
                                   ball_pos[1],
                                   s=10,
                                   marker='*',
                                   c='blue',
                                   animated=True)
                return scat1, scat2

            scat1, scat2 = init()

            def update(time):
                ax.set_title('Sample #{},Time #{}'.format(i, time))
                players_poss, ball_pos = X[time].reshape(
                    22, 2), Y[time][:2].reshape(2)
                scat1.set_offsets(players_poss)
                scat2.set_offsets(ball_pos)
                return scat1, scat2

            ani = FuncAnimation(fig,
                                update,
                                frames=self.football_dataset.Tx,
                                init_func=None,
                                interval=100)
            ani.save(os.path.join(self.img_root, '%s%d.mp4' % (file_name, i)))

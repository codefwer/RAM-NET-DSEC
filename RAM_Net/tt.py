import numpy as np


path = '/home/neurocomp0/workspace/EventScape/Town05/sequence_23/events/data/05_023_0001_events.npz'

events = np.load(path)

print(len(events['t']))

path2 = ''
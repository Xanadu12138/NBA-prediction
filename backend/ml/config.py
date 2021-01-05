import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import pandas as pd 
import numpy as np 
import os

# Settings for model
use_cuda = torch.cuda.is_available()
CURRENT_COMP_VECTOR_SIZE = 2
TEAM_VECTOR_SIZE = 21
batch_size = 64
learning_rate = 0.001
num_epochs = 500
savePath = os.path.join('models','dnn.pt')

# Settings for data processing
season = '2018-2019' # Select which season for training model

# Extract essentials attribute for predict games.
selectedAttr = ['PlayerName', 'Tm', 'G', 'GS', 'FG', 'FGA', 'FGAver', '3P', '3PA', '3PAver', '2P', '2PA', '2PAver', 'FT', 'FTA', 'FTAver', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']
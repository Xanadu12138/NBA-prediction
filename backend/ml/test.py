import config as config
import dnn
import os
import torch
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import pandas as pd 
import numpy as np 
import os
from torch.utils.data.dataset import Dataset


class NBADataset(Dataset):
    '''
    Custom dataset class.
    Paramters: csv path & teamdict. 
    teamdict is a dictionary that key is team name and values are represent of this team.
    Return: A torch.dataset object, item of this dataset is (tm1Stats, tm2Stats, tm1His, tm2His, label)
    '''
    def __init__(self, csv_path, teamDict):
        self.data = pd.read_csv(csv_path)
        self.teamDict = teamDict

    def __getitem__(self, index):
        # Register regular express
        regx = re.compile('(.*)胜(.*)负')
        tm1 = self.data.iloc[index]['Tm1']
        tm2 = self.data.iloc[index]['Tm2']
        sco1 = self.data.iloc[index]['Sco1']
        sco2 = self.data.iloc[index]['Sco2']
        sco = self.data.iloc[index]['sco']

        # Excract data
        tm1His = regx.findall(sco1)
        tm1His = list(map(int,tm1His[0]))
        tm1Win = tm1His[0]
        tm1Lose = -tm1His[0]

        # Same as tm2
        tm2His = regx.findall(sco2)
        tm2His = list(map(int,tm2His[0]))
        tm2Win = tm2His[0]
        tm2Lose = -tm2His[1]

        # Get result from sco
        sco = list(map(int,sco.split(':')))
        label = 0 if sco[0] > sco[1] else 1
        tm1His = [tm1Win, tm1Lose]
        tm2His = [tm2Win, tm2Lose]
        tm1Stats = self.teamDict[tm1]
        tm2Stats = self.teamDict[tm2]
        
        # To tensor
        tm1Stats = torch.FloatTensor(tm1Stats)
        tm2Stats = torch.FloatTensor(tm2Stats)
        tm1His = torch.IntTensor(tm1His)
        tm2His = torch.IntTensor(tm2His)

        return (tm1Stats, tm2Stats, tm1His, tm2His, label)
        
    def __len__(self):
        return len(self.data)

def GetTeamDict(csv_path):
    teamDict = {}
    with open(csv_path,'r',encoding='utf-8') as csvFile:
       lines = [line for line in csvFile.readlines()]
       lines = lines[1:]
       for line in lines:
           line = line.split(',')
           teamName = line[0]
           teamStats = list(map(float,line[1:]))
           teamDict[teamName] = teamStats

    return teamDict


def LoadDataset(path):
    teamDict = GetTeamDict(path)
    NBA_Dataset = NBADataset('data/teamresult.csv',teamDict)
    # Init sampler
    indices = range(len(NBA_Dataset))
    indices_train = indices[:1100]
    indices_test = indices[1100:]
    train_loader = torch.utils.data.DataLoader(NBA_Dataset, batch_size= 1, sampler = indices_train)
    test_loader = torch.utils.data.DataLoader(NBA_Dataset, batch_size= 1, sampler = indices_test)
    return train_loader, test_loader

def predict():
    savePath = os.path.join('ml', config.savePath)
    teamDic = GetTeamDict('data/2018-19teamstats.csv')
    dnnNet = dnn.DNN()
    if config.use_cuda:
        dnnNet = dnnNet.cuda()
    # Load model
    dnnNet.load_state_dict(torch.load('models/Simdnn.pt'))
    train, test = LoadDataset('data/2018-19teamstats.csv')
    homeTeam, awayTeam, a, b, label = train[0]
    tm1Stats = torch.FloatTensor([teamDic[homeTeam]])
    tm2Stats = torch.FloatTensor([teamDic[awayTeam]])
    tm1His = torch.IntTensor([[0,0]])
    tm2His = torch.IntTensor([[0,0]])
    
    if config.use_cuda:
            tm1Stats, tm2Stats, tm1His, tm2His = tm1Stats.cuda(), tm2Stats.cuda(), tm1His.cuda(), tm2His.cuda()
    
    output = dnnNet(tm1Stats, tm2Stats)
    # output = dnn(tm1Stats, tm2Stats, tm1His, tm2His)
    output = output.cpu()
    prob = output[0][0]
    print(output)
    return str('{:.3f}%'.format(prob * 100))

if __name__ == "__main__":
    predict()
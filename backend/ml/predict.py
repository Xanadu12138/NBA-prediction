import ml.config as config
import ml.load_dataset 
import ml.dnn
import os
import torch
import numpy as np

def predict(homeTeam, awayTeam):
    savePath = os.path.join('ml', config.savePath)
    teamDic = ml.load_dataset.GetTeamDict('ml/data/2018-2019teamstats.csv')
    dnn = ml.dnn.DNN()
    if config.use_cuda:
        dnn = dnn.cuda()
    # Load model
    dnn.load_state_dict(torch.load(savePath))
    tm1Stats = torch.FloatTensor([teamDic[homeTeam]])
    tm2Stats = torch.FloatTensor([teamDic[awayTeam]])
    tm1His = torch.IntTensor([[0,0]])
    tm2His = torch.IntTensor([[0,0]])
    
    if config.use_cuda:
            tm1Stats, tm2Stats, tm1His, tm2His = tm1Stats.cuda(), tm2Stats.cuda(), tm1His.cuda(), tm2His.cuda()
    
    output = dnn(tm1Stats, tm2Stats, tm1His, tm2His)
    output = output.cpu()
    prob = output[0][0]
    print(output)
    return str('{:.3f}%'.format(prob))
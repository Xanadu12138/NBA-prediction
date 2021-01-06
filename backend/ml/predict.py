import ml.config as config
import ml.load_dataset 
import ml.dnn
import os
import torch
import numpy as np

def predict(homeTeam, awayTeam):
    savePath = os.path.join('ml', config.savePath)
    teamDic = ml.load_dataset.GetTeamDict('ml/data/2018-19teamstats.csv')
    dnnNet = ml.dnn.DNN()
    if config.use_cuda:
        dnnNet = dnnNet.cuda()
    # Load model
    dnnNet.load_state_dict(torch.load(savePath))
    tm1Stats = torch.FloatTensor([teamDic[homeTeam]])
    tm2Stats = torch.FloatTensor([teamDic[awayTeam]])
    tm1His = torch.IntTensor([[5,-2]])
    tm2His = torch.IntTensor([[2,-3]])
    
    if config.use_cuda:
            tm1Stats, tm2Stats, tm1His, tm2His = tm1Stats.cuda(), tm2Stats.cuda(), tm1His.cuda(), tm2His.cuda()
    
    output = dnnNet(tm1Stats, tm2Stats)
    output = output.cpu()
    prob = output[0][0]
    print(output)
    return str('{:.3f}%'.format(prob * 100))
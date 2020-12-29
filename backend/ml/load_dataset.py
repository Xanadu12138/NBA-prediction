
from config import * 
from torch.utils.data.dataset import Dataset
from torchvision import transforms
import re

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


def LoadDataset():
    teamDict = GetTeamDict('data/2018-2019teamstats.csv')
    NBA_Dataset = NBADataset('data/teamresult.csv',teamDict)
    # Init sampler
    indices = range(len(NBA_Dataset))
    indices_train = indices[:985]
    indices_test = indices[985:]
    train_loader = torch.utils.data.DataLoader(NBA_Dataset, batch_size= batch_size, sampler = indices_train)
    test_loader = torch.utils.data.DataLoader(NBA_Dataset, batch_size= batch_size, sampler = indices_test)
    return train_loader, test_loader
    
        

if __name__ == "__main__":
    LoadDataset()
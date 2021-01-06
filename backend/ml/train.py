from utilts import Rightness
from dnn import *
from config import * 
from load_dataset import *


# Load network
dnn = DNN()
if use_cuda:
    dnn = dnn.cuda()
print('Network loading is done!')

# Load Dataset
DatasetName = season + 'teamstats.csv'
DatasetPath = os.path.join('data',DatasetName)
print(DatasetPath)
train_dataset, test_dataset = LoadDataset('data/2018-2019teamstats.csv')

print('Dataset loading is done!')

criterion = nn.CrossEntropyLoss()
optimizer = optim.RMSprop(dnn.parameters(), lr= learning_rate)

# Training with DNN
print('Start training!')
for epoch in range(num_epochs):
    train_right = [] # record accuracy of training set
    for batch_idx, (tm1Stats, tm2Stats, tm1His, tm2His, label) in enumerate(train_dataset):
        dnn.train()
        # Load to GPU if cuda is available
        if use_cuda:
            tm1Stats, tm2Stats, tm1His, tm2His, label = tm1Stats.cuda(), tm2Stats.cuda(), tm1His.cuda(), tm2His.cuda(), label.cuda()
        
        output = dnn(tm1Stats, tm2Stats)

        loss = criterion(output,label)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        right = Rightness(output, label)
        train_right.append(right)

        # Validation per 20 epochs
        if batch_idx % 20:
            dnn.eval()
            val_right = []

            for (tm1Stats, tm2Stats, tm1His, tm2His, label) in test_dataset:
                if use_cuda:
                    tm1Stats, tm2Stats, tm1His, tm2His, label = tm1Stats.cuda(), tm2Stats.cuda(), tm1His.cuda(), tm2His.cuda(), label.cuda()
                
                output = dnn(tm1Stats, tm2Stats)
                right = Rightness(output, label)
                val_right.append(right)
            
            train_r = (sum([tup[0] for tup in train_right]),sum([tup[1] for tup in train_right]))
            val_r = (sum([tup[0] for tup in val_right]),sum([tup[1] for tup in val_right]))
            print('训练周期:{}[{}/{} ({:.0f}%)]\t,Loss:{:.6f}\t,训练正确率:{:.2f}%\t,校验准确率:{:.2f}%'.format(
                epoch, batch_idx * len(label),len(train_dataset.dataset),
                100. * batch_idx / len(train_dataset),loss.data,
                100. * train_r[0] / train_r[1],
                100. * val_r[0] / val_r[1]
            ))

torch.save(dnn.state_dict(), savePath)
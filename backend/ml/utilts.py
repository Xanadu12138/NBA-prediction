from config import * 

def Rightness(output, target):
    right = 0
    topv, topi = torch.topk(output,1)
    topi = topi.view(-1)
    right_tensor = topi - target
    for item in right_tensor:
        if item == 0:
            right = right + 1
    return (right, len(target))
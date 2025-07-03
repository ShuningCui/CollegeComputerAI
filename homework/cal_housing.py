# pip install -U scikit-learn
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from torch.utils.data import TensorDataset, DataLoader
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split

X, y = fetch_california_housing(return_X_y=True,data_home = "./")
x_train,x_val,y_train,y_val = train_test_split(X,y,train_size=0.8)


x_train_tensor = torch.as_tensor(x_train,dtype=torch.float32)
y_train_tensor = torch.as_tensor(y_train,dtype=torch.float32).view(-1,1)
x_test_tensor = torch.as_tensor(x_val,dtype=torch.float32)
y_test_tensor = torch.as_tensor(y_val,dtype=torch.float32).view(-1,1)

train_dataset = TensorDataset(x_train_tensor,y_train_tensor)
test_dataset = TensorDataset(x_test_tensor,y_test_tensor)
train_loader = DataLoader(train_dataset,batch_size=400,shuffle=True)
test_loader = DataLoader(test_dataset,batch_size=200,shuffle=False)

class MylinearRegression(nn.Module):
    def __init__ (self):
        super().__init__()
        self.fc1 = nn.Linear(8,64)
        self.fc2 = nn.Linear(64,128)
        self.fc3 = nn.Linear(128,64)
        self.fc4 = nn.Linear(64,1)

    def forward(self,x):
        y = F.relu(self.fc1(x))
        y = F.relu(self.fc2(y))
        y = F.relu(self.fc3(y))
        y = self.fc4(y)
        return y

model = MylinearRegression()
def mini_batch_train(model,train_loader,optimizer,loss_fn):
    mini_batch_losses = []
    for x_batch,y_batch in train_loader:
        model.train()
        yhat = model(x_batch)
        loss = loss_fn(yhat,y_batch)
        mini_batch_losses.append(loss.item())
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()

    return np.mean(mini_batch_losses)

def mini_batch_test(model,test_loader,loss_fn):
    mini_batch_losses = []
    for x_batch,y_batch in test_loader:
        model.eval()
        yhat = model(x_batch)
        loss = loss_fn(yhat,y_batch)
        mini_batch_losses.append(loss.item())
    
    return np.mean(mini_batch_losses)

def train(model,train_loader,test_loader,optimizer,loss_fn):
    np.random.seed(23)
    torch.manual_seed(23)
    train_losses = []
    test_losses = []
    total_epoches = 0
    epochs = 1000
    for epoch in range(epochs):
        model.train()
        train_loss = mini_batch_train(model,train_loader,optimizer,loss_fn)
        train_losses.append(train_loss)
        total_epoches += 1
        with torch.no_grad():
            model.eval()
            test_loss = mini_batch_test(model,test_loader,loss_fn)
            test_losses.append(test_loss)
        
        print(f"Epoch {epoch+1}/{epochs}, train_loss: {train_loss:.4f}, test_loss: {test_loss:.4f}")

    return train_losses,test_losses

learnRate = 0.001
optimizer = optim.Adam(model.parameters(),lr = learnRate)
loss_fn = nn.MSELoss(reduction = 'mean')
train_losses,test_losses = train(model,train_loader,test_loader,optimizer,loss_fn)
print(train_losses,test_losses)
print(model.state_dict())
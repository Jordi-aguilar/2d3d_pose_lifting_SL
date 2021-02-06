from .hyperparameters import *
import torch
import numpy as np
from timeit import default_timer as timer

# Define a function that trains the model for one epoch
def train_epoch_J(model, trainset, groundset, span_videos_train, optimizer, loss_function):
    timer_beg = timer()
    model.train()
    epoch_loss = []
    
    o = torch.zeros([1,BATCH_SIZE,HIDDEN_SIZE], device=device)
    state = (o, o)
    for i in range(trainset.shape[0]):
        #print(i)
        # Step 1. Remember that Pytorch accumulates gradients.
        # We need to clear them out before each instance
        optimizer.zero_grad()
        
        loss = 0
        
        for j in range(trainset.shape[1]):
            
            #Check if hidden state has to be reseted
            (h_n, c_n) = state
            
            for b, same_video in enumerate(span_videos_train[i,j,:]):
                if not same_video:
                    h_n[0,b,:] = torch.zeros(HIDDEN_SIZE, device=device)
                    c_n[0,b,:] = torch.zeros(HIDDEN_SIZE, device=device)
             
            """
            h_n = [h_n[0,b,:] if same_video else torch.zeros(HIDDEN_SIZE, device=device) for b, same_video in enumerate(span_videos_train[i,j,:])]
            h_n = torch.stack(h_n).unsqueeze(0)
            
            c_n = [c_n[0,b,:] if same_video else torch.zeros(HIDDEN_SIZE, device=device) for b, same_video in enumerate(span_videos_train[i,j,:])]
            c_n = torch.stack(c_n).unsqueeze(0)
            """
            state = (h_n, c_n)
            
            # Step 2. Get our inputs ready for the network, that is, turn them into
            dataX = torch.tensor(trainset[i,j,:,:], device=device).unsqueeze(1)
            dataY = torch.tensor(groundset[i,j,:,:], device=device).unsqueeze(1)
            
            # Step 3. Run our forward pass.
            # Forward through model and carry the previous state forward in time (statefulness)
            y, state = model(dataX, state)
            
            loss += loss_function(y, dataY)
            
        
        loss = loss / SEQ_LEN

        # detach the previous state graph to not backprop gradients further than the BPTT span
        state = (state[0].detach(), # detach h[t] 
        state[1].detach()) # detach c[t]
    
        # Step 4. Compute the loss, gradients, and update the parameters by
        #  calling optimizer.step()
        loss.backward()
        optimizer.step()  
        epoch_loss.append(loss.item())
            
    return epoch_loss, state
from .hyperparameters import *
import torch
import numpy as np
from timeit import default_timer as timer

def test_epoch_J(model, testset, groundset, span_videos_test, loss_function):
    test_loss = []
    state = None
    timer_beg = timer()
    predY = []
    # Evaluation flag
    model.eval()
    # We don't need to keep track of the gradients
    
    o = torch.zeros([1,BATCH_SIZE,HIDDEN_SIZE], device=device)
    state = (o, o)
    
    with torch.no_grad():
        
        for i in range(testset.shape[0]):
            # Step 1. Remember that Pytorch accumulates gradients.
            # We need to clear them out before each instance        
            
            loss = 0
            
            predY_batch = []
            
            for j in range(testset.shape[1]):

                #Check if hidden state has to be reseted
                (h_n, c_n) = state

                for b, same_video in enumerate(span_videos_test[i,j,:]):
                    if not same_video:
                        h_n[0,b,:] = torch.zeros(HIDDEN_SIZE, device=device)
                        c_n[0,b,:] = torch.zeros(HIDDEN_SIZE, device=device)


                state = (h_n, c_n)

                # Step 2. Get our inputs ready for the network, that is, turn them into
                dataX = torch.tensor(testset[i,j,:,:], device=device).unsqueeze(1)
                dataY = torch.tensor(groundset[i,j,:,:], device=device).unsqueeze(1)

                # Step 3. Run our forward pass.
                # Forward through model and carry the previous state forward in time (statefulness)

                y_, state = model(dataX, state)
                predY_batch.append(y_.cpu().numpy())
                
                loss += loss_function(y_, dataY)
            
            
            loss = loss / SEQ_LEN
            
            # detach the previous state graph to not backprop gradients further than the BPTT span
            state = (state[0].detach(), # detach h[t] 
                  state[1].detach()) # detach c[t]

            predY.append(predY_batch)
            
            test_loss.append(loss.item())
            
    timer_end = timer()  
    return test_loss, predY

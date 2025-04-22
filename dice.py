# import numpy.random as random
# import numpy as np
# import matplotlib.pyplot as plt

# def rolldice(nsims):
# # nsims is number of simulations to do
#     nsims=int(nsims)
#     prob=1/6.
#     is_one=(random.rand(nsims,100) < prob)
   
# # generate nsims sets of 100 rolls
#     ndice_array=np.array([2,5,10,25,100])

#     for i,ndice in enumerate(ndice_array):
#         plt.figure(i) # create a new figure for each plot
#         plt.hist( np.sum(is_one[:,0:ndice],axis=1), 
# range=(-0.5,ndice+0.5),bins=(ndice + 1))
#         plt.title(str(ndice) + ' dice')
#         # convert ndice to a string with str(), then use that to title the plot
#         plt.xlabel('Total number of ones')
        
        
        
#         print(f'ndice: {ndice}')
#         print(f'np.mean: {np.mean( np.sum(is_one[:,
#          0:ndice],axis =1) ) }')
#         print(f'np.sum: {np.sum( np.sum(is_one[:,0:ndice],axis=1) )*1./nsims:.4f}')
#         print(f'Expected mean: {ndice*prob:.4f} ') 


import numpy as np
import matplotlib.pyplot as plt
from scipy.special import factorial,comb
def rolldice(nsims):
    # nsims is number of simulations t
    nsims = int(nsims)
    prob = 1/6. 
    is_one = (np.random.rand(nsims, 100) < prob)
    ndice_array = np.array([2, 5, 10, 25, 100])

    for i, ndice in enumerate(ndice_array):
        plt.figure(i)  # Create a new figure for each plot
        results = np.sum(is_one[:, 0:ndice], axis=1)
        #plt.hist(results, range=(-0.5, ndice + 0.5), bins=(ndice + 1), edgecolor='black')
        #x=np.arrange(ndice+1)
        plt.hist( np.sum(is_one[:,0:ndice],axis=1),range=(-0.5,ndice+0.5),bins=(ndice + 1))
        x=np.arange(ndice)
        plt.plot(x,nsims*factorial(ndice)/factorial(x)/ \
        factorial(ndice-x)*prob**x*(1-prob)**(ndice-x),'r-')
        #plt.plot(x,nsims*comb(ndice,x)*prob**x*(1-prob)**(ndice-x),'ro')
        
        plt.title(str(ndice) + ' dice')
        plt.xlabel('Total number of ones')
        plt.ylabel('Frequency')
        plt.grid(True)

        # Statistical calculations
        print(f'\nndice: {ndice}')
        print(f'np.mean: {np.mean(np.sum(is_one[:, 0:ndice], axis=1))}')
        print(f'np.sum: {np.sum(np.sum(is_one[:, 0:ndice], axis=1)) * 1. / nsims:.4f}')
        print(f'Expected mean: {ndice * prob:.4f}')

        plt.show()  







        

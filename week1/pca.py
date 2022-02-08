from noseload import *
import numpy as np 
from matplotlib.pyplot import figure, plot, title, legend, xlabel, ylabel, show


def component_checker(varArray,thresh):
    variateDensity = varArray
    varExp = 0.0 #empty starter
    for i in range(len(variateDensity)):
        if varExp <= thresh:
            varExp += variateDensity[i]
        else: 
            print("finished with number of needed components: "+str(i) + " and explains "+str(varExp[0]*100)+"%")
            break

def component_plotter(data,vh,componentX,componentY):
    V = vh.T
    Z = centerMatrix @ V
    i = componentX
    j = componentY
    f = figure()
    title('NanoNose data: PCA')
    for c in range(C):
        class_mask = y==c
        plot(Z[class_mask,i],Z[class_mask,j],'o',alpha=0.5)
    legend(classNames)
    xlabel('PC{0}'.format(i+1))
    ylabel('PC{0}'.format(j+1))
    show()
    
    

means = np.empty((num_features,1),dtype=float) 
centerMatrix = np.empty((M,N))

for i in range(num_features):
    means[i] = np.mean(X[:,i])
    centerMatrix[:,i] = X[:,i]-means[i] #center
    
    
#singular value decomp 
u, s, vh = np.linalg.svd(centerMatrix) #s is already diagonalized

variateDensity = np.empty((num_features,1))
cumVar = np.sum(np.square(s))

for i in range(num_features):
    variateDensity[i] = np.square(s[i])/cumVar
    
threes_a_charm = np.sum([variateDensity[:3]]) #calculate variation explained

#check how many needed for 95% var explained
component_checker(variateDensity,0.95)
    

component_plotter(centerMatrix,vh,0,1)

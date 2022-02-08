from noseload import * 
from matplotlib.pyplot import figure, plot, title, legend, xlabel, ylabel, show


A = 0 #feature definitions 
B = 1 

plot(X[:,A],X[:,B],'o')

f = figure()
title('NanoNose data AB')

for c in range(C):
    class_mask = y==c
    plot(X[class_mask,A],X[class_mask,B],'o',alpha=0.3)
    
legend(classNames)
xlabel(attributeNames[A])
ylabel(attributeNames[B])
show()
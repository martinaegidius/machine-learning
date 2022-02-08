import xlrd 
import numpy as np 

doc = xlrd.open_workbook('/home/max/Desktop/s194119/machine_learning/02450Toolbox_Python/Data/nanonose.xls').sheet_by_index(0)

attributeNames = doc.row_values(rowx=0,start_colx=3,end_colx=11)
classLabels = doc.col_values(0,2,None)
classNames = sorted(set(classLabels))
classDict = dict(zip(classNames,range(len(classNames))))

y = np.array([classDict[value] for value in classLabels])
X = np.empty((len(classLabels),8))
num_features = 8
for i in range(num_features):
    X[:,i] = np.array(doc.col_values(i+3,2,None)).T
    
             
M = len(y)
N = len(attributeNames)
C = len(classNames)

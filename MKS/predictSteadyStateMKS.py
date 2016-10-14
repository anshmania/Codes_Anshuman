import MKS
import numpy as np
import matplotlib.pylab as plt
import pickle as pk
from MSf import MSf
import time

#Generate delta microstructures
MSf1 = MKS.GenDelta(21,False);
MSf2 = MKS.GenDelta(21,True);

#Pull in datasets
filename1 = "CalibrationModels/21deltaM_1surroundedBy2_strain.dat"
filename2 = "CalibrationModels/21deltaM_2surroundedBy1_strain.dat"

filenamePredict = "validationModel/21_2phase_strain.dat"
f = open("validationModel/21_2phase_strain.inp.microstructure")

MSpredict = pk.load(f)
MSpredict[MSpredict <1] = 2
f.close()

#Extract strain values
strain1 = MKS.ABstrains(filename1)
strain2 = MKS.ABstrains(filename2)
strainpredict = MKS.ABstrains(filenamePredict)
strainpredict = strainpredict/np.mean(strainpredict)

#Generate Microstructure Function
MSfpredict = MSf(MSpredict)
MSfpredict = MSfpredict[:,:,:,0,:] #Random microstructure

Macro = .02 #macroscale strain
coeff = MKS.GenC(MSf1, MSf2, filename1, filename2, Macro)

#Number of slice to look at for comparison of results.
n= 13

if MSpredict.shape[0] > coeff.shape[0]:
    coeff = MKS.ExpandCoeff(coeff,MSpredict.shape[0])
    n = MSpredict.shape[0]/2+3

startTime = time.time()
strainCalcpredict = MKS.NewResponse(coeff, Macro, MSfpredict)
endTime = time.time()

print 'Time to compute new response',(endTime-startTime),'secs'

plt.subplot(211)
p1 = plt.imshow(strainCalcpredict[n,:,:]/np.mean(strainCalcpredict))
plt.colorbar()
plt.title('Results using MKS')
plt.subplot(212)
p2 = plt.imshow(strainpredict[n,:,:])
plt.colorbar()
plt.title('Results using FEM')
plt.show()
#plt.subplot(211)
#p3 = plt.imshow(MSpredict[n,:,:])
#plt.title('2 Phase Microstructure')
#plt.subplot(212)
#error = ((strainCalcpredict[n,:,:])/np.mean(strainCalcpredict)-strainpredict[n,:,:])\
#        /(strainCalcpredict[n,:,:]/np.mean(strainCalcpredict))
#p3 = plt.imshow(((strainCalcpredict[n,:,:]/np.mean(strainCalcpredict))-strainpredict[n,:,:])\
#        /(strainCalcpredict[n,:,:]/np.mean(strainCalcpredict)))
#plt.title('Error between FEM and MKS')
#plt.colorbar()
#plt.show()


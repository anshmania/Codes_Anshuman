import scipy as sp
import numpy as np
from MS import MS

def MSf(MAT):
    Dim = MAT.shape #np array dimension
    l = len(Dim)
    print "array dimensions = ",l
    phases = sp.unique(MAT) #identify phases
    print "unique phases = ",phases
    numPhases = len(phases) #number of phases
    print "number of phases = ", numPhases
    if l == 2:
        MicroSF = np.zeros([Dim[0],Dim[1],1,1,numPhases])
        for ii in range(numPhases):
            Mask = np.ma.masked_equal(MAT, phases[ii])
            MicroSF[:,:,0,0,ii] = Mask*MicroSF[:,:,0,0,ii]
            MicroSF[:,:,0,0,ii] = MicroSF[:,:,0,0,ii]/phases[ii]
    elif l == 3:
        MicroSF = np.zeros([Dim[0],Dim[1],Dim[2],1,numPhases])
        for ii in range(numPhases):
            Mask = np.ma.masked_equal(MAT, phases[ii])
            MicroSF[:,:,:,0,ii] = Mask*MicroSF[:,:,:,0,ii]
            MicroSF[:,:,:,0,ii] = MicroSF[:,:,:,0,ii]/phases[ii]
    return MicroSF

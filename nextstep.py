import numpy as np
import pyedflib
import glob
import matplotlib.pyplot as plt
import pandas as pd

# generates a square wave
file_name = pyedflib.data.get_generator_filename()
f = pyedflib.EdfReader(file_name)
n = f.signals_in_file
signal_labels = f.getSignalLabels()
sigbufs = np.zeros((n, f.getNSamples()[0]))
for i in np.arange(n):
    sigbufs[i, :] = f.readSignal(i)

#print(sigbufs[0])
#print(type(sigbufs))
#print(sigbufs.shape)
#print(sigbufs[0], sigbufs[0].size, np.mean(sigbufs[0]))

#plt.plot(np.arange(10000), sigbufs[0][100000:110000])
#plt.show()


# the number of samples for each channel found in a file are homogenous
# there are 21 channels in each file

path = "./physionet.org/files/eegmat/1.0.0/"
rows = []
cols = pyedflib.EdfReader(path+"Subject00_1.edf").getSignalLabels()
mean_data = np.array([])


for file in glob.glob(path + "*"):
    data_entry = []
    if "Subject" in file:
        name = file[file.rfind("/")+1:file.rfind(".")]
        rows.append(name)
        #attribs.append(name)
        f = pyedflib.EdfReader(file)
        n = f.signals_in_file
        #attribs.append(n)
        nsamples = []
        for i in np.arange(n):
            nsamples.append(f.getNSamples()[i])
            data_entry.append(np.mean(f.readSignal(i)))
        mean_data = np.append(mean_data, data_entry)
        print(f.getSampleFrequency(0))
        #print(f"There are {n} channels in file {name}.")
        #print(nsamples)
        #print(f.getSignalLabels(), len(f.getSignalLabels()))
        #print(len(np.unique(nsamples) == 1))

        #print(np.unique(nsamples))
mean_data = mean_data.reshape((len(rows), len(cols)))
print(mean_data.shape)
df = pd.DataFrame(data=mean_data, index=rows, columns=cols)
#print(df.head(10))

        #print(file[file.rfind("/")+1:])
        #f = pyedflib.EdfReader(file)
        # number of channels in the file
        #n = f.signals_in_file
        # at which sites the waves were recorded eg.: 'EEG Fp1'
        #signal_labels = f.getSignalLabels()
        # print(f.getNSamples()[0])
        # 1D zero containing array. 
        # stores individual signals as rows
        #sigbufs = np.zeros((n, f.getNSamples()[0]))
        #print(sigbufs, sigbufs.shape)
        #for i in np.arange(n):
        #    sigbufs[i, :] = f.readSignal(i)
        
        #plt.plot(np.arange(f.getNSamples()[0]), sigbufs[0])
        #plt.title("EEG signal")
        #plt.show()
        #break;


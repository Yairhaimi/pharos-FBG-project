#%% NOTES
# W00 is background meas for the first FBG.
# settings: ppd=20, atn=10%, attenuator = 0.25%, lambda_bragg=1035.
# W01: first fbg. same settings.
# W02: second fbg. had some problems with it not being written idk.
# settings: attenuator=2%, lambda_bragg = 1050.
# 
# Daily conclusion: FBGs are not even being written into the core. Data is probably meaningless.
# A z-offset should be set to fix this problem.
# We took a microscope screen capture of the fiber's cross-section. This image should be analyzed in python or matlab in order to find the correct z-offset.
# 
#%% preamble

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import glob

files = glob.glob('./measurements/*')

data = [ pd.read_csv(f, header=None, skiprows=3, names=['f', 'amplitude'])[:-18] for f in files ]

#%%


n_skip_points = 15

for i, d in enumerate(data[:1]):
    f = d['f']
    amp = d['amplitude']
    
    plt.figure()
    plt.plot(*(f, amp)[::n_skip_points], '.', label='meas', markevery=n_skip_points)
    plt.xlabel('$f [Hz]$')
    plt.ylabel('Amplitude $[dB]$')
    plt.title(f'#{i+1} plot')
    plt.grid()

# %%

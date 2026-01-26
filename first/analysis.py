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

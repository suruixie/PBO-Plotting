#Read and plot gps time series
fgps = 'MCD1.pbo.nam08.csv'
ffig ='MCD1.png'

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as dates
from datetime import date as date

def loadpbogps(filename):
    gpsts = np.genfromtxt(filename, skiprows=12, dtype=[('Date','S10'),('North','float32'),('East','float32'),('Vertical','float32'),\
        ('North Std Deviation','float32'),('East Std Deviation','float32'),('Vertical Std Deviation','float32'),('Quality','S5')], delimiter=",")
    t_str = range(len(gpsts))
    gpsnev = np.zeros((len(gpsts),7))
    for i in range(len(gpsts)):
        yyyy_mm_dd = gpsts[i][0].split("-")
        t_str[i] = date(int(yyyy_mm_dd[0]),int(yyyy_mm_dd[1]),int(yyyy_mm_dd[2]))
        gpsnev[i,1] = gpsts[i][1]
        gpsnev[i,2] = gpsts[i][2]
        gpsnev[i,3] = gpsts[i][3]
        gpsnev[i,4] = gpsts[i][4]
        gpsnev[i,5] = gpsts[i][5]
        gpsnev[i,6] = gpsts[i][6]
    gpsnev[:,0] = dates.date2num(t_str)
    return gpsnev

def plottneu(tneu):
    fig, ax = plt.subplots(3,1, figsize=(10,10), sharex=True)
    ax[0].plot(tneu[:,0],tneu[:,1],c='red', marker='o', markersize=3,  mec='none', lw=0, figure=fig)
    ax[1].plot(tneu[:,0],tneu[:,2],c='red', marker='o', markersize=3,  mec='none', lw=0, figure=fig)
    ax[2].plot(tneu[:,0],tneu[:,3],c='red', marker='o', markersize=3,  mec='none', lw=0, figure=fig)
    ax[0].set_ylabel("North (mm)")
    ax[1].set_ylabel("East (mm)")
    ax[2].set_ylabel("Up (mm)")
    fmtter = dates.DateFormatter('%Y')
    ax[2].xaxis.set_major_formatter(fmtter)
    fig.savefig(ffig)
    plt.show()

gps_tneu = loadpbogps(fgps)
plottneu (gps_tneu)




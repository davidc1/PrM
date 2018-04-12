import struct
from struct import *
import pandas as pd
import matplotlib.pyplot as plt
import sys,os
import numpy as np

plt.ion()

def GetWaveforms(fin):

    bf = open(fin,'rb')
    bd = bf.read()
    
    b = 0
    
    byte_v = [4,4,4,2,4,2,4,2,4,2,2,2,4,2,2,4,4,4,4,4,4,4]
    
    currbyte = 0
    ctr = 0
    fmt = ''
    for byte in byte_v:
        if byte == 4:
            fmt = 'I'
        if byte == 2:
            fmt = 'H'
        cS = struct.unpack(fmt,bd[currbyte:currbyte+byte])[0]
        currbyte += byte
        #print 'word %02i : '%ctr,cS
        ctr += 1

    byte_v = [8,8]
    words_v = []
    for byte in byte_v:
        fmt = 'd'
        cS = struct.unpack(fmt,bd[currbyte:currbyte+byte])[0]
        currbyte += byte
        #print 'word %02i : '%ctr,cS
        words_v.append(cS)
        ctr += 1

    dt = words_v[-1]*1e3

    byte_v = [4,4]
    out_v = []
    for byte in byte_v:
        fmt = 'I'
        cS = struct.unpack(fmt,bd[currbyte:currbyte+byte])[0]
        currbyte += byte
        #print 'word %02i : '%ctr,cS
        ctr += 1
        out_v.append(cS)

    nchan = int(out_v[0])
    nword = int(out_v[1])

    time_v = np.linspace(0,nword*dt,nword)

    #print 'number of channels : ',nchan
    #print 'number of words    : ',nword

    #fig = plt.figure(figsize=(10,6))

    ev_wf_v = []
    
    byte = 4
    wf_v = []
    for i in xrange(50):
        wf_v = []
        for ch in xrange(nchan):
            #print 'WAVEFORM %i'%ch
            wf_v.append([])
            for n in xrange(nword):
                cS = struct.unpack('f',bd[currbyte:currbyte+byte])[0]
                wf_v[-1].append(cS)
                currbyte += byte

        ev_wf_v.append(wf_v)

        '''
        fig.gca().cla()
        
        plt.plot(time_v,wf_v[0],label='Anode Signal')
        plt.xlabel('Time [ms]',fontsize=20,fontweight='bold')
        plt.ylabel('Amplitude [V]',fontsize=20,fontweight='bold')
        plt.plot(time_v,wf_v[1],label='Cathode Signal')
        plt.ylim([-0.025,+.025])
        plt.legend(loc=1,fontsize=16)
        plt.grid()
        
        fig.canvas
        fig.canvas.draw()

        inval = raw_input('type to continue. q to quit.')
        if (inval == 'q'):
            break
        '''

    return ev_wf_v

#!/usr/bin/env python3

# reads DAQ csv file and plots pretty graphs
#
# example usage:
# ./readDAQcsv.py 004.csv 005.csv 006.csv
# or
# python readDAQpoop.py 004.csv 005.csv 006.csv

#import argparse
import sys
import pandas as pd
#import matplotlib.pyplot as plt
from bokeh.layouts import column
from bokeh.plotting import figure, output_file, show
from bokeh.palettes import Dark2_5 as palette
import itertools

output_file('DAQpoop.html')

def hhmmssms_to_ms(t):
    hh, mm, ss, ms = [int(i) for i in t.split(':')]
    return 3600000*hh + 60000*mm + 1000*ss + ms

stool = []
colors = itertools.cycle(palette)

# for each csv file passed as argument, add subplot to graph
for csvfile, color in zip(sys.argv[1:], colors):	# read csv files from args

    df = pd.read_csv(csvfile)   # open csv file as pandas dataframe

    # define time array (ms)
    time = []

    # parse sensor data
    sensorval = df.iloc[0:,3:].values.tolist()

    # create a new plot
    s = figure(plot_width=800, plot_height=200, title=None)

    # Calculate t0 in ms
    t0_ms = hhmmssms_to_ms(df.PC_TIME_STAMP.unique().tolist()[0])

    # Perform depth-first search to create continuous time array
    for timestamp in df.PC_TIME_STAMP.unique().tolist():
        timestamp_ms = hhmmssms_to_ms(timestamp) - t0_ms
        for reftime in df.REF_TIME[df.PC_TIME_STAMP == timestamp].unique().tolist():
            time.append(timestamp_ms + float(reftime)*100)

    s.line(time, sensorval, color=color, line_width=2)
    s.circle(time, sensorval, size=4, color=color, alpha=0.5)

    #s.line(df.REF_TIME.values.tolist(), df.iloc[0:,3:].values.tolist(), color=color, line_width=2)
    #s.circle(df.REF_TIME.values.tolist(), df.iloc[0:,3:].values.tolist(), size=4, color=color, alpha=0.5)

    s.yaxis.axis_label = str(df.columns.values[3])

    stool.append(s)

    #plt.plot(df.REF_TIME,df.iloc[0:,3:], label=df.columns[3])

print(stool)
s.xaxis.axis_label = str('time (ms)')
show(column(stool))

#plt.legend()
#plt.ylabel('human words')
#plt.xlabel('time')
#plt.grid(b=True, which='major')
#plt.grid(b=True, which='minor')
#plt.minorticks_on()
#plt.show()

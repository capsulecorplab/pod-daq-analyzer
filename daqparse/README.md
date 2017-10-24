# daqparse - interpret CSV data from DAQ

DAQ data is expected to be in regular CSV form, with a first line providing
column leaders.

The tools for interpreting the data are expected to run on a laptop or
desktop machine, not the pod computers.  Scripts are envisioned in a
combination of Python and NumPy-based visualization such as Bokeh.

Example csv files included as 004.csv and 005.csv

# Dependencies

Following modules are imported using python3:

* sys
* pandas
* bokeh
* itertools

# Setup (linux)

Install dependencies:

    $ pip3 install sys bokeh pandas itertools

Change file permission to executable:

    $ chmod +x readDAQcsv.py

# Run DAQ parser (example)

    $ ./readDAQcsv.py 004.csv 005.csv

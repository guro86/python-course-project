# python-course-project

Description of project: 

I tested an implemetation using one GP to predict a multivariate output, and
then I created an ensamnle class that uses specifict gaussian processes for
each output dimension. The result is that the accuracty is improved.


To do: 

* Add derivative caluclations. 
* Improve the precition method so that that it takes us instead of ms. That
  since it is potentially going to be used in MCMC which is sensitive to
  performace. 

Description of files:
.
├── data.p                    #pickled and processed train and test data 
├── data_preparation.py       #script that preprocesses the data and save it
├── gp_accuracy_test.py       #Checking accuracy between one or several gps
├── gp_performance_improvement.ipy #Testing my new class
├── lib                       #Library module
│   ├── dataloader.py         #Data loader that loads data.p
│   ├── gp.py                 #My ensamble gp implementation
│   ├── __init__.py
│   ├── plotting.py           #Plotting functions, now just validation plot
│   └── __pycache__
│       ├── dataloader.cpython-39.pyc
│       ├── gp.cpython-39.pyc
│       ├── __init__.cpython-39.pyc
│       └── plotting.cpython-39.pyc
├── raw_data                  #Raw data coming from a higher order metho
│   ├── calibration_samples.csv
│   └── tu_data.csv
└── README.md                 #This file

3 directories, 15 files

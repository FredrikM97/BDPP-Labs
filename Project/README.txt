BDPP_Project-ML-Combined contains all the data needed for analysis and preprocessing. 

# Overview
* Since all is run through one file there is different stages, IBM does not handle different types in the columns therefor they are casted at the beginning after importing the data.
* In case of running locally uncomment the "setup_spark" function call.

* Different functions that is repeated is then defined, these are defined at the top since they are used from the first part in order to start logging.
* Thereafter # Setup environment is used to define state, directories and different output modes. 
* Be careful to run log_mode, debug_mode and enable_plots since they can cause problem on greater data sets and is only used for analysis and debugging of code in order to run the code as a job behind the scene and still present data.

Debugging: 
* Since the program logs data if log_mode is enabled then they will per default be stored into a "models" and "analysis" folder, the log_mode include storing: actions, images and models. 
* The debug_mode limits the number of data points to give faster processing. enable_plots decide if plots should be displayed. Since they call on pandas dataframe for plotting they are optional to use!


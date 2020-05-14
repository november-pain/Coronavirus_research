# The purpose of program.

The purpose of this program is to analise data about
COVID-19 in USA. It should find the correlation between testing activity
and increase of number of new covid cases. Program makes calculations for each
state separately and draws a graph. The idea of those calculations is to
compare ratios of growth in number of positive cases, number of negative cases
and number of all conducted tests for each day. This should show how much the 
increasing in test number affects statistics. 

## Input data.
The file with input data is us_states_covid19_daily.csv where is the all 
data that is required by the program.


The program uses Kaggle API to collect data from internet. It downloads and 
unzips the dataset, but this requires authentication. I have uploaded the 
csv file to github so user can use it. The other way is to authenticate 
using Kaggle account and downloading json file.

## The stucture of the main module.
The main module where all calculations are made is us_states_covid.py.
This module includes:
* `def csv_to_df(path)` - this function reads csv file and puts all data in
DataFrame. 
* `def date_convert(num)` - this function converts data format into datetime
object
* `class State` - every instance of this class represents a State of USA.
It contains DataFrame with data about covid tests. During initialization it
it creates its DataFrame, proceeds all calculations, draws a graph and puts
it into results directory. 
* `class USA` - the main class which contains an array of all instances of class
State, that are created during the initialization. Also it collects all 
claculation results of each state and calculates the average.


 
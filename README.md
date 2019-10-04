# Spectral Meter Usage App

This repository contains the setup and usage instructions for the gRPC and Flask based app to get meter usage data

## Setup

Create a new directory on your computer, then set up and activate a python3 virtual environment

```bash
virtualenv env
source env/bin/activate 
```

Clone this github repository and download the required libraries
```bash
git clone https://github.com/avarnajain/spectral_meterusage.git
pip3 install -r requirements.txt
```

## Usage

To use the app, you have to start two servers on two different bash terminals, remember to activate the virtual environment on both

1. gRPC server - accessing the data from the csv file

```bash
python3 gRPC_server.py
```

2. Flask server - returning the data to you on your browser

```bash
python3 flask_server.py
```

Go to your browser and enter the address for your flask app, set to ```localhost:5000```

Fill out the form for the dates you want, press submit, and voila!

### Example Graph

An example of the graph returned is as follows:

![meter usage graph](example_plot.png)

If you fill out the form with a date range for which we have no data or with invalid dates, the flask server will redirect back to the homepage and give a 404 error. If part of the date range specified is in the database, the graph will show the data for those specific days only

## Testing
I used the python unittest module to test my Flask routes. The following command on your terminal will run the tests in python (make sure your gRPC server is running in the background)

```bash
python3 tests.py
```
I also used the python coverage module to check the coverage of my tests on the flask app. Run the following command on your bash terminal to see the coverage 

```bash
coverage report -m
```

The app is currently at 98% total coverage

![test coverage](test_coverage.png)

## Resources and Blockers

gRPC Server + csv

Using the gRPC server was the most time consuming part of this prompt for me. After a fair bit of reading, I decided to follow the steps provided by the following [link](https://www.semantics3.com/blog/a-simplified-guide-to-grpc-in-python-6c4e25f0c506/) to set up my basic gRPC server. Following the same steps, I modified the functions as needed for the prompt, starting with a single input function that queried the csv file, and then moving onto the two input (start and end date) function. My main blocker with the gRPC server was formatting my response to be a dictionary or a list. I had to settle with returning a string version of the meter usage values, which I then convert back into a dictionary of datetime objects on my flask server. Since I have worked with csv files before, I used the same csv library I am familiar with to open and read the data provided. 

Flask Server + HTML

I set up a flask server with a form on the homepage with start and end date as the input values. Since the data given to me was for a month only, I thought it might be more interesting to see patterns in meter usage over the course of a day, which I showcase in the output in the form of a line graph. But this can easily be changed based on the use case for the app.

Plotting

I have some previous experience using ggplot on R, but none using pandas, so I took some time to read through the types of ways to join dataframes in order to create the line plot. I finally settled with using the merge function, which I was only able to use with a for loop and two data frames at a time, instead of a list of dataframes. Once the final df was created, I plot the figure and added some detail on the axes and title. 

Everytime a plot is created, it is stored in the static folder with a name based on the time the plot was created, making each plot unique to prevent caching on the browser. 

Testing

To test my flask app, I decided to use the python unittest module. To run the tests, you have to first run the gRPC_server locally on a different terminal. I wrote 4 different tests for the app - 
1. To check that the homepage renders the form itself
2. To check that a plot is returned on the successful submission of the form
3. To check that a 404 error is returned when the form is submitted with dates for which we have no data
4. To check that a 404 error is returned when the form is submitted with invalid dates

I also used the python coverage module to check my test coverage.



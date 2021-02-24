# SENTIDATALYZER
Sentidatalyzer is a sentiment analyzer application that identifies the customer sentiment through the customer feedback and accordingly sends the input data to the output file for analytics to predict customer’s satisfaction behaviour .

## TCS INFRAMIND SEASON 4 ROUND 2 SUBMISSION: ENTERPRISE AI
![] (https://github.com/swapnil-mishra/sentidatalyzer/blob/main/git-images/tcscover.png)
<img src="https://github.com/swapnil-mishra/sentidatalyzer/blob/main/git-images/home.png" width="500">  <img src="https://github.com/swapnil-mishra/sentidatalyzer/blob/main/git-images/analyze.png" width="500">

### STEPS TO FOLLOW:
#### Accessing files:

 - open the folder from file menu
 - open new terminal and check python 3 version : `python --version`
 - install flask and other modules: `pip install module_name`
 - run the program: `python app.py`
 - CTRL+click the link (Ex: http://127.0.0.1:5000/) received at the end of running the python file
 - The output file opens in a new tab.

#### Entering data:
 - navigate to analyze now in `index.html` to fill up customer feedback form and click submit
 - sentiment analysis output is shown on the right side of display
 - data entered by the user is appended on submit inside `data.csv`

#### Analyzing data:
 - go to `data.ipynb` file and run all the cells.
 - data outputs of analysis will be available in the python script file. Visualization outputs are written to respective plots images inside `static/plots` path and the model data output inside `Output.csv` file

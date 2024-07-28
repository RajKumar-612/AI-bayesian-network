bnet.py:
This program learns the conditonal probabilty tables for the bayesian network from the training data and calculates
the probabilty for any event given evidence (if available) using inference by enumeration.

Code Structure:
The program reads the training_data and calculates the conditonal probabilty tables for the bayesian network.
Command line arguemts are read and appropriate values are assigned to query evidence variables.
If any variable value is not given then its value is None.
probabilties of query variables and given varibales are calculated using inference by enumaration,
and the division of these two values will be the final answer.
While doing inference by enumaration all the possibilities are combined i.e for all the variables whose value is None,
both true and false cases are calculated.

Usage:

To run the program, navigate to the project directory and run the following command:

python bnet.py <training_data> <query variable values> [given <evidence variable values>]
Example:
python bnet.py training_data.txt Bt Gf given Ff










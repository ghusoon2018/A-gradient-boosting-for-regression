# A-gradient-boosting-for-regression

A dataset is created from a base dataset by subtracting the prediction of the offset function from each example. 

This  generates the data each time as needed. 
The amount of space used is constant, independent on the size of the data set

A boosting learner takes in a dataset and a base learner, and returns a new predictor. The base learner, takes a dataset, and returns a Learner object.

#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from learnProblem import Data_set, Learner

 class Boosted_dataset(Data_set):
    def __init__(self, base_dataset, offset_fun):
         # new dataset,  offset_fun(e) is subtracted from the target of each example 
        self.base_dataset = base_dataset 
        self.offset_fun = offset_fun
        Data_set.__init__(self, base_dataset.train, base_dataset.test,
        base_dataset.prob_test, base_dataset.target_index)
        
    def create_features(self):
    self.input_features = self.base_dataset.input_features

    def newout(e):
    return self.base_dataset.target(e) - self.offset_fun(e)
    newout.frange = self.base_dataset.target.frange
    self.target = newout

    #  The base learner, takes a dataset, and returns a Learner object.

class Boosting_learner(Learner):
    def __init__(self, dataset, base_learner_class):
    self.dataset = dataset
    self.base_learner_class = base_learner_class
    mean = sum(self.dataset.target(e)
               
    for e in self.dataset.train)/len(self.dataset.train)
    
    self.predictor = lambda e:mean # function that returns mean for each example
    self.predictor.__doc__ = "lambda e:"+str(mean)
    self.offsets = [self.predictor]
    self.errors = [data.evaluate_dataset(data.test, self.predictor, "sum-of-squares")]
    self.display(1,"Predict mean test set error=", self.errors[0] )


    def learn(self, num_ensemble=10):
    # adds num_ensemble learners to the ensemble. returns a new predictor.

    for i in range(num_ensemble):
        train_subset = Boosted_dataset(self.dataset, self.predictor)
        learner = self.base_learner_class(train_subset)
        new_offset = learner.learn()
        self.offsets.append(new_offset)
        
    def new_pred(e, old_pred=self.predictor, off=new_offset):
        return old_pred(e)+off(e)
        self.predictor = new_pred
        self.errors.append(data.evaluate_dataset(data.test, self.predictor,"sum-of-squares"))
        self.display(1,"After Iteration",len(self.offsets)-1,"test set error=", self.errors[-1])
        return self.predictor



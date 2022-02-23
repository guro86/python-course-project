# python-course-project

Description of the project:

Gaussian process techniques play an essential role in regression, and modelers widely use them as surrogate models in place of a simulation tool to make optimization/calibration methods practical. 
Gaussian processes are available through several high-level APIs. For example, Sklearn offers a Gaussian process regressor to fit a multivariate input and a univariate output. 
My research demands regressors that simultaneously predict multivariate outputs and corresponding derivatives. 

Therefore, in my project, I will try to inherit the GaussianProcessRegressor class from Sklearn and extend it with a method that calculates derivatives. 
Additionally, I will create an ensemble class that uses several Gaussian processes to evaluate several outputs simultaneously. 

# Master Thesis
Disclaimer: The submitted master thesis, "Statistical Distance-based Model-agnostic Confidance Measueres" makes use of a pre-existing code base for the library "SafeML". The development of the library is not a contribution for the master thesis, However, imporvements to the library in the form of refactorization to increase speed and addition of a new distance measure are a contribution of the master thesis. All files in this repo are to be considered the main contribution of the thesis.

An installation of the full library and its depandancies is not necessary to run the parts relevant to the master thesis, as the module "DistanceMetricsVec.py" - which includes the refactored distance metrics and the new statistical test - only requires the numpy library.


# Included Notebooks

the following notebooks are included in the repo:
## Bootstrap Power Analysis

The testing of the proposed non-parametric power analysis method is in the notebook
"BootstrapPowerAnalysis_GTSRB.ipynb"

## Epps and Singleton Test

The evaluation of Epps and Singleton method can be found in the notebook
"ES_Distance_Evaluation.ipynb"

Additionally, time comparasion of all the test with the CPU implementation and GPU (which is not released publicly yet) can be found in the notebook
"TimeComparasion.ipynb"

## Scope Compliace Uncertainy Estimators 

The evaluation and development of the SCUEs and its differet iterations can be found in the notbooks
"DesignCorruption_iter*"

Additionally, the testing of the method for the CARLA dataset is in the notebook
"CARLA_dataset.ipynb"



# SafeML

The original public SafeML library can be found in the repo
https://github.com/ISorokos/SafeML
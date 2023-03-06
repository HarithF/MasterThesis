# Master Thesis
Disclaimer: The submitted master thesis, _Statistical Distance-based Model-agnostic Confidance Measueres_ makes use of a pre-existing code base for the library _SafeML_. The development of the library is not a contribution for the master thesis, However, imporvements to the library in the form of refactorization to increase speed and addition of a new distance measure are a contribution of the master thesis. All files in this repo are to be considered the main contribution of the thesis.

An installation of the full library and its depandancies is not necessary to run the parts relevant to the master thesis, as the module **DistanceMetricsVec.py** - which includes the refactored distance metrics and the new statistical test - only requires the numpy library.

However it can be installed using the following command:
`pip install safeml`


# Included Notebooks

the following notebooks are included in the repo:
## Bootstrap Power Analysis

The testing of the proposed non-parametric power analysis method is in the notebook
**BootstrapPowerAnalysis_GTSRB.ipynb**

## Epps and Singleton Test

The evaluation of Epps and Singleton method can be found in the notebook
**ES_Distance_Evaluation.ipynb**

Additionally, time comparasion of all the test with the CPU implementation and GPU (which is not released publicly yet) can be found in the notebook
**TimeComparasion.ipynb**

## Scope Compliace Uncertainy Estimators 

The evaluation and development of the SCUEs and its differet iterations can be found in the notbooks
__DesignCorruption_iter*__

Additionally, the testing of the method for the CARLA dataset is in the notebook
**CARLA_dataset.ipynb**

## Utils

The calculation of the critical values is done through the function in the module **CriticalValues.py**, where a table of precalculated Anderson-Darling Values for different confidance levels and number of trials (for Bonferroni correction) are tabuleted (in **AD_crit.csv**) as the calcualtation of these values is time consuming.



# SafeML

The original public SafeML library can be found in the repo
https://github.com/ISorokos/SafeML
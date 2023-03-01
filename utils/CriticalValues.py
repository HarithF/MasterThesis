import numpy as np
import pandas as pd
import os

def KS_crit(alpha, n, m):
    """
    calculates scaled the critical distance value at which hypothesis test is rejected for two samples testing
    with arrays of different sizes Kolmogrov Sirminov test.
    
    Args:
        alpha (float): confidance level of the hypothesis test
        n (int): size of array 1
        m (int): size of array 2
        
    Returns:
        (flaot): critical value c(a)"""
    
    c = np.sqrt((-1 * np.log(alpha/2)) * 0.5)
    scale = np.sqrt((n+m)/(n*m))

    return c*scale


def AD_crit(alpha, n, m, trails = None):
    """
    calculates scaled the critical distance value at which hypothesis test is rejected for two samples testing
    with arrays of different sizes for Anderson Darling test.
    
    Args:
        alpha (float): confidance level of the hypothesis test
        n (int): size of array 1
        m (int): size of array 2
        
    Returns:
        (flaot): critical value c(a)
    """
    k = n + m
    ad_infDict = {.15:1.610, .1: 1.9335, .05:2.4921, .01:3.857}

    if (trails is not None):
        vals = pd.read_csv(os.path.join(os.getcwd(),"AD_crit.csv"), index_col=0)
        ad_inf = vals[str(alpha)].loc[trails]
    else:
        if (alpha not in ad_infDict.keys()):
            raise "alpha value not enumerated"
        else:
            ad_inf = ad_infDict[alpha]
        

    c = (ad_inf - 1)*(1 - (1.55/k)) + 1
    
    return c

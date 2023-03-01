'''
Description: This module contains the vectorized functions for SafeML Metrics calculation.
Referances:

'''

import numpy as np


#Cramer-Von Mises Distance

def CVM_Dist_p(XX, YY):
    '''
    L1-version of the cramer von mieses distance
    F. Schmid & M. Trede (1995) A distribution free test for the two sample problem for general alternatives, Computational Statistics & Data Analysis, 20:4, 409-419
    '''
    nx = len(XX)
    ny = len(YY)
    n = nx + ny

    XY = np.concatenate([XX,YY])
    X2 = np.concatenate([np.repeat(1/nx, nx), np.repeat(0, ny)])
    Y2 = np.concatenate([np.repeat(0, nx), np.repeat(1/ny, ny)])

    S_Ind = np.argsort(XY)
    XY_Sorted = XY[S_Ind]
    X2_Sorted = X2[S_Ind]
    Y2_Sorted = Y2[S_Ind]

    Res = 0
    E_CDF = X2_Sorted[:-1].cumsum()
    F_CDF = Y2_Sorted[:-1].cumsum()
    height_mask = (XY_Sorted[1:] != XY_Sorted[:-1])
    power = 1
    
    Res =  np.sum((abs(F_CDF - E_CDF)*height_mask)**power)
    
    return  Res
    
    
    
def CVM_Dist_PVal(XX, YY, nboots = 1000):
    '''
    This function returns the Cramer-Von Mises distance between given numpy arrays and pVal.
    nboots is the optional input for pVal accuracy. Default value is 1000.
    '''

    CVM = CVM_Dist_p(XX,YY)
    na = len(XX)
    nb = len(YY)
    n = na + nb
    comb = np.concatenate([XX,YY])

    e_list = np.random.rand(nboots, n).argpartition(na)[:,:na]
    f_list = np.random.rand(nboots, n).argpartition(na)[:,:na]
    
    result = np.empty(nboots)
    for i,(x,y) in enumerate(zip(e_list, f_list)):
        result[i] = CVM_Dist_p(comb[x],comb[y])
        
    bigger = (result > CVM).sum()
    
    pVal = bigger/nboots

    return pVal, CVM


#Wasserstein Distance

def Wasserstein_Dist_p(XX, YY):
    '''
    This function returns Wasserstein Distance between the two given numpy arrays. 
    Ramdas, A., Garcia, N., & Cuturi, M. (2015). On Wasserstein Two Sample Testing and Related Families of Nonparametric Tests (arXiv:1509.02237). 

    '''
    nx = len(XX)
    ny = len(YY)
    n = nx + ny
    
    #print(XX)
    XY = np.concatenate([XX,YY])
    X2 = np.concatenate([np.repeat(1/nx, nx), np.repeat(0, ny)])
    Y2 = np.concatenate([np.repeat(0, nx), np.repeat(1/ny, ny)])

    S_Ind = np.argsort(XY)
    XY_Sorted = XY[S_Ind]
    X2_Sorted = X2[S_Ind]
    Y2_Sorted = Y2[S_Ind]

    Res = 0
    E_CDF = X2_Sorted[:-1].cumsum()
    F_CDF = Y2_Sorted[:-1].cumsum()
    power = 1
    width = (XY_Sorted[1:] - XY_Sorted[:-1])
    Res = ((abs(E_CDF - F_CDF)**power) * width).sum()

    return Res

def Wasserstein_Dist_PVal(XX, YY, nboots = 1000):
    '''
    This function returns the Wasserstein Distance between given numpy arrays and corresponding pVal.
    nboots is the optional input for pVal accuracy. Default value is 1000.

    '''
    WD = Wasserstein_Dist_p(XX,YY)
    na = len(XX)
    nb = len(YY)
    n = na + nb
    comb = np.concatenate([XX,YY])

    e_list = np.random.rand(nboots, n).argpartition(na)[:,:na]
    f_list = np.random.rand(nboots, n).argpartition(na)[:,:na]
    
    result = np.empty(nboots)
    for i,(x,y) in enumerate(zip(e_list, f_list)):
        result[i] = Wasserstein_Dist_p(comb[x],comb[y])
        
    bigger = (result > WD).sum()
    
    pVal = bigger/nboots

    return pVal, WD

#Anderson Darling Distance

def Anderson_Darling_Dist_p(XX, YY):
    '''
    This function returns Anderson Darling Distance between the two given numpy arrays. 

    Pettitt, A.N. (1976). A two-sample Anderson-Darling rank statistic. Biometrika, 63, 161-168.
    '''
    nx = len(XX)
    ny = len(YY)
    n = nx + ny

    XY = np.concatenate([XX,YY])
    X2 = np.concatenate([np.repeat(1/nx, nx), np.repeat(0, ny)])
    Y2 = np.concatenate([np.repeat(0, nx), np.repeat(1/ny, ny)])

    S_Ind = np.argsort(XY)
    XY_Sorted = XY[S_Ind]
    X2_Sorted = X2[S_Ind]
    Y2_Sorted = Y2[S_Ind]

    Res = 0
    E_CDF = X2_Sorted[:-1].cumsum()
    F_CDF = Y2_Sorted[:-1].cumsum()
    G_CDF = np.arange(0, n-1, 1)/n
    SD = (n * G_CDF * (1-G_CDF))**0.5
    mask = (XY_Sorted[1:] != XY_Sorted[:-1]) & (SD > 0)
    power = 1
    
    Res = ((abs(F_CDF[mask] - E_CDF[mask])/SD[mask])**power).sum()

    AD_Dist = Res
    
    return AD_Dist

def Anderson_Darling_Dist_PVal(XX, YY, nboots = 1000):
    '''
    This function returns Wasserstein Distance between the two given numpy arrays with pVal. 
    nboots is the optional input for pVal accuracy. Default value is 1000.

    
    '''
    AD = Anderson_Darling_Dist_p(XX,YY)
    na = len(XX)
    nb = len(YY)
    n = na + nb
    comb = np.concatenate([XX,YY])

    e_list = np.random.rand(nboots, n).argpartition(na)[:,:na]
    f_list = np.random.rand(nboots, n).argpartition(na)[:,:na]
    
    result = np.empty(nboots)
    for i,(x,y) in enumerate(zip(e_list, f_list)):
        result[i] = Anderson_Darling_Dist_p(comb[x],comb[y])
        
    bigger = (result > AD).sum()
    
    pVal = bigger/nboots

    return pVal, AD


#Kolmogorov Smirnov Distance

def Kolmogorov_Smirnov_Dist_p(XX, YY):
    '''
    This function returns Kolmogorov Smirnov Distance between the two given numpy arrays. 
    '''
    nx = len(XX)
    ny = len(YY)
    n = nx + ny

    XY = np.concatenate([XX,YY])
    X2 = np.concatenate([np.repeat(1/nx, nx), np.repeat(0, ny)])
    Y2 = np.concatenate([np.repeat(0, nx), np.repeat(1/ny, ny)])

    S_Ind = np.argsort(XY)
    XY_Sorted = XY[S_Ind]
    X2_Sorted = X2[S_Ind]
    Y2_Sorted = Y2[S_Ind]

    E_CDF = X2_Sorted[:-1].cumsum()
    F_CDF = Y2_Sorted[:-1].cumsum()
    height_mask = (XY_Sorted[1:] != XY_Sorted[:-1])
    power = 1
    
    Res = (abs(E_CDF - F_CDF)*height_mask).max()
    
    KS_Dist = Res**power
    
    return KS_Dist
  
def Kolmogorov_Smirnov_Dist_PVal(XX, YY, nboots = 1000):
    '''
    This function returns Kolmogorov Smirnov Distance between the two given numpy arrays with pVal. 
    nboots is the optional input for pVal accuracy. Default value is 1000.

    '''
    KSD = Kolmogorov_Smirnov_Dist_p(XX,YY)
    na = len(XX)
    nb = len(YY)
    n = na + nb
    comb = np.concatenate([XX,YY])

    e_list = np.random.rand(nboots, n).argpartition(na)[:,:na]
    f_list = np.random.rand(nboots, n).argpartition(na)[:,:na]
    
    result = np.empty(nboots)
    for i,(x,y) in enumerate(zip(e_list, f_list)):
        result[i] = Kolmogorov_Smirnov_Dist_p(comb[x],comb[y])
        
    bigger = (result > KSD).sum()
    
    pVal = bigger/nboots

    return pVal, KSD


# DTS Distance (Combination of Anderson Darling and Cramer-Von Mises Distances)

def DTS_Dist_p(XX, YY):
    '''
    This function returns DTS Distance between the two given numpy arrays. 
    Dowd, C. (2020). A New ECDF Two-Sample Test Statistic (arXiv:2007.01360). 
    '''
  

    import numpy as np
    nx = len(XX)
    ny = len(YY)
    n = nx + ny

    XY = np.concatenate([XX,YY])
    X2 = np.concatenate([np.repeat(1/nx, nx), np.repeat(0, ny)])
    Y2 = np.concatenate([np.repeat(0, nx), np.repeat(1/ny, ny)])

    S_Ind = np.argsort(XY)
    XY_Sorted = XY[S_Ind]
    X2_Sorted = X2[S_Ind]
    Y2_Sorted = Y2[S_Ind]

    Res = 0
    E_CDF = X2_Sorted[:-1].cumsum()
    F_CDF = Y2_Sorted[:-1].cumsum()
    G_CDF = np.arange(0, n-1, 1)/n
    SD = (n * G_CDF * (1-G_CDF))**0.5
    mask = (SD > 0)
    width = (XY_Sorted[1:] - XY_Sorted[:-1])
    power = 1
    
    Res = (((abs(E_CDF[mask] - F_CDF[mask])/SD[mask])**power)*width[mask]).sum()
    
    return Res

def DTS_Dist_PVal(XX, YY, nboots = 1000):
    '''
    This function returns DTS Distanc between the two given numpy arrays with pVal. 
    nboots is the optional input for pVal accuracy. Default value is 1000.

    '''
    DTS = DTS_Dist_p(XX,YY)
    na = len(XX)
    nb = len(YY)
    n = na + nb
    comb = np.concatenate([XX,YY])

    e_list = np.random.rand(nboots, n).argpartition(na)[:,:na]
    f_list = np.random.rand(nboots, n).argpartition(na)[:,:na]
    
    result = np.empty(nboots)
    for i,(x,y) in enumerate(zip(e_list, f_list)):
        result[i] = DTS_Dist_p(comb[x],comb[y])
        
    bigger = (result > DTS).sum()
    
    pVal = bigger/nboots

    return pVal, DTS

def ES_Dist(XX, YY, t=(0.4, 0.8)):
    from scipy.stats import chi2
    
    XX, YY, t = np.asarray(XX), np.asarray(YY), np.asarray(t)
    XY = np.concatenate((XX, YY))
    
    nx, ny = len(XX), len(YY)
    n = nx + ny
    

    # rescale t with semi-interquantile range
    sigma = (np.percentile(XY, 75, interpolation = 'midpoint') - 
             np.percentile(XY, 25, interpolation = 'midpoint')) / 2 

    ts = t.reshape((-1, 1)) / sigma

    # covariance estimation
    gxm = np.vstack((np.cos(ts*XX), np.sin(ts*XX)))
    gym = np.vstack((np.cos(ts*YY), np.sin(ts*YY)))
    g_diff = np.mean(gxm, axis=1) - np.mean(gym, axis=1)
    
    Sx = ((nx - 1)/nx) * np.cov(gxm)
    Sy = ((ny - 1)/ny) * np.cov(gym)
    
    omega = (n/nx)*Sx + (n/ny)*Sy
    omega_inv = np.linalg.pinv(omega)
    
    rank = np.linalg.matrix_rank(omega_inv)
    
    
    W2 = n*np.dot(g_diff, np.dot(omega_inv, g_diff.T)) #equation (10) in the paper

    # apply small-sample correction
    if (max(nx, ny) < 25):
        corr = 1.0/(1.0 + n**(-0.45) + 10.1*(nx**(-1.7) + ny**(-1.7)))
        W2 = corr * W2

    p = 1 - chi2.cdf(W2, rank)

    return W2, p
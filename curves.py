import numpy as np
from scipy.optimize import curve_fit

def schreiber(X):
    # from schreiber 1904
    p,pet = X
    return 1 - np.exp(-pet/p)

def oldekop(X):
    # from ol'dekop 1911
    p,pet = X
    return (pet/p)*np.tanh(p/pet)

def turc_pike(X):
    # from Turc 1954 and Pike 1964
    p,pet = X
    return (pet/p) / (((pet/p)**2)+1)**0.5
    
def budyko(X):
    # from Budyko 1958
    p,pet = X
    return np.sqrt(((pet/p)*np.tanh(p/pet))*(1-np.exp(-pet/p)))

def mcy(X,n):
    # from Mezentsev 1955, Choudhury 1999, and Yang et al. 2008
    p,pet = X
    return (((pet/p)**-n)+1)**(-1/n)

def fit_mcy(X,y):
    popt,pcov = curve_fit(mcy,X,y) # fit for n
    n = popt[0] # extract n
    if n<= 0:
        print 'Warning: Parameter out of range 0 < n <= 1.'
    
    return n
    
def fuzhang(X,omega):
    # from Fu 1981 and Zhang et al. 2004
    p,pet = X
    return 1+(pet/p)-(((pet/p)**omega)+1)**(1/omega)
        
def fit_fuzhang(X,y):
    popt,pcov = curve_fit(fuzhang,X,y)
    omega = popt[0]
    if omega<= 1:
        print 'Warning: Parameter out of range 1 < omega < inf.'
    
    return omega

def zhang(X,w):
    # from Zhang et al. 2001
    p,pet = X
    return (1+w*(pet/p))/(1+w*(pet/p)+(pet/p)**-1)
    
def fit_zhang(X,y):
    popt,pcov = curve_fit(zhang,X,y)
    w = popt[0]
    if w<= 0 or w>1:
        print 'Warning: Parameter out of range 0 < w <= 1.'
        
    return w
    
def sharif(X):
    # from Sharif et al. 2007
    p,pet = X
    return (2*(pet/p))/(2*(pet/p)+1)
    
def zhou(X,k):
    # from zhou et al. 2015 GRL
    p,pet = X
    return (k*(pet/p))/(k*(pet/p)+1)

def fit_zhou(X,y):
    popt,pcov = curve_fit(zhou,X,y)
    k = popt[0]
    if k<= 0 or k>1:
        print 'Warning: Parameter out of range 0 < k <= 1.' 
        
    return k

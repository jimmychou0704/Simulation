
# coding: utf-8

# In[89]:

import numpy as np
from scipy import stats

class BSM(object):
    
    def __init__(self, S0, K, T, r, sigma):
        self.S0 = float(S0)           #stock price today
        self.K = K             #strike 
        self.T = T             #maturnity day, in years 
        self.r = r             #interest rate 
        self.sigma = sigma     #standard deviation
    
    def d1(self):
        return (np.log(self.S0/self.K)+(self.r+(self.sigma**2)/2)*(self.T))                /(self.sigma*np.sqrt(self.T))
    def d2(self):
        return (np.log(self.S0/self.K)+(self.r-(self.sigma**2)/2)*(self.T))                /(self.sigma*np.sqrt(self.T))
    
    def call_price(self):
        return self.S0*stats.norm.cdf(self.d1(),0,1) -               np.exp(-self.r*self.T)*self.K*stats.norm.cdf(self.d2(), 0,1)
        
    def vega(self):
        return self.S0*stats.norm.pdf(self.d1())*np.sqrt(self.T)


# In[91]:

T = 1
r = 0.01
sigma = 0.02
a = BSM(100, 105, T, r, sigma)
print a.vega()


# In[71]:

(np.log(100.0/105)+(0.01/365+0.5*0.02**2)*np.sqrt(20))/0.02


# In[76]:

(np.log(100.0/105)+(0.01/365 + 0.5*0.02**2)*20)/(0.02*np.sqrt(20))


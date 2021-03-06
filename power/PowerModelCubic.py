'''
Created on 16-Feb-2017

@author: itadmin
'''

from power.PowerModel import PowerModel
import math

class PowerModelCubic(PowerModel):

    maxPower = 0.0
    constant = 0.0
    staticPower = 0.0

    def __init__(self,maxPower,staticPowerPercent):
        self.maxPower=maxPower
        self.setStaticPower(self,staticPowerPercent * maxPower)
        self.setConstant(self.maxpower - self.getStaticPower()/math.pow(100,3))

    def getPower(self,utilization):
        if(utilization < 0 and utilization >1 ):
            try:
                raise Exception()
            except Exception:
                print "Utilization value must be between 0 and 1"
        if(utilization == 0):
            return 0
        
        return self.getStaticPower() + self.getConstant() * math.pow(utilization * 100, 3)

    def setStaticPower(self,staticPower):
        self.staticPower = staticPower

    def setmaxPower(self,maxPower):
        self.maxPower = maxPower

    def setConstant(self,constant):
        self.constant = constant

    def getStaticPower(self):
        return self.staticPower

    def getmaxPower(self):
        return self.maxPower

    def getConstant(self):    
        return self.getConstant

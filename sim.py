i = 100

def eq(va, vp, k):
   Ra = 0
   Rp = 0
   result = {"ra":0,"rp":0}
   result["ra"]=Ra
   result["rp"]=Rp
   return result


    
# platform best response
def platformbr(va, vp, k):
    result = {'p':0,'revenue':0, 'demand':0}

# app best response
def appbr(va, vp, k, p):
    result = {'rho':0,'revenue':0, 'demand':0}

    for rho in range(0,va):
        demand = appdemand(va, vp, k, p, rho)
        ra = rho*demand
        
        if ra>result["revenue"]:
            result["rho"]=rho
            result["revenue"]=ra
            result["demand"]=demand

    return result

#app demand
def appdemand(va, vp, k, p, rho):
    demand=0
    for i in range(0,getrange(va,vp,k,p,rho)):
        vai = va - k*i - (p+rho)
        vap = vp - i - p
        if (vai>vap) and (vai>0):
            demand = demand + 1
        #print i, vai, vap, demand
    return demand

# get range of max possible consumers
def getrange(va,vp,k,p,rho):
    psiP = max(0,vp-p)
    psiA = max(0,(va-p-rho)/k)
    return max(psiA,psiP)

#print appdemand(100,60,4,0,0)
appbr(100,50,4,0)
#appdemand()

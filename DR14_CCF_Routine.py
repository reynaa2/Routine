from astropy.io import fits
import apogee.tools.read as apread
import numpy as np

allStarDR14 = apread.allStar(rmcommissioning=True,main=False,ak=True,akvers='targ',adddist=False)
locationIDs = allStarDR14['LOCATION_ID']
apogeeIDs = allStarDR14['APOGEE_ID']
apogeeIDs = [s.decode('utf-8') for s in apogeeIDs] #remove bit from string

# R calculation
def calcR401(x, pos1=0, pos2=401, peakLoc=201):
    '''
    Calculates the value of R with the given array x
    Returns:  The value of R for whole CCF
    Assupmtion: the center peak lies in CCF lag space 201
    '''
    # if peakLoc is near the edges just skip it
    if (peakLoc <= 10) or (peakLoc >= 390):
        return np.nan
    Mirror = (x[peakLoc:pos2])[::-1]
    sigmaA = np.sqrt(1.0 / (2.0 * len(Mirror)) * np.sum((x[pos1:peakLoc] - Mirror)**2))
    r401 = np.max(x) / (np.sqrt(2.0) * sigmaA)
    return r401

def calcR151(x, pos1=125.5, pos2=276.5, peakLoc=201):

    if (peakLoc <= 10) or (peakLoc >= 390):
        return np.nan
    Mirror = (x[peakLoc:pos2])[::-1]
    sigmaA = np.sqrt(1.0 / (2.0 * len(Mirror)) * np.sum((x[pos1:peakLoc] - Mirror)**2))
    r151 = np.max(x) / (np.sqrt(2.0) * sigmaA)
    return r151

def calcR101(x, pos1=150.5, pos2=251.5, peakLoc=201):

    if (peakLoc <= 10) or (peakLoc >= 390):
        return np.nan
    Mirror = (x[peakLoc:pos2])[::-1]
    sigmaA = np.sqrt(1.0 / (2.0 * len(Mirror)) * np.sum((x[pos1:peakLoc] - Mirror)**2))
    r101 = np.max(x) / (np.sqrt(2.0) * sigmaA)
    return r101

def calcR51(x, pos1=175.5, pos2=226.5, peakLoc=201):

    if (peakLoc <= 10) or (peakLoc >= 390):
        return np.nan
    Mirror = (x[peakLoc:pos2])[::-1]
    sigmaA = np.sqrt(1.0 / (2.0 * len(Mirror)) * np.sum((x[pos1:peakLoc] - Mirror)**2))
    r51 = np.max(x) / (np.sqrt(2.0) * sigmaA)
    return r51

def FWHM(CCF):
    ccf_max = max(CCF) #y value
    ccf_min = min(CCF)# y value
    height = (ccf_max - ccf_min)
    half_pt = height/2.0
    nearest = (np.abs(CCF-height)).argmin()
    dist = nearest - ccf_min
    fwhm = 2.0 * dist
    return fwhm


def bisector(xccf,yccf,nvisits):
    height = max(yccf) - min(yccf)
    norm = height/len(yccf)
    nbounds = 5

    empty = arange(0,nbounds,1)    
    zones = min(yccf)+(height*empty/(nbounds-1))
    x_bisector = []
    y_bisector = []
    for i in range(nbounds):
        y_bisector.append((zone[i] + zone[i+1])/2.0)
        inbound = np.where(yccf >= zone[i] and ccf <= zone[i+1])

        if len(inbound) > 1:
            xmean = np.mean(xccf[inbound])
            x_bisector.append(xmean)
        else:
            x_bisector.append(-999)
   # bisector_pts = np.vstack([x_bisector,y_bisector])
    #return bisector_pts
    return x_bisector, y_bisector

def xrange(nvisits, x_bisector):
    xr = max(x_bisector) - min(x_bisector)
    return xr
    

# Loop for CCF output:
def ccf_loop(locationID,apogeeID,nvisits,r401,r151,r101,r51,mxr,fwhm,CCF):
    
    visit = np.arange(0,nvisits,1)
    cols = ['Location_ID','Apogee_ID','Visit#','R(401)','R(151)','R(101)','R(51)','MaxXRange','FWHM']
    for i in range(401):
        x = 'CCF_'+str(i)
        cols.append(x)
    df = pd.DataFrame(columns=cols)
    for j in range(nvisits):
        data = [locationID[j],apogeeID[j],visit[j],r401[j],r151[j],r101[j],r51[j],mxr[j],fwhm[j]]

        for k in range(len(CCF)):
            data.append(CCF[k])
            
    data = df.loc[len(df)+1]
    return data


# Main routine to call in data stored in each CCF:
x = np.arange(0,401,1)
for i in range(len(apogeeIDs)):
        apogeeID = apogeeIDs[i]
        locationID = locationIDs[i]
        path = '/Volumes/coveydata/APOGEE_Spectra/APOGEE2_DR14/dr14/apogee/spectro/redux/r8/stars/apo25m/'+str(locationID)+'/'+'apStar-r8-'+str(apogeeID)+'.fits'
        if len(path) == 34: #If Statement designed to read in apStarC files
            if locationID != 1:
                CData = fits.open(path)
                Cstpt = Data[9]
                CCCFs = Cstpt.data[0][28]
                CHDU0 = fits.getheader(path,0)
                Cnvisits = CHDU0['NVISITS']

                if Cnvisits >= 3:
                    for visit in range(0,Cnvisits):
                        snr = CHDU0['SNVIS'+str(visit+1)]
                        if Cnvisits !=1:
                            CCCF = CCCFs[visit+2]
                            CCF = CCCFs[visit+2]
                            r401 = calcR401(CCCF)
                            r151 = calcR151(CCCF)
                            r101 = calcR101(CCCF)
                            r51 = calcR51(CCCF)
                            fwhm = FWHM(CCCF)
                            bs_pts = bisector(x,CCCF,nvisits)
                            mxr = x_range(nvisits, bs_pts[0])
                        else:
                            CCF = CCCFs
        else:
            if locationID !=1:
                Data = fits.open(path)
                stpt = Data[9]
                CCFs = stpt.data[0][28]
                HDU0 = fits.getheader(path,0)
                nvisits = HDU0['NVISITS']

                if nvisits >= 3:
                    for visit in range(0,nvisits):
                        SNR = HDU0['SNRVIS'+str(visit+1)]
                        if nvisits!=1:
                            CCF = CCFs[visit+2]
                            r401 = calcR401(CCF)
                            r151 = calcR151(CCF)
                            r101 = calcR101(CCF)
                            r51 = calcR51(CCF)
                            fwhm = FWHM(CCF)
                            bs_pts = bisector(x,CCF,nvisits)
                            mxr = x_range(nvisits, bs_pts[0])
                            
                        else:
                            CCF = CCFs
                            
                        ccf_loop(locationID,apogeeID,nvisit,r401,r151,r101,r51,mxr,fwhm,CCF) #Send information to loop to get a csv file!

                
        
                           

          
            
    
    

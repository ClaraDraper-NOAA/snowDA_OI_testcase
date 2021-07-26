mport numpy as np 
from netCDF4 import Dataset
import matplotlib.pyplot as plt 

tile = '3' 

fname = 'SNOANLOI.tile'+tile+'.nc'

ncid = Dataset(fname) 

# station variables
stn_lat = ncid['latitude@MetaData'][:]
stn_lon = ncid['longitude@MetaData'][:] 
stn_lon[stn_lon<0] = stn_lon[stn_lon<0]+360 

stn_ii = ncid['IDIM_index@MetaData'][:] 
stn_jj = ncid['JDIM_index@MetaData'][:] 

stn_obs = ncid['snwdph@ObsValue'][:] 
stn_fcs = ncid['snwdph@hofx'][:] 
stn_anl = ncid['snwdph@anal'][:] 

if (1==1): 
    f = np.where(stn_jj > -1)[:]  # screen out obs not used

    stn_lat = stn_lat[f] 
    stn_lon = stn_lon[f] 
    stn_ii = stn_ii[f]-1 # subtract 1 to convert to python indexing
    stn_jj = stn_jj[f]-1 # subtract 1 to convert to python indexing
    stn_obs = stn_obs[f] 
    stn_fcs = stn_fcs[f] 
    stn_anl = stn_anl[f] 

#plt.plot(grd_lons[stn_ii,stn_jj], grd_lats[stn_ii,stn_jj],'.')

# grid variables 
grd_lon = ncid['Lon'][0,:,:] 
grd_lat = ncid['Lat'][0,:,:]  

grd_fcs = ncid['SND_Forecast'][0,:,:]  
grd_anl = ncid['SND_Analysis'][0,:,:]  
grd_anl[grd_anl<-9999.] = np.nan 
grd_obs = ncid['imsSND'][0,:,:] 
grd_obs[grd_obs<-9999.] = np.nan 

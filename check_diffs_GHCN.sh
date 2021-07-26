#!/bin/ksh 

echo 'any differences will be listed below:' 
for t in 1 2 3 4 5 6 
do 
cmp SNOANLOI_GHCN.tile${t}.nc output/SNOANLOI_GHCN.tile${t}.nc
done 

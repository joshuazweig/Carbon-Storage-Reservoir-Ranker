from data_parcer import *
from score import *
import numpy
#import matplotlib.pyplot as plt
#import skfuzzy as fuzz

res = get_res_dic()
nps = get_nps_dic()
wtr = get_water_dic()
flt = get_fault_dic()

dta = []

def normalize(lst):
    mx = max(lst)
    mn = min(lst)
    return [(x-mn)/(mx-mn) for x in lst]

print("Vectorizing data (this make take a whle)...")
for rec in res:
  nps_scores = []
  wtr_scores = []
  flt_scores = []
  for np in nps:
    nps_scores.append(score_res_nat_park(rec, np))
  for wt in wtr:
    wtr_scores.append(score_res_water(rec, wt))
  for fl in flt:
    flt_scores.append(score_res_fault(rec, fl))

  nps_scores = normalize(nps_scores)
  wtr_scores = normalize(wtr_scores)
  flt_scores = normalize(flt_scores)
  rec['nps'] = numpy.mean(nps_scores)
  rec['wtr'] = numpy.mean(wtr_scores)
  rec['flt'] = numpy.mean(flt_scores)
  del rec['Basin Name']
  del rec['Resource Name'] #You'll need this at some point
  del rec['Long']
  del rec['Lat']

  temp = []
  for value in rec.values():
    temp.append(value)
  dta.append(temp.copy())

print(dta[0])
#Yay! Everything is vectorized! That was hardish
#Not as hard as I tohught it would be 

#Let's cluster some shit
print("Clustering data (this might also take a while...")
result = skfuzzy.cmeans(dta, 3, error=0.005, maxiter=1000, init=None)
from data_parcer import *
from score import *
import numpy
import matplotlib.pyplot as plt
import skfuzzy as fuzz



res = get_res_dic()
nps = get_nps_dic()
wtr = get_water_dic()
flt = get_fault_dic()

def normalize(lst):
    mx = max(lst)
    mn = min(lst)
    return [(x-mn)/(mx-mn) for x in lst]

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


#Yay! Everything is vectorized! That was hardish
#Not as hard as I tohught it would be 


#Let's cluster some shit!
fig1, axes1 = plt.subplots(3, 3, figsize=(8, 8))

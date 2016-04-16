#Normlaize all scores to 0-100
from math import sqrt

def score_res_nat_park(res_dic, nat_park_dic):
  #compute score

  r_lat = float(res_dic['Lat'])
  r_long = float(res_dic['Long'])
  n_lat = float(nat_park_dic['Lat'])
  n_long = float(nat_park_dic['Long'])
  dist = sqrt(abs(pow((r_long - n_long), 2) + pow((r_lat - n_long), 2)))
  
  return float(1) / float(dist * dist)

def score_res_water(res_dic, water_dic):
  #copmute score
  r_lat = float(res_dic['Lat'])
  r_long = float(res_dic['Long'])
  n_lat = float(water_dic['Lat'])
  n_long = float(water_dic['Long']) 
  water_importance = water_dic['Score']
  dist = sqrt(abs(pow((r_long - n_long), 2) + pow((r_lat - n_long), 2)))

  return float(water_importance) / float(dist * dist) #reflects inverse relationship between distance and source

def score_res_fault(res_dic, fault_dic):
  #compute score
  try: #Actually figure out what  '1.#QNAN000000e+000' means later
    r_lat = float(res_dic['Lat'])
    r_long = float(res_dic['Long'])
    n_lat = float(fault_dic['Lat'])
    n_long = float(fault_dic['Long']) 
    dist = sqrt(abs(pow((r_long - n_long), 2) + pow((r_lat - n_long), 2)))
    fault_risk_score = fault_dic['Score']

    return float(fault_risk_score) / float(dist * dist)
  except ValueError:
    return -1

#def score_population(res_dic, population_dic):
  #compute score




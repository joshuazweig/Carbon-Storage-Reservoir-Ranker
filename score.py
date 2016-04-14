#Normlaize all scores to 0-100

def score_res_nat_park(res_dic, nat_park_dic):
  #compute score

def score_res_water(res_dic, water_dic):
  #copmute score
  dist = sqrt(pow((res_dic['Long'] - water_dic['Long']), 2) + pow((res_dic['Lat'] - water_dic['Lat']), 2))
  water_importance = water_dic['Score']

  return float(water_importance) / float(dist * dist) #reflects inverse relationship between distance and source

def score_res_fault(res_dic, fault_dic):
  #compute score
  # dist = sqrt(pow((res_dic['Long'] - fault_dic['Long']), 2) + pow((res_dic['Lat'] - fault_dic['Lat']), 2))
  # fault_risk_score = fault_dic['Score']

def score_population(res_dic, population_dic):
  #compute score
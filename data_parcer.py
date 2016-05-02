import shapefile
#import arcpy 
from score import *

#####################################Load Reservoir Data###################################################
#See dic for fields being saved, this dictioantires will later be appended with the rest of the 
#elements of the data vector scores (prelimenaerlily loaded above, still need ot be computed))
def get_res_dic():
  #print(datetime.datetime.now().time())
  print("Reading reservoir data...")
  res = shapefile.Reader("./Data/Saline/NATCARB_Saline_10K_v1502")
  res_records = res.records()
  #res_shapes = res.shapeRecords()
  res_coords = []
  i = 0
  for idx, rec in enumerate(res_records):
    if(idx%10 == 0):
      dic = {
      'Resource Name' : rec[3],
      'Basin Name' : rec[4],
      'Avg Volume/Capacity Estimate' : rec[7],
      'Depth' : rec[9],
      'Thickness' : rec[10],
      'Salinity' : rec[11], 
      'Preassure' : rec[12],
      'Temperature' : rec[13],
      'Porosity' : rec[14],
      'Permeability' : rec[15],
      'Area' : rec[22],
      'Long' : rec[23],
      'Lat' : rec[24]
      #'Shape' : res_shapes[i]
      }
      res_coords.append(dic.copy())
      i += 1

  return res_coords


######################################End Load Reservoir Data##############################################

###############################Load National Park Data#####################################################
#Fill a list of dictionaries with Long, Lat of Park Center, Shape file of Pakr
#Assume parks are equally important (score will only be a function of distance and no particular char of park)
def get_nps_dic():
  #print(datetime.datetime.now().time())
  print("Reading National Park data...")
  nps = shapefile.Reader("./Data/Nat Parks/nps_boundary")
  nps_records = nps.records()
  #nps_shapes = nps.shapeRecords()
  nps_coords = []
  i = 0
  for rec in nps_records:
    dic = {'Long' : rec[len(nps_records[0]) - 2], 
    'Lat' : rec[len(nps_records[0]) - 1]
    #'Shape' : nps_shapes[i]
    }
    nps_coords.append(dic.copy())
    i += 1

  return nps_coords

######################################End National Park Data###############################################

###################################Load Water Data#########################################################
#Fill water list with long, lat, and score as given by the US forest service

def get_water_dic():
  #print(datetime.datetime.now().time())
  print("Reading water source data...")
  water = shapefile.Reader("./Data/Water/ForestsToFaucets")
  water_records = water.records()
 # water_shapes = water.shapeRecords()
  water_coords = []
  for rec in water_records:
    dic = {
    'Long' : rec[2],
    'Lat' : rec[21],
    'Score' : rec[22] }
    water_coords.append(dic.copy())

  return water_coords
####################################End Load Water Data###################################################

#######################################Load Fault Data###################################################
#Fill a list of dictionaries with Long, Lat of Fault Center, Shape file of fault and Slip Rate Score
def get_fault_dic():
  #print(datetime.datetime.now().time())
  print("Reading fault line data...")
  fault = shapefile.Reader("./Data/sectionsALL")
  fault_records = fault.records()
  #fault_shapes = fault.shapeRecords()
  fault_coords = [] #long, lat (of center), shape
  i = 0
  min_slip_rate = 100000
  max_slip_rate = -1000000
  for rec in fault_records:
    if (not isinstance(rec[6], float)):
      if(rec[6] == '<0.2'):
        rec[6] = .1
      elif(rec[6] == '0.2-1'):
        rec[6] = .6
      elif(rec[6] == '1-5'):
        rec[6] = 3.0
      elif(rec[6] == '>5'):
        rec[6] = 5.1
      else:
        rec[6] = 2.6

    if(float(rec[6]) > max_slip_rate):
      max_slip_rate = rec[6]
    if(float(rec[6]) < min_slip_rate):
      min_slip_rate = rec[6]

  for rec in fault_records:
    dic = {'Long' : rec[len(fault_records[0]) - 2], 
    'Lat' : rec[len(fault_records[0]) - 1], 
   # 'Shape' : fault_shapes[i], 
    'Score' : ((float(rec[6]) - min_slip_rate) / (max_slip_rate - min_slip_rate))}
    fault_coords.append(dic.copy())
    i += 1

  return fault_coords

#################################End Load Fault Data########################################################

#population
#.gdb

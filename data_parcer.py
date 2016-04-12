import shapefile
#import arcpy 

###############################Load National Park Data#####################################################
#Fill a list of dictionaries with Long, Lat of Park Center, Shape file of Pakr
#Assume parks are equally important (score will only be a function of distance and no particular char of park)
nps = shapefile.Reader("./Data/Nat Parks/nps_boundary")
nps_records = nps.records()
nps_shapes = nps.shapeRecords()
print(nps.fields)
nps_coords = []
i = 0
for rec in nps_records:
  dic = {'Long' : rec[len(nps_records[0]) - 2], 'Lat' : rec[len(nps_records[0]) - 1], 'Shape' : nps_shapes[i]}
  nps_coords.append(dic.copy())
  i += 1

for a in nps_coords:
  print(a)
# water = shapefile.Reader("./Data/Water/ForestsToFaucets")
# water_records = water.records()


######################################End National Park Data###############################################

#######################################Load Fault Data###################################################
#Fill a list of dictionaries with Long, Lat of Fault Center, Shape file of fault and Slip Rate Score
fault = shapefile.Reader("./Data/sectionsALL")
fault_records = fault.records()
fault_shapes = fault.shapeRecords()
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
  dic = {'Long' : rec[len(fault_records[0]) - 2], 'Lat' : rec[len(fault_records[0]) - 1], 
    'Shape' : fault_shapes[i], 'Score' : ((float(rec[6]) - min_slip_rate) / (max_slip_rate - min_slip_rate))}
  fault_coords.append(dic.copy())
  i += 1

#################################End Load Fault Data########################################################

#population
#.gdb

#res

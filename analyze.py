from data_parcer import *
from score import *
import numpy
#import matplotlib.pyplot as plt
import skfuzzy as fuzz
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from visual import *
import pandas
from pandas.tools.plotting import parallel_coordinates as pc
from matplotlib.collections import LineCollection
from sklearn import manifold
from sklearn.metrics import euclidean_distances
from sklearn.decomposition import PCA
from matplotlib import colors
from mpl_toolkits.mplot3d import Axes3D
import sqlite3
from tempfile import TemporaryFile

# res = get_res_dic()
# nps = get_nps_dic()
# wtr = get_water_dic()
# flt = get_fault_dic()

# dta = []

# def normalize(lst):
#     mx = max(lst)
#     mn = min(lst)
#     return [(x-mn)/(mx-mn) for x in lst]

# def reject_outliers(data, m=2):
#     return data[abs(data - np.mean(data)) < m * np.std(data)]

# #print(datetime.datetime.now().time())
# print("Vectorizing data (this make take a whle)...")
# j = 0
# for rec in res:
#   print("Vectorizing well ", j)
#   j = j+1
#   nps_scores = []
#   wtr_scores = []
#   flt_scores = []
#   for np in nps:
#     nps_scores.append(score_res_nat_park(rec, np))
#   for wt in wtr:
#     wtr_scores.append(score_res_water(rec, wt))
#   for fl in flt:
#     flt_scores.append(score_res_fault(rec, fl))

#   nps_scores = normalize(nps_scores)
#   wtr_scores = normalize(wtr_scores)
#   flt_scores = normalize(flt_scores)
#   rec['nps'] = numpy.mean(nps_scores)
#   rec['wtr'] = numpy.mean(wtr_scores)
#   rec['flt'] = numpy.mean(flt_scores)
#   del rec['Basin Name']
#   del rec['Resource Name'] #You'll need this at some point
#   del rec['Long']
#   del rec['Lat']

#   temp = []
#   for value in rec.values():
#     temp.append(value)
#   dta.append(temp.copy())

#numpy.save('dump', dta)

dta = numpy.load('pca.npy')
#print(dta[0])
#Yay! Everything is vectorized! That was hardish
#Not as hard as I tohught it would be 

#Let's cluster some shit
#print(datetime.datetime.now().time())
print("Clustering data")
#xpts = np.empty(1)
#ypts = np.empty(1)
labels = numpy.empty(1)
fig1, axes1 = plt.subplots(3, 3)
#alldata = numpy.vstack((xpts, ypts))
fpcs = []

for i in range(6, 10):

  print("\n \n ", i, " clusters \n \n")
  #print(dta[0])
  dta = numpy.array(dta, dtype = float)
  print(dta.shape)
  # dta = numpy.transpose(dta)
  # centeres, fuzzy_partiioned, u0, distances, jm, p, fpc = fuzz.cmeans(dta, i, 2, error=0.002, maxiter=1000, init=None)
  # print("Center: ", centeres)
  # print("Fuzzy Partitioned Matrix: ", fuzzy_partiioned)
  # print("u0: ", u0)
  # print("Eudlidian Distance Matrix: ", distances)
  # print("jm: ", jm)
  # print("p: ", p)

  # print("fpc: ", fpc)

  # Store fpc values for later
  # fpcs.append(fpc)

#  fuzzy_partiioned = numpy.transpose(fuzzy_partiioned)

  # print(fuzzy_partiioned.shape)
  # parallel_coordinates(fuzzy_partiioned).show()
  #pc(fuzzy_partiioned, [0]).show()
  # pca = PCA(3)
  # pca.fit_transform(dta)
  x = dta[:,0]
  y = dta[:,1]
  z = dta[:,2]
  fig = plt.figure()
  ax = fig.add_subplot(111, projection='3d')
  ax.scatter(x, y, z, zdir='z', c= 'red')
  #ax.scatter(dta[0], dta[1], dta[2], zdir='z', c= 'red')

  # pcb = PCA(3)
  # pcb.fit_transform(centeres)
  # x1 = centeres[:,0]
  # y1 = centeres[:,1]
  # z1 = centeres[:,2]
  # ax1 = fig.add_subplot(111, projection='3d')
  # ax.scatter(x1, y1, z1, zdir='z', c= 'green')
  #ax.scatter(centeres[0], centeres[1], centeres[2], zdir='z', c= 'green')

  # ax1 = fig.add_subplot(111)
  # pca = PCA(3)
  # pca.fit_transform(dta)
  # x = dta[:,0]
  # y = dta[:,1]
  # ax1.plot(dta)

  #pca.fit_transform(centeres)
  #cx = centeres[:,0]
  #cy = centeres[:,1]

  #ax1.scatter(cx, cy, , 'r')

  plt.show()







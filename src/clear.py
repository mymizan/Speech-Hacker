import os
from os.path import join, getsize

chuncks = './chunks/'
filters = './filtered/'

try :
  os.rmdir(chuncks)
  os.rmdir(filters)
  os.remove('list.txt')
  os.remove('myDict.py')
except(Exception):
  print('')

try:
  os.mkdir('chunks')
  os.mkdir('filtered')
except(Exception):
  print('')






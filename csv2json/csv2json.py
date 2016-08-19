#!/usr/bin/python

import sys
import csv
import json
from ast import literal_eval


class Csvtojsonconverter : 

  def __init__(self,path) :
    
    self.path = str(path)
#    print "Path is " + self.path
    self.jsonfile = open('sample_libmodule.json', 'w')   
    self.jsonfile.write("{")
    self.data_dict = {} 

  def write_json(self,row_element) :
    
    self.row_element = row_element
    self.data_dict = {}
    data = self.create_data_dictionary(self.row_element)
    self.out = json.dumps(data, indent=4, separators=(', ', ': '))
    self.jsonfile.write(self.out)

  def read_csv(self,path) :
  
    with open(self.path, "rb") as self.inputfile:
      self.row = list(csv.reader(self.inputfile))
      self.header = self.row.pop(0) # ignore header
#      print self.header
      self.length_colns = len(self.header)
      self.length_row = len(self.row)
      for i in range(self.length_row) :
        if not self.row[i] :
          continue
        self.write_json(self.row[i])
      self.jsonfile.write("}")

  def create_data_dictionary(self,row_element) :

    for i in range(len(self.header)) :
      try:
            # Interpret the string as a Python literal
        value = literal_eval(self.row_element[i])
        self.row_element[i] = value
      except Exception:
            # If that doesn't work, assume it's an unquoted string
        pass
      self.data_dict.update({self.header[i] : self.row_element[i]})
    
    return self.data_dict


csv_Obj = Csvtojsonconverter(sys.argv[1])

csv_Obj.read_csv(csv_Obj.path)

  

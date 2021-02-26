""" Combine identically structured datafiles and creates a new master file for analysis """
import os

""" Files should have the same root name and vary by a number in the index range (ATPmatches2016.csv) """
name = 'ATPmatches'
ext = '.csv' # This could be varied and an 'ext_out' could be spcified to change the output file. 
start_index = 1990
end_index = 2021

""" Output file will be root name only (ATPmatches.csv) """
file_out = open(str(name) + str(ext),'w')

# Loop from the end of the index
for line in open(str(name) + str(end_index) + str(ext)):
    file_out.write(line)

# Gather remaining data    
for num in range(start_index,end_index):
    f = open(name + str(num) + str(ext))
    
    # Skip headers
    f.__next__() 
    
    for line in f:
         file_out.write(line)
    f.close()

""" Save and close the masterfile in the folder """
file_out.close()

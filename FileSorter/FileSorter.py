""" Organise Files by Filetype """
import os, shutil

""" Set for user input, alternatively integrate with your project code """
path = input('Enter path:')
files = os.listir(path)

for i in files:
  """ Split filename to get extension """
  name, ext = os.path.splitext(i)
  ext = ext[1:]
  
  """ if folder exists add, else create and add """
  if os.path.exists(path + '/' + ext):
    shutil.move(path + '/' + i, path + '/' + ext + '/' + i)
  else:
    os.makedir(path + '/' + ext)
    shutil.move(path + '/' + i, path + '/' + ext + '/' + i)

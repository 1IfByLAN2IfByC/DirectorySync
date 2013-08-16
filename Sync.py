
#  python sync tool

import os as os
import datetime

class sync:

  def __init__(self, source, destination ):
    self.src = source
    self.dest = destination


  def checkRoot(self, src , dest):
# first check to see if the file exists at the destination
    try:
      with open(dest): pass

    except IOError:
      print('''the dest file doesn't exist''')
      os.mkdir(dest)


  def syncDir(self, src, dest):

  def main(self, src, dest):
    self.checkRoot(src, dest)



INPUT =
OUTPUT =
sy = sync(INPUT,OUTPUT)

sy.main(sy.src, sy.dest)

print(tSrc, '\n', tDest)

if tSrc > tDest:
  print('the source is newer')

else:
  print('the destination is newer')



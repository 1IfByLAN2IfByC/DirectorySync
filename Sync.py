
#  python sync tool

import os as os
import datetime
import time
import shutil


class sync:

  def __init__(self, source, destination ):
    self.src = source
    self.dest = destination


  def checkRoot(self, src , dest):
    if not os.path.exists(dest):
        os.mkdir(dest)

  def syncDir(self, src, dest):
      srcList = os.listdir(src)
      srcTime = [None]*len(srcList)
      destList = os.listdir(src)
      destTime = [None]*len(srcList)
      
      for i in range(len(srcList)):
          srcList[i] = src + srcList[i]
          destList[i] = dest + destList[i]
          srcTime[i] = os.path.getmtime(srcList[i])
          print(srcList[i])
          
          # IF THE DESTINATION PATH EXISTS 
          if os.path.exists(destList[i]) == True:
              destTime[i] = os.path.getmtime(destList[i])
              # IF THE DESTINATION IS OLDER
              if destTime[i] < srcTime[i]:
                  try: # IF DESTINATION IS A DIRECTORY USE COPYTREE
                    shutil.rmtree(destList[i])
                    shutil.copytree(srcList[i], destList[i])
              
                  except OSError: # IF NOT, USE COPY2
                    shutil.copy2(srcList[i], destList[i]) 
              else:
                  pass
            
          else:
              try:
                  shutil.copytree(srcList[i], destList[i])
              
              except OSError:
                  shutil.copy2(srcList[i], destList[i])             
     
      return srcList, srcTime, destList, destTime

          

  def main(self, src, dest):
    self.checkRoot(src, dest)
    srcList, srcTime, destList, destTime = self.syncDir(src,dest)
    now = time.mktime(datetime.datetime.now().timetuple())
    
    return srcList, srcTime, destList, destTime

#sy = sync('c:\users\Arl_guest\desktop','c:\users\Arl_guest\desktop\TEST')
sy = sync('/home/michael/Dropbox/', '/home/michael/TEST/')

srcList, srcTime, destList, destTime = sy.main(sy.src, sy.dest)
print('Sync Finished')




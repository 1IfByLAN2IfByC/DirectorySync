
#program that backs up the specified directories to an external source
import shutil, errno, datetime, os, tarfile
def main():
        #declare sources 
        C = '/C/Shares/'

        #declare destination root
        Save_root = r'/External_HDD/Backups/Server/'

        #declare how long (in days) you want to keep daily backups
        dailyDuration = 7

        #declare what on which day you want to keep those past the above
        keepDay = 'Sat'     #Capitalize the first letter

        #find out what day it is
        today = str(datetime.date.today())

        #make a new folder to house all the backups
        save = Save_root+today+'_Backup'
        os.mkdir(save)

        Backup(C, save, 'Server')

        # create tarball of the newly created folder
        tar = tarfile.open(save+'.tar.bz2', 'w:bz2')
        tar.add(save)
        tar.close()

        # delete the non-compressed file 
        os.rmtree(save)

        ## remove any old backups
        clean_up(today, Save_root, dailyDuration, keepDay)

def Backup(source, destination_root, name):
        save =  destination_root +r'/'+ name
        shutil.copytree(source, save)

def clean_up(today, directory, dailyDuration, keepDay):
        os.chdir(directory)
        age = datetime.datetime.now() - datetime.timedelta(days = dailyDuration)

        for somefile in os.listdir('.'):
                 file_age = os.path.getmtime(somefile)
                 file_age = datetime.datetime.fromtimestamp(file_age)
                 file_day = file_age.strftime("%a")

                 #check if the file is older than specified date 
                 #check if the file was created on the keep day

                 if file_age < age and file_day != keepDay:
                    if os.path.isfile(somefile) == True:
                        os.remove(somefile)

                    else:
                        os.rmdir(somefile)

                 else:
                    pass

main()



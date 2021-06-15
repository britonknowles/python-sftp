import functools
import paramiko 

class AllowAnythingPolicy(paramiko.MissingHostKeyPolicy):
    def missing_host_key(self, client, hostname, key):
        return
      
Download_path = 'C:\your\download\spot'

address = 'ftp://your.site'
username = 'user'
password = 'pass'

client = paramiko.SSHClient()
client.set_missing_host_key_policy(AllowAnythingPolicy())
client.connect(address, username= username, password=password)

# Load list of previously checked files into an array
fileObj = open("tracker.txt", "r")
checked_files = fileObj.read().splitlines()
fileObj.close()

# Begin SFTP Session
sftp = client.open_sftp()
# Specify SFTP home directory
sftp.chdir('/')
for filename in sftp.listdir(path='/'):
    tracker = open("tracker.txt","a")
    # Check for partial match in file name
    if "thing-to-search-for" in filename:
        # Check array to make sure file has not already been downloaded
        if filename not in checked_files:
        # Download file
            sftp.get(filename, Download_path+'/\/'+filename)
        # Add current file to list of checked files
            tracker.write(filename+"\n")
            print(filename)
    tracker.close()
                       

      
client.close() 

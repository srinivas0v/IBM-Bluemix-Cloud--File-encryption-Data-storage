# IBM-Bluemix-Cloud--File-encryption-Data-storage
python flask app deployed on IBM Bluemix cloud
The objective was security of files in cloud data storage 'Dropbox' like service. The user can upload a file which will be encrypted using GNU Privacy Guard and uploaded to the object store. The encrypted file can be downloaded & decrypted locally. The objects can be listed. Built using Cloud Foundry, Python

Code.py 
running locally, will 
    - create a simple menu to: list local files 
    - menu has exit option
    - checksum (add all bytes together) or XOR all bytes in the file
    - upload file and checksum to Bluemix 
    - menu should list cloud files
    - be able to get file from cloud to local, then compare checksum

Created two cloud based folders, one for new version of files the other folder  for the previous version (backup)
    - allow a user to list the contents of a remote folder 
    - allow a user to remove all (cloud) files that are greater in size than a user specified size
      (for example, all cloud storage files greater than 1000 bytes)


Code1.py 
running locally, should 
    - create a simple menu to: list local files 
    - allow a user to input an encryption key (4 digits)
    - allow a user to select which text files to encrypt
    - menu has a option to decrypt local files using the key
    - menu has exit option
    
    Using local menu     
    - upload files to cloud storage and delete that (original) file locally (only encrypted files stored locally)
    - menu should list cloud files
    - be able to get file from cloud to local
    
 Created two cloud based folders, one for text one for all other file types 
    - allow a user to list the contents of a remote folder 
    - allow a user to remove all (cloud) files that are greater in size than a user specified size
      (for example, all cloud storage files greater than 1000 bytes)
      
 Replaced cloud folders with SQL database, place "uploaded" files into that DB.
    - Allow a user to see which files are in that in that DB.
    - Allow user to delete or replace files.

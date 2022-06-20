# Credentials Folder

## The purpose of this folder is to store all credentials needed to log into your server and databases. This is important for many reasons. But the two most important reasons is
    1. Grading , servers and databases will be logged into to check code and functionality of application. Not changes will be unless directed and coordinated with the team.
    2. Help. If a class TA or class CTO needs to help a team with an issue, this folder will help facilitate this giving the TA or CTO all needed info AND instructions for logging into your team's server. 


# Below is a list of items required. Missing items will causes points to be deducted from multiple milestone submissions.

1. Server URL or IP
    34.83.255.32:8000
2. SSH username
    andy
3. SSH password or key.
    <br> If a ssh key is used please upload the key to the credentials folder.
    Public and Private Key Files are used, please refer to credentials folder.
    Password for “sudo ssh”: CSC648!@#Team03
4. Database URL or IP and port used.
    <br><strong> NOTE THIS DOES NOT MEAN YOUR DATABASE NEEDS A PUBLIC FACING PORT.</strong> But knowing the IP and port number will help with SSH tunneling into the database. The default port is more than sufficient for this class.
    Host: 34.83.255.32 Port: 3306
5. Database username
    playdateadmin
6. Database password
    Pl@yd@te03
7. Database name (basically the name that contains all your tables)
    playdate
8. Instructions on how to use the above information.
    You can put the key files in the folder: ~/.ssh of your local computer.
    When connect to the server, use command:
    $ sudo ssh -i ~/.ssh/team03-testuser andy@34.83.255.32
    password for this sudo ssh is: CSC648!@#Team03
    (If you have created your own key files with a password before, you shall first enter your own password, then enter ours.)
    
    
# Most important things to Remember
## These values need to kept update to date throughout the semester. <br>
## <strong>Failure to do so will result it points be deducted from milestone submissions.</strong><br>
## You may store the most of the above in this README.md file. DO NOT Store the SSH key or any keys in this README.md file.

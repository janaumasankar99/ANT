'''
Created on Mar 22, 2018

@author: ju2106
'''
#import Final_json as _jsonModule
import paramiko,socket,time,json,re
from paramiko_expect import SSHClientInteraction
#myData=json.load(open('C:\\Users\\ju2106\\Desktop\\5G\\sample.json','r'))
class cliModule:
    def __init__(self):
        pass
    def loginSession(self,hostName,userName,password,port,prompt):
        """
        Description  : Login to a SSH session 
        Parameters:
            hostName : Hostname of SSH session
            userName : Username of SSH session
            password : Password of SSH session
            port     : Port number of SSH session 
            prompt   : Name of the Prompt 
        Return Value:
            ssh : Handle name of the session in the case of successful login
            False: Returns False in the case of any failures in logging.
        """
        tries = 3
        flag=True
        count=0
        for i in range(tries+1):
            try:
                ssh=paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(hostName,port,userName,password)
                shell = ssh.invoke_shell()
                resp = shell.recv(9999)
                print(resp)
                #time.sleep(10)
                while(count<5):
                    m = re.search(prompt,str(resp))
                    if m:
                        #print("count is",count)
                        print("prompt is identified") 
                        print(str(resp))
                        break
                    else:
                        count=count+1
                        print("count is",count)
                        flag=False
                        
                    
                  
                
                        
                    #resp = shell.recv(9999)
                
                print ("SSH session opened for "+hostName)
                return ssh
            except(paramiko.BadHostKeyException, paramiko.AuthenticationException, paramiko.SSHException, socket.error) as e:
                if (i<tries):
                        time.sleep(1)
                        print ("login to %s failed..... retrying..... retry = %d"%(hostName, i+1))
                        continue
                else:
                    print("Unable to login "+hostName+", Error: ",e)
                    return False
                
    

    def executeCLI(self,sshHandle,command):
        """
        Description:   Execute any command on SSH session.
        Parameters:
            sshHandle : sshHandle which is opened to execute a command
        Return Value:
            commandResponse : The output of the command response for any command.
            False: Returns False in the case of any failures in executing a command.
        """
        try:
            stdin, stdout, stderr = sshHandle.exec_command(command)
            errout=stderr.read()
            if errout:
                print ("Failed to execute command")
                return False
            else:
                commandResponse=stdout.read()
            return commandResponse
        except(Exception) as e:
            print ("Unable to execute command")
            return False
            
    def closeSession(self,sshHandle):
        """
        Description:   Closes a SSH session
        Parameters:
            sshHandle : sshHandle which is opened.
        Return Value:
            True : Returns True if session is closed successfully.
            False: Returns False if session is not closed successfully.
        """
        try:
            sshHandle.close()
            print ("SSH session is closed")
            return True
        except(Exception) as e:
            print("Unable to close session, Error: ",e) 
            return False


     
cls=cliModule()
ssh=cls.loginSession('107.112.136.205', 'm02129', 'Att@2018', 22,'debasish')
print ('The retun value of login session is %s'%(ssh))

if ssh!=False:
    print (cls.executeCLI(ssh, 'show snmp server '))
    cls.closeSession(ssh)
else:
    print ("Error in logging to SSH host")

         
        
        
        
        
        
        
        
        
        
        
        
        
        
        
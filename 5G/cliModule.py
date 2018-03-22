'''
Created on Mar 22, 2018

@author: ju2106
'''
import Final_json as jsonModule
import paramiko,socket,time,json
myData=json.load(open('C:\\Users\\ju2106\\Desktop\\5G\\sample.json','r'))
class cliModule:
    def __init__(self,myData):
        self.jsonValue=jsonModule.JSONUtil(myData)
    def loginSession(self,host,userName,password,port):
        tries = 3
        for i in range(tries):
            try:
                ssh=paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(host,port,userName,password)
                print ("SSH session opened for "+host)
                return ssh
            except(paramiko.BadHostKeyException, paramiko.AuthenticationException, paramiko.SSHException, socket.error) as e:
                if (i<=tries):
                        time.sleep(1)
                        #print "login to %s failed..... retrying..... retry = %d"%(host, i+1))
                        print("login to %s failed..... retrying..... retry = %d" %host)
                        continue
                else:
                    print("Unable to login "+host+", Error: ",e)
                    return False

    def executeCommand(self):
        #jsonValue=jsonModule.JSONUtil(myData)
        len=self.jsonValue['recLen']
        for lenIndex in range(0,len):
            rule=self.jsonValue[lenIndex,'verifications','rule']
            command=self.jsonValue[lenIndex,'command']
            if(rule=="true"):
                print ("command is %s"%(command))
                break
            print (rule)
            
cls=cliModule(myData)
cls.executeCommand()
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
'''
Created on Mar 27, 2018

@author: ju2106
'''
import paramiko,socket,time,json,re
import Final_json as jsonModule
import Final_json
import cliModule as cli
myData=json.load(open('C:\\Users\\ju2106\\Desktop\\5G\\sample.json','r'))  

class healthCheck:
    
    def __init__(self):
        pass
    
    def healthCheck(self):
        #jsonValue=_jsonModule.JSONUtil(myData)
        pass
    jsonModule.JSONUtil(myData)
    Final_json.JSONUtil(myData)
        
        
health=healthCheck()
health.healthCheck()
        
        
        
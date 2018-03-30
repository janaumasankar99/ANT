import json
from collections import namedtuple
from pprint import pprint 

myData = json.load(open('C:\\Users\\ju2106\\Desktop\\5G\\sample.json','r'))
#data = '{"command":"show active-charging group-of-ruledefs all | grep Total","alarm_type":"Warning","verifications":[{"condition":"regexp","rule":"true","value":"Total group","filter":[""],"export":"false"}]}'
def JSONUtil(myData):
    
    jsonParam={}
    length_json=len(myData['All']['All'][0]['All'])
    jsonParam['recLen']=length_json
    print(length_json)
    for i in range(0,length_json):
        for j in ['command','alarm_type','verifications']:
            #print ("this is correct")
            jsonParam[i,j]=myData['All']['All'][0]['All'][i][j]
            if j is 'verifications':
                #print("DATA",jsonParam[i,j])
                for s,v in jsonParam[i,j][0].items():
                    jsonParam[i,j,s]=v
    #print ("inside %s"%(jsonParam))
    return jsonParam

#JSONUtil()
#jsonparam=JSONUtil(myData)
#print (jsonparam)
#len=jsonparam['recLen']
#print ("The length of JSON is %s"%(len))
print (JSONUtil(myData))
#len=
# stored in dict and u can read as you want 
#print(jsonParam[0,'alarm_type'])
#print(jsonParam[9,'command'])
#print(jsonParam[10,'verifications'])
#print(JSONUtil().jsonParam[10,'verifications','rule'])



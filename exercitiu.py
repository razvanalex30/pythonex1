import json
from datetime import datetime
from CloudCtx import CloudCtx

import sys

if len(sys.argv) < 2:
    print("Input File is missing!")
    sys.exit()
with open(sys.argv[1]) as fread:
    jsondata = fread.read()


# fread = open('C:/Users/RAlexandru/Desktop/data4.json', 'r')
# jsondata = fread.read()


class FromJson:

    @classmethod
    def retrievejson(cls):
        objectjson = json.loads(jsondata)
        listimdata = objectjson['imdata']
        return listimdata

    @classmethod
    def objinitialization(cls):
        listimdata = cls.retrievejson()
        for _ in listimdata:
            CloudCtx.retrievefromjson()

    @classmethod
    def sortcurrenthealth(cls):
        CloudCtx.objCloudCtx.sort(key=lambda x: x.currenthealth)
        for i in range(len(CloudCtx.objCloudCtx)):
            print(CloudCtx.objCloudCtx[i].displaycloudctx())

    @classmethod
    def sorttime(cls):
        CloudCtx.objCloudCtx.sort(key=lambda x: datetime.strptime(x.modTs, "%d-%m-%Y %I:%M:%S %p"), reverse=True)
        for i in range(len(CloudCtx.objCloudCtx)):
            print(CloudCtx.objCloudCtx[i].displaycloudctx())


FromJson.retrievejson()
FromJson.objinitialization()
# FromJson.sortcurrenthealth()
FromJson.sorttime()

fread.close()

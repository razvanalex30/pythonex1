import json
from datetime import datetime
from CloudCtx import CloudCtx

import sys

if len(sys.argv) < 2:
    print("Input File is missing!")
    sys.exit()
with open(sys.argv[1]) as fread:
    jsondata = fread.read()


class FromJson:
    """
    External Class used to parse all the information from JSON file and to create the objects
    """
    @classmethod
    def retrievejson(cls):
        """
        Retrieve information from the JSON file
        :return: listimdata used for creating the CloudCtx and HealthInst objects
        """
        objectjson = json.loads(jsondata)
        listimdata = objectjson['imdata']
        return listimdata

    @classmethod
    def objinitialization(cls):
        """
        The initialization of the objects. Parsing all the dictionaries to create the objects
        """
        listimdata = cls.retrievejson()
        for elem in listimdata:
            CloudCtx.retrievefromjson(elem)

    @classmethod
    def sortcurrenthealth(cls):
        """
        Method used to sort the objects from low -> highest of the currenthealth
        """
        CloudCtx.objCloudCtx.sort(key=lambda x: x.currenthealth)
        for i in range(len(CloudCtx.objCloudCtx)):
            print(CloudCtx.objCloudCtx[i].displaycloudctx())

    @classmethod
    def sorttime(cls):
        """
        Method used to sort the object from the most recent -> oldest of the ModTs
        """
        CloudCtx.objCloudCtx.sort(key=lambda x: datetime.strptime(x.modTs, "%d-%m-%Y %I:%M:%S %p"), reverse=True)
        for i in range(len(CloudCtx.objCloudCtx)):
            print(CloudCtx.objCloudCtx[i].displaycloudctx())


FromJson.retrievejson()
FromJson.objinitialization()
FromJson.sortcurrenthealth()
# FromJson.sorttime()

fread.close()

import json
from datetime import datetime
from cloud_ctx import CloudCtx

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
    def retrieve_json(cls):
        """
        Retrieve information from the JSON file
        :return: listimdata used for creating the CloudCtx and HealthInst objects
        """
        objectjson = json.loads(jsondata)
        listimdata = objectjson['imdata']
        return listimdata

    @classmethod
    def obj_initialization(cls):
        """
        The initialization of the objects. Parsing all the dictionaries to create the objects
        """
        listimdata = cls.retrieve_json()
        for elem in listimdata:
            CloudCtx.retrieve_from_json(elem)

    @classmethod
    def sort_currenthealth(cls):
        """
        Method used to sort the objects from low -> highest of the currenthealth
        """
        CloudCtx.objCloudCtx.sort(key=lambda x: x.currenthealth)
        for elem in CloudCtx.objCloudCtx:
            print(elem.display_cloud_ctx())

    @classmethod
    def sort_time(cls):
        """
        Method used to sort the object from the most recent -> oldest of the ModTs
        """
        CloudCtx.objCloudCtx.sort(key=lambda x: datetime.strptime(x.modTs, "%d-%m-%Y %I:%M:%S %p"), reverse=True)
        for elem in CloudCtx.objCloudCtx:
            print(elem.display_cloud_ctx())


FromJson.retrieve_json()
FromJson.obj_initialization()
FromJson.sort_currenthealth()
FromJson.sort_time()

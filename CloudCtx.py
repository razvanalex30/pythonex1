import json
from datetime import datetime
from HealthInst import HealthInst

import sys

# if len(sys.argv) < 2:
#     print("Input File is missing!")
#     sys.exit()
# with open(sys.argv[1]) as fread:
#     jsondata = fread.read()
fread = open('C:/Users/RAlexandru/Desktop/data4.json', 'r')
jsondata = fread.read()
#
objectjson = json.loads(jsondata)
nrobjects = int(objectjson['totalCount'])
listimdata = objectjson['imdata']



class CloudCtx:
    """
    CloudCtx class
    """
    objCloudCtx = list()
    counter = 0
    name = None
    tenantName = None
    description = None
    nameAlias = None
    ctxProfileName = None
    currenthealth = 0
    modTs = None

    @staticmethod
    def timeretrieve(dict1, dict2):
        """
        Used for converting the time from json to the desired output <day-month-year hour:minute:second Am/PM>
        :param dict1: input dictionary 1
        :param dict2: input dictionary 2
        """
        timevar = dict2['modTs'][0:19]
        dateobj = datetime.strptime(timevar, "%Y-%m-%dT%H:%M:%S")
        datestring = dateobj.strftime("%d-%m-%Y %I:%M:%S %p")
        dict1['modTs'] = datestring

    @staticmethod
    def dictcreate(dict1, dict2):
        """
        Makes the correlation between dictionary 1 keys and dictionary 2 keys.
        :param dict1: input dictionary 1
        :param dict2: input dictionary 2
        """
        for key in dict1:
            dict1[key] = dict2[key]

    @staticmethod
    def rplemptystr(inputstring):
        """
        :param inputstring: Has a string as an input
        :return: Returns "-" if the string is empty or the respective value of the string
        """
        if inputstring == "":
            return "-"
        else:
            return inputstring

    def referencehealthinst(self):
        """
        Used to retrieve the current health of the corresponding HealthInst object to the CloudCtx object.
        :return: Currenth Health of the corresponding HealthInst object
        """
        currhealth = HealthInst.objHealthInst[CloudCtx.objCloudCtx.index(self)]
        if currhealth.currenthealth is not None:
            self.currenthealth = int(currhealth.currenthealth)
            return currhealth.currenthealth
        else:
            self.currenthealth = 0

    @classmethod
    def retrievefromjson(cls):
        """
        Retrieve the values of the attributes from the Json file
        :return: Get attributes values for the class.
        """
        attrdict1 = {'name': None, 'tenantName': None, 'description': None, 'nameAlias': None,
                     'ctxProfileName': None, 'modTs': None}
        pos = listimdata[cls.counter]
        elem = pos['hcloudCtx']['attributes']
        cls.dictcreate(attrdict1, elem)
        cls.timeretrieve(attrdict1, elem)
        objhealthinst = HealthInst.retrievefromjson2()
        HealthInst.objHealthInst.append(objhealthinst)
        return cls(**attrdict1)

    def __init__(self, name, tenantName, description, nameAlias, ctxProfileName, modTs):
        """
        Object initialization.
        """
        self.currenthealth = None
        self.name = self.rplemptystr(name)
        self.tenantName = self.rplemptystr(tenantName)
        self.description = self.rplemptystr(description)
        self.nameAlias = self.rplemptystr(nameAlias)
        self.ctxProfileName = self.rplemptystr(ctxProfileName)
        self.modTs = self.rplemptystr(modTs)
        CloudCtx.objCloudCtx.append(self)
        self.referencehealthinst()
        CloudCtx.counter += 1

    def displaycloudctx(self):
        """
        Used to display info about the CloudCtx object.
        :return: Info about the CloudCtx object created, with the corresponding current health value.
        """
        return '''
        Name: {} ;
        Tenant Name: {} ;
        Current Health: {} ;
        ModTs: {}
        '''.format(self.name, self.tenantName, self.currenthealth, self.modTs)
import json
from datetime import datetime

import sys

if len(sys.argv) < 2:
    print("Input File is missing!")
    sys.exit()
with open(sys.argv[1]) as fread:
    jsondata = fread.read()
# fread = open('C:/Users/RAlexandru/Desktop/data4.json', 'r')
# jsondata = fread.read()

objectjson = json.loads(jsondata)
nrobjects = int(objectjson['totalCount'])
listimdata = objectjson['imdata']

objCloudCtx = list()
objHealthInst = list()


class CloudCtx:
    """
    CloudCtx class
    """
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
        currhealth = objHealthInst[objCloudCtx.index(self)]
        if currhealth.currenthealth is not None:
            self.currenthealth = int(currhealth.currenthealth)
            return currhealth.currenthealth
        else:
            return None

    @classmethod
    def retrievefromjson(cls):
        """
        Retrieve the values of the attributes from the Json file
        :return: Get attributes values for the class.
        """
        attrdict1 = {'name': None, 'tenantName': None, 'description': None, 'nameAlias': None,
                     'ctxProfileName': None, 'modTs': None}
        pos = listimdata[len(objCloudCtx)]
        elem = pos['hcloudCtx']['attributes']
        cls.dictcreate(attrdict1, elem)
        cls.timeretrieve(attrdict1, elem)
        objhealthinst = HealthInst.retrievefromjson2()
        objHealthInst.append(objhealthinst)
        return cls(**attrdict1)

    def __init__(self, name, tenantName, description, nameAlias, ctxProfileName, modTs):
        """
        Object initialization.
        """
        self.name = self.rplemptystr(name)
        self.tenantName = self.rplemptystr(tenantName)
        self.description = self.rplemptystr(description)
        self.nameAlias = self.rplemptystr(nameAlias)
        self.ctxProfileName = self.rplemptystr(ctxProfileName)
        self.modTs = self.rplemptystr(modTs)
        objCloudCtx.append(self)
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


class HealthInst:
    """
    Class HealthInst
    """
    cur = None
    maxSev = None
    displayedhealth = None
    counter = 0

    @staticmethod
    def dictcreate(dict1, dict2):
        """
        Makes the correlation between dictionary 1 keys and dictionary 2 keys.
        :param dict1: input dictionary 1
        :param dict2: input dictionary 2
        """
        for key in dict1:
            dict1[key] = dict2[key]

    @classmethod
    def retrievefromjson2(cls):
        """
        Retrieve the values of the attributes from the Json file
        :return: Get attributes values for the class HealthInst
        """
        attrdict2 = {'cur': None, 'maxSev': None}
        pos = listimdata[len(objHealthInst)]
        elem = pos['hcloudCtx']['children']
        if elem:
            healthinstval = elem[0]['healthInst']['attributes']
            cls.dictcreate(attrdict2, healthinstval)
            attrdict2['displayedhealth'] = 'Healthy' if int(attrdict2['cur']) == 100 else 'Unhealthy'
            return cls(**attrdict2)
        else:
            attrdict2['displayedhealth'] = None
            return cls(**attrdict2)

    def __init__(self, cur, maxSev, displayedhealth):
        """
        Object initialization
        """
        self.currenthealth = cur
        self.max_sev = maxSev
        self.displayedhealth = displayedhealth
        HealthInst.counter += 1

    def displayhealthinst(self):
        """
        Used to return info about the HealthInst object
        :return: Info about the HealthInst object.
        """
        return '''
        Current Health: {} ;
        Max Sev: {} ;
        Displayed Health: {}
          '''.format(self.currenthealth, self.max_sev, self.displayedhealth)


def objinitialization(lenlist):
    """
    Used to create the objects CloudCtx and HealthInst from the JSON file
    :param lenlist: Number of objects in total in the JSON file
    """
    for elem in range(lenlist):
        CloudCtx.retrievefromjson()


objinitialization(nrobjects)


# ------Request 11-------
# objCloudCtx.sort(key=lambda x: x.currenthealth)
#
# for i in range(len(objCloudCtx)):
#     print(objCloudCtx[i].displaycloudctx())
# print("\n")


def objectcounter(inputlist):
    """

    :param inputlist: The list which contains the references to the CloudCtx/HealthInst objects
    :return: Returns the length of the list in order to keep track of the objects created.
    """
    return len(inputlist)


# print(objectcounter(objCloudCtx))
# -----Request 15-------

objCloudCtx.sort(key=lambda x: datetime.strptime(x.modTs, "%d-%m-%Y %I:%M:%S %p"), reverse=True)
for i in range(len(objCloudCtx)):
    print(objCloudCtx[i].displaycloudctx())

print(CloudCtx.counter)
print(HealthInst.counter)

fread.close()

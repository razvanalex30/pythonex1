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


def rplemptystr(inputstring):
    if inputstring == "":
        return "-"
    else:
        return inputstring


def dictcreate(dict1, dict2):
    for key in dict1:
        dict1[key] = dict2[key]


def timeretrieve(dict1, dict2):
    timevar = dict2['modTs'][0:19]
    dateobj = datetime.strptime(timevar, "%Y-%m-%dT%H:%M:%S")
    datestring = dateobj.strftime("%d-%m-%Y %I:%M:%S %p")
    dict1['modTs'] = datestring


class CloudCtx:
    counter = 0
    name = None
    tenantName = None
    description = None
    nameAlias = None
    ctxProfileName = None
    currenthealth = 0
    modTs = None

    def referencehealthinst(self):
        currhealth = objHealthInst[objCloudCtx.index(self)]
        if currhealth.currenthealth is not None:
            self.currenthealth = int(currhealth.currenthealth)
            return currhealth.currenthealth
        else:
            return None

    @classmethod
    def retrievefromjson(cls):
        attrdict1 = {'name': None, 'tenantName': None, 'description': None, 'nameAlias': None,
                     'ctxProfileName': None, 'modTs': None}
        pos = listimdata[len(objCloudCtx)]
        elem = pos['hcloudCtx']['attributes']
        dictcreate(attrdict1, elem)
        timeretrieve(attrdict1, elem)
        objhealthinst = HealthInst.retrievefromjson2()
        objHealthInst.append(objhealthinst)
        return cls(**attrdict1)

    def __init__(self, name, tenantName, description, nameAlias, ctxProfileName, modTs):
        self.name = rplemptystr(name)
        self.tenantName = rplemptystr(tenantName)
        self.description = rplemptystr(description)
        self.nameAlias = rplemptystr(nameAlias)
        self.ctxProfileName = rplemptystr(ctxProfileName)
        self.modTs = rplemptystr(modTs)
        objCloudCtx.append(self)
        self.referencehealthinst()
        CloudCtx.counter += 1

    def displaycloudctx(self):

        return '''
        Name: {} ;
        Tenant Name: {} ;
        Current Health: {} ;
        ModTs: {}
        '''.format(self.name, self.tenantName, self.currenthealth, self.modTs)


class HealthInst:
    cur = None
    maxSev = None
    displayedhealth = None
    counter = 0

    @classmethod
    def retrievefromjson2(cls):
        attrdict2 = {'cur': None, 'maxSev': None}
        pos = listimdata[len(objHealthInst)]
        elem = pos['hcloudCtx']['children']
        if elem:
            healthinstval = elem[0]['healthInst']['attributes']
            dictcreate(attrdict2, healthinstval)
            attrdict2['displayedhealth'] = 'Healthy' if int(attrdict2['cur']) == 100 else 'Unhealthy'
            return cls(**attrdict2)
        else:
            attrdict2['displayedhealth'] = None
            return cls(**attrdict2)

    def __init__(self, cur, maxSev, displayedhealth):
        self.currenthealth = cur
        self.max_sev = maxSev
        self.displayedhealth = displayedhealth
        HealthInst.counter += 1

    def displayhealthinst(self):
        return '''
        Current Health: {} ;
        Max Sev: {} ;
        Displayed Health: {}
          '''.format(self.currenthealth, self.max_sev, self.displayedhealth)


def objinitialization(lenlist):
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
    return len(inputlist)


# print(objectcounter(objCloudCtx))
# -----Request 15-------

objCloudCtx.sort(key=lambda x: datetime.strptime(x.modTs, "%d-%m-%Y %I:%M:%S %p"), reverse=True)
for i in range(len(objCloudCtx)):
    print(objCloudCtx[i].displaycloudctx())

print(CloudCtx.counter)
print(HealthInst.counter)

fread.close()

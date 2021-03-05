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


def isempty(a):
    if a == "":
        return "-"
    else:
        return a


def dictcr(x, y):
    for key in x:
        x[key] = y[key]
    return None


def time(x, y):
    timevar = y['modTs'][0:19]
    date_object = datetime.strptime(timevar, "%Y-%m-%dT%H:%M:%S")
    date_time = date_object.strftime("%d-%m-%Y %I:%M:%S %p")
    x['modTs'] = date_time
    return None


class CloudCtx:
    counter = 0
    name = None
    tenantName = None
    description = None
    nameAlias = None
    ctxProfileName = None
    current_health = 0
    modTs = None

    def reference(self):
        currhealth = objHealthInst[objCloudCtx.index(self)]
        if currhealth.current_health is not None:
            self.current_health = int(currhealth.current_health)
            return currhealth.current_health
        else:
            return None

    @classmethod
    def from_json(cls):
        attrdict1 = {'name': None, 'tenantName': None, 'description': None, 'nameAlias': None,
                     'ctxProfileName': None, 'modTs': None}
        pos = listimdata[len(objCloudCtx)]
        elem = pos['hcloudCtx']['attributes']
        dictcr(attrdict1, elem)
        time(attrdict1, elem)
        objhealthinst = HealthInst.from_json2()
        objHealthInst.append(objhealthinst)
        return cls(**attrdict1)

    def __init__(self, name, tenantName, description, nameAlias, ctxProfileName, modTs):
        self.name = isempty(name)
        self.tenant_name = isempty(tenantName)
        self.description = isempty(description)
        self.name_alias = isempty(nameAlias)
        self.ctx_profile_name = isempty(ctxProfileName)
        self.modTs = isempty(modTs)
        objCloudCtx.append(self)
        self.reference()
        CloudCtx.counter += 1

    def display(self):

        return '''
        Name: {} ;
        Tenant Name: {} ;
        Current Health: {} ;
        ModTs: {}
        '''.format(self.name, self.tenant_name, self.current_health, self.modTs)


class HealthInst:
    cur = None
    maxSev = None
    displayed_health = None
    counter = 0

    @classmethod
    def from_json2(cls):
        attrdict2 = {'cur': None, 'maxSev': None}
        pos = listimdata[len(objHealthInst)]
        elem = pos['hcloudCtx']['children']
        if elem:
            healthinstval = elem[0]['healthInst']['attributes']
            dictcr(attrdict2, healthinstval)
            attrdict2['displayed_health'] = 'Healthy' if int(attrdict2['cur']) == 100 else 'Unhealthy'
            return cls(**attrdict2)
        else:
            attrdict2['displayed_health'] = None
            return cls(**attrdict2)

    def __init__(self, cur, maxSev, displayed_health):
        self.current_health = cur
        self.max_sev = maxSev
        self.displayed_health = displayed_health
        HealthInst.counter += 1

    def afisare(self):
        return '''
        Current Health: {} ;
        Max Sev: {} ;
        Displayed Health: {}
          '''.format(self.current_health, self.max_sev, self.displayed_health)


def initialization(a):
    for elem in range(a):
        CloudCtx.from_json()
    return None


initialization(nrobjects)


######################### Request 11 ###########################################
# objCloudCtx.sort(key=lambda x: x.current_health)
#
# for i in range(len(objCloudCtx)):
#     print(objCloudCtx[i].display())
# print("\n")


def trackobjects(a):
    return len(a)


# print(trackobiecte(objCloudCtx))
################################# Request 15 ###################################

objCloudCtx.sort(key=lambda x: datetime.strptime(x.modTs, "%d-%m-%Y %I:%M:%S %p"), reverse=True)
for i in range(len(objCloudCtx)):
    print(objCloudCtx[i].display())

print(CloudCtx.counter)
print(HealthInst.counter)

fread.close()

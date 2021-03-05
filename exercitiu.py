import json
from datetime import datetime

# import sys
#
# if len(sys.argv)<2:
#     print("Input File is missing!")
#     sys.exit()
# with open(sys.argv[1]) as fisier:
#     jsondata = fisier.read()
fread = open('C:/Users/RAlexandru/Desktop/data3.json', 'r')
jsondata = fread.read()

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


class CloudCtx:
    counter = 0
    name = None
    tenant_name = None
    description = None
    name_alias = None
    ctx_profile_name = None
    current_health = 0
    modTs = None

    def reference(self):
        currhealth = objHealthInst[objCloudCtx.index(self)]
        if (currhealth.current_health != None):
            self.current_health = int(currhealth.current_health)
            return currhealth.current_health
        else:
            return None

    @classmethod
    def from_json(cls):
        attrdict1 = {'name': None, 'tenant_name': None, 'description': None, 'name_alias': None,
                     'ctx_profile_name': None, 'modTs': None}
        super1 = listimdata[len(objCloudCtx)]
        superelem = super1['hcloudCtx']['attributes']
        attrdict1['name'] = superelem['name']
        attrdict1['tenant_name'] = superelem['tenantName']
        attrdict1['description'] = superelem['description']
        attrdict1['name_alias'] = superelem['nameAlias']
        attrdict1['ctx_profile_name'] = superelem['ctxProfileName']
        time = superelem['modTs'][0:19]
        date_object = datetime.strptime(time, "%Y-%m-%dT%H:%M:%S")
        date_time = date_object.strftime("%d-%m-%Y %I:%M:%S %p")
        attrdict1['modTs'] = date_time
        objhealthinst = HealthInst.from_json2()
        objHealthInst.append(objhealthinst)
        return cls(**attrdict1)

    def __init__(self, name, tenant_name, description, name_alias, ctx_profile_name, modTs):
        self.name = isempty(name)
        self.tenant_name = isempty(tenant_name)
        self.description = isempty(description)
        self.name_alias = isempty(name_alias)
        self.ctx_profile_name = isempty(ctx_profile_name)
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
    current_health = None
    max_sev = None
    displayed_health = None
    counter = 0

    @classmethod
    def from_json2(cls):
        attrdict2 = {'current_health': None, 'max_sev': None, "displayed_health": None}
        super2 = listimdata[len(objHealthInst)]
        superelem = super2['hcloudCtx']['children']
        if superelem != []:
            superelem2 = superelem[0]
            superelem3 = superelem2['healthInst']['attributes']
            attrdict2['current_health'] = superelem3['cur']
            attrdict2['max_sev'] = superelem3['maxSev']
            attrdict2['displayed_health'] = 'Healthy' if int(superelem3['cur']) == 100 else 'Unhealthy'
            return cls(**attrdict2)
        else:
            return cls(**attrdict2)

    def __init__(self, current_health, max_sev, displayed_health):
        self.current_health = current_health
        self.max_sev = max_sev
        self.displayed_health = displayed_health
        HealthInst.counter += 1

    def afisare(self):
        return '''
        Current Health: {} ;
        Max Sev: {} ;
        Displayed Health: {}
          '''.format(self.current_health, self.max_sev, self.displayed_health)


def initialization(a):
    for i in range(a):
        CloudCtx.from_json()
    return None


initialization(nrobjects)

######################### Request 11 ###########################################
objCloudCtx.sort(key=lambda x: x.current_health)

for i in range(len(objCloudCtx)):
    print(objCloudCtx[i].display())
print("\n")


def trackobiecte(a):
    return len(a)


# print(trackobiecte(objCloudCtx))
################################# Request 15 ###################################

# obj1.sort(key=lambda x: datetime.strptime(x.modTs,"%d-%m-%Y %I:%M:%S %p"),reverse=True)
# for i in range(len(obj1)):
#     print(obj1[i].display())

print(CloudCtx.counter)
print(HealthInst.counter)
fread.close()

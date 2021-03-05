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

objCloudCtx = list()
objHealthInst = list()


def isempty(a):
    if a == "":
        return "-"
    else:
        return a


class CloudCtx:
    name = None
    tenant_name = None
    description = None
    name_alias = None
    ctx_profile_name = None
    displayed_health = 0
    modTs = None

    def reference(self):
        currhealth = objHealthInst[objCloudCtx.index(self)]
        if (currhealth.current_health != None):
            self.displayed_health = int(currhealth.current_health)
            return currhealth.current_health
        else:
            return None

    @classmethod
    def from_json(cls, jsondata):
        lista1 = objectjson['imdata']
        dictionar = {'name': None, 'tenant_name': None, 'description': None, 'name_alias': None,
                     'ctx_profile_name': None, 'modTs': None}
        super1 = lista1[len(objCloudCtx)]
        superelem = super1['hcloudCtx']['attributes']
        dictionar['name'] = superelem['name']
        dictionar['tenant_name'] = superelem['tenantName']
        dictionar['description'] = superelem['description']
        dictionar['name_alias'] = superelem['nameAlias']
        dictionar['ctx_profile_name'] = superelem['ctxProfileName']
        time = superelem['modTs'][0:19]
        date_object = datetime.strptime(time, "%Y-%m-%dT%H:%M:%S")
        date_time = date_object.strftime("%d-%m-%Y %I:%M:%S %p")
        dictionar['modTs'] = date_time
        objhealth = HealthInst.from_json2(jsondata)
        objHealthInst.append(objhealth)
        return cls(**dictionar)

    def __init__(self, name, tenant_name, description, name_alias, ctx_profile_name, modTs):
        self.name = isempty(name)
        self.tenant_name = isempty(tenant_name)
        self.description = isempty(description)
        self.name_alias = isempty(name_alias)
        self.ctx_profile_name = isempty(ctx_profile_name)
        self.modTs = isempty(modTs)
        objCloudCtx.append(self)
        self.reference()

    def afisare(self):

        return '''
        Name: {} ;
        Tenant Name: {} ;
        Current Health: {} ;
        ModTs: {}
        '''.format(self.name, self.tenant_name, self.displayed_health, self.modTs)


class HealthInst:
    current_health = None
    max_sev = None
    displayed_health = None

    @classmethod
    def from_json2(cls, jsondata):
        lista1 = objectjson['imdata']
        dictionar2 = {'current_health': None, 'max_sev': None, "displayed_health": None}
        super2 = lista1[len(objHealthInst)]
        superelem = super2['hcloudCtx']['children']
        if (superelem) != []:
            superelem2 = superelem[0]
            superelem3 = superelem2['healthInst']['attributes']
            dictionar2['current_health'] = superelem3['cur']
            dictionar2['max_sev'] = superelem3['maxSev']
            dictionar2['displayed_health'] = 'Healthy' if int(superelem3['cur']) == 100 else 'Unhealthy'
            return cls(**dictionar2)
        else:
            return cls(**dictionar2)

    def __init__(self, current_health, max_sev, displayed_health):
        self.current_health = current_health
        self.max_sev = max_sev
        self.displayed_health = displayed_health

    def afisare(self):
        return '''
        Current Health: {} ;
        Max Sev: {} ;
        Displayed Health: {}
          '''.format(self.current_health, self.max_sev, self.displayed_health)


def initialization(a):
    for i in range(a):
        CloudCtx.from_json(jsondata)
    return None


initialization(nrobjects)

######################### Request 11 ###########################################
objCloudCtx.sort(key=lambda x: x.displayed_health)

for i in range(len(objCloudCtx)):
    print(objCloudCtx[i].afisare())
print("\n")


def trackobiecte(a):
    return len(a)


print(trackobiecte(objCloudCtx))
################################# Request 15 ###################################

# obj1.sort(key=lambda x: datetime.strptime(x.modTs,"%d-%m-%Y %I:%M:%S %p"),reverse=True)
# for i in range(len(obj1)):
#     print(obj1[i].afisare())
print(len(objHealthInst))
fread.close()

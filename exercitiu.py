import json
from datetime import datetime

fisier = open('C:/Users/RAlexandru/Desktop/data.json', 'r')
jsondata = fisier.read()

objectjson=json.loads(jsondata)
nrobjects=int(objectjson['totalCount'])


obj1 = list()
obj2 = list()


def isempty(a):
    if a=="":
        return "-"
    else:
        return a
class CloudCtx:

    name=None
    tenant_name=None
    description=None
    name_alias=None
    ctx_profile_name=None
    displayed_health = None
    modTs=None

    def referinta(self):
        x = obj2[obj1.index(self)]
        self.displayed_health=int(x.current_health)
        return x.current_health


    @classmethod
    def from_json(cls, jsondata):
        obiect = json.loads(jsondata)
        lista1 = obiect['imdata']
        dictionar = {'name': None, 'tenant_name': None, 'description': None, 'name_alias': None, 'ctx_profile_name': None}
        super1 = lista1[len(obj1)]
        superelem = super1['hcloudCtx']['attributes']
        dictionar['name'] = superelem['name']
        dictionar['tenant_name'] = superelem['tenantName']
        dictionar['description'] = superelem['description']
        dictionar['name_alias'] = superelem['nameAlias']
        dictionar['ctx_profile_name'] = superelem['ctxProfileName']
        time=superelem['modTs'][0:19]
        date_object = datetime.strptime(time, "%Y-%m-%dT%H:%M:%S")
        date_time = date_object.strftime("%d-%m-%Y %I:%M:%S %p")
        dictionar['modTs']=date_time
        return cls(**dictionar)

    def __init__(self, name, tenant_name, description, name_alias, ctx_profile_name,modTs):
        self.name = isempty(name)
        self.tenant_name = isempty(tenant_name)
        self.description = isempty(description)
        self.name_alias = isempty(name_alias)
        self.ctx_profile_name = isempty(ctx_profile_name)
        self.modTs=isempty(modTs)
        obj1.append(self)

    def afisare(self):
        self.referinta()
        return 'Name: {} ; Tenant Name: {} ; Current Health: {} ; ModTs: {}'.format(self.name, self.tenant_name, self.displayed_health,self.modTs)


class HealthInst:
    current_health=None
    max_sev=None
    displayed_health=None

    @classmethod
    def from_json2(cls, jsondata):
        obiect = json.loads(jsondata)
        lista1 = obiect['imdata']
        dictionar2 = {'current_health': None, 'max_sev': None, "displayed_health": None}
        super2 = lista1[len(obj2)]
        superelem = super2['hcloudCtx']['children']
        superelem2 = superelem[0]
        superelem3 = superelem2['healthInst']['attributes']
        dictionar2['current_health'] = superelem3['cur']
        dictionar2['max_sev'] = superelem3['maxSev']
        dictionar2['displayed_health'] = 'Healthy' if int(superelem3['cur']) == 100 else 'Unhealthy'
        return cls(**dictionar2)

    def __init__(self, current_health, max_sev, displayed_health):
        self.current_health = current_health
        self.max_sev = max_sev
        self.displayed_health = displayed_health
        obj2.append(self)

    def afisare(self):
        return 'Current Health: {} ; Max Sev: {} ; Displayed Health: {}'.format(self.current_health, self.max_sev,self.displayed_health)

def initializare(a):
    for i in range(a):
        CloudCtx.from_json(jsondata)
        HealthInst.from_json2(jsondata)
    return None


initializare(nrobjects)

print("\n")

######################### Request 11 ###########################################
# obj1.sort(key=lambda x: x.displayed_health)
#
# for i in range(len(obj1)):
#     print("Name: {}; Tenant Name: {}; Displayed Health: {}".format(obj1[i].name,obj1[i].tenant_name,obj1[i].displayed_health))
# print("\n")
def trackobiecte(a):
    return len(a)

print(trackobiecte(obj1))
################################# Request 15 ###################################

obj1.sort(key=lambda x: datetime.strptime(x.modTs,"%d-%m-%Y %I:%M:%S %p"),reverse=True)
for i in range(len(obj1)):
    print("Name: {}; Tenant Name: {}; Displayed Health: {}; ModTS: {};".format(obj1[i].name,obj1[i].tenant_name,obj1[i].displayed_health,obj1[i].modTs))


import json
from datetime import datetime

fisier = open('C:/Users/RAlexandru/Desktop/data.json', 'r')
jsondata = fisier.read()

obj1 = list()
obj2 = list()


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
        dictionar = {'name': None, 'tenant_name': None, 'description': None, 'name_alias': None, 'ctx_profile_name': None, 'modTs':None}
        super1 = lista1[len(obj1)]
        superelem = super1['hcloudCtx']['attributes']
        dictionar['name'] = superelem['name']
        dictionar['tenant_name'] = superelem['tenantName']
        dictionar['description'] = superelem['description']
        dictionar['name_alias'] = superelem['nameAlias']
        dictionar['ctx_profile_name'] = superelem['ctxProfileName']
        time=superelem['modTs'][0:19]
        time2=time[::-1]
        time3=datetime.strptime(time2,"")

        return cls(**dictionar)

    def __init__(self, name, tenant_name, description, name_alias, ctx_profile_name,modTs):
        self.name = name if name != "" else "-"
        self.tenant_name = tenant_name if tenant_name != "" else "-"
        self.description = description if description != "" else "-"
        self.name_alias = name_alias if name_alias != "" else "-"
        self.ctx_profile_name = ctx_profile_name if ctx_profile_name != "" else "-"
        self.modTs=modTs if modTs!="" else "-"

        obj1.append(self)

    def afisare(self):
        self.referinta()
        return 'Name: {} ; Tenant Name: {} ; Displayed Health: {} ;'.format(self.name, self.tenant_name, self.displayed_health)


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


obiect1 = CloudCtx.from_json(jsondata)
obiect2 = CloudCtx.from_json(jsondata)
obiect3 = CloudCtx.from_json(jsondata)
obiect4 = CloudCtx.from_json(jsondata)
obiect5 = CloudCtx.from_json(jsondata)



obiect6 = HealthInst.from_json2(jsondata)
obiect7 = HealthInst.from_json2(jsondata)
obiect8 = HealthInst.from_json2(jsondata)
obiect9 = HealthInst.from_json2(jsondata)
obiect10 = HealthInst.from_json2(jsondata)

print(obiect1.afisare())
print(obiect2.afisare())
print(obiect3.afisare())
print(obiect4.afisare())
print(obiect5.afisare())

print("\n")
obj1.sort(key=lambda x: x.displayed_health)

for i in range(len(obj1)):
    print(obj1[i].displayed_health)
print("\n")
def trackobiecte(a):
    return len(a)

print(trackobiecte(obj1))

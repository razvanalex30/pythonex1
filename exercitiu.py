import json

fisier=open('C:/Users/RAlexandru/Desktop/json.txt', 'r')
jsondata = fisier.read()

# obiect=json.loads(jsondata)
# lista1=obiect['imdata']
# counter=int(obiect['totalCount'])

obj1=list()
obj2=list()
class CloudCtx:

    @classmethod
    def from_json(cls,jsondata):
        obiect = json.loads(jsondata)
        lista1 = obiect['imdata']
        dictionar={'name':None,'tenant_name':None,'description':None,'name_alias':None,'ctx_profile_name':None}
        for elem in lista1:
            dictionar['name']=elem['hcloudCtx']['attributes']['name'] if elem['hcloudCtx']['attributes']['name']!="" else "-"
            dictionar['tenant_name']=elem['hcloudCtx']['attributes']['tenantName'] if elem['hcloudCtx']['attributes']['tenantName']!="" else "-"
            dictionar['description']=elem['hcloudCtx']['attributes']['description'] if elem['hcloudCtx']['attributes']['description']!="" else "-"
            dictionar['name_alias']=elem['hcloudCtx']['attributes']['nameAlias'] if elem['hcloudCtx']['attributes']['nameAlias']!="" else "-"
            dictionar['ctx_profile_name']=elem['hcloudCtx']['attributes']['ctxProfileName'] if elem['hcloudCtx']['attributes']['ctxProfileName']!="" else "-"
        return cls(**dictionar)

    def __init__(self,name,tenant_name,description,name_alias,ctx_profile_name):
        self.name=name
        self.tenant_name=tenant_name
        self.description=description
        self.name_alias=name_alias
        self.ctx_profile_name=ctx_profile_name

    def afisare(self):
        return 'Name: {} ; Tenant Name: {} ; Description: {} ; Name Alias: {} ; Ctx Profile Name: {} ;'.format(self.name,
        self.tenant_name,self.description,self.name_alias,self.ctx_profile_name)



# class HealthInst:
#
#     def __init__(self,current_health,max_sev):
#         self.current_health=current_health
#         self.max_sev=max_sev
#
#     def afisare(self):
#         return 'Current Health: {} ; Max Sev: {} ;'.format(self.current_health, self.max_sev)
#
#     def status_health(self):
#         if int(self.current_health)==100:
#             return 'Healthy'
#         else:
#             return 'Unhealthy'
#
# def func1(a):
#     for elem in a:
#         print(type(elem))
#         name=elem['hcloudCtx']['attributes']['name']
#         if(name==""):
#             name="-"
#         tenant_name=elem['hcloudCtx']['attributes']['tenantName']
#         if (tenant_name == ""):
#             tenant_name = "-"
#         description=elem['hcloudCtx']['attributes']['description']
#         if (description == ""):
#             description = "-"
#         name_alias=elem['hcloudCtx']['attributes']['nameAlias']
#         if (name_alias == ""):
#             name_alias = "-"
#         ctx_profile_name=elem['hcloudCtx']['attributes']['ctxProfileName']
#         if (ctx_profile_name == ""):
#             ctx_profile_name = "-"
#         obj = CloudCtx(name,tenant_name,description,name_alias,ctx_profile_name)
#         obj1.append(obj)
#         print(obj.afisare())
#
#
# def func2(a):
#     for elem in a:
#         current_health=elem['hcloudCtx']['children']
#         for elem2 in current_health:
#             current_health=elem2['healthInst']['attributes']['cur']
#             max_sev=elem2['healthInst']['attributes']['maxSev']
#             obj3=HealthInst(current_health,max_sev)
#             obj2.append(obj3)
#             print(obj3.afisare(),obj3.status_health())
#
# func1(lista1)
# print("\n")
# func2(lista1)
# fisier.close()
# print("\n")
# print(obj1[1].retrieve())
# print("\n")
# print(obj2)
#
obj = CloudCtx.from_json(jsondata)
print(obj.name_alias)


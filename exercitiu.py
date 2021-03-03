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
            dictionar['name']= elem['hcloudCtx']['attributes']['name']
            if(dictionar['name']==""):
                dictionar['name']="-"
            dictionar['tenant_name']=elem['hcloudCtx']['attributes']['tenantName']
            if (dictionar['tenant_name'] == ""):
                dictionar['tenant_name'] = "-"
            dictionar['description']=elem['hcloudCtx']['attributes']['description']
            if (dictionar['description'] == ""):
                dictionar['description'] = "-"
            dictionar['name_alias']=elem['hcloudCtx']['attributes']['nameAlias']
            if (dictionar['name_alias'] == ""):
                dictionar['name_alias'] = "-"
            dictionar['ctx_profile_name']=elem['hcloudCtx']['attributes']['ctxProfileName']
            if (dictionar['ctx_profile_name'] == ""):
                dictionar['ctx_profile_name'] = "-"
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
# json_string='''{
#                     "awsVPC": "",
#                     "azResourceGroup": "",
#                     "azVirtualNetwork": "",
#                     "childAction": "",
#                     "ctxProfileName": "ct_ctxprofile_us-west-1",
#                     "delegateDn": "uni/tn-infra/ctxprofile-ct_ctxprofile_us-west-1",
#                     "description": "",
#                     "dn": "acct-[infra]/region-[us-west-1]/context-[overlay-1]-addr-[10.10.0.0/25]",
#                     "encap": "16777199",
#                     "encapType": "vxlan",
#                     "fvCtxDn": "uni/tn-infra/ctx-overlay-1",
#                     "interSitePeeringEnabled": "yes",
#                     "lcOwn": "local",
#                     "modTs": "2020-10-22T16:27:14.966+00:00",
#                     "name": "overlay-1",
#                     "nameAlias": "",
#                     "primaryCidr": "10.10.0.0/25",
#                     "resolvedObjDn": "ctxdefcont/ctxProfileVrfDef-[uni/tn-infra/ctxprofile-ct_ctxprofile_us-west-1]-ctxDef-[uni/tn-infra/ctx-overlay-1]",
#                     "status": "",
#                     "tenantName": "infra",
#                     "type": "regular"
# }'''
obj = CloudCtx.from_json(jsondata)
print(obj.ctx_profile_name)


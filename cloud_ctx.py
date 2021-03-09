from datetime import datetime
from health_inst import HealthInst


class CloudCtx:
    """
    CloudCtx class
    """
    objCloudCtx = list()
    counter = 0
    currenthealth = 0
    modTs = None

    @staticmethod
    def time_retrieve(dict1, dict2):
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
    def dict_create(dict1, dict2):
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

    def reference_health_inst(self):
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
    def retrieve_from_json(cls, elem):
        """
        Retrieve the values of the attributes from the Json file
        :return: Get attributes values for the class.
        """
        attrdict1 = {'name': None, 'tenantName': None, 'description': None, 'nameAlias': None,
                     'ctxProfileName': None, 'modTs': None}
        elem2 = elem['hcloudCtx']['attributes']
        cls.dict_create(attrdict1, elem2)
        cls.time_retrieve(attrdict1, elem2)
        objhealthinst = HealthInst.retrieve_from_json2(elem)
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
        self.reference_health_inst()
        CloudCtx.counter += 1

    def display_cloud_ctx(self):
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

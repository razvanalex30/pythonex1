import json

# import sys

# if len(sys.argv) < 2:
#     print("Input File is missing!")
#     sys.exit()
# with open(sys.argv[1]) as fread:
#     jsondata = fread.read()
fread = open('C:/Users/RAlexandru/Desktop/data4.json', 'r')
jsondata = fread.read()
#
objectjson = json.loads(jsondata)
nrobjects = int(objectjson['totalCount'])
listimdata = objectjson['imdata']


class HealthInst:
    """
    Class HealthInst
    """

    objHealthInst = list()
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
        pos = listimdata[cls.counter]
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

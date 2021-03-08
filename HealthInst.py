class HealthInst:
    """
    Class HealthInst
    """
    cur = None
    maxSev = None
    displayedhealth = None
    counter = 0

    @classmethod
    def retrievefromjson2(cls):
        """
        Retrieve the values of the attributes from the Json file
        :return: Get attributes values for the class HealthInst
        """
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
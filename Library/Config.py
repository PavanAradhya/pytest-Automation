from configparser import ConfigParser

def readconfig(section,key):
    configobj = ConfigParser()
    configobj.read("./Configuration_files/Config.cfg")
    return configobj.get(section,key)
#print(readconfig("Details","URL"))

def elementLoc(section,key):
    configobj = ConfigParser()
    configobj.read("./Configuration_files/Elements.cfg")
    return configobj.get(section, key)




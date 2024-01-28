from XLogger import XLogger
# import XObject, { XObjectPack } from "./XObject.js";

# /**
#  * Xpell Module Object Manager
#  * @description this manager holds the module XObjects that should be managed (XObject children will not be managed separately)
#  * XModules uses the Object Manager to create new XObjects by providing the class of the object by name
#  */



class XObjectManager:
  
    def __init__(self,moduleName):
         #Object Classes dictionary
        self._object_classes = {}

         #Live XObject that is being maintained by the Object Manager
        self._xobjects = {}

         #Object Names index - uses to get object by name
        self._names_index = {}
        if moduleName:
            XLogger.log("Object Manager for  " + moduleName + " loaded")
        else:
            XLogger.log("Object Manager loaded")
        



    @property
    def _objects(self):
        return self._xobjects
    
    @property
    def _classes(self):
        return self._object_classes
    

    # /**
    #  * Checks if an object is found in the object manager
    #  * @param xObjectId 
    #  * @returns 
    #  */
    def hasObject(self,xObjectId):
        return hasattr(self._xobjects,xObjectId)
    

    # /**
    #  * Register multiple classes dictionary into the object manager
    #  * @param xObjects - key value list -> \{"view":XView,...\}
    #  */
    def registerObjects(self,xObjects):
        # names = Object.keys(xObjects)
        # names.forEach(name => this.registerObject(name, xObjects[name]))
        for name in xObjects:
            self.registerObject(name, xObjects[name])
    

    # /**
    #  * Registers single XObject
    #  * @param name - name of the object
    #  * @param xObjects The object class
    #  */
    def registerObject(self,name, xObjects):
        self._object_classes[name] = xObjects


    # /**
    #  * Checks if a class (name) is found in the object manager classes dictionary
    #  * @param name - class name
    #  * @returns {boolean} 
    #  */
    def hasObjectClass(self,name):
        return hasattr(this._object_classes,name)
    

    # /**
    #  * Retrieves XObject class instance
    #  * @param name class name
    #  * @returns {XObject}
    #  */
    def getObjectClass(self,name):
        return self._object_classes[name]
    

    # /**
    #  * Retrieves all the classes dictionary
    #  * @returns XObjectManagerIndex
    #  */
    def getAllClasses(self):
        return self._object_classes
    

    

    # /**
    #  * Add XObject instance to the manager
    #  * @param xObject XObject to maintain
    #  */
    def addObject(self,xObject):
        if xObject and xObject._id:
            self._xobjects[xObject._id] = xObject
            if not xObject._name or len(xObject._name)==0:
                xObject._name = xObject._id
            self._names_index[xObject._name] = xObject._id
        else:
            XLogger.log("unable to add object")

    '''
     * Remove XObject from the manager 
     * @param xObjectId object id to remove
     '''
    def removeObject(self,xObjectId):
        obj = self._xobjects[xObjectId]
        if obj:
            del self._names_index[obj.name] 
            del self._xobjects[xObjectId] 
        
    

    '''
     * Retrieves XObject instance
     * @param xObjectId XObject id 
     * @returns {XObject}
    '''
    def getObject(self,xObjectId):
        return self._xobjects[xObjectId]
    

    '''
     * alias to getObject
     * @param id 
     * @returns 
     '''
    def go(self,id):
        return self.getObject(id)
    
    

    '''
     * Retrieves XObject instance
     * @param objectName XObject name 
     * @returns {XObject}
    '''
    def getObjectByName(self,objectName):
        if self._names_index[objectName]:
            return self.getObject(self._names_index[objectName])
        else: 
            return null
    

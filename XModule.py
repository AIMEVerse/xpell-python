

'''
 * XModule - Xpell Base Module
 * The class is being extended by modules with the following logic:
 * 1. Every module must have a name
 * 2. Module holds Object manager to manager the module specific object (extends XObject)
 * 3. Every module can execute XCommand (XCommand, JSON, text(CLI style)),
 *    the rules of the method invocation is the "underscore" sign, meaning functions that will start with "_" sign
 *    will be exposed to XPell Interpreter
 *
 * @example
 *  
 *    The following module:
 *      
 *    class myModule extends XModule {
 *          constructor() {...}
 *          _my_Command(xCommand) {
 *              ...
 *          }
 *    }
 * 
 *    will be called like:
 * 
 *    XModule.execute("my-Command")
 *      - when calling the method there is no need for the underscore sign, spaces and dashes will be converted to underscore
 *  
'''

# import XUtils from "./XUtils.js"
# import XParser from "./XParser.js"
from XLogger import _xlog
from XObjectManager import XObjectManager
# import XObjectManager from "./XObjectManager.js";
# import * as _XC from "./XConst.js"
# import { XObjectData, XObject, XObjectPack } from "./XObject.js";
from XCommand import XCommand
import json
import uuid


# /**
#  * Xpell Base Module
#  * This class represents xpell base module to be extends
#  * @class XModule
#  * 
#  */
class XModule:


    # data - json object of XModuleData
    def __init__(self,data):
        self._name = data["_name"]
        self._id =  str(uuid.uuid4())
        self._object_manager = XObjectManager(self._name)
        

    

    def load(self): 
        _xlog.log("Module " + self._name + " loaded")
    

    '''
     * Creates new XObject from data object
     * @param data - The data of the new object (JSON)
     * @return {XObject|*}
    '''
    def create(self,data):
        xObject = None
        # if "_type" in data:
        #     if self._object_manager.has_object_class(data["_type"]):
        #         x_object_class = self._object_manager.get_object_class(data["_type"])
        #         if hasattr(x_object_class, "defaults"):
        #             XUtils.merge_defaults_with_data(data, x_object_class.defaults)
        #         x_object = x_object_class(data)
        #     else:
        #         raise Exception("Xpell object '" + data["_type"] + "' not found")
        # else:
        #     x_object = XObject(data)

        # self._object_manager.add_object(x_object)

        # if "_children" in data:
        #     for spell in data["_children"]:
        #         new_spell = self.create(spell)
        #         x_object.append(new_spell)

        # x_object.on_create()

        return xObject
        # if (data.hasOwnProperty("_type")) {
        #     if (this._object_manger.hasObjectClass(<string>data["_type"])) {
        #         let xObjectClass = this._object_manger.getObjectClass(<string>data["_type"]);
        #         if (xObjectClass.hasOwnProperty("defaults")) {
        #             XUtils.merge_defaults_with_data(data, xObjectClass.defaults);
        #         }
        #         xObject = new xObjectClass(data);
        #     }
        #     else {
        #         throw "Xpell object '" + data["_type"] + "' not found";
        #     }
        # }
        # else {
        #     xObject = new XObject(data);
        # }

        # this._object_manger.addObject(xObject)
        # if (data._children) {
        #     data._children.forEach(async (spell) => {
        #         let new_spell = this.create(<any>spell);
        #         xObject.append(new_spell)
        #     });
        # }
        # xObject.onCreate()
    

    # /**
    #  * removes and XObject from the object manager
    #  * @param objectId op
    #  */
    def remove(self,objectId):
        obj = self._object_manger.getObject(objectId)
        if (obj):
            self._object_manger.removeObject(objectId)
            # if(obj["dispose"] && typeof obj.dispose === "function") {
            #     (<XObject>obj).dispose()
            # }
        
    


    def _info(self,xCommand):
        _xl.log("module info")
    

    # //xpell interpreter 
    # /**
    #  * Run xpell command - 
    #  * CLI mode, parse the command to XCommand JSON format and call execute method
    #  * @param {string} XCommand input - text 
    #  * @returns command execution result
    #  */
    async def run(self,stringXCommand): 
        if stringXCommand:
            strCmd = stringXCommand.trim()
            #//add module name to run command if not exists (in case of direct call from the module)
            if not strCmd.startsWith(this._name):
                strCmd = this._name + " " + strCmd            
            #xCommand = XParser.parse(strCmd)
            return await this.execute(xCommand)
        else:
            # throw an error "Unable to parse Xpell Command"
            raise Exception("Unable to parse Xpell Command")
            
    
    




    # /**
    #  * execute xpell command - CLI mode
    #  * @param {XCommand} XCommand input (JSON)
    #  * @returns command execution result
    #  */
    async def execute(self,xCommand):
        _xlog.log("execute command: " + json.dumps(xCommand))


        # //search for xpell wrapping functions (starts with _ "underscore" example -> _start() , async _spell_async_func() )
        # if xCommand._op:
        #     lop:string = "_" + xCommand._op.replaceAll('-', '_') #//search for local op = lop
        # if (this[lop] && typeof this[lop] === 'function') {
        #     return this[lop](xCommand)
        # }
        # else if (this._object_manger) //direct xpell injection to specific module
        # {

        #     const o = this._object_manger.getObjectByName(xCommand._op)
        #     if (o) { o.execute(xCommand) }
        #     else { throw "Xpell Module cant find op:" + xCommand._op }
        # }
        # else {
        #     throw "Xpell Module cant find op:" + xCommand._op
        # }
        # }
        



    # /**
    #  * This method triggers every frame from the Xpell engine.
    #  * The method can be override by the extending module to support extended on_frame functionality
    #  * @param frameNumber Current frame number
    #  */
    async def on_frame(self,frameNumber):
        # _xlog.log("on_frame module: " + str(frameNumber))
        om_objects = self._object_manager._objects  # Assuming self is an instance of a class containing _object_manager
        for key in om_objects:
            on_frame_callback = om_objects[key]
            if on_frame_callback and hasattr(on_frame_callback, 'on_frame') and callable(getattr(on_frame_callback, 'on_frame')):
                await on_frame_callback.on_frame(frame_number)

    


    
    '''
     * Returns the XObject instance from the module Object Manager
     * @param objectId 
     * @returns XObject
    '''
    def getObject(objectId):
        return self._object_manger.getObject(objectId)
    

    '''
     * Imports external object pack to the engine
     * The object class should be like XObjects with static implementation of getObjects() method
     * @param {XObjects} xObjectPack 
    '''
    def importObjectPack(xObjectPack):
        self._object_manger.registerObjects(xObjectPack.getObjects())
    

    '''
     * Imports external object pack to the engine
     * @deprecated - use importObjectPack instead
     * @param xObjectPack 
    '''
    def importObjects(xObjectPack):
        self.importObjectPack(xObjectPack)
    

    '''
     * Imports external objects to the engine
     * The object class should be like XObjects with static implementation of getObjects() method
     * @param xObjectName 
     * @param xObject 
    '''
    def importObject(xObjectName, xObject):
         self._object_manger.registerObject(xObjectName, xObject)
    


gm = {"_name":"xmodule"}
GenericModule = XModule(gm)
# export default XModule
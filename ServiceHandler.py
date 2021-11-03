from WinrmService import WinrmService

START_SERVICE = "start-service -name {0}"
STOP_SERVICE = "stop-service -name {0} -force"
RESTART_SERVICE = "restart-service -name {0} -force"
GET_SERVICE_STATUS = "(get-service -name {0}).Status"

class ServiceHandler(WinrmService):
    def startService(self,serviceName:str):
        self.runCommand(START_SERVICE.format(serviceName))
    def stopService(self,serviceName:str):
        self.runCommand(STOP_SERVICE.format(serviceName))
    def restartService(self,serviceName:str):
        self.runCommand(RESTART_SERVICE.format(serviceName))
    def getServiceStatus(self,serviceName:str):
        return self.runCommand(GET_SERVICE_STATUS.format(serviceName))
    def isServiceUp(self,serviceName:str):
        if(self.getServiceStatus(serviceName).find("Running")!=-1):
            return True
        else:
            return False
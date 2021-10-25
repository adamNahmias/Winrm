from RemoteMachine import RemoteMachine
import subprocess
from  subprocess import CompletedProcess

TEST_CONNECTION = "Test-WSMan -ComputerName {ComputerName}"
IPCONFIG_COMMAND = "ipconfig /all"

class WinrmService():
    def __init__(self,Ip:str,user:str,password:str):
        self._machineDetails:RemoteMachine = RemoteMachine(IpAddr=Ip,userName=user,password=password)
    def machineDetails(self):
        return self._machineDetails

    def TestConnection(self):
        result:CompletedProcess = self.run(cmd=TEST_CONNECTION.format(ComputerName =self._machineDetails.IpAddr))
        return result
    def ipconfig(self):
        result:CompletedProcess = self.run(cmd=IPCONFIG_COMMAND)
        return result

    def run(self, cmd):
        completed:CompletedProcess = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
        return completed

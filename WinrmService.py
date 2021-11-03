from RemoteMachine import RemoteMachine
import subprocess
from  subprocess import CompletedProcess

TEST_CONNECTION = "Test-WSMan -ComputerName {ComputerName}"
IPCONFIG_COMMAND = "ipconfig /all"
SESSION_OPTION= "$options = New-PSSessionOption -SkipCNCheck -SkipCACheck"
INVOKE_COMMAND = "{creds};{session_options}; Invoke-Command -ComputerName {IP} -Credential $credObject -ScriptBlock {{{cmd}}} -UseSSL -SessionOption $options"
CREDENIALS_BODY = "$credObject = New-Object System.Management.Automation.PSCredential ('{username}', (ConvertTo-SecureString '{password}' -AsPlainText -Force))"

class WinrmService():
    def __init__(self,remoteMachine:RemoteMachine):
        self._machineDetails:RemoteMachine = remoteMachine
        self._creds: str = CREDENIALS_BODY.format(username=self._machineDetails.userName,password=self._machineDetails.password)

    def TestConnection(self):
        result:str=self._run(cmd=TEST_CONNECTION.format(ComputerName =self._machineDetails.IpAddr))
        if(result.find("wsmid")!=-1):
            return True
        else:
            return False

    def runCommand(self,command):
        return self._run(INVOKE_COMMAND.format(creds=self._creds,session_options=SESSION_OPTION,cmd=command,IP=self._machineDetails.IpAddr))

    def _run(self, cmd):
        print("run command : " + cmd)
        result:CompletedProcess = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
        try:
            result.check_returncode()
            return result.stdout.decode()
        except:
            print(result.stderr.decode())
            return result.stderr.decode()
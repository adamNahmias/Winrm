from WinrmService import WinrmService
import os
UPLOAD_FILE= "{session};Copy-Item –Path '{srcPath}' –Destination '{dstPath}' –ToSession ($session)"
DOWNLOAD_FILE = "{session};Copy-Item –Path '{srcPath}' –Destination '{dstPath}' –FromSession ($session)"
SESSION = "{creds};{session_options};$session = New-PSSession –ComputerName {IP} -Credential $credObject -SessionOption $session_options -UseSSL"
SESSION_OPTION= "$session_options = New-PSSessionOption -SkipCNCheck -SkipCACheck"
TEST_PATH =  "Test-Path -Path {0}"

class FileService(WinrmService):
    def uploadFile(self,srcPath:str,dstPath:str):
        session = SESSION.format(creds=self._creds,session_options=SESSION_OPTION,IP=self._machineDetails.IpAddr)
        self._run(UPLOAD_FILE.format(session=session,srcPath=srcPath,dstPath=dstPath))
    def downloadFile(self,srcPath:str,dstPath:str):
        session = SESSION.format(creds=self._creds,session_options=SESSION_OPTION,IP=self._machineDetails.IpAddr)
        self._run(DOWNLOAD_FILE.format(session=session,srcPath=srcPath,dstPath=dstPath))
    def isFileExist(self,filePath:str):
        return os.path.isfile(filePath)
    def isFileExistOnRemoteMachine(self,filePath:str):
        if((self.runCommand(TEST_PATH.format(filePath)).find("True")!=-1)):
            return True
        else:
            return False


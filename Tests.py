from unittest import TestCase
from WinrmService import WinrmService
from RemoteMachine import  RemoteMachine
from ServiceHandler import  ServiceHandler
from FileService import  FileService
# Press the green button in the gutter to run the script.
remote_machine: RemoteMachine = RemoteMachine(IpAddr="192.168.194.130", userName="administrator", password="Deep123!")
winrm_svc: WinrmService = WinrmService(remote_machine)
srvHandler:ServiceHandler = ServiceHandler(remote_machine)
file_svc:FileService = FileService(remote_machine)

class Test(TestCase):
    def test_connection(self):
        assert winrm_svc.TestConnection()==True
    def test_runCommand(self):
        out:str = winrm_svc.runCommand("ipconfig")
        assert out.find("Windows IP Configuration")!=-1
    def test_stopService(self):
        srvHandler.startService("AppReadiness")
        assert srvHandler.isServiceUp("AppReadiness") ==True
        srvHandler.stopService("AppReadiness")
        assert srvHandler.isServiceUp("AppReadiness") ==False
    def test_startService(self):
        srvHandler.stopService("AppReadiness")
        assert srvHandler.isServiceUp("AppReadiness") ==False
        srvHandler.startService("AppReadiness")
        assert srvHandler.isServiceUp("AppReadiness") ==True

    def test_uploadFile(self):
        file_svc.uploadFile("C:\\Temp\\adam.txt", "C:\\adam.txt")
        assert file_svc.isFileExistOnRemoteMachine("C:\\adam.txt") ==True
    def test_downloadFile(self):
        file_svc.downloadFile("C:\\david.txt", "c:\\Temp\\david.txt")
        assert file_svc.isFileExist("c:\\Temp\\david.txt") ==True


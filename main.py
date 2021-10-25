from WinrmService import WinrmService
from subprocess import CompletedProcess
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    winrm_svc:WinrmService  = WinrmService(Ip="127.0.0.1",user="caadmin",password="YSaWKZ0Hf_yA4j7p")
    result:CompletedProcess = winrm_svc.ipconfig()
    print(result.stdout)
    print(result.args)

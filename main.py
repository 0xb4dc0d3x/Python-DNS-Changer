import ctypes, sys, os , types, traceback

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
#Change the Change_me from ipconfig in cmd
    adp = "Change_me" 


    print("DONT FORGET TO RUN AS ADMINISTRATOR!!!")
    b = (input("keys:\n"
              "enter 0 to exit \n"
              "enter 1 for shecan DNS \n"
              "enter 2 for Google DNS \n"
              "enter 3 for Cloudflare DNS \n"
              "enter 4 for reset DNS to default \n"
              ":-->>"))
    a = int(b)

    if a == 1 :
        os.system('netsh interface ip set dns name=' + adp + ' source="static" address="178.22.122.100"')
        os.system('netsh interface ip add dns name=' + adp + '  addr="185.51.200.2" index=2')

    elif a == 2 :
        os.system('netsh interface ip set dns name=' + adp + ' source="static" address="8.8.8.8"')
        os.system('netsh interface ip add dns name=' + adp + ' addr="8.8.4.4" index=2')
    
    elif a == 3 :
        os.system('netsh interface ip set dns name=' + adp + ' source="static" address="1.1.1.1"')
        os.system('netsh interface ip add dns name=' + adp + ' addr="1.0.0.1" index=2')

    elif a == 4 :
        os.system('netsh interface ip set dns name=' + adp + ' source=dhcp')

    elif a == 0 :
        os.system('echo exit | nslookup')


    print("dns changed succfully")
    os.system('echo exit | nslookup')
    input('Press ENTER to exit')

else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
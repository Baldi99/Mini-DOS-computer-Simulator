import subprocess
import time
start=2
print('Checking RAM.....')
time.sleep(5)
print('5MB OK')
time.sleep(2)
print('Checking CPU.....')
time.sleep(5)
print('Intel(R)8088')
time.sleep(2)
print('Checking Drive and Disk.....')
print('')
print('Drive        Disk       State')
time.sleep(10)
print('Drive A   Floppy  Disk   OK')
time.sleep(2)
print('Drive C    Hard Disk     OK')
print('')
time.sleep(5)
time.sleep(2)
a=input('Go to BIOS?(Y/N)')
if a =='Y'or 'y':
    print('ERROR')
subprocess.run('cls', shell=True)
if start==1:
    while True:
        input('Systeam is ERROR!')
print('Starting DOS.....')
print('(Time will be long)')
time.sleep(25)
print('PY-DOS version 1.0 Operating interface Beta')
time.sleep(1.5)
while True:
    cmd=input('C:>')
    if cmd =='tel 16300 telnet':
        print('Checking .')
        time.sleep(10)
        print('OK')
        time.sleep(3)
        print('calling 16300...')
        time.sleep(20)
        print('Done!Telnet is ')
        net=1
    elif cmd == 'format c:'or 'format C:':
        print('Wharing!Your data will be lose!')
        yn=input('format drive C:?(Y/N)')
        if yn=='Y'or yn=='y':
            print('Formating.....')
            print('0%')
            time.sleep(15)
            print('15%')
            time.sleep(15)
            print('20%')
            time.sleep(15)
            print('35%')
            time.sleep(15)
            print('40%')
            time.sleep(15)
            print('65%')
            time.sleep(15)
            print('70%')
            time.sleep(15)
            print('85%')
            time.sleep(15)
            print('95%')
            time.sleep(15)
            print('99%')
            time.sleep(25)
            print('Done!')
            start=1
    else:
        print('What is this')


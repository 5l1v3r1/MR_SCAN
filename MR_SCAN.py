import sys, os, subprocess
BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'
full_ip = ''
dot = '.'
ip_base = '192.168'
ip_sub = '0'
ip_sub2 = '0'
#schéma de montage ip = ip_base + ip_sub + ip_sub2 , ne pas oublier le 'dot' pour faire le point de séparation !
os.system('clear')
def banner():
    """ Create a very cool banner ! """
    spaces = " " * 76
    sys.stdout.write(GREEN + spaces + """
    ███▄ ▄███▓ ██▀███    ██████  ▄████▄   ▄▄▄       ███▄    █
    ▓██▒▀█▀ ██▒▓██ ▒ ██▒▒██    ▒ ▒██▀ ▀█  ▒████▄     ██ ▀█   █
    ▓██    ▓██░▓██ ░▄█ ▒░ ▓██▄   ▒▓█    ▄ ▒██  ▀█▄  ▓██  ▀█ ██▒
    ▒██    ▒██ ▒██▀▀█▄    ▒   ██▒▒▓▓▄ ▄██▒░██▄▄▄▄██ ▓██▒  ▐▌██▒
    ▒██▒   ░██▒░██▓ ▒██▒▒██████▒▒▒ ▓███▀ ░ ▓█   ▓██▒▒██░   ▓██░
    ░ ▒░   ░  ░░ ▒▓ ░▒▓░▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒
    ░  ░      ░  ░▒ ░ ▒░░ ░▒  ░ ░  ░  ▒     ▒   ▒▒ ░░ ░░   ░ ▒░
    ░      ░     ░░   ░ ░  ░  ░  ░          ░   ▒      ░   ░ ░
          ░      ░           ░  ░ ░            ░  ░         ░
                                ░
    """ + RED + """                                                    (By b3rt1ng)""" + '\n')
banner()

def mout_ip():
    """ this function is made to mount the different part of the ip adress """
    global ip_base, ip_sub, ip_sub2, full_ip
    full_ip = ip_base+dot+ip_sub+dot+ip_sub2

def scan():
    """ this function do a ping request on the full ip (which will be made on mount_ip()) and tell if the ip is reachable, if not, it will pass to the next ip """
    mout_ip()
    global full_ip
    try:
        print('Scanning', full_ip, end="\r")
        subprocess.check_output(["ping", "-c", "1", full_ip])
        sys.stdout.write(GREEN + '[+] '); sys.stdout.write(YELLOW + full_ip); sys.stdout.write(WHITE + ' is reachable' + '\n')
        next_ip()
    except subprocess.CalledProcessError: #if the ping failed
        next_ip()

def next_ip():
    """ this function set the ip address to the next one by converting the str to int then make it back as an str """
    global ip_sub, ip_sub2, full_ip
    ip_sub2 = (int(ip_sub2) + 1)
    ip_sub2 = str(ip_sub2)
    if ip_sub2 is '255':
        ip_sub = int(ip_sub) + 1
        ip_sub = str(ip_sub)
        ip_sub2 = '0'
    if full_ip is '192.168.255.255':
        scan_finished()
    scan()

def scan_finished():
    """ this function make the end message appear (this is just to make the ping end because the full ping process is verr long) """
    sys.stdout.write(YELLOW + '[?] '); sys.stdout.write(YELLOW + full_ip); sys.stdout.write(WHITE + ' all the possible ips have been scanned' + '\n')



scan()

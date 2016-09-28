import os,time,sys
import subprocess

bright_level = 1.5

pid = ''
word = ''
display = ''

def attach():
    sp = subprocess.Popen(['strace', '-p'+pid,'-s9999','-e','write'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print sp.stderr.readline()

    for line in iter(sp.stderr.readline, ''):
        if(filter(line) or taskend(line)):
            notify()
        if not line: break

def filter(line):
    if word in line:
        print line
        return True
    return False

def taskend(line):
    if '+++ exited with' in line:
        return True
    return False

def screen_flicker(brightness,interval):
    subprocess.Popen(('xrandr --output '+display+' --brightness '+str(brightness)).split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(interval)

def notify():
    for i in xrange(6):
        time.sleep(0.1)
        print '\a'
        
    
    print '************************RETARD ALERT************************'
    try:
        screen_flicker(bright_level,0.1)
        screen_flicker(1.0,0.3)
    finally:
        screen_flicker(1.0,0)

def init_setting():
    xrandr_p = subprocess.Popen('xrandr -q'.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    for line in iter(xrandr_p.stdout.readline, ''):
        if ' connected' in line:
            global display
            display = line.split()[0]
            return
        if not line: break

def main():
    init_setting()
    global pid
    global word
    pid = sys.argv[1]
    word = sys.argv[2]
    attach()

if __name__ == "__main__":
    main()

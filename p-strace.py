import os,time
import subprocess

def attach(pid,word):
    sp = subprocess.Popen(['strace', '-p'+pid,'-s9999','-e','write'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    for line in iter(sp.stderr.readline, ''):
        if(filter(line,word)):
            notify()
        if not line: break

def filter(line,sensitive_word):
    if sensitive_word in line:
        return True
    return False

def notify():
    for i in xrange(6):
        time.sleep(0.1)
        print '************************RETARD ALERT************************\a'
    print '--Alert Ended--'

def main():
    pid = raw_input('please input pid:')
    word = raw_input('please input sensitive word:')
    attach(pid,word)

if __name__ == "__main__":
    main()

from ftplib import FTP, error_perm
from multiprocessing import Process
from getpass import getpass


def upload(ftp, *filenames):
    for filename in filenames:
        ftp.storbinary('STOR ' + filename, open(filename, "rb"), 1024)

def connection():
    while True:
        passwd = getpass('Password: ')
        try:
            ftp = FTP('ftp-mkusm.alwaysdata.net', 'mkusm', passwd)
        except error_perm:
            choice = raw_input("Wrong password! Try again? [y/N]").lower()
            if choice == 'y':
                continue
            else:
                quit()
        break
    print "Connected"
    return ftp

def change_directory(ftp):
    if ftp.pwd() == '/':
        ftp.cwd('www')
    else:
        raise Exception('Unknown path!')

def run(ftp):
    p = Process(target=upload, args=(ftp, 'index.html', 'css/main.css',
        'images/me_smaller.jpg'))
    print 'Sending files...'
    p.start()
    p.join(10)
    if p.is_alive():
        ftp.close()
        p.terminate()
        p.join()
        print "Failed! Timeout: over 10 sec."
    else:
        ftp.quit()
        print "Success!"

if __name__ == "__main__":
    ftp = connection()
    change_directory(ftp)
    run(ftp)

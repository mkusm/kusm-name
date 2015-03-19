from ftplib import FTP
import getpass

def upload(ftp, *filenames):
    for filename in filenames:
        ftp.storbinary('STOR ' + filename, open(filename, "rb"), 1024)

def connection():
    passwd = getpass.getpass('Password: ')
    ftp = FTP('ftp-mkusm.alwaysdata.net', 'mkusm', passwd)
    return ftp

if __name__ == "__main__":
    ftp = connection()
    if ftp.pwd() == '/':
        ftp.cwd('www')
    upload(ftp, 'index.html', 'css/main.css', 'images/me_smaller.jpg')

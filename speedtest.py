import os
import re
import subprocess
import time

# receive data from stdout
response = subprocess.Popen('speedtest-cli --simple', shell=True, stdout=subprocess.PIPE).stdout.read()

ping = re.findall('Ping:\s(.*?)\s', response, re.MULTILINE)
download = re.findall('Download:\s(.*?)\s', response, re.MULTILINE)
upload = re.findall('Upload:\s(.*?)\s', response, re.MULTILINE)

# Replace commas with periods
ping[0] = ping[0].replace(',', '.')
download[0] = download[0].replace(',', '.')
upload[0] = upload[0].replace(',', '.')

# Try catch writes to SMB directory
try:
    if os.stat('/samba/data/speedtest.csv').st_size == 0:
        print 'Date,Time,Ping (ms),Download (Mbit/s),Upload (Mbit/s)'
except:
    pass

# time formatting
print '{},{},{},{},{}'.format(time.strftime('%m/%d/%y'), time.strftime('%H:%M'), ping[0], download[0], upload[0])

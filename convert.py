#!/usr/bin/python
import os
import subprocess
import threading

new_books='/home/jacombo/Dokumenty/Knihy/New/'
converted_books='/home/jacombo/Dokumenty/Knihy/Done/'
threads = []

def convert(file):
    docs = file.split('.')
    #command = '/usr/bin/ebook-convert ' + new_books+file + converted_books + docs[0] + '.mobi' + ' --input-encoding windows-1252'
    command = ("/usr/bin/ebook-convert '%s%s' '%s%s.mobi'") % (new_books,file,converted_books,docs[0])
    print command
    #subprocess.call(['ebook-convert',  new_books+file , converted_books + docs[0] + '.mobi','--input-encoding', 'windows-1250'])
    #subprocess.call(['ebook-convert',  new_books+file , converted_books + docs[0] + '.mobi','--input-encoding', 'windows-1252'])
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True) 
    for line in iter(process.stdout.readline, b''):
        if len(line.strip()) > 0:        
            print line

for file in os.listdir(new_books):
    convert(file)             
"""
for file in os.listdir(new_books):
    t = threading.Thread(target=convert, args=(file,))
    threads.append(t)
    t.start()

# Wait for all threads to complete
for t in threads:
    t.join()
print "Exiting Main Thread"
"""

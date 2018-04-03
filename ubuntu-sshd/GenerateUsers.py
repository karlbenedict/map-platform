#!/usr/bin/env python3

import random
import crypt
import os

users = []
words = list(open('words.txt'))[1:-1]

user = {}
user['name'] = "root"
user['pw'] = random.choice(words).strip()+"-"+random.choice(words).strip()+"-"+random.choice(words).strip()
user['pwhash'] = crypt.crypt(user['pw'], crypt.mksalt(crypt.METHOD_SHA512))
users.append(user)


for i in range(0,100):
    user = {}
    user['name'] = "user" + "{0:0>3}".format(i)
    user['pw'] = random.choice(words).strip()+"-"+random.choice(words).strip()+"-"+random.choice(words).strip()
    user['pwhash'] = crypt.crypt(user['pw'], crypt.mksalt(crypt.METHOD_SHA512))
    print(user['name'] + ", " + user['pw']+ ", " + user['pwhash'])
    command = "useradd -p \'"+user['pwhash']+"\' -G students --base-dir /opt/geoserver/data_dir/general --create-home "+user['name']
    print(command)
    os.system(command)
    users.append(user)

#print(users)
with open('users.txt', 'w') as f:
    f.write('username,password,password_hashed\n')
    for user in users:
        f.write(user['name'] + ',' + user['pw'] + ','+ user['pwhash'] + '\n')
    
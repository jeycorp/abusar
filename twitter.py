# !/usr/bin/env python

import tweepy, time, json
import colorama

# enter the corresponding information from your Twitter application:
CONSUMER_KEY = ''  # keep the quotes, replace this with your consumer key
CONSUMER_SECRET = ''  # keep the quotes, replace this with your consumer secret key
ACCESS_KEY = ''  # keep the quotes, replace this with your access token
ACCESS_SECRET = ''  # keep the quotes, replace this with your access token secret

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
API = tweepy.API(auth)

try:
    filepath = open('./profiles.txt', 'r')
    with filepath as fp:
        line = fp.readline()
        cnt = 1
        while line:
            line = fp.readline()
            line = line.strip()
            cnt += 1
            try:
                denuncia = API.report_spam(screen_name=line[20:])
                print ('['+colorama.Fore.RED+'Denunciado como SPAM'+colorama.Fore.RESET+'] '+line)
            except Exception as e:
                print ('[' + colorama.Fore.GREEN + 'PERFIL REMOVIDO' + colorama.Fore.RESET + '] ' + line)
                pass
finally:
    filepath.close()

filepath.close()
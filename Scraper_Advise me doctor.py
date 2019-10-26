# -*- coding: UTF-8 -*-

# Parsing Advise me doctor

import urllib.request
from os.path import join
import time
import wget
import os
import requests



#radiorus_file = open('C:\\firefox_download\\radiorus.xml', encoding='utf-8')
radiorus_file = urllib.request.urlopen("http://www.radiorus.ru/brand/rss/57079/")
for line in radiorus_file:
    line = line.decode("utf-8")
    #print (type(line))
    if "title" in line:
        left_title = line.find('<title>')
        right_title = line.rfind('</title>')
        name_title = line[left_title + 1:right_title].replace('title>','').replace('?','').replace('&quot;','').replace('!','').replace(':','').replace(';nbsp;','')
          
    if "pubDate" in line:
        left_date = line.find(',')
        right_date = line.find(':')
        name_date = line[left_date + 1:right_date-2]#.replace(' ','')
        str_list = list(map(str, name_date.split()))
        str_list[0], str_list[2] = str_list[2], str_list[0]
        int_list = "_".join(str(x) for x in str_list)
      
    if "url=" in line:
        left_quote = line.find('"')
        right_quote = line.rfind('" length=')
        link_mp3 = line[left_quote + 1:right_quote].replace('"/>','')
        
        
        #path = 'D:\\Learn\\Health\\Doctor_advise\\'
        path = 'I:\\testdata\\advise_me_doctor\\'
        fullpath = ( path + int_list + "_" + name_title + ".mp3")        
        r = requests.get(link_mp3, stream = True)
        with open(fullpath, 'wb') as f:
            for ch in r:
                f.write(ch)
        
    
        '''
        f = open(join(r"J:\Sergo\Programming\Py\test\streets", int_list + "_" + name_title + ".txt"), "a", encoding = "utf-8")
        print(link_mp3, file=f)
        f.close()   
        '''
        '''
        time.time.sleep(10)
        path = 'D:\\Learn\\Health\\Doctor_advise\\'
        os.system(f"""wget -c --read-timeout=5 --tries=0 "{url}"""")
        '''
        
        
        '''
        fullpath = ( path + int_list + "_" + name_title + ".mp3")  
        wget.download (link_mp3, fullpath)
        '''
        
        '''
        path = 'D:\\Learn\\Health\\Doctor_advise\\'
        fullpath = ( path + int_list + "_" + name_title + ".mp3")
        time.time.sleep(10)
        urllib.request.urlretrieve(link_mp3, fullpath)
        '''
        
        '''
        f = open(join(r"J:\Sergo\Programming\Py\test\streets", int_list + "_" + name_title + ".txt"), "a", encoding = "utf-8")
        print(link_mp3, file=f)
        f.close()                 
        '''             
        




        
              
        
         
        
    
    




        
    
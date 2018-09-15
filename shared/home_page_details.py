#!/usr/bin/env python3

# specific dependency modules next
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

#system level imports first
import sys
import os
import io
import json
#global package imports next
import requests
import gzip
from datetime import datetime

# input_link="https://en.wikipedia.org/wiki/Connaissance_des_Temps"
agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
# link = requests.get(input_link,headers=agent)
# def wiki_journal(link):
# print(soup)
# print("------------------------------------------------")
def archive_link(input_link):
    journal={}
    Journal_link=""
    online_archive=""
    online_access=""
    try:
        for a in input_link.find_all('a'):
            # print(a.get_text())
            if "Journal homepage" in a.get_text():
                journal_link=a['href']
                # print(journal_link)

            if "Online archive" in a.get_text():
                online_archive=a['href']

            if "Online access" in a.get_text():
                online_access=a['href']

        journal['journal_link']=journal_link
        journal['online_archive']=online_archive
        journal['online_access']=online_access
        return journal
    except:
        tr=open("error.txt","a")
        tr.write(input_link, "\n")
        print("error")


def wiki_journal(input_link):
    journal_list=[]
    journal={}
    Discipline=""
    Language=""
    Edited_by=""
    Publication_history=""
    Publisher=""
    Open_access=""
    Impact_factor=""
    ISO=""
    CODEN=""
    ISSN=""

    link = requests.get(input_link,headers=agent)
    soup = BeautifulSoup(link.text,'lxml')
    archive_details=archive_link(soup)
    # print(soup)
    try:
        for tbody in soup.find_all('tbody'):
            for tr in tbody.find_all('tr'):
                # print(th)
                for th in tr.find_all('th'):
                    # print(tr)

                    if "Discipline" in th.get_text():
                        Discipline=tr.find('td').get_text().strip()
                        # print(Discipline)

                    if "Language" in th.get_text():
                        Language=tr.find('td').get_text().strip()

                    if "Edited" in th.get_text():
                        Edited_by=tr.find('td').get_text().strip()


                    if "Publication history" in th.get_text():
                        Publication_history=tr.find('td').get_text().strip()

                    if "Publisher" in th.get_text():
                        Publisher=tr.find('td').get_text().strip()

                    if "Open access" in th.get_text():
                        Open_access=tr.find('td').get_text().strip()

                    if "Impact factor" in th.get_text():
                        Impact_factor=tr.find('td').get_text().strip()
                        # print(Impact_factor)

                    if "ISO" in th.get_text():
                        if tr.find('td'):
                            ISO=tr.find('td').get_text().strip()

                    if "CODEN" in th.get_text():
                        CODEN=tr.find('td').get_text().strip()

                    if "ISSN" in th.get_text():
                        ISSN=tr.find('td').get_text().strip()


        journal['journal_name']=Discipline
        journal['language']=Language
        journal['edited_by']=Edited_by
        journal['publication_history']=Publication_history
        journal['publisher']=Publisher
        journal['open_access']=Open_access
        journal['impact_factor']=Impact_factor
        journal['iso']=ISO
        journal['coden']=CODEN
        journal['issn']=ISSN
        journal['journal_link']=archive_details['journal_link']
        journal['online_archive']=archive_details['online_archive']
        journal['online_access']=archive_details['online_access']
        # print(journal)
        journal_list.append(journal)
        print(journal_list)
        name= input_link.split('wiki/')
        na=name[1]
        names="out_files_wiki/{}.json".format(na)
        tr=open(names,"a")
        json.dump(journal_list,tr)
        # print("working")
        print("-----------------------------")
    #
    except:
        tr=open("error.txt","a")
        tr.write(input_link, "\n")
        print("error")


if __name__ == "__main__":
    '''
    This main function used to collect the infomation on journal article using class functions
    to generate dictionary with our disired fields as keys and bs4 used to parse this information
        '''
    # input_link="https://en.wikipedia.org/wiki/Nature_(journal)"

    input_link=sys.argv[1]
    print(input_link, "\n")
    wiki_journal(input_link)

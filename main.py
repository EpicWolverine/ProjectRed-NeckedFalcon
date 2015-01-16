#!/usr/bin/python -tt
# Copyright 2014 Brendan Ferracciolo
# 
# This file is part of Project Red-Necked Falcon.
#
# Project Red-Necked Falcon is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Project Red-Necked Falcon is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Project Red-Necked Falcon. If not, see <http://www.gnu.org/licenses/>.

"""Project Red-Necked Falcon v0.2
https://github.com/EpicWolverine/ProjectRed-NeckedFalcon

A Python script that collects data on Steam users' games and playing history. Created as part of a school project.
The Red-Necked Falcon is a falcon with rusty red feathers on the back of its head and neck found in India and sub-Saharen Africa.

--- Usage ---
Project Red-Necked Falcon requires:
    * Python 2.7.3. While Python 2.7.3 is the only version of Python Project Red-Necked Falcon officially supports, it may or may not work in older or newer versions of Python.
    * A Steam Web API key. You can obtain one at http://steamcommunity.com/dev. This key must be placed in a text file called apikey.txt in the same folder as main.py.
    * Smily Barry's SteamAPI and its dependancies.
Simply run main.py to generate an output file with 100 Steam users. 

--- License ---
Project Red-Necked Falcon is licensed under the GNU General Public License V3. A full copy of the license can be found in the LICENSE file in this repository or at http://www.gnu.org/licenses/.
Licence tl;dr: http://www.tldrlegal.com/license/gnu-general-public-license-v3-(gpl-3)
"""

import random       # used to generate random Steam User ID
import steamapi     # Smiley Barry's library for accessing the Steam Web API
import sys          # for various I/O functions
import time         # datetime support

versionnumber="0.2"
myapikey=open("apikey.txt").read() # retrieve API key from apikey.txt

steamapi.core.APIConnection(api_key=myapikey) # initialize API

def main():
    print "Project Red-Necked Falcon v" + versionnumber
    print "Collecting data in 5 seconds."
    time.sleep(5)
    
    time.clock() #Start timer
        
    outputfile = open("output.csv", "w")
    outputfile.write("Generated using Project Red-Necked Falcon v" + versionnumber + ".\n")
    outputfile.write("Note: All playtimes are in minutes.\n")
    outputfile.write("Steam User ID,Total Play Time Across All Games,Total Games Owned (including free games),Total Games Played (for > 30 minutes),Most Played Game in the Last 2 Weeks,Time Spent in Most Played Game in the Last 2 Weeks,Active (played a game in the last 2 weeks),Accessed Timestamp\n")
    
    attemptnumber = 0
    numdata = 0
    while numdata < 100:
        attemptnumber += 1
        try:
            randomuserid = "76561198" + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
            print "Attempt #" + str(attemptnumber) + ": Trying " + randomuserid
            datarecord = GetUserInfo(randomuserid)
            outputfile.write(datarecord + "\n")
            print "Succeeded!"
            print datarecord
            numdata += 1
        except Exception as e:
            print "Failed!"
            print e
            pass
    
    outputfile.write("Attempts: " + str(attemptnumber) + "\n")
    print "Attempts: " + str(attemptnumber)
    outputfile.write("Data Points: " + str(numdata) + "\n")
    print "Data Points: " + str(numdata)
    
    outputfile.write("Elapsed time: " + str(time.clock()) + " seconds." + "\n")
    print "Elapsed time: " + str(time.clock()) + " seconds." #Stop timer and print result
    
    outputfile.close()

def GetUserInfo(SteamUserID):
    outputstring = ""
    
    # Initialize user
    currentuser = steamapi.user.SteamUser(SteamUserID)
    outputstring += SteamUserID + ","
        
    # User's Profile Name
    #print "Profile Name: " + currentuser.name
    
    # Note to Self
    #print "Note: All playtimes are in minutes."
    
    # Total Play Time Across All Games
    totalplaytime = 0
    for game in currentuser.games:
        totalplaytime += game.playtime_forever
    #print "Total Play Time Across All Games: " + str(totalplaytime)
    outputstring += str(totalplaytime) + ","
    
    # Total Games Owned
    #print "Total Games Owned: " + str(len(currentuser.games))
    numbergamesowned = len(currentuser.games)
    if numbergamesowned == 0:
        raise Exception("Junk account (owns 0 games)")
    outputstring += str(numbergamesowned) + ","
    
    # Total Games Owned That Have Been Played for > 30 Minutes
    playedgames = 0
    for game in currentuser.games:
        if game.playtime_forever > 30:
            playedgames += 1
    #print "Total Games Played (for > 30 minutes): " + str(playedgames)
    outputstring += str(playedgames) + ","
    
    # Recently Played
    #print "Recently Played (last 2 weeks): "
    #print currentuser.recently_played
    #print currentuser.recently_played[0].playtime_2weeks
    #print currentuser.recently_played[0].playtime_forever
    #for game in currentuser.recently_played:
        #print "- " + str(game)
        #print "  2 weeks: " + str(game.playtime_2weeks)
        #print "  Forever: " + str(game.playtime_forever)
    try:
        outputstring += currentuser.recently_played[0].name.encode('ascii', 'ignore') + " (" + str(currentuser.recently_played[0].appid) + "),"
        outputstring += str(currentuser.recently_played[0].playtime_2weeks) + ","
    except IndexError:
        outputstring += ",0,"
    
    # Account Active?
    useractive = False
    if len(currentuser.recently_played) > 0:
        useractive = True
    #print "Active?: " + str(useractive)
    outputstring += str(useractive) + ","
    
    # Timestamp
    #print "Date Accessed: " + time.strftime("%Y/%m/%d %H:%M:%S")
    outputstring += time.strftime("%Y/%m/%d %H:%M:%S")
    
    return outputstring
	
	
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    #GetUserInfo(sys.argv[1])
    main()

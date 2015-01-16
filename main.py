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

"""Project Red-Necked Falcon v0.1"""

import random       # used to generate random Steam User ID
import steamapi     # Smiley Barry's library for accessing the Steam Web API
import sys          # for various I/O functions
import time         # datetime support

myapikey=open("apikey.txt").read() # retrieve API key from apikey.txt

steamapi.core.APIConnection(api_key=myapikey) # initialize API

def main():
    print "Project Red-Necked Falcon v0.1"
    print "Collecting data in 5 seconds."
    time.sleep(5)
    
    time.clock() #Start timer
        
    outputfile = open("output.csv", "w")
    outputfile.write("Generated using Project Red-Necked Falcon v0.1.\n")
    outputfile.write("Note: All playtimes are in minutes.\n")
    outputfile.write("Steam User ID,Total Play Time Across All Games,Total Games Owned (including free games),Total Games Played (for > 30 minutes),Most Played Game in the Last 2 Weeks,Time Spent in Most Played Game in the Last 2 Weeks,Active (played a game in the last 2 weeks),Accessed Timestamp\n")
    
    attemptnumber = 0
    numdata = 0
    while numdata < 100:
        attemptnumber += 1
        try:
            randomuserid = "76561198" + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
            print "Trying " + randomuserid
            datarecord = GetUserInfo(randomuserid)
            outputfile.write(datarecord + "\n")
            print "Succeeded!"
            print datarecord
            numdata += 1
        except Exception as e:
            print "Failed!"
            print e
            pass
    
    print "Attempts: " + str(attemptnumber)
    print "Data Points: " + str(numdata)
    outputfile.close()
    
    print "Elapsed time: " + str(time.clock()) + " seconds." #Stop timer and print result

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
    outputstring += str(len(currentuser.games)) + ","
    
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
        outputstring += currentuser.recently_played[0].name + " (" + str(currentuser.recently_played[0].appid) + "),"
        outputstring += str(currentuser.recently_played[0].playtime_2weeks) + ","
    except IndexError:
        outputstring += ",,"
    
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

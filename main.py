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

"""<insert man page here>"""

import steamapi     # Smiley Barry's library for accessing the Steam Web API
import sys          # for various I/O functions
import time         # datetime support

myapikey=open("apikey.txt").read() #change this to retrieve api key from a text file later

def main(SteamUserID):
    # Timestamp
    print "Date Accessed: " + time.strftime("%Y/%m/%d %H:%M:%S")
    
    # Initialize user
    steamapi.core.APIConnection(api_key=myapikey)
    currentuser = steamapi.user.SteamUser(SteamUserID)
    
    # User's Profile Name
    print "Profile Name: " + currentuser.name
    
    # Note to Self
    print "Note: All playtimes are in minutes."
    
    # Total Play Time Across All Games
    totalplaytime = 0
    for game in currentuser.games:
        totalplaytime += game.playtime_forever
    print "Total Play Time Across All Games: " + str(totalplaytime)
    
    # Total Games Owned
    print "Total Games Owned: " + str(len(currentuser.games))
    
    # Total Games Owned That Have Been Played for > 30 Minutes
    playedgames = 0
    for game in currentuser.games:
        if game.playtime_forever > 30:
            playedgames += 1
    print "Total Games Played (for > 30 minutes): " + str(playedgames)
    
    # Recently Played
    print "Recently Played (last 2 weeks): "
    #print currentuser.recently_played
    for game in currentuser.recently_played:
        print "- " + str(game)
        print "  2 weeks: " + str(game.playtime_2weeks)
        print "  Forever: " + str(game.playtime_forever)
    #print currentuser.recently_played[0].playtime_2weeks
    #print currentuser.recently_played[0].playtime_forever
    
    # Account Active?
    useractive = False
    if len(currentuser.recently_played) > 0:
        useractive = True
    print "Active?: " + str(useractive)
	
	
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main(sys.argv[1])

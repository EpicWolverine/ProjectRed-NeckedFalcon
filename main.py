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

import steamapi

myapikey=open("apikey.txt").read() #change this to retrieve api key from a text file later

def main():
    steamapi.core.APIConnection(api_key=myapikey)
    currentuser = steamapi.user.SteamUser()
    print currentuser.recently_played
    print currentuser.recently_played[0].playtime_2weeks
    print currentuser.recently_played[0].playtime_forever
	
	
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()

from simpleMenu import simpleMenu, pause
from saveTypeMenu import saveTypeMenu
from gameConfigs import gameConfigs
from gameInfo import gameInfo
import os

workDir = os.getcwd()

configDir = workDir + '\\' +'Configs'
backupDir = workDir + '\\' +'Backups'

#loads config
#json format {
# 				gamename : path
#			 }
configs = gameConfigs('configs.json')

if( not os.path.isdir( configDir ) ):
	os.mkdir( configDir )
if( not os.path.isdir( backupDir ) ):
	os.mkdir( backupDir )

sMenu = simpleMenu('Main Menu')

def makeConfig():
	#get input from user on the name of the game
	#and the save file location
	gameName  = input( 'Game name ->' )
	pathToDir = input( 'Save Location ->' )
	#save to json
	configs.add( gameName, pathToDir )
	#add to menu
	gameBackupsDir = backupDir + '\\' + gameName
	game = gameInfo( gameName, pathToDir, gameBackupsDir )
	sMenu.menu_option_add(	saveTypeMenu_open,
							gameName,
							args=game)
	#c.menu_option_add_withArgs(	saveTypeMenu_open,
	#							[	gameName,
	#								pathToDir,
	#								configDir,
	#								workDir],
	#							gameName)

	#creates backup folder
	if( not os.path.isdir( gameBackupsDir ) ):
		os.mkdir( gameBackupsDir )
	sMenu.run = False

def deleteConfig():
	#gets input from user on what to delete
	item = input( 'Delete ->' )
	#get game name from menu names
	name = sMenu.menuOptions[ item ][ 1 ]
	#remove from json
	configs.delete( name )
	sMenu.run = False
	

def saveTypeMenu_open( data ):
	#passes data to saveTypeMenu class
	saveTypeMenu( data )

#adds items to menu that all redirect to saveTypeMenu_open function
while(True):
	if(sMenu.breaking == True):
		break

	sMenu.reset('')
	sMenu.change_back_to_outside_loop_break()
	for config in configs.file:
		#gets name from json
		name = config

		#check if it's not using internal configuration options TODO
		if ( name not in  ['configsLocation','backupsLocation'] ):
			#get name from path
			path = configs.file[ name ]
			#save data to gameInfo object
			gameBackupsDir = backupDir + '\\' + name
			game = gameInfo( name, path, gameBackupsDir )
			#add option to menu and passes gameInfo
			sMenu.menu_option_add(	saveTypeMenu_open,
									name,
									args = game)
	#add option to json and menu
	sMenu.menu_option_add( makeConfig, 'Make new config' )
	#add option from json and menu
	sMenu.menu_option_add( deleteConfig, 'Delete config' )
	#start running the menu
	#print(c.last_int())
	#pause()
	sMenu.menu_start()
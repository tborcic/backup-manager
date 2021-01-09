from simpleMenu import simpleMenu, pause
import os
import time
from distutils.dir_util import copy_tree
from pynput import keyboard

#gets current time in format
def getCurrTime():
	currTime= time.strftime( "%Y_%m_%d %H_%M_%S" )
	currTime= currTime.strip()
	return currTime

class manualSaveMenu():
	def __init__(self,data):
		#get game data as gameInfo object
		self.game = data
		#sets title to be gameName Manual
		name = self.game.name + ' Manual'
		sMenu = simpleMenu(name)
		#add all the menu option
		sMenu.menu_option_add( self.save, 'Save' )
		sMenu.menu_option_add( self.load,'Load' )
		sMenu.menu_option_add( self.openFolder, 'Open Folder' )
		sMenu.menu_option_add( self.openBackups, 'Open Backups' )
		sMenu.menu_option_add( self.hotkeySaving, 'Hotkey' )

		sMenu.menu_start()

	def backup(self, makeNote):
		#init addedpath with current time for later
		addedPath = getCurrTime()
		#init custom note in case of adding a note 
		# to the folder along with current time
		customNote = ''
		if (makeNote):
			customNote = input("Note : ")
			#if note is not empty add to addedPath
			if(customNote is not ""):
				addedPath += "-" + customNote
		#add added path to backupLocation
		backupPath = self.game.backupLocation + "\\" + addedPath
		#check if backupPath allready exists (prob not)
		if( not os.path.isdir( backupPath ) ):
			os.mkdir( backupPath )
		#copys files from save location to a new backup location
		if ( copy_tree( self.game.saveLocation, backupPath ) ):
			print( "Made backup" )

	def save( self ):
		#call backup with True so user can make a custom note
		self.backup( True )
		pause()
	
	def loadFromFiles(self, dirName, pausing = True):
		#get backup location
		backupPath = self.game.backupLocation + "\\" + dirName
		#restore from backup to save game location
		if ( copy_tree ( backupPath, self.game.saveLocation ) ):
			print( "Loaded backup: \'" + dirName +'\'' )
		if(pausing):
			pause()

	def load(self):
		#makes a menu with title gameName Load
		name = self.game.name + ' Load'
		sMenu=simpleMenu( name )

		#gets list of all the backup folders and adds it to backups
		#from oldest to newest
		backups = []
		for _, dirs ,_ in os.walk( self.game.backupLocation ):
			for directory in dirs:
				backups.append(directory)
		
		#maximum list in menu is set to 9
		#check if it's less then that and display up to that number
		max = 9
		numOfBackups = len(backups)
		if ( numOfBackups < max ):
			max = numOfBackups
		
		#loop that goes from the lenght of the backups array
		#down to that lenght reduced by the max variable
		for i in reversed( range( numOfBackups - max, numOfBackups ) ):
			sMenu.menu_option_add( self.loadFromFiles, backups[ i ], args = backups[ i ] )
		#delets the backups afther display since they are no longer needed
		del backups[:]
		#start the manual backup menu
		sMenu.menu_start()

	def loadLatest( self ):
		#gets all the backup folders and gets the newest
		backups = []
		for _, dirs, _ in os.walk( self.game.backupLocation ):
			for directory in dirs:
				backups.append( directory )
		lastIndex = len( backups )-1
		#store the newest as lastItem
		lastItem = backups[lastIndex]
		#delets the backups afther storing the name
		del backups[:]
		#loads the backup directory named lastName
		self.loadFromFiles( lastItem, pausing = False )

	def openFolder( self ):
		#opens save location
		os.startfile( self.game.saveLocation )

	def openBackups(self):
		#opens backup location
		os.startfile( self.game.backupLocation )

	def on_release( self, key ):
		#checks if f5 is released and backups the save file
		#without propting for a custom note
		if key == keyboard.Key.f5:
			self.backup( False )
		#restores the backup from the newset file
		elif key == keyboard.Key.f9:
			self.loadLatest()

	def hotkeySaving( self ):
		#starts listnening when any keyboard key gets released
		listener = keyboard.Listener(
					on_release = self.on_release)
		listener.start()
		#on pressing enter it stops the listener
		print('F5 to save, F9 to load, Press Enter while the terminal is focused to stop')
		pause( text = '' )
		listener.stop()
from simpleMenu import simpleMenu, pause
from manualSaveMenu import manualSaveMenu
from gameInfo import gameInfo

#creates a menu that seperates to openAuto and openManual
class saveTypeMenu():
	def __init__( self, data ):
		self.game=data
		sMenu=simpleMenu( self.game.name )
		sMenu.menu_option_add( self.openAuto,'AutoSave' )
		sMenu.menu_option_add( self.openManual,'ManualSave' )
		sMenu.menu_start()
	
	def openAuto( self ):
		#TODO
		print('auto not available yet')
		pause()
		pass

	def openManual( self ):
		manualSaveMenu( self.game )
		pass
# data is [	0 name of game, 
# 			1 path to game saves, 
# 			2 backups directory]
'''
self.game.name
self.game.saveLocation
self.game.backupLocation
'''
class gameInfo:
	def __init__( self, name, saveLocation, backupLocation ):
		self.name = name
		self.saveLocation = saveLocation
		self.backupLocation = backupLocation
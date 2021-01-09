from sJson import sJson

class gameConfigs:
	#for storing and writing the json object containing
	#game names and path to save locations
	def __init__( self, filename ):
		self.json = sJson()
		self.configFileLocation = filename
		self.file = self.json.read( filename )
		if(not self.file):
			self.json.makeEmpty( self.configFileLocation )
			self.file = self.json.read( filename )
		self.gameName = ''
		self.gamePath = ''

	def add( self, gamename, path ):
		self.file[ gamename ] = path
		self.json.write( self.configFileLocation, self.file )
	
	def delete( self, gamename ):
		self.file.pop( gamename )
		self.json.write( self.configFileLocation, self.file )
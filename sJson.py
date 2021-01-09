import json

class sJson:
	def __init__( self ):
		pass

	def read( self, filename ):
		# returns json object from file if possible
		try:
			with open( filename, 'r' ) as json_file:
				data = json.load( json_file )
			return data
		except Exception as e:
			print( e )
			return False

	def makeEmpty( self, filename ):
		data = {}
		self.write( filename,data )
		
	def write( self, filename, data ):
		# writes json object to file if possible
		try:
			with open( filename, 'w' ) as json_file:
				json.dump( data, json_file, indent = 4, sort_keys = True )
			return True
		except Exception as e:
			print( e )
			return False

	'''
	def getValue( self, obj, data ):
		#get value from imputed key values can be array or touple of arrays for multiple 
		#	return values
		#if it's multiple arrays, touple sugested
		returnData = []
		parsing = obj
		#check if it's a single key else processes multiple
		if ( isinstance( data, str ) ):
			return parsing[ data ]
		else:
			#value = json[1][2][3]
			#for each key or branch
			for d in data:
				temp = parsing
				#check if it's the last key value
				#because string splits into chars
				if ( isinstance( d, str ) ):
					temp = temp[ d ]
				else:
					#branch to last part of json object
					for d2 in d:
						temp = temp[ d2 ]
				returnData.append( temp )
			return tuple( returnData )

	def getValueFromFile( self, filename, data ):
		#reads file and passess it to getValue
		parsing = self.read( filename )
		return self.getValue( parsing, data )
	'''

import webapp2

class TxtHandler(webapp2.RequestHandler):
	def post(self):
		blue = False
		red = False
		yellow = False
		white = False
		body = self.request.get('Body').lower()
		self.response.headers['Content-Type'] = 'text/plain' 
		if 'blue' in body:
			blue = True
			self.response.write('Blue, reminds me of the sea.')
		elif 'red' in body:
			red = True
			self.response.write('What a fine color red is.')
		elif 'yellow' in body:
			yellow = True
			self.response.write('Yellow, like the sun.')
		elif 'white' in body:
			white = True
			self.response.write('Yarrr, that be a fine color!')
		else:
			self.response.write('Hmm, don't think I know that one.')
	
	def get(self):
		self.response.headers['Content-Type'] = 'text/plain' 
		self.response.write('Yarrr, that be a fine color!')

app = webapp2.WSGIApplication([('/sms/reply/', TxtHandler)])		

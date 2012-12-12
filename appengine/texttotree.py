import webapp2

class TxtHandler(webapp2.RequestHandler):
	def post(self):
		body = self.request.get('Body').lower()
		self.response.headers['Content-Type'] = 'text/plain'
		if 'blue' in body:
			self.response.write('Ye old seadog, ye. I feel pretty and blue like the sea.')
		elif 'red' in body:
			self.response.write('Arr, don\'t I look nice in red.')
		elif 'yellow' in body:
			self.response.write('Ye think me some kind of coward!?')
		elif 'white' in body:
			self.response.write('I\'d expect as much from a landlubber like ye!')
		elif 'orange' in body:
			self.response.write('Blow me down! That\'s a tough one.')
		elif 'purple' in body:
			self.response.write('Some scallywag hornswaggled me purple, so this is the best I can do.')
		elif 'green' in body:
			self.response.write('Even an old salt like me get\'s queasy once in a while.')
                elif 'pink' in body:
                        self.response.write('I look good, and anyone who disagrees can walk the plank!')
		elif 'rainbow' in body:
			self.response.write('A proud choice! I\'m givin\' it all I\'ve got.')
		elif 'none' in body:
			self.response.write('Son of biscuit eater! It\'s gone dark!')
		else:
			self.response.write('Ahoy, matey! What color be to your liking?')

app = webapp2.WSGIApplication([('/sms/reply/', TxtHandler)])		

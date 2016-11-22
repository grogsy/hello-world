class ContactList(list):
	
	def search(self, name):
		'''Return all contacts that contain the search value
		in their name.'''
		matching_contacts = []
		for contact in self:
			if name in contact.name:
				matching_contacts.append(contact)
		return matching_contacts
		
class Contact:
	all_contacts = ContactList()
	
	def __init__(self, name, email):
		self.name = name
		self.email = email
		self.all_contacts.append(self)
		
class Friend(Contact):
	
	def __init__(self, email, phone):
		Contact.__init__(name, email)
		AddressHolder.__init__(
			self, street, city, state, code)
		self.phone = phone
		
#example of a mixin class
class MailSender:
	'''To be used with class Contact'''
	def send_mail(self, message):
		print("Sending email to " + self.email)
		#Add email logic here
		
class EmailableContact(Contact, MailSender):
	'''Mixin of Mailsender and Contact'''
	pass
	
class AddressHolder:
	
	def __init__(self, street, city, state, code):
		self.street = street
		self.city = city
		self.state = state
		self.code = code
		
#classes below exhibit the diamond-problem
class BaseClass:
	num_base_calls = 0
	def call_me(self):
		print("Calling method on Base Class")
		self.num_base_calls += 1
		
class LeftSubClass(BaseClass):
	num_left_calls = 0
	def call_me(self):
		super().call_me()
		print("Calling method on Left Subclass")
		self.num_left_calls +=1
		
class RightSubClass(BaseClass):
	num_right_calls = 0
	def call_me(self):
		super().call_me()
		print("Calling method on Right Subclass")
		self.num_right_calls += 1
		
class SubClass(LeftSubClass, RightSubClass):
	num_sub_calls = 0
	def call_me(self):
		super().call_me()
		print("Calling method on Subclass")
		self.num_sub_calls += 1
		
		

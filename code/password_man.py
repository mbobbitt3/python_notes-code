from io import UnsupportedOperation
import json
import sys
import os
from base64 import b64encode
from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from Crypto.Random import get_random_bytes
#import pwnedpasswords

# you're gonna need the cryptodome library for this to run correctly

# The password list - We start with it populated for testing purposes
entries = {}

# The password file name to store the data to
# The encryption key for the caesar cypher
#encryption_key = 16
aes_key = get_random_bytes(32)# generate random 32 byte  key for AES using good rand byte gen 
iv = os.urandom(16) # generate random 16 byte init vector for AES-CBC 
menu_text = """
What would you like to do:
1. Add an entry
2. Lookup an entry
3. Edit entry
4. Quit program
5. Print dictionary for testing
6. file print
Please enter a number (1-6)"""


def password_encrypt(unencrypted_message, aes_key):
    """Returns an encrypted message using AES-256

    :param unencryptedMessage (string)
    :param 
    :return (string) The encrypted message
	"""
    cipher = AES.new(aes_key, AES.MODE_CBC, iv) #new aes inst
#note: ctx_bytes message must be casted in bytes to work
    ctx_bytes = cipher.encrypt(pad(bytes(unencrypted_message, 'utf-8'), AES.block_size)) 
    ctx = b64encode(ctx_bytes).decode('utf-8')
    return (ctx)
def password_decrypt(ctx):
	"""Returns a decrypted message using AES-256.
	:param ctx: :
	:return (string): The decrypted message
	"""
	decode_ctx = b64decode(ctx)
	cipher = AES.new(aes_key, AES.MODE_CBC, iv)
	plaint= unpad(cipher.decrypt(decode_ctx), AES.block_size)
	return plaint

def add_entry():
	"""Adds an entry with an entry title, username, password and url
	Includes all user interface interactions to get the necessary information from the user
	"""

	fd = open("passwds.json", 'a+')
	platform = input("enter platform for password to be saved: ")
	entries[platform] ={}
	user =  input("enter username for platform: ")
	entries[platform]['user'] = user
	passwd = input("enter password associated with for platform: ")
	entries[platform]['passwd'] = password_encrypt(passwd, aes_key)
	url = input("enter url asociated with platform: ")
	entries[platform]['url'] = url
	j_data = json.dump(entries, fd)
	fd.write(',\n')
	fd.close()


def print_entry():
	"""Asks the user for the name of the entry and prints all related information in a pretty format. Includes all information about an entry.
	"""
	print("Which entry do you want to lookup the information for?")
	for key in entries:
		print(key)
	entry = input('Enter entry name: ')

    # Fill in your code here
	if (entry in entries):
		entries[entry]['passwd'] = password_decrypt(entries[entry]['passwd'])
		print(entries[entry])
	else:
		print("entry does not exist")

def file_print():
	fd = open("passwds.json", 'r')
	data = json.loads(fd)
	print(data)
	fd.close()
def edit_entry():
	"""
	this is 2n add feature: Allow User to edit fields from entries 
	"""
	f = "passwds.json"
	with open(f, 'r') as fd:
		data = json.load(fd)
		fd.close()
	for key in entries:
		print(key)
	entry = input("name of platform to edit: ")
	if(entry in entries):
		for key in entries[entry]:
			print(key)
		field = input("enter field you want to edit: ")
		if(field in entries[entry] and field != 'passwd'):
			entries[entry][field] = input("enter changes to value in field: ")
			data[entry][field] = entries[entry][field]
			with open(f, 'w') as fd:
				j_data = json.dump(data, fd)
				fd.close()
		elif(field  == 'passwd'):
			new_passwd = input("Enter new password: ")
			enc_passwd = password_encrypt(new_passwd, aes_key)
			entries[entry][field] = enc_passwd
			with open(f, 'w') as fd:
				js_passwd = json.dump(entries, fd)
		else:
			print("that field does not exist")
			edit_entry()
	else:
		print("that is not a valid platform name")
		edit_entry()

def end_program():
    sys.exit()

def print_dictionary():
    print(entries)


menu_dict = {'1': add_entry,
             '2': print_entry,
			 '3': edit_entry,
             '4': end_program,
             '5': print_dictionary,
			 '6': file_print}

while True:
    user_choice = input(menu_text)
    if user_choice in menu_dict and menu_dict[user_choice]:
        menu_dict[user_choice]()
    else:
        print('Not a valid choice')

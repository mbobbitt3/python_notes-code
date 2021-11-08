from io import UnsupportedOperation
import pickle
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
password_file_name = "PasswordFile.pickle"
# The encryption key for the caesar cypher
#encryption_key = 16
aes_key = get_random_bytes(32)# generate random 32 byte  key for AES using good rand byte gen 
iv = os.urandom(16) # generate random 16 byte init vector for AES-CBC 
menu_text = """
What would you like to do:
1. Open password file
2. Add an entry
3. Lookup an entry
4. Edit entry
5. Save password file
6. Quit program
7. Print dictionary for testing
Please enter a number (1-7)"""


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

#return password_encrypt(encrypted_message, -key)

def load_password_file():
    """Loads a password file.  The file must be in the same directory as the .py file

    :param file_name (string) The file to load.  Must be a pickle file in the correct format
    """
    global entries, encryption_key
    entries, encryption_key = pickle.load(open(password_file_name, "rb"))


def save_password_file():
    """Saves a password file.  The file will be created if it doesn't exist.

    :param file_name (string) The file to save.
    """
    pickle.dump((entries, encryption_key), open(password_file_name, "wb"))


def add_entry():
    """Adds an entry with an entry title, username, password and url
    
    Includes all user interface interactions to get the necessary information from the user
    """
    # Fill in your code here
    platform = input("enter platform for password to be saved: ")
    entries[platform] ={}
    user =  input("enter username for platform: ")
    entries[platform]['user'] = user
    passwd = input("enter password associated with for platform: ")
    entries[platform]['passwd'] = password_encrypt(passwd, aes_key)
    url = input("enter url asociated with platform: ")
    entries[platform]['url'] = url



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

def edit_entry():
	"""
	this is 2n add feature: Allow User to edit fields from entries 
	"""

	for key in entries:
		print(key)
	entry = input("name of platform to edit: ")
	if(entry in entries):
		for key in entries[entry]:
			print(key)
		field = input("enter field you want to edit: ")
		if(field in entries[entry] and field != 'passwd'):
			entries[entry][field] = input("enter changes to value in field: ")
		elif(field  == 'passwd'):
			new_passwd = input("Enter new password: ")
			enc_passwd = password_encrypt(new_passwd, aes_key)
			entries[entry][field] = enc_passwd
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


menu_dict = {'1': load_password_file,
             '2': add_entry,
             '3': print_entry,
			 '4': edit_entry,
             '5': save_password_file,
             '6': end_program,
             '7': print_dictionary}

while True:
    user_choice = input(menu_text)
    if user_choice in menu_dict and menu_dict[user_choice]:
        menu_dict[user_choice]()
    else:
        print('Not a valid choice')

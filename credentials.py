import os

BASE_PATH = "credentials/{0}"
SQL_USERNAME_PATH = BASE_PATH.format("sql_username.txt")
SQL_PASSWORD_PATH = BASE_PATH.format("sql_password.txt")

def get_sql_username():
	if os.path.isfile(SQL_USERNAME_PATH):
		return open(SQL_USERNAME_PATH).read().split("\n")[0]
	else:
		credential_val = str(raw_input("Input SQL Username: ")).strip()
		with open(SQL_USERNAME_PATH, 'w') as the_file:
			the_file.write(credential_val)
		return credential_val

def get_sql_password():
	if os.path.isfile(SQL_PASSWORD_PATH):
		return open(SQL_PASSWORD_PATH).read().split("\n")[0]
	else:
		credential_val = str(raw_input("Input SQL Password: ")).strip()
		with open(SQL_PASSWORD_PATH, 'w') as the_file:
			the_file.write(credential_val)
		return credential_val

if __name__ == '__main__':
	print get_sql_username()
	print get_sql_password()

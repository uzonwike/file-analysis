import database
help_text = '''The following commands are available: 
1. list (list all files)
2. sentiment <sentiment> (list all files of with a sentiment of <sentiment>)
3. path <path> (list all files where the file's path contains <path>)
4. data <path> (list the data of file with path of <path>)
5. table (toggle table format on/off)
'''

# Console for getting file information
def main():
	print_as_table = True
	database.db.connect()
	print("Type 'commands' to see the list of available commands")
	while True:
		commands = raw_input("> ").split()
		if len(commands) > 0:
			if commands[0] in ["q", "quit", "exit"]:
				break
			elif commands[0] in ["commands", "help"]:
				print(help_text)
			elif commands[0] == "table":
				print_as_table = not print_as_table
				print("Display as table: " + str(print_as_table))
			else:
				func = get_function(commands[0])
				if func:
					args = commands[1:]
					try:
						func(*args, table = print_as_table)
					except:
						print("Invalid command, try again.")
				else:
					print("No such command, try again.")


	database.db.close()

# Get the function to execute from database.py
def get_function(name):
	if name == "list":
		return database.print_all_files
	elif name == "sentiment":
		return database.print_files_with_sentiment
	elif name == "path":
		return database.print_files_path_contains
	elif name == "data":
		return database.print_file_data

# Start the console if we run this file
if __name__ == '__main__':
	main()
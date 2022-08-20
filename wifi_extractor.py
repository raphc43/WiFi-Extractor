import os

def extract_wifi_details():
	"""Function to extract and display WiFi details """
	exit = False
	while exit == False:
		wifi_details = input("Select a command by entering a number -> '1) Show WiFi list' or '2) Show WiFi password': " 
							"\nOr enter '0' to exit.")

		# Show a list of registered WiFi
		if str(wifi_details) == '1':
			os.system('cmd /c "color a & netsh wlan show profile"')

		# Display Wifi details including password/security key
		elif str(wifi_details) == '2':
			take_input = input('Please enter your WiFi name: ')
			os.system(f'cmd /c "color a & netsh wlan show profile {take_input} key=clear"')

		# Exit if '0'
		elif str(wifi_details) == '0':
			exit = True
		
		else:
			'Command invalid'
	return

extract_wifi_details()
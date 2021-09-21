'''
The program will read config.txt file from the same directory. After that, it will extract config file parameters as variables with necessary typecasting.
The given sample does not represnt what is invalid config line. Invalid lines could occur multiple reasons. Any sample will be helpfull to implement it. 
Using the config variables, I check if server load exceeds the given threshold, it will send a notifcation to server admin. 
'''
filename = "config.txt"
# store lines info
variables = []
# Read File 
with open(filename) as f:
	for line in f:
		if not line.startswith("#"):
			variables.append([n for n in line.strip().split('=')])
# Dynamically variable assign
for pair in variables:
	x,y =pair[0], pair[1]
	exec('%s=%s'%(x,'y'))

def bool_conversion(arg):
	# Convert boolean
	if 'true' or 'on' or 'yes':
		return True
	else:
		return False

#Type casting 
server_id=int(server_id)
server_load_alarm=float(server_load_alarm) 
verbose=bool_conversion(verbose)
test_mode=bool_conversion(test_mode)
debug_mode=bool_conversion(debug_mode)
send_notifications=bool_conversion(send_notifications)

def notification():
	'''
	Email/SMS notification system 
	To be implemented in future 
	'''
	pass 

def load_alarm_exceed(threshload):
	if server_load_alarm>=threshload:
		if send_notifications is not True:
			# send notificatoin 
			notification() 
		print("Alert! Server load is exceeding!")


if __name__ == '__main__':
	load_alarm_exceed(1)






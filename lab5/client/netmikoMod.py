from netmiko import ConnectHandler

myserver = {
	'device_type': 'linux',
	'host': '192.168.125.3', #Your Server IP
	'username':'broccoli', #your Server Username
	'password': '123', #your server password
	'port': 22,
	'secret':'',
}

net_connect = ConnectHandler(**myserver)
myserver.get('enable')(cmd="sudo su", pattern='password') 
output = net_connect.send_command('sudo apt-get update && apt-get -y install nmap')
print(output)
myserver.exit_enable_mode()

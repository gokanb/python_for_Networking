import platform
from termcolor import colored

operating_system = platform.system()
print(colored(f'My current Operating System is {operating_system} ', 'blue'))
if (operating_system == 'Windows'):
    ping_command = 'ping -n 10 127.0.0.1'
    
elif (operating_system == 'Linux'):
    ping_command = 'ping -c 10 127.0.0.1'
    
else:
    ping_command = 'ping -c 10 127.0.0.1'
    
print(colored(ping_command, 'yellow'))
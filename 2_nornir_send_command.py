from nornir import InitNornir
from nornir.core.task import Task, Result
from nornir_netmiko.tasks import netmiko_send_command
from nornir_napalm.plugins.tasks import napalm_get
from nornir_utils.plugins.functions import print_result
import time


nr = InitNornir(config_file="config.yaml", dry_run=True)
commands = ["show ip route", "show arp", "sh ip int bri", "sh int status | ex down"]

for command in commands:
	TXT = command
	print("################ EXECUTING: " + TXT + " ####################")
	time.sleep(5)

	results = nr.run(task=netmiko_send_command, command_string=command)
	
	print_result(results)
	time.sleep(10)

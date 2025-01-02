#! /usr/bin/env python3
'''
massdl v0.3 - Copyright 2024 James Slaughter,
This file is part of massdl v0.3.

massdl v0.3 is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

massdl v0.3 is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with massdl v0.3.  If not, see <http://www.gnu.org/licenses/>.
'''

#python import
import sys
import os
import subprocess
import time
import datetime
import argparse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from urllib.parse import urlparse

__ScriptVersion__ = "massdl-v0.3"
LOGFILE = "" #<--add a logfile location
DEFAULT_DIR = "" #<--add a default output location

# ANSI color codes
RC = "\033[1;31m"  # Red
GC = "\033[1;32m"  # Green
YC = "\033[1;33m"  # Yellow
EC = "\033[0m"     # End color

def echoerror(message):
    print(f"{RC}[x]: {message}{EC}", file=sys.stderr)
    with open(LOGFILE, "a") as log:
        log.write(f"[*]: {message}\n")    

def echoinfo(message):
    print(f"{GC}[*]{EC}: {message}")
    with open(LOGFILE, "a") as log:
        log.write(f"[*]: {message}\n")

def echowarn(message):
    print(f"{YC}[-]: {message}{EC}")
    with open(LOGFILE, "a") as log:
        log.write(f"[*]: {message}\n")

'''
Usage()
Function: Display the usage parameters when called
'''
def Usage():
    print ('Usage: [required] --mode [domain|list] [--target] [optional] --ua --screenshotter --output --debug --help')
    print ('Example 1: /opt/massdl/massdl.py --mode domain --target example.com --ua 2 --screenshotter --output /your/directory/your file --debug')
    print ('Example 2: /opt/massdl/massdl.py --mode list --target domains.txt --ua 5 --screenshotter --output /your/directory/ --debug')
    print ('Required Arguments:')
    print ('--mode - Operation mode: domain or list')
    print ('--target - Target domain or list file')
    print ('OR')
    print ('--targetlist - List containing multiple domains to examine in one session')
    print ('Optional Arguments:')
    print ('--ua - User Agent number (1-9)')
    print ('--screenshotter - Screenshot the target domain')    
    print ('--output - Choose where you wish the output to be directed')
    print ('--debug - Prints verbose logging to the screen to troubleshoot issues with a recon installation.')
    print ('--usage - You\'re looking at it!')
    print ('--help - Prints program help')
    print ('')
    print ('User Agents:')
    print ('1: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari//537.36 Edge/18.19582"')
    print ('2: "Mozilla/5.0 (Linux; U; Android 4.0.3; ko-kr; LG-L160L Build/IML74K) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"')
    print ('3: "Microsoft Office Word 2014 (16.0.4549) Windows NT 6.1"')
    print ('4: "Microsoft Office/14.0 (Windows NT 6.1; Microsoft Outlook 14.0.7143; Pro"')
    print ('5: "Mozilla/5.0 (Windows NT; Windows NT 10.0; en-US) WindowsPowerShell/5.1.19041.1237"')
    print ('6: "Mozilla/5.0 (Linux; Android 10; SM-G975F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 MicroMessenger/7.0.21(0x27001534) NetType/WIFI Language/en"')
    print ('7: "Mozilla/5.0 (Linux; U; Android 10; en-us; SM-G975F Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 MQQBrowser/10.0 Mobile Safari/537.36 QQ/8.4.0.674"')
    print ('8: "Mozilla/5.0 (Linux; Android 9; en-us; SM-G965U Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36 QQ/8.3.5.432"')
    print ('9: "Mozilla/5.0 (Linux; Adr 10; SM-G970F Build/QQ2A.200305.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.101 Mobile Safari/537.36" ')
    sys.exit(-1)    

'''
Parse() - Parses program arguments
'''
def parse_args():     
    parser = argparse.ArgumentParser(description="massdl - Mass Download Script")
    parser.add_argument("--mode", choices=["domain", "list"], help="Operation mode: domain or list")
    parser.add_argument("--target", help="Target domain or list file")
    parser.add_argument("--ua", type=int, choices=range(1, 10), help="User Agent number (1-9)")
    parser.add_argument("--screenshotter", action='store_true', help="Screenshot the target domain")
    parser.add_argument("--output", help="Output file")
    parser.add_argument('--usage', action='store_true', help='Display program usage.')

    args = parser.parse_args()

    if args.usage:
        Usage()

    return args

def initialize():
    echoinfo("--------------------------------------------------------------------------------")
    echoinfo(f"Running massdl.py version {__ScriptVersion__} on {datetime.datetime.now()}")
    echoinfo("--------------------------------------------------------------------------------")


# Function to take screenshot of a website with a specific user agent
#def capture_website(url, folder, user_agent):
def capture_website(args, url, user_agent):
    # Set up Chrome options for headless browsing
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument(f"user-agent={user_agent}")
    domain = ''

    # Create a new Chrome driver instance
    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        # Navigate to the URL
        driver.get(url)
        
        # Wait for the page to load (you might need to adjust this)
        #time.sleep(5)
        
        # Parse the domain from the URL
        domain = urlparse(url).netloc

        # Check if args.output is None or empty
        if not args.output:
            #raise ValueError("Output directory is not specified. Please use the --output argument to set an output directory.")
            args.output = DEFAULT_DIR
            echowarn(f"Output directory is not specified. Using default directory: {args.output}")
            
        # Ensure the output directory exists
        os.makedirs(args.output, exist_ok=True)

        html_content = driver.page_source
        html_path = os.path.join(args.output, f"{domain}.html")
        with open(html_path, 'w', encoding='utf-8') as html_file:
            html_file.write(html_content)        

        echoinfo(f"HTML saved for '{url}' at {os.path.join(args.output, f'{domain}.html')}")

        if (args.screenshotter):
            # Get the full page height
            total_height = driver.execute_script("return document.body.scrollHeight")
            # Get the window width
            total_width = driver.execute_script("return document.body.scrollWidth")
            
            # Set window size to capture everything
            driver.set_window_size(total_width, total_height)
            
            # Take a screenshot and save it
            screenshot_path = os.path.join(args.output, f"{domain}.png")
            driver.save_screenshot(screenshot_path)
            echoinfo(f"Screenshot saved for '{url}' at {screenshot_path}")
            
            # Reset window size to default (optional)
            driver.set_window_size(1920, 1080)  # You can adjust these values as needed
    except ValueError as ve:
        echoerror(f"Error: {str(ve)}")
    except Exception as e:
        echoerror(f"Error capturing data for {url}: {str(e)}")
    finally:
        # Close the browser
        driver.quit()

def pipe_to_singledl(args, user_agent):
    echoinfo(f"User Agent is: '{user_agent}'")
    echoinfo(f"Target domain is: '{args.target}'")

    url = args.target
    capture_website(args, url, user_agent)

def pipe_to_massdl(args, user_agent):
    echoinfo(f"Target file is: {args.target}")
    echoinfo(f"User Agent is: {user_agent}")
    
    with open(args.target, "r") as f:
        for line in f:
            url = line.strip()
            echoinfo(f"Target domain is: '{url}'")
 
            capture_website(args, url, user_agent)
            print ('\n')

def wrap_up():
    echoinfo(f"Program complete on {datetime.datetime.now()}")

def main():

    #args = 0

    args = parse_args()

    if (args == -1):
        Usage()
        #Terminate(ret) 

    user_agents = {
        1: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari//537.36 Edge/18.19582",
        2: "Mozilla/5.0 (Linux; U; Android 4.0.3; ko-kr; LG-L160L Build/IML74K) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
        3: "Microsoft Office Word 2014 (16.0.4549) Windows NT 6.1",
        4: "Microsoft Office/14.0 (Windows NT 6.1; Microsoft Outlook 14.0.7143; Pro",
        5: "Mozilla/5.0 (Windows NT; Windows NT 10.0; en-US) WindowsPowerShell/5.1.19041.1237",
        6: "Mozilla/5.0 (Linux; Android 10; SM-G975F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 MicroMessenger/7.0.21(0x27001534) NetType/WIFI Language/en",
        7: "Mozilla/5.0 (Linux; U; Android 10; en-us; SM-G975F Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 MQQBrowser/10.0 Mobile Safari/537.36 QQ/8.4.0.674",
        8: "Mozilla/5.0 (Linux; Android 9; en-us; SM-G965U Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36 QQ/8.3.5.432",
        9: "Mozilla/5.0 (Linux; Adr 10; SM-G970F Build/QQ2A.200305.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.101 Mobile Safari/537.36"
    }

    user_agent = user_agents.get(args.ua, "Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko")

    initialize()

    if args.mode == "list":
        #pipe_to_massdl(args.target, user_agent)
        pipe_to_massdl(args, user_agent)
    elif args.mode == "domain":
        #pipe_to_singledl(args.target, user_agent)
        pipe_to_singledl(args, user_agent)

    wrap_up()

if __name__ == "__main__":
    main()

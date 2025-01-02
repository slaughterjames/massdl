# massdl
A small Python script used to download the contents of a webpage quickly and/or take a screenshot of it.

usage: massdl.py [-h] [--mode {domain,list}] [--target TARGET] [--ua {1,2,3,4,5,6,7,8,9}] [--screenshotter] [--output OUTPUT] [--usage]

massdl - Mass Download Script

options:
  -h, --help            show this help message and exit
  --mode {domain,list}  Operation mode: domain or list
  --target TARGET       Target domain or list file
  --ua {1,2,3,4,5,6,7,8,9}
                        User Agent number (1-9)
  --screenshotter       Screenshot the target domain
  --output OUTPUT       Output file
  --usage               Display program usage.

Expanded:

Usage: [required] --mode [domain|list] [--target] [optional] --ua --screenshotter --output --debug --help
Example 1: /opt/massdl/massdl.py --mode domain --target example.com --ua 2 --screenshotter --output /your/directory/your file --debug
Example 2: /opt/massdl/massdl.py --mode list --target domains.txt --ua 5 --screenshotter --output /your/directory/ --debug
Required Arguments:
--mode - Operation mode: domain or list
--target - Target domain or list file
OR
--targetlist - List containing multiple domains to examine in one session
Optional Arguments:
--ua - User Agent number (1-9)
--screenshotter - Screenshot the target domain
--output - Choose where you wish the output to be directed
--debug - Prints verbose logging to the screen to troubleshoot issues with a recon installation.
--usage - You're looking at it!
--help - Prints program help

User Agents:
1: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari//537.36 Edge/18.19582"
2: "Mozilla/5.0 (Linux; U; Android 4.0.3; ko-kr; LG-L160L Build/IML74K) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"
3: "Microsoft Office Word 2014 (16.0.4549) Windows NT 6.1"
4: "Microsoft Office/14.0 (Windows NT 6.1; Microsoft Outlook 14.0.7143; Pro"
5: "Mozilla/5.0 (Windows NT; Windows NT 10.0; en-US) WindowsPowerShell/5.1.19041.1237"
6: "Mozilla/5.0 (Linux; Android 10; SM-G975F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 MicroMessenger/7.0.21(0x27001534) NetType/WIFI Language/en"
7: "Mozilla/5.0 (Linux; U; Android 10; en-us; SM-G975F Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 MQQBrowser/10.0 Mobile Safari/537.36 QQ/8.4.0.674"
8: "Mozilla/5.0 (Linux; Android 9; en-us; SM-G965U Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36 QQ/8.3.5.432"
9: "Mozilla/5.0 (Linux; Adr 10; SM-G970F Build/QQ2A.200305.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.101 Mobile Safari/537.36" 

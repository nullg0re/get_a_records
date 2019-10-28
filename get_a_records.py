#!/usr/bin/python
import argparse
import dns.resolver
from colorama import Fore, Style

def get_args():
	parser = argparse.ArgumentParser(description="Mass A Record Gathering")
	parser.add_argument('-f','--file',type=argparse.FileType('r'),help="File with subdomains",required=True)
	parser.add_argument('-o','--outfile',type=str,help="File to write records too")

	args = parser.parse_args()

	file = args.file
	outfile = args.outfile

	return file, outfile

def save_to_file(subdomain,records,outfile):
	f = open(outfile, 'a+')
	f.write("[+] %s [+]\n" % subdomain)
	for record in records:
		f.write(record+"\n")
	f.close
	return

def record_lookup(subdomain, outfile="0"):
	if outfile == "0":
		answers = dns.resolver.query(subdomain,'A')
		for record in answers:
			print record
		return
	else:
		answers = dns.resolver.query(subdomain,'A')
		records = []
		for record in answers:
			print record
			records.append(str(record))
		save_to_file(subdomain,records,outfile)
		return
def main():
	# Get arguments
	file, outfile = get_args()

	if file is not None and outfile is None:
		# For subdomain in file of subdomains
		# perform dns lookup for a records
		print(Fore.MAGENTA+"[*] Performing DNS Lookups On Subdomains Found In %s."+Style.RESET_ALL) % file.name
		for line in file:
			subdomain = line.strip()
			print(Style.BRIGHT+Fore.GREEN+"[+] %s."+Style.RESET_ALL) % subdomain
			record_lookup(subdomain,outfile)

	if file is not None and outfile is not None:
		print(Fore.MAGENTA+"[*] Performing DNS Lookups On Subdomains Found in %s."+Style.RESET_ALL) % file.name
		print(Fore.MAGENTA+"[*] Saving records to %s"+Style.RESET_ALL) % outfile
		for line in file:
			subdomain = line.strip()
			print(Style.BRIGHT+Fore.GREEN+"[+] %s."+Style.RESET_ALL) % subdomain
			record_lookup(subdomain, outfile)

if __name__ == '__main__':
	main()

# get_a_records
Mass A Record Collector Script

This script takes a list of Fully Qualified Host Names (FQDNs) and performs DNS queries on each FQDN to obtain the IP address in the A record for the FQDN.

This script is used as a quick OSINT script.

# Help Menu:
```
./get_a_records.py -h
usage: get_a_records.py [-h] -f FILE [-o OUTFILE]

Mass A Record Gathering

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  File with subdomains
  -o OUTFILE, --outfile OUTFILE
                        File to write records too
```
# Example Output:
```
./get_a_records.py -f subdomains.txt -o ips.txt
[*] Performing DNS Lookups On Subdomains Found in subdomains.txt.
[*] Saving records to ips.txt
[+] webapps.morainevalley.edu.
64.107.14.212
[+] directory.morainevalley.edu.
64.107.14.205
[+] dropbox.morainevalley.edu.
64.107.14.212
[+] ldap1.morainevalley.edu.
64.107.14.213
[+] lib.morainevalley.edu.
64.107.14.205
[+] multimedia.morainevalley.edu.
64.107.14.212
[+] ext.morainevalley.edu.
34.231.191.220
18.232.224.67
[+] moodle.morainevalley.edu.
64.107.13.110
[+] ldap2.morainevalley.edu.
64.107.14.218
[+] wellness.morainevalley.edu.
64.107.14.212
[+] library.morainevalley.edu.
64.107.14.30
<<snip>>
```
# Example File Output:
```
cat ips.txt 
[+] webapps.morainevalley.edu [+]
64.107.14.212
[+] directory.morainevalley.edu [+]
64.107.14.205
[+] dropbox.morainevalley.edu [+]
64.107.14.212
[+] ldap1.morainevalley.edu [+]
64.107.14.213
[+] lib.morainevalley.edu [+]
64.107.14.205
[+] multimedia.morainevalley.edu [+]
64.107.14.212
[+] ext.morainevalley.edu [+]
34.231.191.220
18.232.224.67
[+] moodle.morainevalley.edu [+]
64.107.13.110
[+] ldap2.morainevalley.edu [+]
64.107.14.218
[+] wellness.morainevalley.edu [+]
64.107.14.212
[+] library.morainevalley.edu [+]
64.107.14.30
[+] apps.morainevalley.edu [+]
64.107.14.208
[+] WWW.morainevalley.edu [+]
34.231.191.220
18.232.224.67
[+] vcse.morainevalley.edu [+]
64.107.14.13
[+] smtp.morainevalley.edu [+]
64.107.14.203
[+] learn.morainevalley.edu [+]
64.107.14.202
[+] imap.morainevalley.edu [+]
64.107.14.203
[+] cube.morainevalley.edu [+]
64.107.11.246
[+] notes.morainevalley.edu [+]
64.107.14.6
[+] astra.morainevalley.edu [+]
64.107.12.247
[+] meeting.morainevalley.edu [+]
64.107.14.32
[+] cit.morainevalley.edu [+]
64.107.14.155
[+] online.morainevalley.edu [+]
64.107.14.205
[+] books.morainevalley.edu [+]
207.138.59.100
[+] news.morainevalley.edu [+]
64.107.14.212
[+] www.morainevalley.edu [+]
34.231.191.220
18.232.224.67
[+] netlab.morainevalley.edu [+]
64.107.13.100
[+] pop3.morainevalley.edu [+]
64.107.14.203
[+] www.library.morainevalley.edu [+]
64.107.14.30
<<snip>>
```

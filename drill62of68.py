# Author: Kristen Findley
# Date: 25 January 2017
# Python: Version 2.7
# Description: Create program that uses the current time in Portland and outputs
#              whether or not the corresponding offices in NY and London are
#              open based on operating hours of 9:00AM to 9:00PM.


import datetime

timePDX = str(datetime.datetime.now().time()) # obtain current time in Portland

hrPDX = int(timePDX[:2]) # obtain hour and convert to int to perform mathematic operations

hrNYC = hrPDX + 3
hrLondon = hrPDX + 8

if hrNYC >= 9 and hrNYC < 21:
    statusNYC = 'open'
else:
    statusNYC = 'closed'

if hrLondon >= 9 and hrLondon < 21:
    statusLondon = 'open'
else:
    statusLondon = 'closed'

if statusNYC == statusLondon:
    print 'At this time (' + timePDX[:8] + ') both the New York and London offices are ' + statusNYC + '.'
else:
    print 'At this time (' + timePDX[:8] + ') the New York office is ' + statusNYC + ' and the London office is ' + statusLondon + '.'


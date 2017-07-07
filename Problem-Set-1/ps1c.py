# *****************************************************************************

	# This program is free software: you can redistribute it and/or modify
	# it under the terms of the GNU General Public License as published by
	# the Free Software Foundation, either version 3 of the License, or
	# (at your option) any later version.

	# This program is distributed in the hope that it will be useful,
	# but WITHOUT ANY WARRANTY; without even the implied warranty of
	# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	# GNU General Public License for more details.

	# You should have received a copy of the GNU General Public License
	# along with this program.  If not, see <http://www.gnu.org/licenses/>.
	
# *****************************************************************************
# Problem Set 1
# Name: Seinu
# Collaborators: None
# Time Spent: 4:45
# Notes:
#	not sure the exact problem but does not return *correct* balance leftover
# *****************************************************************************
def getInterest(annualRate):
	return annualRate / 12

def getMonthPay(balance, monthRate, currPaid):
	return balance * (1 + monthRate) - currPaid

balance = float(raw_input('Enter the outstanding balance on your credit card: '))
payLowB = balance / 12
rate = float(raw_input('Enter the annual credit card interest rate as a decimal: '))
remainBal = balance
monthRate = getInterest(rate)
payHighB = round((balance * (1 + rate) ** 12.0) / 12.0, 2)
currPaid = (payHighB + payLowB)/2.0
i = 1
while(True):
	for i in range(1,13):
		remainBal = getMonthPay(remainBal, monthRate, currPaid)
		
	if remainBal > 0.01:
		payLowB = currPaid
	elif remainBal <= 0.005 and remainBal >= -0.005:
		currPaid += 0.004999
		remainBal = balance
		for i in range(1,13):
			remainBal = getMonthPay(remainBal, monthRate, currPaid)
			
		break
	else:
		payHighB = currPaid
	currPaid = (payHighB + payLowB)/2.0
	remainBal = balance


print('RESULT')
print('Monthly payment to pay off debt in 1 year: ', round(currPaid, 2))
print('Number of months needed: ', i)
print('Balance: ', round(remainBal, 2))

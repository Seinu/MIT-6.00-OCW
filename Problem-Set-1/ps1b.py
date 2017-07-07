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
# Time Spent: 2:30
# *****************************************************************************
def getInterest(annualRate):
	return annualRate / 12

def getMonthPay(balance, monthRate, tens):
	return balance * (1 + monthRate) - tens

balance = int(raw_input('Enter the outstanding balance on your credit card: '))
rate = float(raw_input('Enter the annual credit card interest rate as a decimal: '))
remainBal = balance
tens = 10
monthRate = getInterest(rate)
count = 1
while (remainBal >= 0):
	for i in range(12):
		count = i + 1
		remainBal = getMonthPay(remainBal,  monthRate, tens)
		if remainBal < 0:
			break
	
	if remainBal >= 0:
		tens += 10
		remainBal = balance

print('RESULT')
print('Monthly payment to pay off debt in 1 year: ', tens)
print('Number of months needed: ', count)
print('Balance: ', round(remainBal, 2))

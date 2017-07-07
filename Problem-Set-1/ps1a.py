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
# Time Spent: 1:45
# *****************************************************************************

def getMinPay(minRate, balance):
	return round(minRate * balance, 2)

def getInterest(annualRate, balance):
	return round(annualRate / 12 * balance, 2)

def getPrincipal(minPay, interestPaid):
	return round(minPay - interestPaid, 2)

def getRemainBal(balance, principal):
	return round(balance - principal, 2)


bal = float(raw_input('Enter the outstanding balance on your credit card: '))
annualRate = float(raw_input('Enter the annual credit card interest rate as decimal: '))
minRate = float(raw_input('Enter the minimum monthly payment rate as a decimal: '))

for i in range(12):
	print 'Month: ', i + 1
	minMonthPaid = getMinPay(minRate, bal)
	print 'Minimum monthly payment: ', minMonthPaid
	intPaid = getInterest(annualRate, bal)
	principal = getPrincipal(minMonthPaid, intPaid)
	print 'Principal paid: ', principal
	bal = getRemainBal(bal, principal)
	print 'Remaining balance: ', bal
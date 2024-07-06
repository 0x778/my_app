# Copyright (c) 2024, Hussam and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import add_to_date 

class BankLoan(Document):

	def on_update(self):
		self.custom_schedule = []
		dat = self.custom_repayment_date
		total = self.loan_amount + self.loan_amount * self.interest / 100
		for i in range(int(self.repayment_months)):
			repayment = self.append("custom_schedule",{})
			repayment.payment_date = dat
			repayment.principal_amount = self.loan_amount / self.repayment_months
			repayment.interest_amount = repayment.principal_amount * self.interest / 100
			repayment.total_payment = repayment.principal_amount + repayment.interest_amount
			repayment.balance_loan_amount = total - repayment.total_payment
			total = repayment.balance_loan_amount
			if self.custom_type_of_payment == "Every month":
				dat = add_to_date(dat,months = 1)
			if self.custom_type_of_payment == "Every week":
				dat = add_to_date(dat,weeks = 1)
			

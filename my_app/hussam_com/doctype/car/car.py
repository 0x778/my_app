# Copyright (c) 2024, Hussam and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import _


class Car(Document):

	def before_save(self):
		self.validate()

	def validate(self):
		Name = self.custom_carplate
		if len(Name)!=8:
			frappe.throw(_("Name must be in 8 digit"))
		if Name[4] != "-" or Name[:4].isalpha()==False or Name[5:].isnumeric() == False :
			frappe.throw(_("Error in the Name format"))		

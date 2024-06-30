# Copyright (c) 2024, Hussam and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Car(Document):
	def valdiate(self):
		carplate = self.carplate
		if len(carplate)!=8:
			frappe.throw(_("Carplate must be in 8 digit and format abcd-123"))
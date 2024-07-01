from erpnext.selling.doctype.sales_order.sales_order import SalesOrder
import frappe
from frappe import _
from frappe.utils import getdate,date_diff

class CustomSalesOrder(SalesOrder):
    def before_save(self):
        self.Daysleft()

    def Daysleft(self):
        now = getdate()
        diff = date_diff(self.delivery_date,now)
        if diff >= 0 : 
            self.custom_days_left = diff
    
def Updatedaysleft():
    left = frappe.db.get_list("Sales Order",filters=[["status","in",["Draft","To Deliver","To Deliver and Bill"]]],fields=["name","delivery_date","status","custom_days_left"])
    now = getdate()
    for o in left :
        diff = date_diff(o["delivery_date"],now)
        if diff >= 0 : 
            frappe.db.set_value("Sales Order",o["name"],"custom_days_left",diff,update_modified=False)
    frappe.db.commit()
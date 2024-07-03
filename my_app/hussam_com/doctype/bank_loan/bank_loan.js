// Copyright (c) 2024, Hussam and contributors
// For license information, please see license.txt

 frappe.ui.form.on("Bank Loan", {
// 	refresh(frm) {

// 	},

repayment_months : function(frm){
    if(frm.doc.loan_amount && frm.doc.repayment_months){
       let amount = frm.doc.loan_amount / frm.doc.repayment_months ;
       frm.doc.monthly_repayment = amount ;
    }

}




});

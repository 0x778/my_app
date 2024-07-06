// Copyright (c) 2024, Hussam and contributors
// For license information, please see license.txt

 frappe.ui.form.on("Bank Loan", {
// 	refresh(frm) {

// 	},

repayment_months : function(frm){
calculate(frm);
},
interest : function(frm){
calculate(frm);
},
loan_amount : function(frm){
    calculate(frm);
}




});

function calculate(frm){
    if(frm.doc.loan_amount && frm.doc.repayment_months){
        let amount = frm.doc.loan_amount / frm.doc.repayment_months ;
        amount = amount + amount *  frm.doc.interest / 100 ;
        frm.doc.monthly_repayment = amount ;
        //console.log(frm.doc.monthly_repayment);
        refresh_field("monthly_repayment");
     }
     else{
        frm.doc.monthly_repayment = 0 ;
        refresh_field("monthly_repayment");
     }
}
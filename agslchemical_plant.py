import streamlit as st

st.title("WELCOME TO AMOTOI GLOBAL SERVICES LIMITED")

from PIL import Image
img = Image.open("agsl logo.png")

st.image(img, width=200)

customer_name = st.text_input("Name of Individual or Company:\n")
tin_name = st.text_input("Tax Identification Number:\n")
location = st.selectbox("Select Location: ",
                     [ 'Port-Harcourt', 'Lekki', 'Uyo', 'Abuja', 'Yenagoa'])

inquiry_type = st.selectbox("Select Document Type: ",
                     [ 'Request for Proposal', 'Request for Quotation', 'Request for Proforma Invoice', 'Waybill'])

order_date = st.date_input('Date of Order')

st.text("Details of your Order")

chemical_item = {}
chemical_history =[]

chemical_name = st.text_input("Name of Chemical requested:\n")
quantity = st.text_input("Quantity requested:\n")
unit = st.text_input("Unit of Measurement")

st.text("This is what i ordered")
confirm_Order = st.checkbox('I agree')

cost = st.number_input("Amount:\n")
chemical_item = {'name':chemical_name, 'number':(quantity), 'number':(cost)}
chemical_history.append(chemical_item)

user_input = st.text_input("Would you like to make another requisition?")       
grand_total = 0
                  
for index, chemical in enumerate(chemical_history):
        chemical_total = chemical['number'] * chemical['number']
        grand_total = grand_total + chemical_total
        ('%d %s @ N%.2f Sub_TotalN%.2f' % (chemical['number'], chemical['name'], chemical['number'], chemical_total))
                   
chemical_total = 0
        
st.text("Your Invoice No is ....")
st.write('Grand Total: N%.2f' % grand_total )

payment_mode = st.selectbox("Select Preferred Pay Option: ",
                     ['Bank Guarantee', 'Cheque', 'Transfer', 'Others'])

st.write("You have Selected: ", payment_mode)
                           
payment_Mode = st.text_input("If Others state preferred payment option\n")

st.text("Your Order has been confirmed and your Invoice paid in full ")

payment_status = st.radio("Confirmation: ", ('Yes', 'No'))


if (payment_status == 'Yes'):
    st.button('Yes')
    st.text('Order Complete')
else:
    st.button('No')
    st.text('Order Incomplete')   
    
receipt_number = st.text_input("Receipt No:\n")
waybill_number = st.text_input("Waybill No:\n")                            
    
delivery_mode = st.selectbox("Select preferred handling: ",
                             ['DDP', 'Ex-Works'])

st.write("You have Selected: ", delivery_mode)

delivery_mode = st.text_input("Preferred Delivery Location\n")

st.text("*Cost to Preferred Delivery Location to be negotiated")

                             
if(st.button('Submit')):
    st.text('Thank You')
    
    st.text('AGSL Chemical plant is located at Ohia Oshimini, Mbodo-Aluu, Rivers State')
    st.text('the new Port-Harcourt Intl Airport road from Obirikwerre')
    st.text('Scheule a facilty visit today!')
    st.text('Thank You & Have a Good Day!!!')
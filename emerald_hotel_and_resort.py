#Name:Jaden Auville
#Prog Purpose: This program reads in a hotel data file, performs calculations, and creates an HTML file for the results

import datetime

############ define rate tuples ############

#            SR  DR  SU
#             0   1   2
ROOM_RATES = (195,250,350)
#           s-tax   occ-tax
#              0      1
TAX_RATES = (0.065,0.1125)
########### define files and list ############
infile = "emerald.csv"
outfile = "emerald-web-page.html"
guest = []
############ define program functions ############
def main():
    read_in_guest_file()
    perform_calculations()
    open_out_file()
    create_output_html()
def read_in_guest_file():
    guest_data = open(infile, "r")
    guest_in   = guest_data.readlines()
    guest_data.close()
    #### split the data and insert into list called: guest
    for i in guest_in:
        guest.append(i.split(","))
        

def perform_calculations():
    global grandtotal
    grandtotal=0

    for i in range(len(guest)):
        room_type = str(guest[i][2])
        num_nights = int(guest[i][3])
        
        if room_type =="SR":
            subtotal = ROOM_RATES[0] * num_nights
        elif room_type =="DR":
            subtotal = ROOM_RATES[1] * num_nights
        else: 
            subtotal = ROOM_RATES[2] * num_nights
       
        salestax  = subtotal * TAX_RATES[0]
        occupancy = subtotal * TAX_RATES[1]
        total     = subtotal + salestax + occupancy
        grandtotal += total
         
        guest[i].append(subtotal)
        guest[i].append(salestax)
        guest[i].append(occupancy)
        guest[i].append(total)
      

def open_out_file():        
    global f
    f = open(outfile, 'w')
    f.write('<html> <head> <title> Emerald Beach Hotel & Resort </title>\n')
    f.write('<style> td{text-align: right} </style> </head>\n')
    f.write('<body style="background-image: url(emerald_bg.png);">\n')

def create_output_html():
    global f
    
    currency="8,.2f"
    today = str(datetime.datetime.now())
    time = today[0:16] 

    tr = '<tr><td>'
    td = '</td><td>'
    endtr = '</td></tr>\n'
    endtd = '</td><td>'
    tr0 = '<tr><td colspan = 0>'
    tr1 = '<tr><td colspan = 1>'
    tr2 = '<tr><td colspan = 2>'
    tr3 = '<tr><td colspan = 3>'
    tr4 = '<tr><td colspan = 4>'
    tr5 = '<tr><td colspan = 5>'
    tr6 = '<tr><td colspan = 6>'
    tr7 = '<tr><td colspan = 7>'
    tr8 = '<tr><td colspan = 8>'

    f.write("<table border = 5; style = 'background-color: #F7F9FB; margin: auto;'>")
    f.write(tr8 + "<h1 style = 'text-align:center; color: #5085A5;'>Emerald Beach Hotel & Resort</h1>" + endtr)
    f.write(tr8 + "<h2 style = 'text-align:center; color: #5085A5;'>Guest Sales Report</h2>" + tr7 + "Date/Time" +endtd + time + endtr)
    f.write(tr1 + "Last Name" + endtd + "First Name" + endtd + "Room Type" + endtd + "Num Nights" + endtd + "Subtotal" + endtd + "Sales Tax" +endtd+ "Occupancy Tax" +endtd + "Total")
    for i in range(len(guest)):
        data1 = tr+guest[i][0]+endtd+guest[i][1]+endtd+guest[i][2]+endtd+str(guest[i][3])
        data2 = endtd+format(guest[i][4],currency)+endtd+format(guest[i][5],currency)+endtd+format(guest[i][6],currency)+endtd+format(guest[i][7],currency)+endtr
        f.write(data1 + data2)
    
    f.write(tr7 + "Grand Total" + endtd + format(grandtotal,currency) + endtr)
   
    f.write('</table><br />')
    f.write("</body></html>")
    f.close()
    print('Open ' + outfile + ' to view data.')
##call on main program to execute##
main()

import mysql.connector

import pickle

mydb=mysql.connector.connect(host="localhost",
                            user="root",
                            password="saurabh",
                            database="showroom")
mycursor=mydb.cursor(buffered=True)
    
#mycursor.excute('create database showroom')

#main menu
def Menu():
    print("...........................................................................")
    print("\t**************WELCOME TO SHOWROOM**************")
    print("...........................................................................")
    print("\t\t\t MAIN MENU")
    print("\t1: Insert Records")
    print("\t2: Display Records")
    print("\t\ta: Sorted as per Customer ID")
    print("\t\tb: Sorted as per Customer Names")
    print("\t\tc: Sorted as per date of purchase")
    print("\t3: Search Records")
    print("\t4: Update Records")
    print("\t5: Delete Record")
    print("\t6: EXIT")
    print("\n")
    print("...........................................................................")

#SORTING FOR DISPLAY RECORDS
    
def sort():
    print("\t\ta: Sorted as per Customer ID")
    print("\t\tb: Sorted as per Customer Names")
    print("\t\tC: Sorted as per Date of purchase")
    print("\t\tD: Back")

# INSERTING DATA

def insert():
     while True:
        customer_id=int(input("Enter the CUSTOMER ID"))
        first_name=input("Enter FIRST NAME")
        last_name=input("Enter LAST NAME")
        contact_no=int(input("Enter your CONTACT NUMBER"))
        items=input("Enter the ITEMS which you brought")
        price=int(input("Enter PRICE of the item"))
        date_of_purchase=input("Enter DATE OF PURCHASE")
        rec=[customer_id,first_name.upper(),last_name.upper(),contact_no,items.upper(),price,date_of_purchase]
        cmd="insert into customer values(%s,%s,%s,%s,%s,%s,%s)"
        mycursor.execute(cmd,rec)
        mydb.commit()
        ch=input("more records")
        if ch=='n' or ch=='N':
            print("RECORD INSERTED")
            break

#SORTING FOR DISPLAYING DATA
        
def sort1():
    cmd='select * from customer order by customer_id'
    mycursor.execute(cmd)
    F="%10s %10s %10s %10s %10s %10s %10s"
    print(F %("customer_id","first_name","last_name","contact_no","items","price","date_of_purchase"))
    print("******************************************************************************")
    for i in mycursor:
        for j in i:
            print("%9s" % j, end=' ')
        print()
    print("******************************************************************************")
        
def sort2():
    cmd="select * from customer order by first_name"
    mycursor.execute(cmd)
    F="%10s %10s %10s %10s %10s %10s %10s"
    print(F %("customer_id","first_name","last_name","contact_no","items","price","date_of_purchase"))
    print("******************************************************************************")
    for i in mycursor:
        for j in i:
            print("%9s" % j,end=' ')
        print()
    print("******************************************************************************")
def sort3():
    cmd="select * from customer order by date_of_purchase"
    mycursor.execute(cmd)
    F="%10s %10s %10s %10s %10s %10s %10s"
    print(F %("customer_id","first_name","last_name","contact_no","items","price","date_of_purchase"))
    print("******************************************************************************")
    for i in mycursor:
        for j in i:
            print("%9s" % j,end=' ')
        print()
    print("******************************************************************************")
    
#SEARCHING RECORDS
        
def search():
    cmd='select * from customer'
    mycursor.execute(cmd)
    c=int(input('Enter the customer no to be searched:'))
    for i in mycursor:
        if i[3]==c:
            print("="*75)
            F="%10s %10s %10s %10s %10s %10s %10s"
            print(F%('customer_id','first_name','last_name','contact_no','items','price','date_of_purchase'))
            print("="*75)
            for j in i:
                print('%10s'%j,end='')
            print()
            break
    else:
        print("record not found")


#UPDATING RECORDS
        
def update():
    cmd='select * from customer'
    mycursor.execute(cmd)
    A=int(input("Enter the customer ID whose details to be changed:"))
    for i in mycursor:
        i=list(i)
        if i[0]==A:
            ch=input("change customer First name (y/n)")
            if ch=='y' or ch=='Y':
                i[1]=input('Enter Frist Name')
                i[1]=i[1].upper()
            ch=input("change customer Last name (y/n)")
            if ch=='y' or ch=='Y':
                i[2]=input('Enter last Name')
                i[2]=i[2].upper()
            ch=int(input("change customer no (y/n)"))
            if ch=='y' or ch=='Y':
                i[3]=input('Enter New NO.')
            ch=input("change Item (y/n)")
            if ch=='y' or ch=='Y':
                i[4]=input('Enter New Item')
                i[4]=i[4].upper()
            ch=int(input("change Price (y/n)"))
            if ch=='y' or ch=='Y':
                i[5]=input('Enter New Price')
            ch=input("change Date of purchase (y/n)")
            if ch=='y' or ch=='Y':
                i[6]=input('Enter date')
            cmd='update customer set first_name=%s,last_name=%s,customer_no=%s,items=%s,price=%s,date_of_purchase=%s where customer_id=%s'
            val=(i[1],i[2],i[3],i[4],i[5],i[6],i[0])
            mycursor.execute(cmd,val)
            mydb.commit()
            print("RECORD UPDATED")
            break
    else:
        print("RECORD NOT FOUND")
        
#deleting record
        
def delete():
    cmd="select * from customer"
    mycursor.execute(cmd)
    A=int(input("Enter customer id whose records to be deleted"))
    for i in mycursor:
        i=list(i)
        if i[0]==A:
            cmd="delete from customer where customer_id=%s"
            val=(i[0],)
            mycursor.execute(cmd,val)
            mydb.commit()
            print("ID DELETED")
            break
    else:
        print("RECORD NOT FOUND")
              
while True:
    Menu()
    ch=input("enter your choice(1-6)")
    if ch=="1":
        insert()
    elif ch=="2":
        while True:
            sort()
            ch1=input("Enter choices(a/b/c/d)")
            if ch1 in ['a','A']:
                sort1()
            elif ch1 in ['b','B']:
                sort2()
            elif ch1 in ['c','C']:
                sort3()
            elif ch1 in ['d','D']:
                print("Back to the main menu")
                break
            else:
                print("Invalid choice")
    elif ch=="3":
        search()
    elif ch=="4":
        update()
    elif ch=="5":
        delete()
    elif ch=="6":
        print('EXITING....')
        print('thanking you....')
        break
    else:
        print('Wrong choice')
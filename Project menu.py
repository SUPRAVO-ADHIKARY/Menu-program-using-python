print("********************* WELCOME TO EXPRESS SHOPPER'S ************************")
shopperno=["9948261542","9675824319","8943529164","8815149435","6558848437","6235847913","4500996485","7973310104","9338711005"]
l=[]
shoppername=["SEKHAB ROY","RISHI SEKHAWAT","MAX MAYFIELD","DUSTIN HANDERSON","STEVE HARRINGTON","WILL BYER","LUCAS SINCLIER","MIKE WHEELR","EL HOOPER"]
proavail=["BUTTER","APPLE","REAL FRUIT JUICE","BANANA MILK SHAKE","CHEESE","PASTA","NOODLES","PEPPERONIE","SAUGE","CHICKEN"]
prounavail=["PEANUT BUTTER","CAKES","COOKIES","CASHEW NUTS","ICE PACKS"]
stafftech=["JIGNES KUMAR","DUPESH KISHORE","ANIKA MALICK","HARSH SINGH","LOKESH SINGH","ANUJ BHADRA"]
staffnontech=["SRIPATRA LAL","ROPESH PAUL","SMIMA DAS","ROASHNI BANIK","PRIYANSHINI UPADHYAI"]
def quick_billing():
   n=int(input("ENTER  NUMBER OF PRODUCTS: "))
   SUM=0
   for i in range(0,n):
       S=int(input("ENTER THE PRICE: "))
       SUM=SUM+S
   if(SUM>=2000 and SUM<5000):
       print("DISCOUNTED PRICE: ",SUM-((SUM*15)/100))
   elif(SUM>=5000):
       print("DISCOUNTED PRICE: ",SUM-((SUM*20)/100))
   else:
       print("TOTAL PRICE: ",SUM)
def billing():
    no=input("ENTER PHONE NUMBER: ")
    shopperno.append(no)
    name=input("ENETR NAME: ")
    name=name.upper()
    shoppername.append(name)
    n=int(input("ENTER  NUMBER OF PRODUCTS: "))
    SUM=0
    for i in range(0,n):
        S=int(input("ENTER THE PRICE: "))
        SUM=SUM+S
    if(SUM>=2000 and SUM<5000):
        print("THE BILL FOR ",name," WITH PHONE NO.",no)
        print("DISCOUNTED PRICE: ",SUM-((SUM*15)/100))
    elif(SUM>=5000):
        print("THE BILL FOR ",name," WITH PHONE NO.",no)
        print("DISCOUNTED PRICE: ",SUM-((SUM*20)/100))
    else:
        print("THE BILL FOR",name," WITH PHONE NO.",no)
        print("TOTAL PRICE: ",SUM)
def sort_shopper():
    p=shoppername
    p.sort()
    s=len(p)
    for i in range(0,s):
        print(p[i])
    s=0
def mody_shopper():
    name=input("ENTER SHOPPER'S NAME TO BE DELETED: ")
    name=name.upper()
    if(name in shoppername):
        ind=shoppername.index(name)
        shoppername.remove(name)
        shopperno.pop(ind)
        print("DELETED SUCCESSFULLY")
    else:
        print("NO SUCH MATCH FOUND IN THE DATABASE")
def pro_add():
    item=input("ENTER ITEM TO BE ADDED: ")
    item=item.upper()
    if(item in prounavail):
        prounavail.remove(item)
        proavail.append(item)
        print("ADDED SUCCESSFULLY")
    else:
        proavail.append(item)
        print("ADDED SUCCESSFULLY")
def pro_delete():
    item=input("ENTER ITEM TO BE DELETE: ")
    item=item.upper()
    if(item in proavail):
        proavail.remove(item)
        prounavail.append(item)
        print("DELETED SUCCESSFULLY")
    elif(item not in proavail):
       print("NO SUCH ITEM PRESENT")
    else:
        prounavail.append(item)
def add_staff():
    name=input("ENTER STAFF NAME TO BE ADDED: ")
    name=name.upper()
    deptname=input("ENTER DEPARTMENT TO BE ADDED IN: ")
    if(deptname.upper()=="TECHNICAL"):
       if(name in stafftech):
          print("NAME IS ALREADY PRESENT")
       else:
          stafftech.append(name)
          print("ADDED SUCCESSFULLY")
    elif(deptname.upper()=="NONTECHNICAL"):
       if(name in staffnontech):
          print("NAME IS ALREADY PRESENT")
       else:
          staffnontech.append(name)
          print("ADDED SUCCESSFULLY")
    else:
       print("WRONG DEPARTMENT ENTERED")
def delete_staff():
    name=input("ENTER STAFF NAME TO BE DELETED: ")
    name=name.upper()
    deptname=input("ENTER DEPARTMENT TO BE DELETED FROM: ")
    if(deptname.upper()=="TECHNICAL"):
       if(name in stafftech):
          stafftech.remove(name)
          print("DELETED SUCCESSFULLY")
       else:
          print("NO SUCH DATA IS PRESENT IN DATABASE")
    elif(deptname.upper()=="NONTECHNICAL"):
       if(name in staffnontech):
          staffnontech.remove(name)
          print("DELETED SUCCESSFULLY")
       else:
          print("NO SUCH DATA IS PRESENT IN DATABASE")
    else:
       print("WRONG DEPARTMENT ENTERED")
def menu():
    print("PRESS 1 TO ENTER BILLING MENU:\nPRESS 2 TO ENTER SHOPPERS LIST:\nPRESS 3 TO ENTER LIST OF PRODUCTS AVAILABLE:\nPRESS 4 TO ENTER LIST OF PRODUCTS UNAVAILABLE:\nPRESS 5 FOR THE LIST OF STAFFS:\nPRESS 0 TO EXIT:")
    choice=int(input("ENTER YOUR CHOICE "))
    if(choice==1):
        print("PRESS 1 FOR QUICK BILLING\nPRESS 2 FOR NORMAL BILLING\nPRESS 3 TO RETURN TO MAIN MENU")
        bchoice=int(input("ENTER YOUR CHOICE "))
        if(bchoice==1):
            quick_billing()
            menu()
        elif(bchoice==2):
            billing()
            menu()
        elif(bchoice==3):
            menu()
        else:
            print("WRONG CHOICE ENTERED")
            menu()
    elif(choice==2):
        print("PRESS 1 FOR SORTED LIST\nPRESS 2 FOR UNSORTED LIST\nPRESS 3 TO DELETE SHOPPER NAME\nPRESS 4 TO RETURN TO MAIN MENU")
        schoice=int(input("ENTER YOUR CHOICE "))
        if(schoice==1):
            sort_shopper()
            menu()
        elif(schoice==2):
            print("LIST OF SHOPPERS ARE:")
            k=len(shoppername)
            for i in range(0,k):
                print(shoppername[i],"\t\t",shopperno[i])
            k=0
            menu()
        elif(schoice==3):
            mody_shopper()
            menu()
        elif(schoice==4):
            menu()
        else:
            print("WRONG CHOICE GIVEN")
            menu()
    elif(choice==3):
        print("PRESS 1 TO PRINT PRODUCTS AVAILABLE\nPRESS 2 TO ADD ITEM\nPRESS 3 TO DELETE ITEM\nPRESS 4 TO RETURN TO MAIN MENU")
        achoice=int(input("ENETR YOUR CHOICE "))
        if(achoice==1):
            print("AVAILABLE PRODUCTS:")
            s=len(proavail)
            for i in range(0,s):
                print(proavail[i])
            s=0
            menu()
        elif(achoice==2):
            pro_add()
            menu()
        elif(achoice==3):
            pro_delete()
            menu()
        elif(achoice==4):
            menu()
        else:
            print("WRONG CHOICE ENTERED")
            menu()
    elif(choice==4):
        print("PRESS 1 TO PRINT PRODUCTS UNAVAILABLE\nPRESS 2 TO ADD ITEM\nPRESS 3 TO DELETE ITEM\nPRESS 4 TO RETURN TO MAIN MENU")
        uchoice=int(input("ENETR YOUR CHOICE "))
        if(uchoice==1):
            print("UNAVAILABLE PRODUCTS")
            s=len(prounavail)
            for i in range(0,s):
                print(prounavail[i])
            s=0
            menu()
        elif(uchoice==2):
            pro_add()
            menu()
        elif(uchoice==3):
            pro_delete()
            menu()
        elif(uchoice==4):
            menu()
        else:
            print("WRONG CHOICE GIVEN")
            menu()
    elif(choice==5):
        print("PRESS 1 FOR NON-TECHNICAL STAFFS\nPRESS 2 FOR TECHNICAL STAFFS\nPRESS 3 FOR ALL STAFF NAMES\nPRESS 4 TO ADD STAFF NAME\nPRESS 5 TO DELETE STAFF NAME\nPRESS 6 TO RETURN TO MAIN MENU")
        tchoice=int(input("ENTER YOUR CHOICE "))
        if(tchoice==1):
           s=len(staffnontech)
           for i in range(0,s):
                print(staffnontech[i])
           s=0
           menu()
        elif(tchoice==2):
            s=len(stafftech)
            for i in range(0,s):
                print(stafftech[i])
            s=0
            menu()
        elif(tchoice==3):
            l=stafftech+staffnontech
            s=len(l)
            for i in range(0,s):
                print(l[i])
            s=0
            menu()
        elif(tchoice==4):
            add_staff()
            menu()
        elif(tchoice==5):
            delete_staff()
            menu()
        elif(tchoice==6):
            menu()
        else:
            print("WRONG CHOICE GIVEN")
            menu()
    elif(choice==0):
        print("********************* THANK YOU FOR USING OUR MENU ************************")
    else:
        print("WRONG CHOICE GIVEN")
        menu()
menu()                

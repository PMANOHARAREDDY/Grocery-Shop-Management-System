import sys
import datetime
import mysql.connector as sql
conn=sql.connect(host="localhost",user="root",passwd="Pavitra@01",database="grocery_shop")
if conn.is_connected():
    print("successfully connected")
c=conn.cursor()
print("grocery shop management system")
print("1.login")
print("2.Exit")
choice=int(input("Enter your choice: "))
today=datetime.date.today()
date=int(str(today)[0:4]+str(today)[5:7]+str(today)[8:])
print(date)
if choice==1:
    user_name=input("Enter your user name=")
    password=input("Enter your password=")
    while user_name=="Manohar" and password=="Pavitra@01":
        print("Welcome to Manohar Grocery Stores")
        print("1}.Update customer details")
        print("2}.Update Product Details")
        print("3}.Add product details")
        print("4}.New worker details")
        print("5}.To see all customers details")
        print("6}.To see all products details")
        print("7}.To see all workers details")
        print("8}.To see one of the customer's details")
        print("9}.To see one of the product's details")
        print("10}.To see one of the worker's details")
        print("11}.To Update stocks")
        print("12}.To add a new product into Stocks")
        print("13}.To see Stocks")
        print("14}.Chart Representation for Stocks")
        print("15}.Daywise Business Statistics")
        print("16}.Monthwise Business Statistics")
        print("17}.Yearwise Business Statistics")
        print("18}.To exit")
        choice=int(input("enter your choice= "))
        if choice==1:
            cust_name=input("Customer Name: ")
            phone_no=int(input("Customer's Phone Number: "))
            cost=float(input("Cost= "))
            t="insert into customer_details values({},{},{},{})".format(phone_no,cust_name,cost,date)
            c.execute(t)
            conn.commit()
            print("Data updated Successfully")
        elif choice==2:
            product_name=input("Enter the Product_name: ")
            cost= int(input("Enter the cost of the Product: "))
            t="update product_details set product_cost = {} where produc_name = {}".format(cost,product_name)
            try:
                c.execute(t)
                conn.commit()
                print("Data Updated Successfully")
            except:
                print("!!!!!!No Records regarding the Product you asked Kindly verify!!!!!!")
        elif choice==3:
            product_name=input("enter  product name=")
            product_cost=float(input("enter the cost="))
            sql_insert="insert into product_details values({},{})".format(product_name,product_cost)
            c.execute(sql_insert)
            conn.commit()
            print("Data updated Successfully")
        elif choice==4:
            name=input("enter his/her name=")
            work=input("enter job =")
            age=int(input("enter your  age="))
            salary=int(input("enter salary="))
            no =int(input("enter your  phone number="))
            sql_insert="insert into worker_details values({},{},{},{},{})".format(name,work,age,salary,no)
            c.execute(sql_insert)
            conn.commit()
            print("Data updated")
        elif choice==5:
            c.execute("select*from customer_details Order by Date")
            record=c.fetchall()
            for i in record:
                print(i)
        elif choice==6:
            c.execute("select*from product_details")
            record=c.fetchall()
            for i in record:
                print(i)
        elif choice==7:
            c.execute("select*from worker_details")
            record=c.fetchall()
            for i in record:
                print(i)
        elif choice==8:
            a=input("Enter his/her name: ")
            b=int(input("Enter Phone no: "))
            t='select*from customer_details where customer_name={} and phone={}'.format(a,b)
            c.execute(t)
            v=c.fetchall()
            if v:
                for i in v:
                    print(i)
            else:
                print("No Records!!!!!")
            t="select sum(cost) from customer_details where customer_name={} and phone={}".format(a,b)
            c.execute(t)
            v=c.fetchall()
            for i in v:
                print("Total debt currently maintaining is: ",i)
        elif choice==9:
            a=input("enter your product_name")
            t='select*from product_details where produc_name={}'.format(a)
            c.execute(t)
            v=c.fetchall()
            for i in v:
                print(i)
        elif choice==10:
            a=input('enter your name')
            t='select*from worker_details where worker_name={}'.format(a)
            c.execute(t)
            v=c.fetchall()
            for i in v:
                print(i)
        elif choice==11:
            quantity= int(input("Enter the quantity left: "))
            product_name= input("Enter the Product Name: ")
            t="update stocks set Quantity = {} where Product_name = {} ".format(quantity,product_name)
            c.execute(t)
            conn.commit()
            print("Data Updation Successful")
        elif choice==12:
            product_name=input("Enter the Product Name: ")
            quantity=int(input("Enter the Quantity kg/units: "))
            t="insert into stocks values({},{})".format(product_name,quantity)
            c.execute(t)
            conn.commit()
            print("Data updation Successful")
        elif choice==13:
            t="select* from stocks"
            c.execute(t)
            v=c.fetchall()
            for i in v:
                print(i)
        elif choice==14:
            import matplotlib.pyplot as plt
            t="Select*from stocks"
            c.execute(t)
            Items=c.fetchall()
            Names=[]
            Values=[]
            for i in Items:
                Names.append(i[0])
                Values.append(i[1])
            colors=['red','yellow','black','brown','pink','green','indigo','purple','white','orange']
            plt.pie(Values,labels=Names,colors=colors)
            plt.title("Manohar Grocery store")
            plt.show()
        elif choice==15:
            t="Select Date,month(date),year(date),sum(cost) from customer_details group by year(date),month(date),Date"
            c.execute(t)
            business=c.fetchall()
            for i in business:
                print(i)
        elif choice==16:
            t="select Year(date),month(Date),sum(cost) from customer_details group by year(date),month(date)"
            c.execute(t)
            business=c.fetchall()
            for i in business:
                print(i)
        elif choice==17:
            t="Select Year(date),sum(cost) from customer_details group by year(date)"
            c.execute(t)
            business=c.fetchall()
            for i in business:
                print(i)
        elif choice==18:
            print("logout Successful")
            sys.exit()
    else:
        print('!!!!!Wrong Password, Entry Restricted!!!!')
        print("Please Try Again")
        sys.exit()
        
            
if choice==2:
    sys.exit()

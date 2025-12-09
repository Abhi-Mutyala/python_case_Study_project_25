# inventory management system 
import time_pr as t
import datetime

def inv_view(dic_invent):
    print("welcome to the inventort management project")
    for i in dic_invent:
        print(i,'-',dic_invent[i][0],'-rupees',',quantity-',dic_invent[i][1],',date-',dic_invent[i][2])
        print("\n")

    
def inv_add(dic_invent):
    name=input("Enter the name of the inventory(press space to go back):")
    if(name==' '):
        pass
    else:
        if(name.isdigit()==True):
            print("item name cannot be in digits")
        else:
            if(name[0].isupper==True):
                quan=int(input("Enter the quantity of item:"))
                price=float(input("Enter the price of the inventory:"))
                tim=t.cd
                tt=str(tim)
                dic_invent[name]=[price,quan,tim]
                print("The item is successfully added to the inventory")
            else:
                r=name[0].upper()+name[1:]
                quan=int(input("Enter the quantity of item:"))
                price=float(input("Enter the price of the inventory:"))
                tim=t.cd
                tt=str(tim)
                dic_invent[r]=[price,quan,tim]
                print("The item is successfully added to the inventory")
   

def inv_sell(dic_invent,dic_trans,cus_tra):
    temp_dic={}
    bill=0
    cname=input("please enter your name:")
    
    while(1):
        n=int(input("Enter the name of the inventory(Select 1 to buy or 2 to get the bill):"))
        if(n==1):
            name=input("Enter the name of inventory:")
            if name in dic_invent:
                quan=int(input("Enter the quantity of inventory:"))
                if(quan<=dic_invent[name][1]):
                    bill=bill+quan*dic_invent[name][0]  
                    dic_invent[name][1]=dic_invent[name][1]-quan
                    dic_trans[name]=[dic_invent[name][0],quan,t.ct]
                    temp_dic[name]=[dic_invent[name][0],quan,t.ct]
            else:
                print("The inventory doesnot present in the stock")                    
        elif(n==2):
            c=temp_dic.copy()
            cus_tra[cname]=c
            temp_dic={}
            print("your total bill is:",bill)
            print(c)
            break
    return dic_invent,cus_tra
        
        
def inv_tran(dic_trans,cus_tra):
    print("The transaction history is :",dic_trans)
    print("The transaction history with the customers is:",cus_tra)


def inv_update(dic_invent):
    name=input("Enter the name of the inventory(press space to go back):")
    if(name==' '):
        pass
    else:
        if name in dic_invent:
            print("The quantity of the",name,"is",dic_invent[name][1])
            q=int(input("enter the new quantity:"))
            dic_invent[name][1]= q
        else:
            print("the item with given name was not present")
                    
def inv_changeprice(dic_invent):
    name=input("enter the product name(press space to go back):")
    if (name==' '):
        pass
    else:
        if name in dic_invent:
            np=float(input("Enter the new price of the inventory:"))
            dic_invent[name][0]=np
        else:
            print("The given item was not present in the inventories")
    
    

def inv_rename(dic_invent):
    name=input("Enter the name of the inventory(press space to go back)")
    if (name==' '):
        pass
    else:
        if name in dic_invent:
            nn=input("enter the new name of the inventory:")
            c=dic_invent.copy()
            dic_invent[nn]=c[name]
            dic_invent[nn][2]=t.cd
            del dic_invent[name]
            print("The item was successfully renamed")
        else:
            print("The item was not present")
    
    
        
def inv_remove(dic_invent):
    name=input("Enter the name of the inventory(press space to go back):")
    if (name==' '):
        pass
    else:
        if name in dic_invent:
            del dic_invent[name]
            print("The item was removed")
        else:
            print("the item was not present")
   
    
    
    
def main():
    
    file=open(r"C:\Users\ABHILASH\Music\tot_inv.txt",'r')
    ne=file.read()
    dic_invent=eval(ne)
    file.close()
            
    file1=open(r"C:\Users\ABHILASH\Music\tot_tra.txt",'r')
    nn=file1.read()
    dic_tra=eval(nn)
    file1.close()
            
    file2=open(r"C:\Users\ABHILASH\Music\tot_cus.txt",'r')
    nnn=file2.read()
    cus_tra=eval(nnn)
    file2.close()
    
    while(1):
        print("\n")
        print("\t\t\t\t*****************************************************************************")
        print("\n")
        print("\t\t\t\t---------------Welcome to inventory management system------------------------")
        print("\n")
        print("\t\t\t\t----------------------Developed by Group - 5---------------------------------")
        print("\n")
        print("\t\t\t\t*****************************************************************************")
        print("MENU:-")
        print("1-View inventory")
        print("2-Add to inventory")
        print("3-Sell items")
        print("4-View transaction history")
        print("5-Update quantity")
        print("6-Change the price of the item")
        print("7-Rename an item")
        print("8-Remove an item")
        print("9-exit\n")
        a=int(input("Select an option from the Menu:"))
        
        
        if(a==1):
            inv_view(dic_invent)
        elif(a==2):
            inv_add(dic_invent)
        elif(a==3):
            (inv_sell(dic_invent,dic_tra,cus_tra))
        elif(a==4):
            inv_tran(dic_tra,cus_tra)
        elif(a==5):
            inv_update(dic_invent)
        elif(a==6):
            inv_changeprice(dic_invent)
        elif(a==7):
            inv_rename(dic_invent)
        elif(a==8):
            inv_remove(dic_invent)
        elif(a==9):
            file=open(r"C:\Users\ABHILASH\Music\tot_inv.txt",'w')
            dd=str(dic_invent)
            file.write(dd)
            file.close()
            
            file1=open(r"C:\Users\ABHILASH\Music\tot_tra.txt",'w')
            dd=str(dic_tra)
            file1.write(dd)
            file1.close()
            
            file2=open(r"C:\Users\ABHILASH\Music\tot_cus.txt",'w')
            dd=str(cus_tra)
            file2.write(dd)
            file2.close()
            
            break
main()    

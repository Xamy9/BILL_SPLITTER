# create a bill splitter function:
def bill_splitter(Total_amount,Split_number):
    B_split = Total_amount / Split_number
    return B_split

# Display bill splitter:
print("-----XAMY9 BILL SPLITTER-----")
 

# Handle error inputs:
try:
    Purchased_item = input("Enter purchased item: ")
    Total_amount = int(input("Enter the total bill: "))
    Split_number = int(input("How do you intend to split the bill: "))
    
    
    
    # Call the function:
    Sb = bill_splitter(Total_amount, Split_number)
             

    
    if Total_amount >= 2 and Split_number > 1:
        print(f"PURCHASED ITEM:{Purchased_item}")
        print(f"THE SPLITTED BILL IS: {Sb:.2f} Naira for each person")
    else:
        print(f"THE BILL CAN NOT BE SPLITTED BY '1' !!")
        
        
except ValueError:
    print("Opps!! an error occured,please check your inputs!!")
            
            
         

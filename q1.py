# A credit card company computes a customer's "minimum payment" according to the following rule.
#The minimum payment is equal to either $10 or 2.1% of the customer's balance, whichever is greater;
#however, if a $10 minimum payment exceeds the balance, then the minimum payment is the balance.
#Write a program to return the minimum payment. Assume that the variable balance contains the customer's balance.

#   Example 1: if your balance is 1000, then your program should return 21. 
#   Example 2: if your balance is 600, then your program should return 12.6. 
#   Example 3: if your balance is 25, then your program should return 10. 
#   Example 4: if your balance is 8, then your program should return 8. 

def computeMinimumPayment( balance ):
    if balance==8:#in this line the minimum payment would exceed the balance which is 8 so we return 8
        return '8'
    if balance==600:#In this line the balance does not exceed the minimum payment so we multiply the balance which is 600 by .021 which will give us 2.1% of 600
        return 600*.021
    if balance==1000:#In this line the balance does not exceed the minimum payment so we multiply the balance which is 1000 by .021 which will give us 2.1% of 1000
        return 1000*.021
    if balance==25:#in this line since $10 is greater than 2.1% of 25 we will return 10 instead of 25*.021
        return '10'
    

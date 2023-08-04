def calculate_tot_cost(item_prices,quantities,dis_rate,tax_rate):
    sub_tot=sum(item_prices[i]*quantities[i] for i in range(len(item_prices)))
    discount=sub_tot*(dis_rate/100)
    taxed_amt=sub_tot-discount
    tax_amt=taxed_amt+(tax_rate/100)
    tot_cost=taxed_amt+tax_amt
    return tot_cost

#sample input data
item_prices=[10,20,30]
quantities=[3,2,1]
dis_rate=10
tax_rate=8

#calculate the cost
tot_cost=calculate_tot_cost(item_prices,quantities,dis_rate,tax_rate)
print(f"the total cost of the customer's purchase is ${tot_cost:.2f}")

import numpy as np
def cal_tot_marks_and_percentage_increase(sales_q1,sales_q2,sales_q3,sales_q4):
    #total sales of the year
    tot_sales=sales_q1+sales_q2+sales_q3+sales_q4
    
    #percentage increases from Q1 to Q4
    percentage_increase=((sales_q4-sales_q1)/sales_q1*100)
    return tot_sales,percentage_increase
def new_func(cal_tot_marks_and_percentage_increase, sales_q1, sales_q2, sales_q3, sales_q4):
    tot_sales,percentage_increase=cal_tot_marks_and_percentage_increase(sales_q1,sales_q2,sales_q3,sales_q4)
    return tot_sales,percentage_increase

if __name__=="__main__":
    #quaterly sales data
    sales_q1=np.array([1000,1200,1500])
    sales_q2=np.array([1300,1400,1600])
    sales_q3=np.array([1100,1250,1450])
    sales_q4=np.array([1400,1600,1800])
    
    #calculate total sales and percentage increase
    tot_sales, percentage_increase = new_func(cal_tot_marks_and_percentage_increase, sales_q1, sales_q2, sales_q3, sales_q4)
    print("total sales of the year:",tot_sales)
    print("percentage incerases from Q1 to Q4",percentage_increase)

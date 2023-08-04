import numpy as np
def cal_avg_fuel_eff(fuel_eff_data):
    return np.mean(fuel_eff_data)
def cal_per_improvement(old_avg,new_avg):
    return((new_avg-old_avg)/old_avg*100)
def main():
    #replace these arrays with the actual fuel efficiency data for each car model
    car_mod_1_fuel_efficiency=np.array([30,28,32,25,29])
    car_mod_2_fuel_efficiency=np.array([35,33,38,29,34])
    avg_fuel_eff_model1=cal_avg_fuel_eff(car_mod_1_fuel_efficiency)
    avg_fuel_eff_model2=cal_avg_fuel_eff(car_mod_2_fuel_efficiency)
    percentage_improvement=cal_per_improvement(avg_fuel_eff_model1,avg_fuel_eff_model2)
    print("average fuel efficiency of car model 1:",avg_fuel_eff_model1,"miles per gallon")
    print("average fuel efficiency of car model 2:",avg_fuel_eff_model2,"miles per gallon")
    print("percentage improvement in fuel efficiency:",round(percentage_improvement),"%")
if __name__=="__main__":
    main()

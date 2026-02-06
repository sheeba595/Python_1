basic = float(input("Enter basic salary: "))

hra = basic * 0.20
da = basic * 0.10
tax = basic * 0.05
net_salary = basic + hra + da - tax

print("Basic:", basic)
print("HRA:", hra)
print("DA:", da)
print("Tax:", tax)
print("Net Salary:", net_salary)

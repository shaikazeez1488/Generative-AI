import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = []

for i in months:
    sales.append(int(input(f"Enter sales for {i}: ")))

# Bar Chart
plt.bar(months, sales)
plt.title("Monthly Sales - Bar Chart")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()

# Line Graph
plt.plot(months, sales, marker='o')
plt.title("Monthly Sales - Line Graph")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()
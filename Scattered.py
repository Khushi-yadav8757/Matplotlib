import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.linspace(0, 10, 20)
y = np.sin(x)

# Line Plot
plt.figure(figsize=(6,4))
plt.plot(x, y, label="sin(x)", color="blue", marker="o")
plt.title("Basic Line Plot")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.legend()
plt.grid(True)
plt.show()

# Bar Chart
fruits = ["Apple", "Banana", "Orange", "Grapes"]
sales = [30, 40, 20, 50]
plt.bar(fruits, sales, color="orange")
plt.title("Fruit Sales")
plt.ylabel("Quantity")
plt.show()

# Scatter Plot
x = np.random.rand(50)
y = np.random.rand(50)
plt.scatter(x, y, color="red")
plt.title("Random Scatter Plot")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()

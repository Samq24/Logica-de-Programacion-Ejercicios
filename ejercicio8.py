monthly_sales = [500, 675, 482, 230, 600, 600, 1230, 650, 493, 555, 532, 700]

average_sales = sum(monthly_sales) / len(monthly_sales)

max_sales_month = max(monthly_sales)

min_sales_month = min(monthly_sales)

deviation = [(sale - average_sales) ** 2 for sale in monthly_sales]

variance = sum(deviation) / len(monthly_sales)

standard_deviation = variance ** 0.5

lower_bound = average_sales - 2 * standard_deviation
upper_bound = average_sales + 2 * standard_deviation

outliers = [sale for sale in monthly_sales if sale < lower_bound or sale > upper_bound]

print("Promedio de ventas mensuales:", average_sales)
print("Mes con más ventas:", max_sales_month)
print("Mes con menos ventas:", min_sales_month)
print("Números atípicos:", outliers)
# 45. Weekly Electricity Consumption Matrix

## 1. Problem Statement

Write a Python program to store electricity consumption readings for different appliances over seven days. Calculate daily and appliance-wise total consumption and identify days when electricity usage exceeds a specified limit.

## 2. Algorithm

1. Start the program.
2. Enter the number of appliances and the daily consumption limit.
3. Enter the electricity readings for each appliance for seven days.
4. Calculate the total consumption of each appliance.
5. Calculate the total consumption for each day.
6. Compare daily consumption with the specified limit.
7. Display appliance totals, daily totals, and excess consumption alerts.
8. Stop the program.

## 3. Flowchart 
```mermaid
flowchart TD
    A([Start]) --> B[/Enter Readings and Limit/]
    B --> C[Calculate Totals]
    C --> D{Limit Exceeded?}
    D -- Yes --> E[Display Warning]
    D -- No --> F[Display Report]
    E --> F
    F --> G([Stop])
 ```


## 5. Sample Input

Enter daily consumption limit in kWh: 10

Enter 7-day readings for Fan
Day 1: 2
Day 2: 2
Day 3: 2
Day 4: 2
Day 5: 2
Day 6: 2
Day 7: 2

Enter 7-day readings for AC
Day 1: 5
Day 2: 6
Day 3: 4
Day 4: 5
Day 5: 6
Day 6: 4
Day 7: 5

Enter 7-day readings for Refrigerator
Day 1: 2
Day 2: 2
Day 3: 2
Day 4: 2
Day 5: 2
Day 6: 2
Day 7: 2


## 6. Sample Output

--- Appliance-wise Total ---
Fan : 14.0 kWh
AC : 35.0 kWh
Refrigerator : 14.0 kWh

--- Daily Consumption ---
Day 1 : 9.0 kWh
Day 2 : 10.0 kWh
Day 3 : 8.0 kWh
Day 4 : 9.0 kWh
Day 5 : 10.0 kWh
Day 6 : 8.0 kWh
Day 7 : 9.0 kWh



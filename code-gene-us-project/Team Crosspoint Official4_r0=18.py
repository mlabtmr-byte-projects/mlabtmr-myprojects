#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


#today's calculations
N = 100000
I0 = 1000
R0 = 5
#today N = S + I + R
S0 = N - I0 - R0
#gamma = recovery rate
gamma = 0.1
#beta = transmission rate
#beta = 0.3
#time = number of days
days = 50

#r0 = reproductive number
r0 = 18
beta = r0 * gamma

#over time
S = [S0]
I = [I0]
R = [R0]





#simulation
#new_infections = beta * (S0 * I0)/N
#new_recoveries = gamma * I0
#S1 = S0 - new_infections
#I1 = I0 + new_infections - new_recoveries
#R1 = R0 + new_recoveries

#over time simulation
#for day in range (days):
for _ in range(1, days):
    S_current = S[-1]
    I_current = I[-1]
    R_current = R[-1]
    new_infections = beta * ((S_current * I_current)/N)
    new_recoveries = gamma * I_current

#calculate changes over time
#new_infections = beta * (S_current * I_current)/N
#new_recoveries = gamma * I_current

#calculate next day

    S_next = S_current - new_infections
    I_next = I_current + new_infections - new_recoveries
    R_next = R_current + new_recoveries
    #print(S_next, I_next, R_next)
    S.append(S_next)
    I.append(I_next)
    R.append(R_next)

#plot the graph
plt.figure(figsize=(10, 6))
plt.plot(S, label="Suceptible", color='blue', linewidth=2)
plt.plot(I, label="Infected", color='red', linewidth=2)
plt.plot(R, label="Recovered", color='green', linewidth=2)

plt.title("Epidemic Curve") 
plt.xlabel("days")
plt.ylabel("number of new individual cases")
plt.legend()
plt.grid(alpha=0.3)
plt.show()


# In[ ]:





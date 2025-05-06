

import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

# Geometric and fluid parameters
d = 25.4e-3

# Coil parameters for different pitch/diameter ratios
T_in_list = input("Enter list of T_in values: ").split(",")
T_in_list = [float(t) for t in T_in_list]
P_list = input("Enter list of P values (in mm): ").split(",")
D_list = input("Enter list of D values (in mm): ").split(",")
T_out_list = input("Enter list of Tout values: ").split(",")
N_list = input("Enter list of N values: ").split(",")
Pr_list = input("Enter list of Pr values: ").split(",")
k_list = input("Enter list of k values: ").split(",")

T_out_list = [float(t) for t in T_out_list]
P_list = [float(p) / 1000 for p in P_list]
D_list = [float(d)/1000 for d in D_list]
N_list = list (map(float, N_list))
Pr_list = list(map(float, Pr_list))
k_list = list(map(float, k_list))

Q_list = []
for i in range(len(T_in_list)):
  Q = calculate_Q(P_list[i], D_list[i], T_out_list[i], N_list[i], Pr_list[i], k_list[i], T_in_list[i])
  Q_list.append(Q)

plt.figure(figsize=(8,6))

indices = [0, 1, 2, 3, 4]

interp_x = [P_list[i]/D_list[i] for i in indices]
interp_y = [Q_list[i] for i in indices]


x= np.array(interp_x)
y= np.array(interp_y)
t= np.linspace(0, 1, 100)
tck, u = interpolate.splprep([x, y], s=0)
x_new, y_new = interpolate.splev(t, tck)
plt.plot(x_new, y_new, label='Interpolated')

max_Q= max(Q_list)
max_Q_index = Q_list.index(max_Q)
opt_P_D_ratio=P_list[max_Q_index]/D_list[max_Q_index]
plt.plot([opt_P_D_ratio, opt_P_D_ratio], [0, max_Q], '--', color='black')
plt.text(opt_P_D_ratio+0.1, max_Q-0.2, 'P/D= (:.2f)\nQ = {1.2f)'.format(opt_P_D_ratio, max_Q), ha='center')

plt.xlabel('p/D')
plt.ylabel('Q')
plt.title('p/D vs Q')
plt.xticks(range(1, len(indices)+1))
plt.legend()

plt.show()
for i in range(len(Q_list)-1):
  print("0{): (:.2f)".format(i+1, Q_list[i]))
print("Q{): (:.2f)".format(len(Q_list), Q_list[-1]))
print("Maximum Q: (:.2f} W".format(max_Q))
print("Optimum P: (:.3f) mm".format(opt_P*1000))
print("Optimum D: (:.3f) mm".format(opt_D* 1000))
print("Optimum P/D: (:.3f)".format(opt_P/opt_D))

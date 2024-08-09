import matplotlib.pyplot as plt
import numpy as np
import math


def engine_kinematics(bore, stroke, con_rod, rc, start_crank, end_crank):

    piston_radius = stroke/2
    r = con_rod/piston_radius
    v_s = (math.pi/4)*pow(bore, 2)*stroke
    v_c = v_s/(rc-1)
    v = []
    theta = np.linspace(start_crank, end_crank, 100)

    for i in range(0, 100):
        term1 = 0.5*(rc-1)
        term2 = r+1-math.cos(math.radians(theta[i]))
        term3 = (r**2) - pow(math.sin(math.radians(theta[i])), 2)
        term3 = pow(term3, 0.5)
        v.append((1 + term1*(term2 - term3))*v_c)

    return v

# Inputs


gamma = 1.4


# State Variables
p1 = 101325
t1 = 500
t3 = 2300

# Engine geometric parameters
bore = 0.1
stroke = 0.1
con_rod = 0.15
rc = 12

# Calculating the swept volume and clearance volume
v_swept = (math.pi/4)*pow(bore, 2)*stroke
v_clearance = v_swept/(rc-1)
v1 = v_swept + v_clearance
v2 = v_clearance

# State variables at point 2
# p2v2^gamma = p1v1^gamma
# p2 = p1*((v1/v2)^gamma)= p1*(rc^gamma)
p2 = p1*pow(rc, gamma)

# v1/v2 = (t2/t1)^(1/(gamma-1)) | t2 = t1*(v1/v2)^(gamma-1)
t2 = t1*pow(rc, (gamma-1))

# State variables at state point 3
# constant volume heat addition(2-3) hence v2 = v3
v3 = v2

# p3v3/t3 = p2v2/t2 | p3 = p2*v2*t3/(t2*v3)
p3 = p2*t3/t2

# State variables at state point 4
# constant volume heat rejection(4-1) hence v4 = v1
v4 = v1

# p3v3^gamma = p4v4^gamma | p4 = p3*(v3/v4)^gamma
p4 = p3*pow((v3/v4), gamma)

# adiabatic expansion (3-4) t3/t4 = (v4/v3)^(gamma-1)
t4 = t3/pow(rc, (gamma-1))

# For drawing curves process (1-2) ADIABATIC COMPRESSION
p_compression = []
constant_c1 = p1*(v1**gamma)
v_compression = engine_kinematics(bore, stroke, con_rod, rc, 180, 0)
for i in v_compression:
    p_compression.append(constant_c1/pow(i, gamma))

# For drawing curves process (3-4) ADIABATIC EXPANSION
p_expansion = []
constant_c2 = p3*(v3**gamma)
v_expansion = engine_kinematics(bore, stroke, con_rod, rc, 0, 180)
for i in v_expansion:
    p_expansion.append(constant_c2/(pow(i, gamma)))

# Efficiency of the engine
thermal_efficiency = 1-(1/pow(rc, (gamma-1)))

# plotting the curves
plt.figure(1)
plt.plot(v_compression, p_compression)
plt.plot([v2, v3], [p2, p3])
plt.plot(v_expansion, p_expansion)
plt.plot([v4, v1], [p4, p1])
plt.xlabel('Volume (V)')
plt.ylabel('Pressure (P)')


print('The efficiency of  Diesel Cycle is ', thermal_efficiency)


from pylab import *
import math
p_min=10**5
#p_max=20*10**5
v_max=0.5
γ=1.4
r=4
rc=1.5

# Process 1-2
p1=p_min
v1=v_max
c1=p1*v1**γ
v2=v1/r
p2=c1/v2**γ

# Process 2-3
p3=p2
v3=rc*v2

# Process 3-4
c2=p3*v3**γ
v4=v1
p4=c2/v4**γ

# Plotting Part

# 1-2

v=linspace(v2,v1,50)
p=c1/v**γ
plot(v,p,'r-')

#2-3
v=linspace(v2,v3,50)
p=zeros(50)+p2
plot(v,p,'b-')

# 3-4
v=linspace(v3,v4,50)
p=c2/v**γ
plot(v,p,'g-')

# 4-1
p=linspace(p1,p4,50)
v=zeros(50)+v1
plot(v,p,'m-')

text(v1,p1,'1')
text(v2,p2+4000,'2')
text(v3,p3,'3')
text(v4,p4,'4')
xlabel('Volume (V)')
ylabel('Pressure (P)')
show()

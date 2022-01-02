% Motor constants
J = 0.0023;
L = 0.0047;
R_electronic = 4.73;
k_e = 0.274;
k_m = k_e;
M_oth = 0.25;
U_max = 7.02;

% PID
K_p = 5;
K_i = 0.01;
K_d = 0.25;

target = 360;
close all
simOut  = sim("modelLba3.slx");
plot(simOut.angle.time, simOut.angle.data)

grid on
hold on 
line([0 10],[360 360],'LineStyle','--', 'color','red')
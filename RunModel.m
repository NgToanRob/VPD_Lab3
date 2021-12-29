% Motor constants
J = 0.0023;
L = 0.0047;
R_electronic = 4.73;
k_e = 0.274;
k_m = k_e;
M_oth = 0;

% PID
K_p = 5;
K_i = 0.05;
K_d = 0.4;

target = 360;

simOut  = sim("modelLba3.slx");
plot(simOut.angle.time, simOut.angle.data)
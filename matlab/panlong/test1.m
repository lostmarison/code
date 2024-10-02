theta = 0:-0.01*pi:-32*pi; % 极角变化范围
%% t
[a,b] = setspiral(); % 设置螺线参数,r=a+bθ
[x1,y1] = pos(g(213)); %龙头前把手
[x2,y2,theta2] = posafter(g(213),2.86); %龙头后把手
x = zeros(1,100); % 存放龙头后98个把手的横坐标
y = zeros(1,100); % 存放龙头后98个把手的纵坐标
x(1) = x1;y(1)=y1; %存入龙头前把手
x(2) = x2;y(2)=y2; %存入龙头后把手
thetanow = theta2; % 记录龙头后把手位置
% 存入所有把手位置
for i = 3:100
    [x(i),y(i),thetanow] = posafter(thetanow,1.56);
end
%% t+Δt
[m1,n1] = pos(g(213.0001)); 
[m2,n2,thetam2] = posafter(g(213.0001),2.86); 
m = zeros(1,100); 
n = zeros(1,100); 
m(1) = m1;n(1)=n1; 
m(2) = m2;n(2)=n2; 
thetanowm = thetam2; 
for i = 3:100
    [m(i),n(i),thetanowm] = posafter(thetanowm,1.56);
end
%% v = (s(t+Δt)-s(t))/Δt
v = zeros(1,100);
for i = 1:100
    v(i) = (norm([x(i),y(i)]-[m(i),n(i)]))/0.0001;
end
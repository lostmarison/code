theta = 0:-0.01*pi:-32*pi; % 极角变化范围
[a,b] = setspiral(); % 设置螺线参数,r=a+bθ
drawspiral(theta,a,b); % 绘制螺线
hold on
[x1,y1] = pos(g(413)); %龙头前把手
[x2,y2,theta2] = posafter(g(413),2.86); %龙头后把手
x = zeros(1,225); % 存放龙头后225个把手的横坐标
y = zeros(1,225); % 存放龙头后225个把手的纵坐标
x(1) = x1;y(1)=y1; %存入龙头前把手
x(2) = x2;y(2)=y2; %存入龙头后把手
thetanow = theta2; % 记录龙头后把手位置
% 存入所有把手位置
for i = 3:225
    [x(i),y(i),thetanow] = posafter(thetanow,1.56);
end
%% 可视化
scatter(x(1),y(1),80,'filled','bp'); % 绘制龙头前把手（特殊）
% 绘制把手位置
for i = 2:225
    scatter(x(i),y(i),'filled','k');
end
% 连接各把手
for i = 1:224
    line([x(i),x(i+1)],[y(i),y(i+1)],'color','k','LineWidth',1);
end
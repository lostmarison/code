%% 主程序
theta = 0:-0.01*pi:-32*pi; % 极角变化范围
[a,b] = setspiral(); % 设置螺线参数,r=a+bθ
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
drawspiral(theta,a,b); % 绘制螺线
hold on
scatter(x(1),y(1),80,'filled','bp'); % 绘制龙头前把手（特殊）
% 绘制把手位置
for i = 2:225
    scatter(x(i),y(i),'filled','k');
end
% 连接各把手
for i = 1:224
    line([x(i),x(i+1)],[y(i),y(i+1)],'color','k','LineWidth',1);
end
%% L = f(theta)
function L = f(theta) % theta : 0->-32*pi
    L = 0.0139 + 8.8006*(-theta) - 0.0437*(-theta).^2;
end
%% theta = g(t) or theta = g(L)
function theta = g(L)
    syms x;
    assume(x < 32*pi); % x = [0,32*pi]限制范围
    y = 0.0139 + 8.8006*x - 0.0437*x.^2;
    s = solve(y == L);
    theta = double(s); % 将符号变量转换为数值变量
    theta = -theta; % 0->-32*pi
end
%% 螺线参数设定
function [a,b] = setspiral()
    p = 0.55;
    q =16;
    a = p*q;
    b = p/(2*pi);
end
%% 绘制螺线
function [] = drawspiral(theta,a,b)
    r = a+b*theta;
    x = r.*cos(theta);
    y = r.*sin(theta);
    plot(x,y,'r');
    axis equal
    ax = gca;
    ax.XAxisLocation = 'origin';
    ax.YAxisLocation = 'origin';
end
%% 通过角度获取把手位置
function [x,y] = pos(theta)
    [a,b] = setspiral();
    r = a+b.*theta;
    x = r.*cos(theta);
    y = r.*sin(theta);
end
%% 后一个把手位置
function [x,y,thetaafter] = posafter(thetanow,d)
    [a,b] = setspiral();
    r = a+b*thetanow;
    xnow = r.*cos(thetanow);
    ynow = r.*sin(thetanow);
    for i = thetanow:+0.001:0 %θ是负数
        x = (a+b*i).*cos(i);
        y = (a+b*i).*sin(i);
        if(norm([xnow,ynow]-[x,y]) >= d) % 找到第一个大于等于distance的点
            thetaafter = i;
            break;
        end
    end
end

%% 离散化求解不定积分
dx = 0.001; % 步长
x = 0:dx:10; % x=[0,10]范围
f = sqrt(x.^2+1);
f = f*dx; % 小矩形面积
F = zeros(1,length(f)); % 原函数
for i=1:length(f)
    F(i) = sum(f(1:i));
end
%% 绘制图像
plot(x,F);
title('F(x)');
xlabel('x');
ylabel('y');
%% 若积分前函数不具有原函数则将所得数据曲线拟合

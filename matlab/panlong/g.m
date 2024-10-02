% theta = g(t) or theta = g(L)
function theta = g(L)
    syms x;
    assume(x < 32*pi); % x = [0,32*pi]限制范围
    y = 0.0139 + 8.8006*x - 0.0437*x.^2;
    s = solve(y == L);
    theta = double(s); % 将符号变量转换为数值变量
    theta = -theta; % 0->-32*pi
end

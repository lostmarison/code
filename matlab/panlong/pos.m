% 通过角度获取把手位置
function [x,y] = pos(theta)
    [a,b] = setspiral();
    r = a+b.*theta;
    x = r.*cos(theta);
    y = r.*sin(theta);
end
function [] = circle(r)
    t = 0:0.1:2*pi;
    x = r.*sin(t);
    y = r.*cos(t);
    patch(x,y,'yellow');
    %patch(X,Y,C) 通过将X和Y指定为每个顶点的坐标来创建一个或多个彩色多边形补片
    axis square tight 
    alpha(0.3)
end


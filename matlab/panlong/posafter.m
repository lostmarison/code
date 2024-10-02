% 后一个把手位置
function [x,y,thetaafter] = posafter(thetanow,d)
    [a,b] = setspiral();
    r = a+b*thetanow;
    xnow = r.*cos(thetanow);
    ynow = r.*sin(thetanow);
    for i = thetanow:+0.01*pi:0 %θ是负数
        x = (a+b*i).*cos(i);
        y = (a+b*i).*sin(i);
        if(norm([xnow,ynow]-[x,y]) >= d) % 找到第一个大于等于distance的点
            thetaafter = i;
            break;
        end
    end
end
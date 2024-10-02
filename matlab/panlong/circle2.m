function [] = circle2(a,b,r)
    para = [a-r, b-r, 2*r, 2*r];
    rectangle('Position', para, 'Curvature', [1 1]);
end


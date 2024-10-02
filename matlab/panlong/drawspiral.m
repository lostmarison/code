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


% L = f(theta)
function L = f(theta) % theta : 0->-32*pi
    L = 0.0139 + 8.8006*(-theta) - 0.0437*(-theta).^2;
end


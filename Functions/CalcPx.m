function px = CalcPx(p_x_given_ck,p_c_k)
sum = 0;
for i = 1:2
    sum = sum + p_x_given_ck(i)*p_c_k(i);
end

px = sum;
end


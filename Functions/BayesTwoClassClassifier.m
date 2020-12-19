function [choosenClass] = BayesTwoClassClassifier(p_x_given_c1,p_x_given_c2, p_c1, p_c2, x)
prob_c1_given_x = p_x_given_c1*p_c1;
prob_c2_given_x =  p_x_given_c2*p_c2;

if prob_c1_given_x > prob_c2_given_x
    fprintf("for x = %.3f : p(ck= 1| x) > p(ck= 2| x)  => %.3f > %.3f  we choose class 1", x, prob_c1_given_x, prob_c2_given_x);
    choosenClass = 1;
elseif prob_c1_given_x == prob_c2_given_x   
    fprintf("for x = %.3f : p(ck= 1| x) == p(ck= 2| x)  => %.3f == %.3f we choose class 2", x ,prob_c1_given_x, prob_c2_given_x);
    choosenClass = 2;
else
    fprintf("for x = %.3f : p(ck= 1| x) < p(ck= 2| x)  => %.3f < %.3f  we choose class 2", x, prob_c1_given_x, prob_c2_given_x);
    choosenClass = 2;
end
end


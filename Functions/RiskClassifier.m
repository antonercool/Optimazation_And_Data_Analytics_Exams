function chosenClass = RiskClassifier(risk_matrix, p_c1_given_x ,p_c2_given_x, x)
R_a1_given_x = risk_matrix(1,1)*p_c1_given_x + risk_matrix(1,2)*p_c2_given_x;
R_a2_given_x = risk_matrix(2,1)*p_c1_given_x + risk_matrix(2,2)*p_c2_given_x;

if R_a1_given_x < R_a2_given_x
    fprintf("for x = %.3f : R(a1|x3) < R(a2|x3) <--> %.5f < %.5f  --> we choose class 1", x, R_a1_given_x, R_a2_given_x);
    chosenClass = 1;
else
    fprintf("for x = %.3f R(a1|x3) > R(a2|x3) <--> %.5f > %.5f  --> we choose class 2",x,  R_a1_given_x, R_a2_given_x);
    chosenClass = 2;
end
end


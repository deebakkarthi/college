/*
* Half subtractor
* difference =  a ^ b
* carry  = ~a & b
* */
module hs (a,b,d,c);
input a, b;
output d, c;

wire a_bar;
not(a_bar,a);

xor(d,a,b);
and(c,a_bar,b);

endmodule


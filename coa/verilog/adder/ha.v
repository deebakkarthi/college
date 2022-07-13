/*
* Half adder
* sum =  a ^ b
* carry  = a & b
* */
module ha (a,b,s,c);
input a, b;
output s, c;

and(c,a,b);
xor(s,a,b);

endmodule


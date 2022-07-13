`include "ha.v"
module fa (a,b,cin,s,cout);
input a, b, cin;
output s, cout;

wire ha1_sum;
wire ha1_carry;
wire ha2_carry;

ha ha1 (a,b,ha1_sum,ha1_carry);
ha ha2 (ha1_sum, cin, s, ha2_carry);
or(cout,ha1_carry, ha2_carry);

endmodule

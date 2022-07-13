`include "hs.v"
module fs (a,b,bin,d,bout);
input a, b, bin;
output d, bout;

wire hs1_diff;
wire hs1_borrow;
wire hs2_borrow;

hs hs1 (a,b,hs1_diff,hs1_borrow);
hs hs2 (hs1_diff, bin, d, hs2_borrow);
or(bout,hs1_borrow, hs2_borrow);

endmodule

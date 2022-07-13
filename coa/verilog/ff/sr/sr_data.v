module sr (s,r,q,q_bar,clk);
input s, r, clk;
output q, q_bar;

assign q = (r & clk) ~| q_bar;
assign q_bar = (s & clk) ~| q;

endmodule

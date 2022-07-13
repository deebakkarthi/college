module d (d,q,q_bar,clk);
input d, clk;
output q, q_bar;

assign q = d;
assign q_bar = ~d;

endmodule

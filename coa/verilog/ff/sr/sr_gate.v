module sr (s,r,q,q_bar,clk);
input s, r, clk;
output q, q_bar;

wire s_clk;
wire r_clk;

and(s_clk,s,clk);
and(r_clk,r,clk);

nor(q,r_clk,q_bar);
nor(q_bar,s_clk,q);

endmodule

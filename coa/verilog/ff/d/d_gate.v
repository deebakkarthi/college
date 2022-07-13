module d(d,q,q_bar,clk);
input d, clk;
output q, q_bar;

wire d_bar;
not(d_bar,d);

wire tmp[1:0];

nand(tmp[1],d,clk);
nand(tmp[0],d_bar,clk);

nand(q,tmp[1],q_bar);
nand(q_bar,tmp[0],q);

endmodule

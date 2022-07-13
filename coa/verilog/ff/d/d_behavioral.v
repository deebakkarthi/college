module d (d,q,q_bar,clk);
input d, clk;
output reg q, q_bar;

always @ (posedge clk)
begin
	q <= d;
	q_bar <= ~q;
end
endmodule

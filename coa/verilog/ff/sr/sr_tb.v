module tb;
reg s, r, clk;
wire q, q_bar;

sr DUT (s,r,q,q_bar,clk);

initial
begin
	clk = 1;
	forever #1 clk = ~clk;
end

initial
begin
	$display("s|r|q|q_bar");
	for(integer i = 3; i >= 0; i--)
	begin
		{s,r} = i;
		#5;
		$display("%b|%b|%b|%b",s,r,q,q_bar);
	end
	$finish();
end
endmodule

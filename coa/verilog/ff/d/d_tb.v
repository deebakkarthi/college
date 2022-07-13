module tb;
reg d, clk;
wire q, q_bar;

d DUT (d,q,q_bar,clk);

initial
begin
	clk = 1;
	forever #1 clk = ~clk;
end

initial
begin
	$display("d|q|q_bar");
	for(integer i = 0; i < 2; i++)
	begin
		d = i;
		#5;
		$display("%b|%b|%b",d,q,q_bar);
	end
	$finish();
end
endmodule

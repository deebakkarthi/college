module tb;
reg signed [7:0] a;
reg signed [7:0] b;
wire signed [7:0] o;

rcs DUT(a,b,o);
initial
begin
	a = -25;
	b = 50;
	#5;
	$display("%d - %d = %d",a,b,o);
	$display("%b - %b = %b",a,b,o);
end
endmodule

module tb;
reg [7:0] a;
reg [7:0] b;
wire [7:0] o;

rca DUT(a,b,o);
initial
begin
	a = 30;
	b = 20;
	#5;
	$display("%d + %d = %d",a,b,o);
	$display("%b + %b = %b",a,b,o);
end
endmodule

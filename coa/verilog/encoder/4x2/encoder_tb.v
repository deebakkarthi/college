module tb;
reg [3:0] i;
wire [1:0] o;

encoder DUT(i,o);

initial
begin
	for(integer j = 0; j < 4;j++)
	begin
		i = 2**j;
		#5;
		$display("%b\t%b",i,o);
	end
end
endmodule

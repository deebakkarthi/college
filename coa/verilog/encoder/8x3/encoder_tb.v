module tb;
reg [7:0] i;
wire [2:0] o;

encoder DUT(i,o);

initial
begin
	for (integer j = 0; j < 8; j++)
	begin
		i = 2**j;
		#5;
		$display("%b\t%b",i,o);
	end

end

endmodule


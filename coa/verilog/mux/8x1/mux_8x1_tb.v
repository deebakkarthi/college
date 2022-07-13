module tb;
reg [7:0] i;
reg [2:0] s;
wire y;

mux_8x1 DUT(i,s,y);

initial begin
	for(integer j = 0; j < 256; j = j + 1)
	begin
		i = j;
		#5
		$display("%b",i);
		for(integer k = 0; k < 8; k=k+1) begin
			s = k;
			#5
			$display("%b\t%b",s,y);
		end
	end
end
endmodule


module tb;
reg [3:0] i;
reg [1:0] s;
wire y;

mux_4x1 DUT(i,s,y);

initial begin
	for(integer j = 0; j < 16; j = j + 1)
	begin
		i = j;
		#5
		$display("%b",i);
		for(integer k = 0; k < 4; k=k+1) begin
			s = k;
			#5
			$display("%b\t%b",s,y);
		end
	end
end
endmodule


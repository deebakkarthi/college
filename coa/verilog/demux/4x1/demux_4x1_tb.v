module tb;
reg i;
reg [1:0] s;
wire [3:0] y;

demux_4x1 DUT(i,s,y);

initial begin
	i = 1;
	$display("SS\tIIII");
	$display("10\t3210\n");
	for(integer j = 0; j < 4; j = j + 1)
	begin
		s = j;
		#5;
		$display("%b\t%b",s,y);
	end
end
endmodule


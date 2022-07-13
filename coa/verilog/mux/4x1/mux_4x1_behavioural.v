module mux_4x1 (i, s, y);
	input [3:0] i;
	input [1:0] s;
	/*
	* Must be marked as reg since we are using behavioral
	* */
	output reg y;

	always @ (s)
	begin
		y <= i[s];
	end
endmodule

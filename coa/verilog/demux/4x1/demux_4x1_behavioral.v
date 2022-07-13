module demux_4x1 (i,s,y);
input i;
input [1:0] s;
/*
* Has to be declared as reg since we are using
* procedural assignment
* */
output reg [3:0] y;

always @ (s)
begin
	y = 0;
	y[s] = 1;
end
endmodule


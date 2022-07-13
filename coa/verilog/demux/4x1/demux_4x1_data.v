module demux_4x1 (i,s,y);
input i;
input [1:0] s;
output [3:0] y;

assign y[0] = i & ~s[1] & ~s[0];
assign y[1] = i & ~s[1] & s[0];
assign y[2] = i & s[1] & ~s[0];
assign y[3] = i & s[1] & s[0];

endmodule


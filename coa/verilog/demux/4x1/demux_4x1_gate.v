module demux_4x1 (i,s,y);
input i;
input [1:0] s;
output [3:0] y;

wire [1:0] s_bar;

not(s_bar[0],s[0]);
not(s_bar[1],s[1]);

and(y[0],i,s_bar[1],s_bar[0]);
and(y[1],i,s_bar[1],s[0]);
and(y[2],i,s[1],s_bar[0]);
and(y[3],i,s[1],s[0]);

endmodule

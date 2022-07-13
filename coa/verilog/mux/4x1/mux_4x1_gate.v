module mux_4x1 (i,s,y);
	input [3:0] i;
	input [1:0]s;
	output y;

	wire [3:0]tmp;
	wire [1:0]s_bar;

	not(s_bar[1],s[1]);
	not(s_bar[0],s[0]);

	and(tmp[0],i[0],s_bar[1],s_bar[0]);
	and(tmp[1],i[1],s_bar[1],s[0]);
	and(tmp[2],i[2],s[1],s_bar[0]);
	and(tmp[3],i[3],s[1],s[0]);

	or(y,tmp[3],tmp[2],tmp[1],tmp[0]);
endmodule


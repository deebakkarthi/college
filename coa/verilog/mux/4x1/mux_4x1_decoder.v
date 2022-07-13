module decoder (s,o);

input [1:0] s;
output [3:0] o;

wire [1:0] s_bar;

not(s_bar[0],s[0]);
not(s_bar[1],s[1]);

and(o[0],s_bar[1],s_bar[0]);
and(o[1],s_bar[1],s[0]);
and(o[2],s[1],s_bar[0]);
and(o[3],s[1],s[0]);

endmodule

module mux_4x1 (i,s,o);
input [3:0] i;
input [1:0] s;
output o;

wire [3:0] d_out;

/*
* Dot notation
* .og_port_name (your_port_name)
* */
decoder d(.s (s), .o (d_out));

wire [3:0] tmp;

and(tmp[3],d_out[3],i[3]);
and(tmp[2],d_out[2],i[2]);
and(tmp[1],d_out[1],i[1]);
and(tmp[0],d_out[0],i[0]);

or(o,tmp[3],tmp[2],tmp[1],tmp[0]);

endmodule

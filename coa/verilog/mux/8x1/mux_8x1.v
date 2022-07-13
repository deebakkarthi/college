/*
* 8x1 mux using 4x1 and 2x1 mux
*
*     +---+
*  I7-|   |
*  I6-|4x1|
*  I5-|   |----+
*  I4-|   |    |
*     +---+    |    +---+
*      | |     +----|   |
*      | |          |   |
*      v v          |   |
*     S1 S0         |   |
*      ^ ^          |   |   Y
*      | |          |2x1|----->
*     +---+    +----|   |
*  I3-|   |    |    +---+
*  I2-|4x1|----+      |
*  I1-|   |           |
*  I0-|   |           |
*     +---+           S2
* */
module mux_2x1 (i,s,y);
input [1:0] i;
input s;
output y;

wire s_bar;
wire [1:0] tmp;

not(s_bar,s);

and(tmp[0],i[0],s_bar);
and(tmp[1],i[1],s);

or(y,tmp[1],tmp[0]);

endmodule

module mux_4x1 (i,s,y);
input [3:0] i;
input [1:0] s;
output y;

wire [1:0] tmp;

mux_2x1 mux_hi(i[3:2],s[0],tmp[1]);
mux_2x1 mux_lo(i[1:0],s[0],tmp[0]);
mux_2x1 mux_combo(tmp[1:0],s[1],y);

endmodule

module mux_8x1 (i,s,y);
input [7:0] i;
input [2:0] s;
output y;

wire [1:0] tmp;

mux_4x1 mux_hi(i[7:4],s[1:0],tmp[1]);
mux_4x1 mux_lo(i[3:0],s[1:0],tmp[0]);
mux_2x1 mux_combo(tmp[1:0],s[2],y);
endmodule

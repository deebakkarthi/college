module encoder (i,o);
input [3:0] i;
output [1:0] o;

or(o[1],i[3],i[2]);
or(o[0],i[3],i[1]);
endmodule

module encoder(i,o);
input [7:0] i;
output [2:0] o;

or(o[2],i[7],i[6],i[5],i[4]);
or(o[1],i[7],i[6],i[3],i[2]);
or(o[0],i[7],i[5],i[3],i[1]);

endmodule

`include "fa.v"
module rca (a,b,o);
input [7:0] a;
input [7:0] b;
output [7:0] o;

wire [8:0] c;
fa fa1(a[0],b[0],1'b0,o[0],c[1]);
fa fa2(a[1],b[1],c[1],o[1],c[2]);
fa fa3(a[2],b[2],c[2],o[2],c[3]);
fa fa4(a[3],b[3],c[3],o[3],c[4]);
fa fa5(a[4],b[4],c[4],o[4],c[5]);
fa fa6(a[5],b[5],c[5],o[5],c[6]);
fa fa7(a[6],b[6],c[6],o[6],c[7]);
fa fa8(a[7],b[7],c[7],o[7],c[8]);
endmodule

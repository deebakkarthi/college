module encoder(i,o);
input [7:0] i;
output reg [2:0] o;

always @ (i)
begin
	case(i)
		1:
			o <= 0;
		2:
			o <= 1;
		4:
			o <= 2;
		8:
			o <= 3;
		16:
			o <= 4;
		32:
			o <= 5;
		64:
			o <= 6;
		128:
			o <= 7;

	endcase
end
endmodule

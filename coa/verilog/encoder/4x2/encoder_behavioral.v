module encoder (i,o);
input [3:0] i;
output reg [1:0] o;

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
		default:
			o <= 2'bx;
	endcase
end
endmodule

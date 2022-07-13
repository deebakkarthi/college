module sr (s,r,q,q_bar,clk);
input s, r, clk;
output reg q, q_bar;

always @ (posedge clk)
begin
	case ({s,r})
		2'b00: begin
			q <= q;
			q_bar <= q_bar;
		end
		2'b01: begin
			q <= 0;
			q_bar <= 1;
		end
		2'b10: begin
			q <= 1;
			q_bar <= 0;
		end
		2'b11: begin
			q <= 0;
			q_bar <= 0;
		end
		endcase
end
endmodule

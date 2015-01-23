class GridPlot
	attr_accessor :x, :y, :x_complex, :y_complex

	def initialize(x, y, x_complex,y_complex)
		@x = x
		@y = y
		@x_complex = x_complex
		@y_complex = y_complex
	end
end

class Grid

	attr_accessor :sequence, :all_points

	def initialize(sequence)
		@sequence = sequence
		@all_points = []
		create_plots()
	end

	def create_plots()
		@x=1
		@sequence.each do |number|			
			@y=1
			@sequence.each do |second|				
				@all_points << GridPlot.new(@x,@y,number,second)
				@y+=1
			end
			@x+=1
		end
		@all_points
	end

	def print_plots()
		@all_points.each do |point|
			print "x: #{point.x} y: #{point.y} x_complex: #{point.x_complex} y_complex: #{point.y_complex}"
			puts
		end
	end

end




def make_basic_sequence(number)
	complex_arr = []
	for i in 0..number-1
		complex_arr << Complex(i+1, i+1)
	end
	complex_arr
end

#print make_basic_sequence(100)

#x=GridPlot.new(0,1,3,4)

grid_one = Grid.new(make_basic_sequence(100))
grid_one.print_plots


def calculate(start, incircle, s, q, user_input_d):
	list_pi_value = []
	format_length = "." + str(int(user_input_d)- 1) + "f"
	math_pi=format(math.pi, format_length)
	actual_d_of_pi=len(str(math_pi).replace('.',''))

	list_shots_value = []
	for i in range(int(1),int(s) + int(1)):  # +1 is included in the index to allow for a division of 1000s
		x = random.uniform(-1.0, 1.0)
		y = random.uniform(-1.0, 1.0)
		if ((x * x + y * y) < 1):
			incircle += 1

		if ((i %int(q) == 0)):
			list_pi_value.append(4.0 * (incircle / i))
			list_shots_value.append(i)

	#creating a line for the actual value of math.pi and formatting it's data inputs
	list_mathpi = len(list_pi_value)*[math.pi]
	list_mathpi_formatted = (str(list_mathpi)).replace(" ","").replace('""','')
	pi_graph_actual=str(list_mathpi_formatted).replace('[','').replace(']','')
	#creating a line for the ESTIMATED value of pi and formatting it's data inputs
	formatted_pi_estimate=str(list_pi_value).replace('""',"").replace(" ","")
	pie_graph_estimate =(str(formatted_pi_estimate).replace('[','')).replace(']','')

	stop = timeit.default_timer()
	execution_time =str(stop - start)
   
	pi_estimate = 4.0 * incircle /int(s)
	estimated_d_of_pi=len(str(pi_estimate).replace('.',''))
	return pi_estimate, execution_time, estimated_d_of_pi, list_pi_value, pi_graph_actual, pie_graph_estimate


start = sys.argv[0], incircle= sys.argv[1], s= sys.argv[2], q= sys.argv[3], user_input_d= sys.argv[4]
calculate(start, incircle, s, q, user_input_d)


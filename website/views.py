from django.shortcuts import render

def home(request):
	return render(request, 'home.html', {})

def f_to_c(request):
	if request.method == "POST":		
		temperature = request.POST['temperature']
		#if temperature is alpha send a message
		if temperature.isalpha():
			my_temp = "Hey! Your entry is not valid!"
			color = 'danger'
			return render(request, 'f_to_c.html', {
			'color': color,
			'my_temp': my_temp,	
			'temperature': temperature,						
			})
		#error handling if user doesnt fill out the form
		if not temperature:
			my_temp = "Hey! You forgot to fill out the form!"
			color = 'danger'
			return render(request, 'f_to_c.html', {
			'color': color,
			'my_temp': my_temp,	
			'temperature': temperature,						
			})
		
		c_temp = int((float(temperature) - 32) * .55)
		color = 'warning'
		my_temp = str(temperature) + " Fahrenheit is " + str(c_temp) + " Celsius"
		return render(request, 'f_to_c.html', {
			'color': color,
			'my_temp': my_temp,	
			'temperature': temperature,						
			})
	else:
		return render(request, 'f_to_c.html', {})		

def c_to_f(request):
	if request.method == "POST":		
		temperature = request.POST['temperature']
		#if temperature is alpha send a message
		if temperature.isalpha():
			my_temp = "Hey! Your entry is not valid!"
			color = 'danger'
			return render(request, 'c_to_f.html', {
			'color': color,
			'my_temp': my_temp,	
			'temperature': temperature,						
			})
		#error handling if user doesnt fill out the form
		if not temperature:
			my_temp = "Hey! You forgot to fill out the form!"
			color = 'danger'
			return render(request, 'c_to_f.html', {
			'color': color,
			'my_temp': my_temp,	
			'temperature': temperature,						
			})

		f_temp = int((float(temperature) * 1.8 + 32))
		color = 'warning'
		my_temp = str(temperature) + " Celsius is " + str(f_temp) + " Fahrenheit"
		return render(request, 'c_to_f.html', {
			'color': color,
			'my_temp': my_temp,
			'temperature': temperature,			
			})	
	else:
		return render(request, 'c_to_f.html', {})	

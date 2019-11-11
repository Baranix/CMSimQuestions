import csv

with open('questions3.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	question = 1
	for row in csv_reader:

		if "Inverse" not in row[1]: #row[2]:
			values = ['5','4','3','2','1','6']
		else:
			values = ['1','2','3','4','5','6']

		# section = '<div data-cat="' + row[1] + '">\
		# 		<p>' + row[0] + '</p>\
		# 		<input type="radio" name="q' + str(question) + '" value="' + values[0] + '" id="q' + str(question) + 'a1"><label for="q' + str(question) + 'a1"> Strongly Agree</label><br>\
		# 		<input type="radio" name="q' + str(question) + '" value="' + values[1] + '" id="q' + str(question) + 'a2"><label for="q' + str(question) + 'a2"> Agree</label><br>\
		# 		<input type="radio" name="q' + str(question) + '" value="' + values[2] + '" id="q' + str(question) + 'a3"><label for="q' + str(question) + 'a3"> Neither Agree nor Disagree</label><br>\
		# 		<input type="radio" name="q' + str(question) + '" value="' + values[3] + '" id="q' + str(question) + 'a4"><label for="q' + str(question) + 'a4"> Disagree</label><br>\
		# 		<input type="radio" name="q' + str(question) + '" value="' + values[4] + '" id="q' + str(question) + 'a5"><label for="q' + str(question) + 'a5"> Strongly Disagree</label><br>\
		# 		<br>\
		# 		<input type="radio" name="q' + str(question) + '" value="' + values[5] + '" id="q' + str(question) + 'a6"><label for="q' + str(question) + 'a6"> Not Applicable</label><br>\
		# 	</div>'

		section = '<div data-cat="General">\
				<p>' + row[0] + '</p>\
				<input type="radio" name="q' + str(question) + '" value="' + values[0] + '" id="q' + str(question) + 'a1"><label for="q' + str(question) + 'a1"> Strongly Agree</label><br>\
				<input type="radio" name="q' + str(question) + '" value="' + values[1] + '" id="q' + str(question) + 'a2"><label for="q' + str(question) + 'a2"> Agree</label><br>\
				<input type="radio" name="q' + str(question) + '" value="' + values[2] + '" id="q' + str(question) + 'a3"><label for="q' + str(question) + 'a3"> Neither Agree nor Disagree</label><br>\
				<input type="radio" name="q' + str(question) + '" value="' + values[3] + '" id="q' + str(question) + 'a4"><label for="q' + str(question) + 'a4"> Disagree</label><br>\
				<input type="radio" name="q' + str(question) + '" value="' + values[4] + '" id="q' + str(question) + 'a5"><label for="q' + str(question) + 'a5"> Strongly Disagree</label><br>\
				<br>\
				<input type="radio" name="q' + str(question) + '" value="' + values[5] + '" id="q' + str(question) + 'a6"><label for="q' + str(question) + 'a6"> Not Applicable</label><br>\
			</div>'

		print(section)

		question += 1
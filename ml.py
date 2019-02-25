import csv

with open('pima-indians-diabetes.data.csv') as csvfile:
	reader = csv.reader(csvfile, delimiter=',')
	total = 768
	training_total = (int)(total/3)
	print(training_total)
	training_set = []
	test_set = []
	count = 0
	for row in reader:
		count = count + 1
		if count < training_total:
			training_set.append(row)
		test_set.append(row)
		
result_dict ={}
for item in training_set:
	if item[-1] not in result_dict:
		result_dict[item[-1]] = []
	result_dict[item[-1]].append(item)

print(result_dict['0'])
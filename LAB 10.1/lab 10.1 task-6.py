def grade(score):
	if score >= 90:
		return "A"
	elif score >= 80:
		return "B"
	elif score >= 70:
		return "C"
	elif score >= 60:
		return "D"
	else:
		return "F"
if __name__ == "__main__":
	test_scores = [95, 85, 75, 65, 55]
	for s in test_scores:
		print(f"Score: {s} => Grade: {grade(s)}")

import math

def is_russian_letter(symbol):
	if ((symbol >= 'а' and symbol <= 'я') or symbol == 'ё'):
		return True
	if ((symbol >= 'А' and symbol <= 'Я') or symbol == 'Ё'):
		return True
	return False

if __name__ == '__main__':
	# scrapped data
	letters = ['о', 'е', 'а', 'и', 'н', 'т', 'с', 'р', 'в', 'л', 'к', 'м', 'д', 'п', 'у', 'я', 'ы', 'ь', 'г', 'з', 'б', 'ч', 'й', 'х', 'ж', 'ш', 'ю', 'ц', 'щ', 'э', 'ф', 'ъ', 'ё']
	letters_probs = [0.1097, 0.08449999999999999, 0.0801, 0.0735, 0.067, 0.0626, 0.0547, 0.0473, 0.0454, 0.044000000000000004, 0.0349, 0.0321, 0.0298, 0.0281, 0.0262, 0.020099999999999996, 0.019, 0.0174, 0.017, 0.0165, 0.0159, 0.0144, 0.0121, 0.0097, 0.009399999999999999, 0.0073, 0.0064, 0.0048, 0.0036, 0.0032, 0.0026, 0.0004, 0.0004]
	letters_frequency = dict(zip(letters, letters_probs))
	#

	# read text
	original_text = ""
	encoding_type = "utf-8"
	with open("input.txt", encoding=encoding_type) as file:
		original_text = file.read()
	# 

	# calculate letters appearcence amount
	text_frequency = dict(zip(letters, [0] * len(letters)))
	russian_letters_in_text = 0;
	for symbol in original_text:
		symbol = symbol.lower()
		if (is_russian_letter(symbol) == True):
			# print(symbol, end="") 
			text_frequency[symbol] += 1
			russian_letters_in_text += 1
	# 

	# calculate letters frequency
	for letter in letters:
		text_frequency[letter] /= russian_letters_in_text
	# 

	# search for optimal shift of alphabet
	min_abs_error = 1e9
	alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
	optimal_shift = 0
	for shift in range(len(alphabet)):
		curr_error = 0
		for i in range(len(alphabet)):
			letter_index = (i + shift) % len(alphabet)
			# curr_error += math.sqrt((abs(text_frequency[alphabet[letter_index]] - letters_frequency[alphabet[i]])) ** 2)
			curr_error += abs(text_frequency[alphabet[letter_index]] - letters_frequency[alphabet[i]])

		if (curr_error < min_abs_error):
			min_abs_error = curr_error
			optimal_shift = shift
	# 

	# create mapping from original alphabet to shifted alphabet
	shifted_alphabet = []
	for i in range(len(alphabet)):
		shifted_alphabet.append(alphabet[(i - optimal_shift) % len(alphabet)])
		# print(alphabet[(i + optimal_shift) % len(alphabet)], end="")

	alphabet_dict = dict(zip(list(alphabet), shifted_alphabet))
	# 

	# produce decoded text
	decoded_text = ""
	for symbol in original_text:
		if (is_russian_letter(symbol)):
			if (symbol.isupper() == True):
				decoded_text += alphabet_dict[symbol.lower()].upper() 
			else:
				decoded_text += alphabet_dict[symbol]
		else:
			decoded_text += symbol

	with open("output.txt","w+") as file:
		file.write(decoded_text)
	# 

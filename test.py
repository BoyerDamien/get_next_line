# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dboyer <dboyer@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/23 15:44:08 by dboyer            #+#    #+#              #
#    Updated: 2019/11/23 15:44:38 by dboyer           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


# ===============================================================================
#										Packages
# ===============================================================================

import os
import sys

# ================================================================================
#										Functions
# ================================================================================

class GNLTester:

	def __init__(self, argv):
		self.test_files = self.get_test_files(argv)
		self.file_max_len = self.get_max_len(self.test_files)
		self.buffer = [0, 1, 100, 10000]
		self.output = "\t\t\t\t\t\t\tContent\t\tN line\t\tStdin\t\tBuffer size"
		self.test_main = {'test_line_content.c': self.test_line_content, 
						  'test_n_lines.c': self.test_n_lines,
						  'test_standard_input.c' : self.test_standard_input,
		}
	
	def get_test_files(self, args):
		files = os.listdir(args[1])
		return [os.path.join(args[1],f) for f in files]

	def get_max_len(self, str_list):
		result = 0
		for path in str_list:
			file_name = os.path.basename(path)
			result = len(file_name) if len(file_name) > result else result
		return result
	
	def test_line_content(self, buffer_size, file):
		os.system(f"./a.out {file} > testdiff")
		if buffer_size > 0:
			result = os.popen(f"diff testdiff {file}").read()
		elif buffer_size == 0: 
			result = os.popen("cat testdiff").read()
		return "OK" if not result else "FAILED"

	def test_n_lines(self, buffer_size, file):
		os.system(f"./a.out {file} > testdiff")
		n_lines = int(os.popen("cat testdiff").read())
		if buffer_size > 0:
			file_line = int(os.popen(f"cat {file} | wc -l").read().split(" ")[-1])
			return "OK" if n_lines == file_line else "FAILED"
		return "OK" if n_lines == 0 else "FAILED"
	
	def test_wrong_input(self):
		print("Testing wrong input...")
		self.compile(1, 'test_wrong_input.c')
		for i in range(1, 11):
			output = int(os.popen(f"./a.out {-i}").read())
			if (output != -1):
				print(" Your GNL is not protected !")
				return "FAILED"
		for i in range(100, 180):
			output = int(os.popen(f"./a.out {i}").read())
			if (output != -1):
				print(" Your GNL is not protected !")
				return "FAILED"
		print("Result: OK")
		return "OK"

	def test_standard_input(self, buffer_size, file):
		os.system(f"cat {file} | ./a.out > testdiff")
		return self.test_line_content(buffer_size, file)
	
	def compile(self, buffer_size, test_main):
		cc = "gcc"
		files = f"get_next_line.c get_next_line_utils.c {test_main}"
		buffer = f"-D BUFFER_SIZE={buffer_size}"
		cflags = "-Wall -Werror -Wextra -fsanitize=address"
		cmd = f"{cc} {cflags} {files} {buffer}"
		os.system(cmd)
	
	def test(self, file, buffer_size):
		file_name = os.path.basename(file)
		adjustment = self.file_max_len - len(file_name)
		self.output = f"{file_name}{adjustment * ' '}\t\t\t"
		for test in self.test_main:
			self.compile(buffer_size, test)
			result_state = self.test_main[test](buffer_size, file)
			self.output = f"{self.output}\t\t{result_state}"
		self.output = f"{self.output}\t\t{buffer_size}"
		print(self.output)
	
	def run(self):
		self.test_wrong_input()
		print(self.output)
		for file in self.test_files:
			for buffer_size in self.buffer:
				self.test(file, buffer_size)


# ================================================================================
#										Main
# ================================================================================

if __name__ == "__main__":
	test = GNLTester(sys.argv)
	test.run()

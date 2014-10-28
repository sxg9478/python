from System import *
from System.IO import *

class SScanner(object):
	def _init_ (self):
		self._lexeme = Array.CreateInstance(Char, 100)
		self._LETTER = 0
		self._DIGIT = 1
		self._UNKNOWN = 99
		self._int_lit = 10
		self._ident = 11
		self._assign_op = 20
		self._add_op = 21
		self._sub_op = 22
		self._mult_op = 23
		self._div_op = 24
		self._left_paren = 25
		self._right_paren = 26
		self._filedata = ""
		self._EOF = 'E'
	
	def main(args):
		sss = SScanner()
		if args.lenght >= 1:
			sss.fileRead(args[0])
			while self._next token != EOF:
				sss.lex()
		else:
			Console.Writeline("please give the input file")
	
	main=static method(main)
	
	def addchar(self):
		if self._lexlen <= 98:
			self._lexeme[self._lexlen += 1] = self._nextchar
			self._lexeme[self._lexlen] = 0
			self._charindex += 1
		else:
			console.writeline("error:lexeme is too long")
	
	def getchar(self):
		if(self._nextchar = self.getc(self._filedata)) != self._EOF:
			if self.isalpha(self._nextchar):
				self._charclass = self._LETTER
			elif self.isdigit(self._nextchar):
				self._charclass = self._DIGIT
			else:
				self._charclass=self._UNKNOWN
		else:
			self._charclass = self._EOF
	
	def getc(self, filedata):
		if self._charindex < filedata.lenght():
			return filedata.charAt(self._charindex)
		else:
			return self._EOF

	def fileRead(self, inputfile):
		br = None
		try:
			br = BufferedReader(FileReader(inputfile))
			stline = None
			while (stline = br.readline()) != None:
				self._filedata += stline
		except Exception, e:
			e.printStackTrace()
		finally:
	
	def isalpha(self, c):
		return Charcter.isAlphabetic(c)
	
	def isdigit(self, c):
		return Charcter.isDigit(c)
	
	def isspace(self,c):
		return Charcter.isSpaceChar(c)
	
	def getNonBlank(self):
		while self.isspace(self._nextchar):
			self.getchar()
	
	def lookup(self, ch):
		if ch == '(':
			self.addchar()
			self._nexttoken = self._left_paren
		elif ch == ')':
			self.addchar()
			self._nexttoken = self._right_paren
		elif ch == '+':
			self.addchar()
			self._nexttoken = self._add_op
		elif ch == '-':
			self.addchar()
			self._nexttoken = self._sub_op
		elif ch == '*':
			self.addchar()
			self._nexttoken = self._mult_op
		elif ch == '\':
			self.addchar()
			self._nexttoken = self._div_op
		else:
			self.addchar()
			self._nexttoken = self._EOF
		return nexttoken

	def lex(self):
		lexlen=0
	self.getNonBlank()
	if self._charclass == LETTER:
		self.addchar()
		self.getchar()
		while self._charclass == LETTER or self._charclass == DIGIT:
			self.addchar()
			self.getchar()
		nexttoken = ident
	elif self._charclass == DIGIT:
		self.addchar()
		self.getchar()
		while self._charclass == DIGIT:
			self.addchar()
			self.getchar()
	elif self._charclass == UNKNOWN:		
		self.lookup(nextchar)
		self.getchar()
	elif self._charclass == EOF:
		nexttoken = EOF
		lexeme[0] = 'E'
		lexeme[1] = 'O'
		lexeme[2] = 'F'
		lexeme[3] = 0
	console.writeline(lexeme)
	return nexttoken
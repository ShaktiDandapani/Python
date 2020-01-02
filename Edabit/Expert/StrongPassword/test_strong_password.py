import unittest 
from strong_password import strong_password



class TestStrongPassword(unittest.TestCase):


	def setUp(self):

		self.password_1 = "Ed1"
		self.password_2 = "#Edabit"
		self.password_3 = "Cr3ateAStr0ng1"
		self.password_4 = "CreateAStrongOne"


	def test_passwords(self):

		self.assertEqual(strong_password(self.password_1), 3)
		self.assertEqual(strong_password(self.password_2), 1)
		self.assertEqual(strong_password(self.password_3), 1)
		self.assertEqual(strong_password(self.password_4), 2)


if __name__ == '__main__':
	unittest.main()
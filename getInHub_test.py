#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
getInHub.py testing file
"""
import unittest
import getInHub
import requests
import simplejson as json
import designation


class TextprocTestCase(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		pass

	@classmethod
	def tearDownClass(cls):
		pass

	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_init(self):
		Brandon =  int(5)
		Maxine = "805 29th Street Boulder, CO"
		#q = getInHub.location()
		#print(getInHub.location(Brandon).addressString, "is the addressString")
		self.assertRaises(ValueError, getInHub.location,Brandon)
	#	self.assertEqual(getInHub.location(Brandon), Brandon, "'text' does not match input")
	#	self.assertEqual(getInHub.location(Maxine), Maxine, "'text' does not match input")

	def test_constructor(self):
		a = 1
		b = ["cow", "dog"]
		self.assertRaises(Exception, lambda : testproc.Processor(a, b))

	def test_getCT(self):
		# Brandon case
		CTtest1 = {'error':False, 'errorText':"", 'tract':'08013012607', 'county':'08013'}
		# Maxine case
		CTtest2 = {'error':False, 'errorText':"", 'tract':'26049011714', 'county':'26049'}
		test_CT1 = getInHub.getCT('40.002550','-105.256470')
		test_CT2 = getInHub.getCT('43.039140','-83.542910')
		self.assertDictEqual(test_CT1, CTtest1, "Brandon test case failed")
		self.assertDictEqual(test_CT2, CTtest2, "Maxine test case failed")
		#self.addTypeEqualityFunc(typeobj, function)

	def test_getCoord(self):
		TestDict1 = { 'error':False,
					'errorText':"",
					'lat':40.0023989,
					'lng':-105.256342,
					'faddr':'805 29th St, Boulder, CO 80303, USA',
					'country':'US'}
		Ctest1 =getInHub.getCoord("805 29th Street Boulder, CO")
		self.assertDictEqual(TestDict1,Ctest1, "Dicts where not the same")
		#self.assertEqual(x.count(), y, "count() function failed")
'''
	def test_count_alpha(self):
		x = textproc.Processor('HiPPOpotaMUS')
		y = len('HiPPOpotaMUS')
		self.assertEqual(x.count_alpha(), y, "count_alpha() function failed")
		#assert x.count_alpha() == y

	def test_count_numeric(self):
		m = textproc.Processor('00987654321')
		n = len('00987654321')
		self.assertEqual(m.count_numeric(), n, "count_numeric() function failed")
		#assert x.count_numberic() == y

	def test_count_vowels(self):
		p = textproc.Processor('aeiouAEIOU')
		q = len('aeiouAEIOU')
		self.assertEqual(p.count_vowels(), q, "count_vowels() function failed")

	def test_is_phonenumber(self):
		test_phone_numbers = ['970-226-5150', '303.735.5880']

		for number in test_phone_numbers:
			p = textproc.Processor(number)
			self.assertTrue(p.is_phonenumber(), "is_phonenumber() function failed")


		#more fun with list comprehensions - filtering on the fly:
		#a = [1,2,3,5]

		#[i for i in a if i*i > 4]
		#[3, 5]

		# #for number in test_phone_numbers:
		# list_textprocs = [textproc.Processor(number) for number in test_phone_numbers]

		# [self.assertTrue(p.is_phonenumber(), "is_phonenumber() function failed") for p in list_textprocs]

	# Add Your Test Cases Here...
'''


#test_getCT(self)
# Main: Run Test Cases
if __name__ == '__main__':
	unittest.main()

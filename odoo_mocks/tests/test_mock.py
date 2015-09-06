from openerp.tests.common import SingleTransactionCase


class TestOdooMocksWithMocks(SingleTransactionCase):

	def setUp(self):
		super(TestOdooMocksWithMocks, self).setUp()
		self.user_reg = self.registry('res.users')

		def user_reg_read_mock(*args, **kwargs):
			# arg[3] is the user id passed over to the read
			if args[3] == 1337:
				return {'name': 'Odoo Mocks Test User', 'id': 1}
			elif args[3] == 666:
				return {}

		self.user_reg._patch_method('read', user_reg_read_mock)
		self.odoo_mocks = self.registry('wren.colin.mock.example')

	def tearDown(self):
		self.user_reg._revert_method('read')

	def test_01_get_hash_for_test_user(self):
		cr, uid = self.cr, self.uid
		user_hash = self.odoo_mocks.get_user_name_as_hash(cr, uid, 1337)
		correct_hash = 'fbd2228a16926bee21d3866a49aaf09d'
		# Hash for Odoo Mocks Test User is
		self.assertEqual(user_hash, correct_hash, 'Hash from get_user_name_as_hash was incorrect')

	def test_02_user_not_found_raises_error(self):
		with self.assertRaises(ValueError):
			cr, uid = self.cr, self.uid
			self.odoo_mocks.get_user_name_as_hash(cr, uid, 666)
from openerp.tests.common import SingleTransactionCase


class TestOdooMocksWithDemoData(SingleTransactionCase):

	def setUp(self):
		super(TestOdooMocksWithDemoData, self).setUp()
		cr, uid = self.cr, self.uid
		self.user_reg = self.registry('res.users')
		self.odoo_mocks = self.registry('wren.colin.mock.example')
		self.user_id = self.user_reg.search(cr, uid, [['name', '=', 'Odoo Mocks Test User Demo']])[0]

	def test_01_get_hash_for_test_user(self):
		cr, uid = self.cr, self.uid
		user_hash = self.odoo_mocks.get_user_name_as_hash(cr, uid, self.user_id)
		correct_hash = '6e69b97b5b0b5fed8d282b68acd198dc'
		self.assertEqual(user_hash, correct_hash, 'Hash from get_user_name_as_hash was incorrect')

	def test_02_user_not_found_raises_error(self):
		with self.assertRaises(ValueError):
			cr, uid = self.cr, self.uid
			self.odoo_mocks.get_user_name_as_hash(cr, uid, 666)
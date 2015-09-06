from openerp.tests.common import SingleTransactionCase


class TestOdooMocksInSetup(SingleTransactionCase):

	@classmethod
	def setUpClass(cls):
		super(TestOdooMocksInSetup, cls).setUpClass()
		cr, uid = cls.cr, cls.uid
		cls.user_reg = cls.registry('res.users')
		cls.user_id = cls.user_reg.create(cr, uid, {
			'name': 'Odoo Mocks Test User setUp',
			'login': 'test_odoo_mock',
			'password': 'test_odoo_mock'
		})
		cls.odoo_mocks = cls.registry('wren.colin.mock.example')

	def test_01_get_hash_for_test_user(self):
		cr, uid = self.cr, self.uid
		user_hash = self.odoo_mocks.get_user_name_as_hash(cr, uid, self.user_id)
		correct_hash = '2f64943ab8bb7f65a3aba0479e754e1e'
		self.assertEqual(user_hash, correct_hash, 'Hash from get_user_name_as_hash was incorrect')

	def test_02_user_not_found_raises_error(self):
		with self.assertRaises(ValueError):
			cr, uid = self.cr, self.uid
			self.odoo_mocks.get_user_name_as_hash(cr, uid, 666)
from openerp.osv import osv
import logging
import hashlib
_logger = logging.getLogger(__name__)


class ExampleClass(osv.AbstractModel):

	_name = 'wren.colin.mock.example'

	def get_user_name_as_hash(self, cr, uid, user_id):
		"""
		Go and get the user object for the ID specified and return the name as a MD5 hash
		:return: The name of the user in a MD5 hash
		"""
		user_reg = self.pool['res.users']
		user = user_reg.read(cr, uid, user_id, ['name'])
		try:
			user_name = user.get('name')
			md5 = hashlib.md5()
			md5.update(user_name.encode('utf-8'))
			return md5.hexdigest()
		except:
			raise ValueError('User not found in database')

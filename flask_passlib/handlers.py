from werkzeug.security import SALT_CHARS

from passlib.utils.compat import u, str_to_uascii
from passlib.utils import classproperty
import passlib.utils.handlers as uh

import hmac
from hashlib import md5, sha1, sha224, sha256, sha384, sha512


class WerkzeugGenericHandler(uh.GenericHandler):
    checksum_chars = uh.LOWER_HEX_CHARS
    werkzeug_hash_method = None

    # @classmethod
    # def identify(cls, hash):
    #     if hash.count('$') < 2:
    #         return False
    #     method, salt, checksum = hash.split('$', 2)

    #     # does class specify a known unique prefix to look for?
    #     ident = cls.ident
    #     if ident is not None:
    #         return (method + '$').startswith(ident)
    #     return False

    @classproperty
    def _stub_checksum(cls):
        return cls.checksum_chars[0] * cls.checksum_size

class WerkzeugSaltedHash(uh.HasSalt):
    """base class providing common code for Werkzeug hashes"""
    # name, ident, checksum_size must be set by subclass.
    # ident must include "$" suffix.
    setting_kwds = ("salt", "salt_size")

    min_salt_size = 0
    default_salt_size = 8
    max_salt_size = None
    salt_chars = SALT_CHARS

    def _calc_checksum(self, secret, digestmod=None):
        if isinstance(secret, unicode):
            secret = secret.encode('utf-8')
        if isinstance(self.salt, unicode):
            self.salt = self.salt.encode('utf-8')
        # return hmac.new(self.salt, secret, digestmod).hexdigest()
        return str_to_uascii(hmac.new(self.salt, secret, digestmod).hexdigest())

    @classmethod
    def from_string(cls, hash):
        salt, chk = uh.parse_mc2(hash, cls.ident, handler=cls)
        return cls(salt=salt, checksum=chk)

    def to_string(self):
        return uh.render_mc2(self.ident, self.salt,
                             self.checksum or self._stub_checksum)




class werkzeug_salted_md5(WerkzeugSaltedHash, WerkzeugGenericHandler):
    name = "werkzeug_salted_md5"
    ident = u("md5$")
    checksum_size = 32

    def _calc_checksum(self, secret, digestmod=md5):
        return super(werkzeug_salted_md5, self)._calc_checksum(secret, digestmod=digestmod)

class werkzeug_salted_sha1(WerkzeugSaltedHash, WerkzeugGenericHandler):
    name = "werkzeug_salted_sha1"
    ident = u("sha1$")
    checksum_size = 40

    def _calc_checksum(self, secret, digestmod=sha1):
        return super(werkzeug_salted_sha1, self)._calc_checksum(secret, digestmod=digestmod)

class werkzeug_salted_sha224(WerkzeugSaltedHash, WerkzeugGenericHandler):
    name = "werkzeug_salted_sha224"
    ident = u("sha224$")
    checksum_size = 56

    def _calc_checksum(self, secret, digestmod=sha224):
        return super(werkzeug_salted_sha224, self)._calc_checksum(secret, digestmod=digestmod)

class werkzeug_salted_sha256(WerkzeugSaltedHash, WerkzeugGenericHandler):
    name = "werkzeug_salted_sha256"
    ident = u("sha256$")
    checksum_size = 64

    def _calc_checksum(self, secret, digestmod=sha256):
        return super(werkzeug_salted_sha256, self)._calc_checksum(secret, digestmod=digestmod)

class werkzeug_salted_sha384(WerkzeugSaltedHash, WerkzeugGenericHandler):
    name = "werkzeug_salted_sha384"
    ident = u("sha384$")
    checksum_size = 96

    def _calc_checksum(self, secret, digestmod=sha384):
        return super(werkzeug_salted_sha384, self)._calc_checksum(secret, digestmod=digestmod)

class werkzeug_salted_sha512(WerkzeugSaltedHash, WerkzeugGenericHandler):
    name = "werkzeug_salted_sha512"
    ident = u("sha512$")
    checksum_size = 128

    def _calc_checksum(self, secret, digestmod=sha512):
        return super(werkzeug_salted_sha512, self)._calc_checksum(secret, digestmod=digestmod)
from pythoncard.framework import *

class SecureChannel(Shareable):
    AUTHENTICATED = 0x80
    C_DECRYPTION = 0x02
    C_MAC = 0x01
    R_ENCRYPTION = 0x20
    R_MAC = 0x10
    NO_SECURITY_LEVEL = 0x00

    def resetSecurity(self):
        pass

    def getSecurityLevel(self):
        return self.NO_SECURITY_LEVEL

class GPSystem(object):
    APPLICATION_INSTALLED = 0x03
    APPLICATION_SELECTABLE = 0x07
    SECURITY_DOMAIN_PERSONALIZED = 0x0F
    CARD_OP_READY = 0x01
    CARD_INITIALIZED = 0x07
    CARD_SECURED = 0x0F
    CARD_LOCKED = 0x7F
    CARD_TERMINATED = 0xFF
    CVM_GLOBAL_PIN = 0x11

    @staticmethod
    def getSecureChannel():
        return SecureChannel()

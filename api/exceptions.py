
class ServiceNotAvailableException(Exception):
    """ generic exception, should return 503 """
    pass


class CouldNotUpdateAvtaleException(Exception):
    """ fagsystem couldnt execute update of avtale """
    pass


class CouldNotCreateAvtaleException(Exception):
    """ fagsystem couldnt execute creation of avtale """
    pass


class CouldNotCreateCustomerException(Exception):
    """ fagsystem couldnt execute creation of customer """
    pass

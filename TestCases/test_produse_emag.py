import time
import pytest
from selenium.webdriver.common.action_chains import ActionChains
from Utilities.utils import Utils
from ddt import ddt, data, unpack, file_data
import softest
from Pages.produse_page import ProdusePage
from Pages.telefoane_mobile_accesorii_page import TelefoaneMobileAccesoriiPage
from Base.base_driver import BaseDriver
from Pages.login_page import LoginPage


@pytest.mark.usefixtures("setup")
@ddt
class TestSearchAndVerifyFilter(softest.TestCase):
    log = Utils.custom_logger()
    @pytest.fixture(autouse=True)

    def class_setup(self):
        self.produse_page = ProdusePage(self.driver, self.actions)
        self.telefoane_mobile_page = TelefoaneMobileAccesoriiPage(self.driver, self.actions)

    def test_produse(self):

        self.produse_page.laptop_tablete_telefoane()
        self.telefoane_mobile_page.clickTelefoaneMobile()
        self.telefoane_mobile_page.clickAfisareLista()
        self.telefoane_mobile_page.filtruOrdoneazaDupa("Pret descrescator")
        time.sleep(1)
        self.telefoane_mobile_page.filtruEmagGenius("Toate Produsele")
        self.telefoane_mobile_page.clickIntraInCont()
        time.sleep(3)
        self.telefoane_mobile_page.filtruDisponibilitate("Resigilate")
        time.sleep(2)
        self.telefoane_mobile_page.filtruSuperPret("Top Favorite")
        time.sleep(2)
        self.telefoane_mobile_page.filtruPret("200 - 500")

        time.sleep(2)

























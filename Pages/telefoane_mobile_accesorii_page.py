import logging
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Base.base_driver import BaseDriver
from selenium.webdriver.common.action_chains import ActionChains

from Utilities.utils import Utils


class TelefoaneMobileAccesoriiPage(BaseDriver):
    log = Utils.custom_logger(logLevel=logging.WARNING)
    def __init__(self,driver,actions):
        super().__init__(driver)
        self.driver = driver
        self.actions = actions


    #LOCATORS
    TELEFOANE_MOBILE_BUTTON_XPATH = "//a[normalize-space()='Telefoane mobile']"
    ORDONEAZA_DUPA_BUTTON_XPATH = "//div[@class='sort-control-item']"
    ORDONEAZA_LI_XPATH = "//div[@class='sort-control-item']//li"

    AFISARE_LISTA_BUTTON_XPATH = "//div[@class='sort-control-item sort-control-card-collection-view']//button[1]"

    NR_PRODUSE_PAGINA_BUTTON_XPATH = "//div[@class='sort-control-btn-dropdown']"
    NR_PRODUSE_PAGINA_LI_XPATH = "(//div[@class='sort-control-btn-dropdown active'])//li"


    FILTRU_TOATE_PRODUSELE_BUTTON_XPATH = "//div[@id='js-filter-9538-collapse']//a[1]"
    FILTRU_LIVRATE_EMAG_BUTTON_XPATH = "//div[@id='js-filter-9538-collapse']//a[2]"

    FILTRU_DISPONIBILITATE_LI_XPATH = "(//div[@id='js-filter-6407-collapse'])//a[@href]"

    FILTRU_SUPER_PRET_LI_XPATH = "(//div[@id='js-filter-9902-collapse'])//a[@href]"
    FILTRU_INTERVAL_PRET_LI_XPATH = "(//div[@id='js-filter-6411-collapse'])//a[@href]"
    INTRA_IN_CONT_LINK_TEXT = "(//i[@class='em em-close'])[3]"



    def telefoaneMobileButton(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.TELEFOANE_MOBILE_BUTTON_XPATH)


    def ordoneazaDupaButton(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.ORDONEAZA_DUPA_BUTTON_XPATH)

    def ordoneazaDupaList(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.ORDONEAZA_LI_XPATH)





    def nrProdusePaginaButton(self):
        return  self.wait_until_element_is_clickable(By.XPATH, self.NR_PRODUSE_PAGINA_BUTTON_XPATH)

    def nrProdusePaginaList(self):
        self.wait_for_presence_of_all_elements(By.XPATH, self.NR_PRODUSE_PAGINA_LI_XPATH)

    def emagGeniusToateProdusele(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.FILTRU_TOATE_PRODUSELE_BUTTON_XPATH)

    def emagGeniusLivrateEmag(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.FILTRU_LIVRATE_EMAG_BUTTON_XPATH)

    def disponibilitateList(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.FILTRU_DISPONIBILITATE_LI_XPATH)

    def superPretList(self):
        return self.wait_for_presence_of_all_elements(By.XPATH,self.FILTRU_SUPER_PRET_LI_XPATH)

    def pretList(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.FILTRU_INTERVAL_PRET_LI_XPATH)




    def clickAfisareLista(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.AFISARE_LISTA_BUTTON_XPATH).click()

    def clickIntraInCont(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.INTRA_IN_CONT_LINK_TEXT).click()

    def clickTelefoaneMobile(self):
        self.telefoaneMobileButton().click()




    def filtruOrdoneazaDupa(self, ordoneaza):

        self.ordoneazaDupaButton().click()
        lista_ordoneaza_dupa = self.ordoneazaDupaList()

        for results in lista_ordoneaza_dupa:
            if ordoneaza in results.text:
                results.click()
                break



    def filtruNrProdusePagina(self, nrproduse):

        self.nrProdusePaginaButton().click()
        lista_nr_produse = self.nrProdusePaginaList()

        for results in lista_nr_produse:
            if nrproduse in results.text:
                results.click()
                break



    def filtruOrdoneazaDupa(self, ordoneaza):

        self.ordoneazaDupaButton().click()
        lista_ordoneaza_dupa = self.ordoneazaDupaList()

        for results in lista_ordoneaza_dupa:
            if ordoneaza in results.text:
                results.click()
                break







    def filtruEmagGenius(self, optiune):
        self.optiune = optiune

        # accept cookies
        self.wait_until_element_is_clickable(By.XPATH, "//button[normalize-space()='Accept']").click()

        if optiune == "Toate Produsele":
            self.emagGeniusToateProdusele().click()

        elif optiune == "Livrate Emag":
            self.emagGeniusLivrateEmag().click()


        else:
            print("Filtru incorect")



    def filtruDisponibilitate(self, optiune):
        lista_disponibilitate = self.disponibilitateList()
        for results in lista_disponibilitate:
            if optiune in results.text:
                results.click()
                break



    def filtruSuperPret(self, optiune):
        lista_super_pret = self.superPretList()
        for results in lista_super_pret:
            if optiune in results.text:
                results.click()
                break



    def filtruPret(self, optiune):
       lista_preturi = self.pretList()
       for results in lista_preturi:
           if optiune in results.text:
               results.click()
               break



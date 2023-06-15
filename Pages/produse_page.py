from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Base.base_driver import BaseDriver

from selenium.webdriver.common.action_chains import ActionChains
class ProdusePage(BaseDriver):
    def __init__(self,driver,actions):
        super().__init__(driver)

        self.driver = driver
        # self.wait = wait
        self.actions = actions



    #LOCATORS

    LAPTOP_TABLETE_TELEFOANE_XPATH = "//span[normalize-space()='Laptop, Tablete & Telefoane']"
    PC_PERIFERICE_SFOTWARE_XPATH = "//span[normalize-space()='PC, Periferice & Software']"
    TV_AUDIO_VIDEO_FOTO_XPATH = "//span[normalize-space()='TV, Audio-Video & Foto']"
    ELECTROCASNICE_CLIMATIZARE_XPATH = "//span[normalize-space()='Electrocasnice & Climatizare']"
    gaming_carti_birotica_xpath = "//span[normalize-space()='Gaming, Carti & Birotica']"
    bacanie_xpath = "(//span[normalize-space()='Bacanie'])[1]"
    fashion_xpath = "//span[normalize-space()='Fashion']"
    ingrijire_personala_cosmetice_xpath = "//span[normalize-space()='Ingrijire personala & Cosmetice']"
    casa_gradina_bricolaj_xpath = "//span[normalize-space()='Casa, Gradina & Bricolaj']"
    sport_activitati_xpath = "//span[normalize-space()='Sport & Activitati in aer liber']"
    auto_moto_rca_xpath = "//span[contains(text(),'Auto, Moto')]"
    jucarii_copii_bebe_xpath = "//span[normalize-space()='Jucarii, Copii & Bebe']"

    def laptop_tablete_telefoane(self):
        # accept cookies
        # self.wait_until_element_is_clickable(By.XPATH, "//button[normalize-space()='Accept']").click()

        laptop_tablete_telefoane = self.wait_until_element_is_clickable(By.XPATH, self.LAPTOP_TABLETE_TELEFOANE_XPATH)
        self.actions.move_to_element(laptop_tablete_telefoane).perform()




    def pc_periferice_software(self):
        pc_periferice_software= self.wait_until_element_is_clickable(By.XPATH, self.PC_PERIFERICE_SFOTWARE_XPATH)
        self.actions.move_to_element(pc_periferice_software).perform()


    def tv_audio_video_foto(self):
        tv_audio_video_foto= self.wait_until_element_is_clickable(By.XPATH, self.TV_AUDIO_VIDEO_FOTO_XPATH)
        self.actions.move_to_element(tv_audio_video_foto).perform()


    def electrocasnice_climatizare(self):
        electrocasnice_climatizare = self.wait_until_element_is_clickable(By.XPATH, self.ELECTROCASNICE_CLIMATIZARE_XPATH)
        self.actions.move_to_element(electrocasnice_climatizare).perform()


    def gaming_carti_birotica(self):
        gaming_carti_birotica = self.wait_until_element_is_clickable(By.XPATH, self.gaming_carti_birotica_xpath)
        self.actions.move_to_element(gaming_carti_birotica).perform()


    def bacanie(self):
        bacanie = self.wait_until_element_is_clickable(By.XPATH, self.bacanie_xpath)
        self.actions.move_to_element(bacanie).perform()


    def fashion(self):
        fashion = self.wait_until_element_is_clickable(By.XPATH, self.fashion_xpath)
        self.actions.move_to_element(fashion).perform()


    def ingrijire_personala_cosmetice(self):
        ingrijire_personala_cosmetice = self.wait_until_element_is_clickable(By.XPATH, self.ingrijire_personala_cosmetice_xpath )
        self.actions.move_to_element(ingrijire_personala_cosmetice).perform()


    def casa_gradina_bricolaj(self):
        casa_gradina_bricolaj = self.wait_until_element_is_clickable(By.XPATH, self.casa_gradina_bricolaj_xpath )
        self.actions.move_to_element(casa_gradina_bricolaj).perform()


    def sport_activitati(self):
        sport_activitati = self.wait_until_element_is_clickable(By.XPATH, self.sport_activitati_xpath)
        self.actions.move_to_element(sport_activitati).perform()


    def auto_moto_rca(self):
        auto_moto_rca = self.wait_until_element_is_clickable(By.XPATH, self.auto_moto_rca_xpath)
        self.actions.move_to_element(auto_moto_rca).perform()


    def jucarii_copii_bebe(self):
        jucarii_copii_bebe = self.wait_until_element_is_clickable(By.XPATH, self.jucarii_copii_bebe_xpath)
        self.actions.move_to_element(jucarii_copii_bebe).perform()





from playwright.sync_api import *


class navigation:
    def __init__(self, page: Page):
        self.page = page
        self.menu_navigation = page.locator("//tr[@class='MainMenurow']/td/table/tbody/tr/td")

    """
    1. pass the path like Clients -> Client List
    2. split the path by "->" and strip the spaces
    3. click on the main menu and then click on the submenu

    """

    def clean_text(self, text: str) -> str:
        """Clean text by removing all special characters and normalizing"""
        if not text:
            return ""
        # Replace non-breaking spaces and other special spaces
        text = text.replace('\xa0', ' ')  # Non-breaking space
        text = text.replace('\u200b', '')  # Zero-width space
        text = text.replace('\t', ' ')
        text = text.replace('\n', ' ')
        text = text.replace('\r', ' ')
        # Remove extra spaces and strip
        return ' '.join(text.split())

    def click_menu(self, path: str):
        try:

            # Split and clean the path
            menu_items = path.split("->")
            main_menu = menu_items[0].strip()
            sub_menu = menu_items[1].strip()

            print(f"Main menu: '{main_menu}'")
            print(f"Sub menu: '{sub_menu}'")

            # Click on the main menu
            self.page.locator(f"//tr[@class='MainMenurow']/td/table/tbody/tr/td[text()='{main_menu}']").click()

            # Wait for submenu to appear
            self.page.wait_for_timeout(2000)

            # Get all submenu items
            submenu_elements = self.page.locator("//div[@class='FirstchildMenu']//td").all()
            print(f"Found {len(submenu_elements)} submenu elements")

            # Method 1: Direct comparison with cleaned text
            for element in submenu_elements:
                # Get raw text and clean it
                raw_text = element.inner_text() or ""
                cleaned_text = self.clean_text(raw_text)

                print(f"Comparing: '{cleaned_text}' == '{sub_menu}'")

                if cleaned_text == sub_menu:
                    print(f"✓ Match found! Clicking: '{raw_text}'")
                    element.click()
                    return
        except Exception as e:
            print(f"Error while clicking menu: {e}")
            raise
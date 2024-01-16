from selene import browser, be

def close_pop_up():
    browser.wait_until('[class*="button_secondary"]')
    if browser.with_(timeout=10).element('[class*="button_secondary"]').matching(be.visible):
        browser.element('[class*="button_secondary"]').click()
def close_pop_up_adv():
    browser.wait_until('[class*="close_r"]')
    if browser.with_(timeout=10).element('[class*="close_r"]').matching(be.visible):
        browser.element('[class*="close_r"]').click()

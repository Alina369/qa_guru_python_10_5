from selene import browser, be, have

def test_registration_form():
    browser.open("https://demoqa.com/automation-practice-form")
    browser.element("#firstName").type("Anna")
    browser.element("[#lastName").type("Ivanova")
    browser.element("#gender-radio-2").click()
    browser.element("#userNumber").type("8952333222")
    browser.element("#dateOfBirthInput").click()
    browser.element(".react-datepicker__month-select").element('option[value="2"]').click()
    browser.element(".react-datepicker__year-select").element('option[value="1994"]').click()
    browser.element(".react-datepicker__day--024").click()
    browser.element("#submit").click()
    browser.element("example-modal-sizes-title-lg").should(have.texts("Thanks for submitting the form"))




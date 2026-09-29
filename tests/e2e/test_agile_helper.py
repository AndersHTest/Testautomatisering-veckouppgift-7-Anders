import re
from playwright.sync_api import Page, expect


base_url = "https://lejonmanen.github.io/agile-helper/"


def test_has_title(page: Page):
    page.goto(base_url)

    expect(page).to_have_title(re.compile("Agile helper"))


def test_sprint_retrospective(page: Page):
    page.goto(base_url)

    button_locator = page.get_by_role("button")
    button_last = button_locator.get_by_text("Sista")
    button_last.click()

    page.get_by_role("button").get_by_text(re.compile("Sprint retrospective")).click()

    heading = page.get_by_role("heading").get_by_text(re.compile("Sprint retrospective"))

    expect(heading).to_be_visible()

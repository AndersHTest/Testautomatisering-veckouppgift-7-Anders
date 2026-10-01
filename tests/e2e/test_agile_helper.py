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


def test_sprint_planning(page: Page):
    page.goto(base_url)

    page.get_by_role("button").get_by_text(re.compile("Första")).click()
    page.get_by_role("button").get_by_text(re.compile("Sprint planning.+")).click()

    heading = page.get_by_role("heading").get_by_text(re.compile("Sprint planning"))

    expect(heading).to_be_visible()


def test_daily_standup(page: Page):
    page.goto(base_url)

    page.get_by_role("button").get_by_text(re.compile("Någon.+i")).click()
    page.get_by_role("button").get_by_text(re.compile("Börja.+Daily standup")).click()

    heading = page.get_by_role("heading").get_by_text(re.compile("Daily standup"))

    expect(heading).to_be_visible()


def test_sprint_review(page: Page):
    page.goto(base_url)

    page.get_by_role("button").get_by_text(re.compile("Sista")).click()
    page.get_by_role("button").get_by_text(re.compile("Presentera.+Sprint review")).click()

    heading = page.get_by_role("heading").get_by_text(re.compile("Sprint review"))

    expect(heading).to_be_visible()


def test_page_header(page: Page):
    page.goto(base_url)

    heading = page.get_by_role("heading").get_by_text(re.compile("Agile helper"))

    expect(heading).to_be_visible()


def test_page_language(page: Page):
    page.goto(base_url)

    page.get_by_test_id(re.compile("language-en")).click()

    paragraph = page.get_by_role("paragraph").get_by_text(re.compile("What day.+"))

    expect(paragraph).to_be_visible()

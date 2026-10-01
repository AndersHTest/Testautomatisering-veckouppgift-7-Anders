# Playwright
## Vecka 40

<!-- TOC -->
* [Status uppgifter](#status-uppgifter)
  * [Diskutera i grupp](#1-diskutera-i-grupp)
  * [Öva på Regex](#2-öva-på-regex)
  * [Öva på user stories](#3-öva-på-user-stories)
  * [Öva på E2E tests](#4-öva-på-e2e-tests)
<!-- TOC -->
<br>

### Status uppgifter

| Uppgift                         | Status | 🟠🟡🟢 |
|---------------------------------|--------|--------|
| 1 Diskussion                    | 100%   | 🟢     |
| 2 Öva på Regex                  | 100%   | 🟢     |
| 3 Öva på user stories           | 100%   | 🟢     |
| 4 Öva på E2E tests              | 100%   | 🟢     |

<br>

### 1. Diskutera i grupp

#### 1a) Vilka strängar matchas av det reguljära uttrycket: "ab" ?
<pre>
A. "a b"
B. "aBBa"
C. <b><i><u>"sabotör"</u></i></b>
</pre>
#### 1b) Betrakta uttrycket "nisse". Vad skriver jag för att matcha både "Nisse", "NISSE" och "nisse"?
<pre>
T.ex '/nisse/gi' för att matcha alla. Eller '(?i)nisse' för att matcha strängarna enskilt.
</pre>
#### 1c) Vilka strängar matchas av "a*n" ?
<pre>
A. <b><i><u>"an"</u></i></b>
B. "amerikan"
C. "naturlig"
D. "annandag"
</pre>
#### 1d) Vilka strängar matchas av "[ae]n" ?
<pre>
A. "naiv"
B. <b><i><u>"inconsequential"</u></i></b>
C. "bae"
</pre>

#### 1e) Vilka strängar matchas av "je.+e"?
<pre>
A. "je"
B. "jee"
C. <b><i><u>"jeppe"</u></i></b>
D. <b><i><u>"je je"</u></i></b>
</pre>
#### 1f) Vilka strängar matchas av "\san?\s"
<pre>
A. "sansad"
B. " annan "
C. <b><i><u>"    an   na   an   "</u></i></b>
D. <b><i><u>"be a darling"</u></i></b>
</pre>
#### 1g) Skriv ner med egna ord, vad följande uttryck matchar. "Strängar som innehåller…"
````
A. Strängar som innehåller "line" eller "lines".
B. Strängar som börjar med ett eller flera a och avslutas med ö. T.ex "aaaaaaaaö" eller "aö"
C. Uttrycket kommer matcha vokaler i en sträng.
D. Strängar som innehåller enskilda siffror eller siffror i grupp.
F. Strängar som innehåller siffror i formatet nnnn-nn-nn. T.ex 1111-22-33.
````
#### 2a) Betrakta https://lejonmanen.github.io/agile-helper/ . Skriv en user story som <br>beskriver att användaren ska kunna läsa hur man gör en "sprint retrospective".
<pre>
Som en student vill jag kunna surfa in på agile helper och läsa på om<br>Sprint retrospective för att avsluta en sprint på korrekt sätt.
</pre>
#### 2b) Skriv ner ett testscenario för user storyn.
````
* Surfa in på hemsidan
* Tryck på knappen "Sista"
* Tryck på knappen "Avsluta sprinten med att utvärdera ert arbete i Sprint retrospective"
* Kontrollera att rubriken Sprint Retrospective syns.
````
#### 3) Titta på kodexemplet från lektionen.<br>Skriv upp allt du är osäker på och diskutera i grupp, eller fråga om på nästa lektion.
<pre>
def test_view_sprint_planning(page: Page):
    """Testa att det går att se Sprint planning"""
    page.goto("https://lejonmanen.github.io/agile-helper/")

    # Klicka på button "First"
    locator = page.get_by_role("button")
    first_button = locator.get_by_text("First")
    first_button.click(timeout=100)

    # Hitta button med texten "Sprint planning"
    sp_button = page.get_by_role("button").get_by_text(re.compile("Sprint planning"))
    expect(sp_button).to_be_visible()
    
    # Klicka på den
    sp_button.click(timeout=100)

    # Finns rubriken "Sprint planning"?
    sp_heading = page.get_by_role("heading").get_by_text("Sprint planning")
    expect(sp_heading).to_be_visible()
</pre>
````
---
````
<br>

### 2. Öva på Regex

#### 1a) Skriv ett regex som kontrollerar att det finns en längd i strängen, som anges i centimeter:<br>"Fiskarna som jag fångade var 55 cm långa."

````
/\d+\scm/ eller /\d*\scm/
````

#### 1b) Denna gången vill vi veta om det finns två längder.
````
/\d+\scm/g eller /\d*\scm/g    #lägger till /g för att hitta alla matchningar.
````

#### 1c) Längderna ska vara samma enhet.<br>"Fiskarna som jag fångade var 55 cm långa, så båda fick plats i min 1,23 m långa låda."

````
/\d+\scm|\d+,?\d+\sm|\d+\sm/g
````

#### 2) Skriv ett regex som matchar ett svenskt postnummer.
````
/\d{3}\s\d{2}/
````

#### 3) Skriv ett regex som matchar ett datum skrivet enligt den internationella standarden ISO 8601.
````
/\d{4}-\d{2}-\d{2}/
````

#### 4) Skriv ett regex som matchar ett pengavärde i siffror. Exempel på värden som ska matchas:
* 200 kr
* 12,50 kr
* 0,35 kr

````
/\d+,?\d+\s?kr|\d+\s?kr/g
````

#### 5a) Skriv ett regex som matchar en e-postadress..
````
/[\w-\.]+@([\w-]+\.)+([a-z]|[0-9]){2,4}/g
````

#### 5b) Gör ett regex som matchar en komplett e-postadress enligt specifikationen..
````
/[\w-\.]+@([\w-]+\.)+[\w-]{2,4}/g
````
<br>

### 3. Öva på user stories
````
User Story 1:
Som Scrum Master vill jag läsa på om Sprint Planning så att jag inte missar något.

test_sprint_planning


Scenario:
* Surfa in på sidan https://lejonmanen.github.io/agile-helper/
* Tryck på knappen 'Första'
* Tryck på knappen 'Börja sprinten med Sprint planning'.
* Kontrollera att 'Sprint planning' (h2) syns på sidan.
````
````
User Story 2:
Som Scrum Master vill jag läsa på vad man gör på en daily standup så att jag inte missar något.

test_daily_standup


Scenario:
* Surfa in på sidan https://lejonmanen.github.io/agile-helper/
* Tryck på knappen 'Någonstans mitt i'
* Tryck på 'Börja varje dag med Daily Standup'.
* Kontrollera att 'Daily standup' (h2) syns på sidan.

````
````
User Story 3:
Som Scrum Master vill jag läsa på vad som ska göras i en Sprint Review så att jag inte missar något.

test_sprint_review

Scenario:
* Surfa in på sidan https://lejonmanen.github.io/agile-helper/
* Tryck på knappen 'Sista'
* Tryck på knappen 'Presentera ert arbete för produktägaren under Sprint Review.
* Kontrollera att 'Sprint review' (h2) syns på sidan.
````
````
User Story 4:
Som en användare vill jag att rubriken (h1) ska vara Agile helper så att jag vet att jag är på rätt sida.

test_page_header

Scenario:
* Surfa in på sidan https://lejonmanen.github.io/agile-helper/
* Kontrollera att rubriken är 'Agile helper'
````
````
User Story 5:
Som en icke svensktalande person vill jag kunna byta språk på hemsidan till engelska så att jag förstår.

test_page_language

Scenario:
* Surfa in på sidan https://lejonmanen.github.io/agile-helper/
* Klicka på engelska flaggan
* Kontrollera att den första paragrafen är på engelska, den ska börja på "What day".
````

<br>

### 4. Öva på E2E tests

````
def test_sprint_planning(page: Page):
    page.goto(base_url)

    page.get_by_role("button").get_by_text(re.compile("Första")).click()
    page.get_by_role("button").get_by_text(re.compile("Sprint planning.+")).click()

    heading = page.get_by_role("heading").get_by_text(re.compile("Sprint planning"))

    expect(heading).to_be_visible()
````
````
def test_daily_standup(page: Page):
    page.goto(base_url)

    page.get_by_role("button").get_by_text(re.compile("Någon.+i")).click()
    page.get_by_role("button").get_by_text(re.compile("Börja.+Daily standup")).click()

    heading = page.get_by_role("heading").get_by_text(re.compile("Daily standup"))

    expect(heading).to_be_visible()
````
````
def test_sprint_review(page: Page):
    page.goto(base_url)

    page.get_by_role("button").get_by_text(re.compile("Sista")).click()
    page.get_by_role("button").get_by_text(re.compile("Presentera.+Sprint review")).click()

    heading = page.get_by_role("heading").get_by_text(re.compile("Sprint review"))

    expect(heading).to_be_visible()
````
````
def test_page_header(page: Page):

    page.goto(base_url)

    heading = page.get_by_role("heading").get_by_text(re.compile("Agile helper"))

    expect(heading).to_be_visible()
````
````
    page.goto(base_url)

    page.get_by_test_id(re.compile("language-en")).click()

    paragraph = page.get_by_role("paragraph").get_by_text(re.compile("What day.+"))

    expect(paragraph).to_be_visible()
````
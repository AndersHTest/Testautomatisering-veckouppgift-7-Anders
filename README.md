# Playwright
## Vecka 40
<br>

### Status uppgifter

| Uppgift                         | Status | 🟠🟡🟢 |
|---------------------------------|--------|--------|
| 1 Diskussion                    | 100%   | 🟢     |
| 2 Öva på Regex                  | 100%   | 🟢     |
| 3 Öva på user stories           | 0%     | 🟠     |
| 4 Öva på E2E tests              | 0%     | 🟠     |


### 1. Diskussion

#### 1a)
````
C.
````
#### 1b)
````
T.ex '/nisse/gi' för att matcha alla eller '(?i)nisse' för att matcha strängarna en åt gången.
````
#### 1c)
````
A.
````
#### 1d)
````
Ingen full sträng matchas.

'en' matchas i inconsequential (Svar; B).
````

#### 1e)
````
C och D. Förklaring: (je[vilket tecken som helst][minst 1 gång]e)
````
#### 1f)
````
Ingen full sträng matchas. Uttrycket letar efter någon del som börjar med mellanslag och ett a efter.
Sedan ett 'n' 1 gång eller 0 gånger därefter ett whitespace/mellanslag.
Utrycket hade matchat " an " eller " a ".

Det görs två matchningar i sträng C och en matchning i sträng D.
````
#### 1g)
````
A. Strängar som innehåller "line" eller "lines".
B. Strängar som börjar med ett eller flera a och avslutas med ö. T.ex "aaaaaaaaö" eller "aö"
C. Uttrycket kommer matcha vokaler i en sträng.
D. Strängar som innehåller enskilda siffror eller siffror i grupp.
F. Strängar som innehåller siffror i formatet nnnn-nn-nn. T.ex 1111-22-33.
````
#### 2a)
````

User Story:
Som en student vill jag kunna surfa in på agile helper för att avsluta en sprint på korrekt sätt.
````
#### 2b)
````

* Surfa in på hemsidan
* Välj "Sista"
* Välj "Avsluta sprinten med att utvärdera ert arbete i Sprint retrospective"
* Kontrollera att texten om Sprint Retrospective syns. (Rubriken "Sprint retrospective" syns).

````
#### 3)
````
-
````

### 2. Öva på Regex


#### 1a)
````
/\d+\scm/ eller /\d*\scm/
````

#### 1b)
````
/\d+\scm/g eller /\d*\scm/g (#lägger till /g för att hitta alla matchningar)
````

#### 1c)
````
/\d+\scm|\d+,?\d+\sm|\d+\sm/g
````

#### 2)
````
/\d{3}\s\d{2}/
````

#### 3)
````
/\d{4}-\d{2}-\d{2}/
````

#### 4)
````
/\d+,?\d+\s?kr|\d+\s?kr/g
````

#### 5a)
````
/[\w-\.]+@([\w-]+\.)+([a-z]|[0-9]){2,4}/g
````

#### 5b)
````
/[\w-\.]+@([\w-]+\.)+[\w-]{2,4}/g
````

### 3. Öva på user stories

### 4. Öva på E2E tests
![Logo del Proyecto](img/NiTex.png)
## Nicole Durand Zeballos

# Dependencies
1. **Python 3**: Make sure you have Python 3 installed.
2. **wkhtmltopdf**: Necessary tool to convert HTML to PDF.
   ```bash
   sudo apt-get install wkhtmltopdf
3. **colorama**: To work with colorful text in the console.
   ```bash
   pip install colorama
4. **anytree**: To work with tree structures.
   ```bash
   pip install anytree
5. **tabulate**: To format tables.
   ```bash
   pip install tabulate
6. **pdfkit**: To generate PDF files from HTML.
   ```bash
   pip install pdfkit

# How to Compile
1. Clone the repository
   ```bash
   git clone git@github.com:nicoleeed/nitex.git
3. Execution command
   ```bash
   python3 compiler.py
   
# Language Syntax

## Productions
0.  G -> C
1.  C -> TEXT C
2.  C -> NLIST C
3.  C -> LIST C
4.  C -> NL C
5.  C -> STEXT C
6.  C -> TB C
7.  C -> ε
8.  TM -> ALPHANUM TM1
9.  TM -> STEXT TM1
10. TM1 -> TM
11. TM1 -> ε
12. TEXT -> /p BLCO TM BLCC
13. TEXT -> /t1 BLCO TM BLCC
14. TEXT -> /t2 BLCO TM BLCC
15. TEXT -> /t3 BLCO TM BLCC
16. TEXT -> /url BLCO TM BLCC
17. TEXT -> /img BLCO TM BLCC
18. STEXT -> /b BLCO TM BLCC
19. STEXT -> /i BLCO TM BLCC
20. STEXT -> /u BLCO TM BLCC
21. ITEML -> BLCO TM BLCC ITEML1
22. ITEML1 -> , ITEML
23. ITEML1 -> ε
24. LIST -> /l BLCO ITEML BLCC
25. NLIST -> /sl BLCO ITEML BLCC
26. NL -> /n
27. BLCO -> {
28. BLCC -> }
29. CHAR -> PLAIN_TEXT
30. ALPHANUM -> CHAR
31. ALPHANUM -> DIGIT
32. DIGIT -> INT
33. TB -> /tb BTO TBZ BTC BLCO ITEML BLCC
34. BTO -> [
35. BTC -> ]
36. TBZ -> PO DIGIT , DIGIT PC
37. PO -> (
38. PC -> )

## Parse Table

|         | $ | /p | /b | /i | /u | /t1 | /t2 | /t3 | /url | /img | /sl | /l | /n | /tb | { | } | , | PLAIN_TEXT | INT | ( | ) | [ | ] |
|---------|---|----|----|----|----|-----|-----|-----|------|------|-----|----|----|-----|----|----|----|-------------|-----|---|---|---|---|
| G       | 0 | 0  | 0  | 0  | 0  | 0   | 0   | 0   | 0    | 0    | 0   | 0  | 0  | 0   |    |    |    |             |     |   |   |   |   |
| C       | 7 | 1  | 5  | 5  | 5  | 1   | 1   | 1   | 1    | 1    | 2   | 3  | 4  | 6   |    |    |    |             |     |   |   |   |   |
| TM      |   |    | 9  | 9  | 9  |     |     |     |      |      |     |    |    |     |    |    |    | 8           | 8   |   |   |   |   |
| TM1     | 11|    | 10 | 10 | 10 |     |     |     |      |      |     |    |    |     |    | 11 |    | 10          | 10  |   |   |   |   |
| TEXT    |   | 12 |    |    |    | 13  | 14  | 15  | 16   | 17   |     |    |    |     |    |    |    |             |     |   |   |   |   |
| STEXT   |   |    | 18 | 19 | 20 |     |     |     |      |      |     |    |    |     |    |    |    |             |     |   |   |   |   |
| ITEML   |   |    |    |    |    |     |     |     |      |      |     |    |    |     | 21 |    |    |             |     |   |   |   |   |
| ITEML1  | 23|    |    |    |    |     |     |     |      |      |     |    |    |     |    | 23 | 22 |             |     |   |   |   |   |
| LIST    |   |    |    |    |    |     |     |     |      |      |     | 24 |    |     |    |    |    |             |     |   |   |   |   |
| NLIST   |   |    |    |    |    |     |     |     |      |      | 25  |    |    |     |    |    |    |             |     |   |   |   |   |
| NL      |   |    |    |    |    |     |     |     |      |      |     |    | 26 |     |    |    |    |             |     |   |   |   |   |
| BLCO    |   |    |    |    |    |     |     |     |      |      |     |    |    |     | 27 |    |    |             |     |   |   |   |   |
| BLCC    |   |    |    |    |    |     |     |     |      |      |     |    |    |     |    | 28 |    |             |     |   |   |   |   |
| CHAR    |   |    |    |    |    |     |     |     |      |      |     |    |    |     |    |    |    | 31          |     |   |   |   |   |
| ALPHANUM|   |    |    |    |    |     |     |     |      |      |     |    |    |     |    |    |    | 29          | 30  |   |   |   |   |
| DIGIT   |   |    |    |    |    |     |     |     |      |      |     |    |    |     |    |    |    |             | 32  |   |   |   |   |
| TB      |   |    |    |    |    |     |     |     |      |      |     |    |    | 33  |    |    |    |             |     |   |   |   |   |
| TBZ     |   |    |    |    |    |     |     |     |      |      |     |    |    |     |    |    |    |             |     | 36|   |   |   |
| BTO     |   |    |    |    |    |     |     |     |      |      |     |    |    |     |    |    |    |             |     |   |   | 34|   |
| BTC     |   |    |    |    |    |     |     |     |      |      |     |    |    |     |    |    |    |             |     |   |   |   | 35|
| PO      |   |    |    |    |    |     |     |     |      |      |     |    |    |     |    |    |    |             |     | 37|   |   |   |
| PC      |   |    |    |    |    |     |     |     |      |      |     |    |    |     |    |    |    |             |     |   | 38|   |   |

## Terminals

|             |
|-------------|
| /p          |
| /t1         |
| /t2         |
| /t3         |
| /url        |
| /img        |
| /b          |
| /i          |
| /u          |
| /l          |
| /sl         |
| /tb         |
| ,           |
| /n          |
| {           |
| }           |
| PLAIN_TEXT  |
| INT         |
| [           |
| ]           |
| (           |
| )           |
| $           |

# Execution Examples

## Success Execution
Refer to the success execution example file.

- [Success Execution Example](ConsoleOutput/Success_Output.txt)

## Fail Execution: Error Handling
Refer to the error handling example file.

- [Fail Execution Example](ConsoleOutput/Fail_Output.txt)



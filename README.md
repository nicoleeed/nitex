███╗   ██╗██╗████████╗███████╗██╗  ██╗                                                                  
████╗  ██║██║╚══██╔══╝██╔════╝╚██╗██╔╝                                                                  
██╔██╗ ██║██║   ██║   █████╗   ╚███╔╝                                                                   
██║╚██╗██║██║   ██║   ██╔══╝   ██╔██╗                                                                   
██║ ╚████║██║   ██║   ███████╗██╔╝ ██╗                                                                  
╚═╝  ╚═══╝╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝                                                                  

               _  _ ___ ___ ___  _    ___   ___  _   _ ___    _   _  _ ___  
         ___  | \| |_ _/ __/ _ \| |  | __| |   \| | | | _ \  /_\ | \| |   \ 
        |___| |  ` || | (_| (_) | |__| _|  | |) | |_| |   / / _ \| .` | |) |
              |_|\_|___\___\___/|____|___| |___/ \___/|_|_\/_/ \_\_|\_|___/ 


╔═╗╦═╗╔═╗╔╦╗╦ ╦╔═╗╔╦╗╦╔═╗╔╗╔╔═╗
╠═╝╠╦╝║ ║ ║║║ ║║   ║ ║║ ║║║║╚═╗
╩  ╩╚═╚═╝═╩╝╚═╝╚═╝ ╩ ╩╚═╝╝╚╝╚═╝
0  G -> C
1  C -> TEXT C
2  C -> NLIST C
3  C -> LIST C
4  C -> NL C
5  C -> STEXT C
6  C -> TB C
7  C -> ε
8  TM -> ALPHANUM TM1
9  TM -> STEXT TM1
10 TM1 -> TM
11 TM1 -> ε
12 TEXT -> /p BLCO TM BLCC
13 TEXT -> /t1 BLCO TM BLCC
14 TEXT -> /t2 BLCO TM BLCC
15 TEXT -> /t3 BLCO TM BLCC
16 TEXT -> /url BLCO TM BLCC
17 TEXT -> /img BLCO TM BLCC
18 STEXT -> /b BLCO TM BLCC
19 STEXT -> /i BLCO TM BLCC
20 STEXT -> /u BLCO TM BLCC
21 ITEML -> BLCO TM BLCC ITEML1
22 ITEML1 -> , ITEML
23 ITEML1 -> ε
24 LIST -> /l BLCO ITEML BLCC
25 NLIST -> /sl BLCO ITEML BLCC
26 NL -> /n
27 BLCO -> {
28 BLCC -> }
29 CHAR -> PLAIN_TEXT
30 ALPHANUM -> CHAR
31 ALPHANUM -> DIGIT
32 DIGIT -> INT
33 TB -> /tb BTO TBZ BTC BLCO ITEML BLCC
34 BTO -> [
35 BTC -> ]
36 TBZ -> PO DIGIT , DIGIT PC
37 PO -> (
38 PC -> )

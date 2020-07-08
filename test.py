from OSINT.data_source import virustotal
vt = virustotal.Virustotal()


ip_str  = """134[.]209.200.91
139[.]59.1.154
139[.]59.79.105
139[.]59.81.167
157[.]245.78.153
165[.]22.201.190
178[.]62.210.85
188[.]166.14.73
188[.]166.25.156
202[.]59.79.131"""

hash_str = """7a5b645a6ea07f1420758515661051cff71cdb34d2df25de6a62ceb15896a1b6
b11dbaf0dd37dd4079bfdb0c6246e53bc75b25b3a260c380bb92fcaec30ec89b
aeb38a11ffc62ead9cdabba1e6aa5fce28502a361725f69586c70e16de70df2c
71c88a59b16dbcf7f061d01ea2015658136a8d4af60beb01caa94eeb74c733cd
ab209db9694a3b69427fc5857a8a47d0822db4d8372434fc091dfc3e85510719
4a6990be2d43f482fe2ab377b5e798da47ba7e02f23dfb6dba26b5011e222d25
7deeb35d7e88b769d286cc7892ee5966a27c39f03c8ac12dec21733faeffa350"""
hash2_str = """3bb90869523233cf965cf4a171d255c891c0179afd6d28198aa2af4e934f0055
570ef552b426f8337514ebdcb5935a132e5a8851a7252528c49d6d0d4aba34d9
059606e707a90333528043bdefbc7a55a27205aabed0ccd46c3966c2a53eea4e
1cda23e924ca606593a31ad54973266676c6540487a3baa29992c172d380bbd6
23091a9383704d22468f6e54babd57e64ced344900e5d3d693daf8bf609c997b
a2bf84f96f8d616ea248ac8f7bbb9d31b22920be4b3991982be0a88326303470
3cfbf274265860f176d6dbfad4df45a9c6953b71f9f439c87aeac36b38fde5b5
c31afceaef91380c658e4d77a78689cafb0f4179f3b251200e969195cbf4cf7b
1c3f185951b21d35f13b2a999a5d4d6b6db8f4b913e3b198fb2c86d4cd0b7781
852d4c98a786cb2b0fb10b4513163e3934b66e4d95a66de8ddcc6abc066dc61d
78ff0507cac9828fb94595d702cd2c22b8bec7a57c2159b78c924c0d0d5f8ccb
e40bdd8ff9e6432008afd54d6d526049ac6bd925dadc2b5a38f78c96df950d1a
cc0787025b297ed80e322d30b655d7c84c7c3a0d18c2089b4f545a03214b7557
e2db20377e8cc65c4cf262df15e47fc21b9a9f83fb7931d44b8d28c6b9ffc0f1
a319395e6cf01edb4c6ca879f36a11f4cf33b58657de379123851c63da6a3ef4
bec281baf1312fd059a315d5890ac3c959909047b3473103b069e5ca2ba2fdd1
e9b00f6f47eb70b35713bf7afd345a197f6d290afb8d2684afd8345edc086b29
c9ee415401566139237b14373f6a7a36013b6af693c729b9a5c21cc40e0ad5c6
f9a344c251dc391c5d12e8011185fe033b5ae902c5a866ccd8d8b49881b17151
3e196c77c006e299f26fb05df15644366433fceed73219e0ba6acef0b881531b
5a1a9a6bfc422bd547536e340725328cb04fd72587d83f7e06682abdeddb69a7
95bb65edc9e8e070680e0c85f72927a2bbb553f96fc1078d85e7df7a02c15165
365af2ddad27701d9d17a069b21dc95d39a2d2c5f78bea655db9123ff05fe086
b9c703dba1977fb34e9f6ac49ccdd0efb752ed010939d54f30f8d91358a9214d
7b0494937fd5a2bedf94999553d37e6049e45b935732a594e833078ed483a5ed
d6f62ce9696887693081373b87792fa53617f8412fa8e6b1a7de1a01070a9bae
d3f3df7cf1ece2519829ee75d29ca054e8233896b7fe50b41eaafda497ff0498
82155aaf86ba3555d5e809500c67da51e1586a6a97a9755870e22900c8790019
b3650199d6713d669992eebb3c4f05c80a97c470596170b5be16257b73785957
8f1abb122f35e66f20bd345323fb5eb8dbdbde785137c80c1e55fdaf525520bd
aa05a822f26a493efb27046f772790cc67cca29cd9f842b7bc6df2b391ce2ff8
59fd696f95182be1a51011caec172c5461ddacd556a43c329d939842cf7e7d7f
aa05a822f26a493efb27046f772790cc67cca29cd9f842b7bc6df2b391ce2ff8
59fd696f95182be1a51011caec172c5461ddacd556a43c329d939842cf7e7d7f"""

hash3_str = """482858b70888acf67a5c2d30ddee61ca7b57ff856feaad9a2fa2b5d4bc0bbd7d
689f7d3f0def72248c4ff4b30da5022ec808a20e99b139e097c2a0d0ba5bab66
dbb5bba499e0ab07e545055d46acf3f78b5ed35fff83d9c88ce57c6455c02091
e37a0b4145f22ce7f7478918320c019a6014060cb033aafec18a8d130c4c426b
4b0c2f790c7b9c84517648bb36964c859629736dab1fa5466d91bd23f69c9b55
c2d9bbd5163a8e733483bf5d0d4959f053a2307d275b81eb38e69d87f1f5df7e
a0cfec815cb74a7671265fd5e0790a2a79c05fe0ef16d2d0c87584049d06658b
1ea22d132c1d478347d7e4e72d79bae29f18df9bec5a3016a5a9971f702a8095
b9efca96d451c0b4028b6081456c1ddd3035ab39e6a60bdd831bcf4a472a31ae
b081b818e5fbd5d2741822c9e161e536a8497764fab5ac79143614bbce8308f6    
d2fd448a386416fdad0059be1bb61f49e99fc76e7efbd5f5e377dbbf6e7e3599
bdbc9dc2f2812a9808357aafe908e7206c9168bc7fea761dec871926de23eec0"""


url_str= """http://bit[.]ly/iaf-guidelines
http://tecbeck[.]com/IAP39031[.]docx
http://bitly[.]com/38A5BEO
hxxp://134[.]209.196.51/jquery-3.3.2.min.js
hxxp://139[.]59.1.154/ca
hxxp://139[.]59.1.154/submit.php
hxxp://139[.]59.79.105/jquery-3.3.1.min.js
hxxp://139[.]59.79.105/jquery-3.3.2.min.js
hxxp://188[.]166.14.73/jquery-3.3.1.min.js
hxxp://188[.]166.14.73/jquery-3.3.2.min.js
hxxp://157[.]245.78.153/11.txt
hxxp://157[.]245.78.153/12.txt
hxxp://157[.]245.78.153/21.txt
hxxp://157[.]245.78.153/22.txt
hxxp://157[.]245.78.153/31.txt
hxxp://157[.]245.78.153/32.txt
hxxp://157[.]245.78.153/41.txt
hxxp://157[.]245.78.153/42.txt
hxxp://157[.]245.78.153/51.txt
hxxp://157[.]245.78.153/52.txt
hxxp://202[.]59.79.131/7XyT
hxxp://202[.]59.79.131/o2Q7NGUwpFfDzcLMnkuMyAy-IGt8KERPl-6lrRhxcbPJkZwAr33
hxxp://202[.]59.79.131:8080/8g-QvDrvM4hSI0c3D6iC8Aib6wZbs
hxxp://134[.]209.200.91/jquery-3.3.0.min.js
hxxp://139[.]59.1.154/ToKN
hxxp://139[.]59.79.105/jquery-3.3.0.min.js
hxxp://139[.]59.81.167/jquery-3.3.0.min.js
hxxp://165[.]22.201.190/jquery-3.3.0.min.js
hxxp://188[.]166.14.73/jquery-3.3.0.min.js
hxxp://188[.]166.25.156/jquery-3.3.0.min.js
hxxp://202[.]59.79.131/YZn_pcfLiUILewp6Vuku9gvUqfMFnPLBP5Aju9QS709n4zRAd-3e4IuPF5kv0uhXSAiJqurq5yPJ-B9zSZ5rHig07RcWcQPIPD04YZhq1JCGWwYI-AfFFHI0qj4LRDhsuaBdQEihGmxzZ8obxUbv5RUfaxm7XwOkWJK8D9xK5gibPGGBiNs41hYB0Kar325FCcCJAIFIzWOw9WLOt6EfrWaEO69aHp
hxxps://pastebin[.]com/raw/kf3y5uzt
hxxps://pastebin[.]com/raw/ftfSHyPz
hxxps://pastebin[.]com/raw/hAKzruWe
hxxps://hastebin[.]com/raw/ufaxamogav
hxxps://pastebin[.]com/raw/KzmUrrnB
hxxps://pastebin[.]com/raw/aMfFtqjq
hxxps://pastebin[.]com/raw/Q6bMcduX
hxxps://pastebin[.]com/raw/7VmV7jXA
hxxps://pastebin[.]com/raw/8E8YCryu
hxxps://pastebin[.]com/raw/1tKX0v5U
hxxps://pastebin[.]com/raw/kpn2k1jc
hxxps://pastebin[.]com/raw/xiV89Xa9
hxxps://pastebin[.]com/raw/ZMTjGJUn
hxxps://pastebin[.]com/raw/CRuQvJk1
hxxps://pastebin[.]com/raw/zbL0w8sm
hxxps://pastebin[.]com/raw/yP7eQKsv
hxxps://pastebin[.]com/raw/1Q7jYDmz
hxxps://pastebin[.]com/raw/vc8TUZPN
hxxps://pastebin[.]com/raw/R0HzuGWE
hxxps://pastebin[.]com/raw/ehQyY1YX
hxxps://pastebin[.]com/raw/LRztjgkq
hxxps://pastebin[.]com/raw/QyDZhfer
hxxps://pastebin[.]com/raw/MQUG0Q07
hxxps://pastebin[.]com/raw/LtVteHbz
hxxps://pastebin[.]com/raw/k2PQZqzF
hxxps://pastebin[.]com/raw/azzHZ11B
hxxps://pastebin[.]com/raw/4u1ScSn7
hxxps://pastebin[.]com/raw/5tSnVWcn
hxxps://pastebin[.]com/raw/a0kPq7bq
hxxps://pastebin[.]com/raw/cK8nhTYw
hxxps://pastebin[.]com/raw/p34D4vbL
hxxps://pastebin[.]com/raw/YVvG43bi
hxxps://pastebin[.]com/raw/iyKjw7jR
hxxps://pastebin[.]com/raw/0hAzfmrR
hxxps://pastebin[.]com/raw/aGSg1f3Y
hxxps://pastebin[.]com/raw/i5JkU138
hxxps://pastebin[.]com/raw/LQjs18Cy
hxxps://pastebin[.]com/raw/rHeWv7t0
hxxps://pastebin[.]com/raw/bqL6CSp3
hxxps://pastebin[.]com/raw/WJFvRHXv
"""
with open("docs/strongpity_hash.csv") as f:
    strongpity_hashlist = [i.strip() for i in f.read().split()]

hash_list = [i.strip() for i in hash3_str.split()]
url_list = [i.strip().replace('[.]', '.').replace('hxxp', "http") for i in url_str.split()]
term_list = list(set(strongpity_hashlist))
vt.run("hash", term_list, "2020-07-08")
# coding: utf-8
"""
Cage composition:
 (12,14,15,16) = (2,6,0,0,)
"""
desc={"ref": {"Struct33": 'Dutour Sikirić, Mathieu, Olaf Delgado-Friedrichs, and Michel Deza. “Space Fullerenes: a Computer Search for New Frank-Kasper Structures” Acta Crystallographica Section A Foundations of Crystallography 66.Pt 5 (2010): 602–615.',
              "A15": "Frank, F.C., and JS Kasper. “Complex Alloy Structures Regarded as Sphere Packings. II. Analysis and Classification of Representative Structures.” Acta Crystallographica 12.7 (1959): 483–499.",
              "sI": "Jeffrey, G A. “Hydrate Inclusion Compounds.” Inclusion Compounds 1 (1984): 135–190.",
              "CS1": "Kosyakov, Viktor I, and T M Polyanskaya. “Using Structural Data for Estimating the Stability of Water Networks in Clathrate and Semiclathrate Hydrates.” Journal of Structural Chemistry 40.2 (1999): 239–245.",
              "MEP": "http://www.iza-structure.org/databases/"},
      "usage": "No options available.",
      "brief": "Clathrate type I."
      }

pairs="""
17 26
34 39
6 10
33 39
7 12
28 35
32 40
34 41
42 30
43 31
19 15
21 44
3 27
7 36
29 4
23 45
14 18
9 18
25 33
37 29
5 19
8 0
20 5
11 1
27 38
37 45
16 3
25 43
28 43
19 27
21 29
7 38
36 16
32 30
28 27
17 38
30 2
40 23
33 20
26 12
25 9
26 11
22 34
38 4
14 28
6 24
4 41
0 21
7 14
36 23
5 17
25 2
13 39
22 35
14 40
21 11
5 2
32 26
20 10
6 4
6 3
36 29
24 39
16 15
20 41
18 44
23 42
44 31
8 1
15 30
9 1
0 10
13 3
24 37
34 45
0 16
33 8
9 32
31 10
35 2
45 1
18 37
13 42
8 42
11 41
12 44
12 15
13 35
22 40
17 22
24 43
19 31
"""

waters="""
0.625 0.8125 0.5
0.3125 0.6875 0.3125
0.3125 0.3125 0.6875
0.875 0.0 0.6875
0.6875 0.875 0.0
0.5 0.375 0.8125
0.8125 0.8125 0.8125
0.8125 0.1875 0.1875
0.375 0.8125 0.5
0.1875 0.5 0.375
0.6875 0.6875 0.6875
0.5 0.625 0.1875
0.6875 0.3125 0.3125
0.125 0.0 0.6875
0.0 0.3125 0.125
0.625 0.1875 0.5
0.75 0.0 0.5
0.5 0.25 0.0
0.0 0.5 0.25
0.6875 0.3125 0.6875
0.5 0.625 0.8125
0.6875 0.6875 0.3125
0.3125 0.125 0.0
0.125 0.0 0.3125
0.0 0.6875 0.875
0.1875 0.5 0.625
0.5 0.375 0.1875
0.8125 0.1875 0.8125
0.0 0.3125 0.875
0.8125 0.8125 0.1875
0.375 0.1875 0.5
0.8125 0.5 0.625
0.3125 0.3125 0.3125
0.3125 0.6875 0.6875
0.3125 0.875 0.0
0.1875 0.1875 0.8125
0.875 0.0 0.3125
0.0 0.6875 0.125
0.6875 0.125 0.0
0.1875 0.8125 0.8125
0.1875 0.1875 0.1875
0.5 0.75 0.0
0.25 0.0 0.5
0.0 0.5 0.75
0.8125 0.5 0.375
0.1875 0.8125 0.1875
"""

coord= "relative"

cages="""
12 0.5 0.5 0.5
14 0.5 0.0 -0.25
14 0.0 0.25 0.5
14 0.75 0.5 0.0
14 0.5 0.0 0.25
12 0.0 0.0 0.0
14 0.25 0.5 0.0
14 0.0 -0.25 0.5
"""

bondlen = 3


cell = """
12.747893943706936 12.747893943706936 12.747893943706936
"""

density = 0.6637037332735554



from genice.cell import cellvectors
cell = cellvectors(a=12.747893943706936,
                   b=12.747893943706936,
                   c=12.747893943706936)

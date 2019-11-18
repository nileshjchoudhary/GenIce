# coding: utf-8
"""
Data source: Dutour Sikirić, Mathieu, Olaf Delgado-Friedrichs, and Michel Deza. “Space Fullerenes: a Computer Search for New Frank-Kasper Structures” Acta Crystallographica Section A Foundations of Crystallography 66.Pt 5 (2010): 602–615.

Cage composition:
 (12,14,15,16) = (3,2,2,0,)
"""
desc={"ref": {"Z": "Frank, F.C., and JS Kasper. “Complex Alloy Structures Regarded as Sphere Packings. II. Analysis and Classification of Representative Structures.” Acta Crystallographica 12.7 (1959): 483–499.",
              "sIV": "Jeffrey, G A. “Hydrate Inclusion Compounds.” Inclusion Compounds 1 (1984): 135–190.",
              "HS1": "Kosyakov, Viktor I, and T M Polyanskaya. “Using Structural Data for Estimating the Stability of Water Networks in Clathrate and Semiclathrate Hydrates.” Journal of Structural Chemistry 40.2 (1999): 239–245."},
      "usage": "No options available.",
      "brief": "Clathrate type IV."
      }

pairs="""
9 20
38 5
6 1
31 15
32 35
4 23
8 27
23 3
12 34
9 26
37 34
0 36
36 2
20 8
4 11
5 12
5 14
6 13
6 16
32 36
9 13
29 16
22 33
12 30
26 32
26 5
34 20
23 7
33 30
19 15
37 39
18 17
8 33
8 25
18 28
38 24
37 25
19 29
6 34
21 30
14 33
18 3
3 22
11 31
1 30
3 21
27 1
28 2
19 10
28 38
22 0
7 10
13 15
4 24
14 17
22 15
24 27
39 2
16 24
17 25
29 39
9 10
21 2
35 10
11 29
4 35
0 7
27 26
31 32
14 13
19 18
31 1
28 35
16 17
37 38
20 0
12 36
39 7
23 25
11 21
"""

waters="""
0.875 0.75 0.0
0.20834 0.41667 0.80434
0.20834 0.79167 0.19566
0.58333 0.79167 0.19566
0.375 0.375 0.32066
0.375 0.0 0.67934
0.0 0.375 0.67934
0.79167 0.58334 0.19566
0.625 0.625 0.67934
0.66667 0.33333 0.875
0.66667 0.33334 0.125
0.20833 0.41667 0.19566
0.20833 0.79167 0.80434
0.79167 0.20833 0.80434
0.625 0.0 0.67934
0.875 0.125 0.0
0.0 0.25 0.5
0.75 0.0 0.5
0.625 0.0 0.32066
0.79167 0.20833 0.19566
0.79167 0.58333 0.80434
0.33333 0.66667 0.125
0.75 0.875 0.0
0.625 0.625 0.32066
0.25 0.25 0.5
0.75 0.75 0.5
0.41667 0.20833 0.80434
0.375 0.375 0.67934
0.375 0.0 0.32066
0.0 0.375 0.32066
0.33334 0.66667 0.875
0.125 0.25 0.0
0.25 0.125 0.0
0.58334 0.79167 0.80434
0.0 0.625 0.67934
0.41667 0.20834 0.19566
0.125 0.875 0.0
0.0 0.75 0.5
0.25 0.0 0.5
0.0 0.625 0.32066
"""

coord= "relative"

cages="""
12 -0.5 -0.5 0.0
12 0.5 0.0 0.0
14 0.0 0.0 0.28265
15 -0.33333 -0.66667 0.5
12 0.0 0.5 0.0
14 0.0 0.0 -0.28265
15 0.33333 0.66667 0.5
"""

bondlen = 3


cell = """
12.747893943706936 0.0 0.0
-6.373946971853465 11.040000000000003 0.0
8.000039712716786e-16 1.3856475244994196e-15 13.065056338344617
"""

density = 0.6502388941843554



from genice.cell import cellvectors
cell = cellvectors(a=12.747893943706936,
                   b=12.747893943706938,
                   c=13.065056338344617,
                   C=120)

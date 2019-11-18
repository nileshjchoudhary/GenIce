# coding: utf-8
"""
Data source: Dutour Sikirić, Mathieu, Olaf Delgado-Friedrichs, and Michel Deza. “Space Fullerenes: a Computer Search for New Frank-Kasper Structures” Acta Crystallographica Section A Foundations of Crystallography 66.Pt 5 (2010): 602–615.

Cage composition:
 (12,14,15,16) = (11,2,2,4,)
"""

pairs="""
94 26
47 76
96 98
26 37
92 54
62 17
75 44
105 86
101 55
62 24
0 50
90 77
40 33
53 98
64 96
45 85
85 78
15 10
39 93
89 42
106 68
47 32
14 50
63 5
21 44
37 78
52 4
86 43
101 90
79 55
39 65
88 86
34 11
31 4
57 102
56 70
69 8
28 46
22 81
78 17
28 84
29 84
15 91
38 91
34 89
71 21
100 68
75 46
56 91
82 2
1 97
71 103
28 33
5 79
74 102
45 93
58 6
6 57
94 53
29 41
23 100
75 106
50 2
24 51
62 79
31 105
6 92
23 26
25 27
22 18
15 72
84 21
11 74
106 4
81 37
1 69
96 85
35 16
12 88
70 93
102 19
63 26
40 106
73 42
9 19
13 44
60 48
61 50
83 16
14 3
92 96
30 49
13 7
13 3
56 59
58 59
82 83
36 38
58 85
90 51
79 77
104 65
10 83
105 67
73 107
37 69
18 19
24 4
25 5
60 35
61 38
30 67
41 32
11 82
80 65
47 0
39 91
107 2
87 98
41 43
0 89
99 35
0 49
17 8
56 54
29 20
39 99
14 48
6 18
11 60
3 49
10 61
22 94
25 94
28 95
24 95
27 97
38 80
47 103
30 20
77 69
25 17
82 80
31 20
73 7
32 21
59 72
57 72
71 3
12 67
15 74
12 71
103 48
73 14
45 104
30 42
41 49
9 99
46 51
87 68
23 33
16 65
76 2
1 5
95 86
9 54
34 107
53 8
40 55
29 52
81 70
33 52
32 105
87 78
18 27
99 74
58 81
19 104
75 101
102 80
36 54
7 20
59 104
12 107
45 27
100 46
87 63
62 68
22 64
44 31
48 66
1 98
70 97
95 55
13 43
93 64
10 89
23 77
101 43
53 100
9 64
92 97
36 35
60 61
34 103
90 52
40 63
66 76
8 51
66 42
57 36
83 66
72 16
84 88
88 7
76 67
"""

waters="""
0.20955 0.41909 0.11412
0.96076 0.28924 0.61668
0.00242 0.62621 0.06748
0.87621 0.12379 0.19053
0.32849 0.03924 0.38332
0.92152 0.46076 0.56809
0.66667 0.33334 0.77395
0.66667 0.33333 0.22605
0.0 0.0 0.54859
0.74758 0.87379 0.80947
0.25 0.25 0.0
0.75 0.75 0.0
0.87621 0.75242 0.19053
0.79288 0.20712 0.25582
0.79288 0.20713 0.11412
0.37379 0.37621 0.93252
0.37379 0.99758 0.93252
0.12258 0.87743 0.57782
0.79288 0.58576 0.74418
0.87621 0.75243 0.80947
0.41425 0.20712 0.25582
0.58091 0.79046 0.26546
0.62379 0.62621 0.69504
0.45591 0.54409 0.5
0.12258 0.87743 0.42219
0.96076 0.67152 0.61668
0.53924 0.46076 0.56809
0.00242 0.62621 0.69504
0.71076 0.67152 0.38332
0.37379 0.37621 0.30496
0.24758 0.12379 0.19053
0.37379 0.99758 0.30496
0.33333 0.66667 0.23569
0.53924 0.46076 0.43191
0.62379 0.62621 0.06748
0.62379 0.99758 0.93252
0.79288 0.20712 0.88589
0.32849 0.28924 0.61668
0.00242 0.37621 0.93252
0.33334 0.66667 0.86009
0.66667 0.33333 0.46114
0.20955 0.41909 0.26546
0.41425 0.20712 0.11412
0.00242 0.37621 0.30496
0.62379 0.99758 0.30496
0.20954 0.79046 0.73454
0.75485 0.87743 0.42219
0.33334 0.66667 0.13991
0.62379 0.99758 0.06748
0.12621 0.25243 0.19053
0.00242 0.37621 0.06748
0.0 0.0 0.45141
0.32849 0.28924 0.38332
0.75485 0.87743 0.57782
0.87621 0.12379 0.80947
0.92152 0.46076 0.43191
0.12621 0.25242 0.80947
0.66667 0.33334 0.86009
0.41425 0.20713 0.74418
0.24758 0.12379 0.80947
0.75 0.0 0.0
0.0 0.25 0.0
0.20591 0.79409 0.5
0.66667 0.33333 0.53887
0.58091 0.79046 0.73454
0.20954 0.79046 0.88589
0.37379 0.99758 0.06748
0.12621 0.87379 0.19053
0.45591 0.91182 0.5
0.12258 0.24515 0.57782
0.20955 0.41909 0.73454
0.74758 0.87379 0.19053
0.41425 0.20713 0.88589
0.66667 0.33333 0.13991
0.62379 0.62621 0.93252
0.71076 0.03924 0.38332
0.20955 0.79046 0.11412
0.20591 0.41182 0.5
0.32849 0.03924 0.61668
0.08818 0.54409 0.5
0.00242 0.62621 0.93252
0.37379 0.37621 0.69504
0.0 0.75 0.0
0.25 0.0 0.0
0.62379 0.62621 0.30496
0.37379 0.99758 0.69504
0.00242 0.62621 0.30496
0.53924 0.07849 0.56809
0.79288 0.58576 0.25582
0.37379 0.37621 0.06748
0.12258 0.24515 0.42219
0.20955 0.41909 0.88589
0.79288 0.20712 0.74418
0.33334 0.66667 0.76432
0.71076 0.67152 0.61668
0.96076 0.67152 0.38332
0.62379 0.99758 0.69504
0.00242 0.37621 0.69504
0.71076 0.03925 0.61668
0.58091 0.79046 0.88589
0.58819 0.79409 0.5
0.96076 0.28924 0.38332
0.79288 0.58576 0.88589
0.58091 0.79046 0.11412
0.12621 0.87379 0.80947
0.20955 0.79046 0.26546
0.53924 0.07849 0.43191
0.79288 0.58575 0.11412
"""

coord= "relative"

cages="""
12 -0.50484 -0.49515 -0.18655
12 -0.50484 -0.00969 -0.18655
14 0.0 0.0 0.08336
12 0.31394 0.15697 0.5
16 0.0 0.0 -0.30565
12 -0.15697 -0.31394 0.5
12 0.66667 0.33333 -0.34454
12 0.66667 0.33333 0.34454
12 0.00969 0.50484 -0.18655
15 0.33333 0.66667 0.0
16 0.0 0.0 0.30565
12 0.00969 0.50484 0.18655
16 0.33333 0.66667 -0.38309
14 0.0 0.0 -0.08336
12 -0.50484 -0.00969 0.18655
12 -0.15697 0.15697 0.5
16 0.33333 0.66667 0.38309
15 0.66667 0.33333 0.0
12 -0.50484 -0.49515 0.18655
"""

bondlen = 3


cell = """
13.300376876410896 0.0 0.0
-6.650188438205444 11.518464254878959 0.0
2.1742089062438547e-15 3.765840291883113e-15 35.5075260517175
"""

density = 0.593439662425076



from genice.cell import cellvectors
cell = cellvectors(a=13.300376876410896,
                   b=13.300376876410896,
                   c=35.5075260517175,
                   C=119.99999999999999)

desc={"ref": {"Struct28": 'Dutour Sikirić, Mathieu, Olaf Delgado-Friedrichs, and Michel Deza. “Space Fullerenes: a Computer Search for New Frank-Kasper Structures” Acta Crystallographica Section A Foundations of Crystallography 66.Pt 5 (2010): 602–615.'},
      "usage": "No options available.",
      "brief": "Clathrate structure classified by Dutour Sikirić."
      }


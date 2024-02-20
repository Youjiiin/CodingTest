n, m = map(int, input().split())
dna = [input() for _ in range(n)]
s = ''
set_dna = ['A', 'C', 'G', 'T']
hd = 0

for i in range(m):
    a_cnt, c_cnt, g_cnt, t_cnt = 0, 0, 0, 0
    for j in range(n):
        if dna[j][i] == set_dna[0]:
            a_cnt += 1
        elif dna[j][i] == set_dna[1]:
            c_cnt += 1
        elif dna[j][i] == set_dna[2]:
            g_cnt += 1
        elif dna[j][i] == set_dna[3]:
            t_cnt += 1
    cnt_list = [a_cnt, c_cnt, g_cnt, t_cnt]
    select = set_dna[cnt_list.index(max(cnt_list))]
    s += select
    for k in range(n):
        if dna[k][i] != select:
            hd += 1
print(s)
print(hd)
fat_sp = 67836.43
fat_rj = 36678.66
fat_mg = 29229.88
fat_es = 27165.48
fat_outros = 19849.53
fat_total = fat_sp + fat_rj + fat_mg + fat_es + fat_outros

rep_sp = fat_sp * 100 / fat_total
rep_rj = fat_rj * 100 / fat_total
rep_mg = fat_mg * 100 / fat_total
rep_es = fat_es * 100 / fat_total
rep_outros = fat_outros / fat_total

print("O percentual de representação que São Paulo teve foi de {:.2f}%" .format(rep_sp))
print("O percentual de representação que Rio de Janeiro teve foi de {:.2f}%" .format(rep_rj))
print("O percentual de representação que Minas Gerais teve foi de {:.2f}%" .format(rep_mg))
print("O percentual de representação que Espírito Santo teve foi de {:.2f}%" .format(rep_es))
print("O percentual de representação que Outros tiveram foi de {:.2f}%" .format(rep_outros))
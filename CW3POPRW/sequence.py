import pandas as pd

# Wczytaj CSV
df = pd.read_csv('truth_table3.csv', sep=';')

# Wybierz interesujące Cię kolumny
selected_columns = ["PR", "N", "P", "S", "R1'", "R0'", "ST'"]
df_selected = df[selected_columns]

# # Usuń duplikaty (tworzy kopię)
# df_unique = df_selected.drop_duplicates().copy()

# Sklej jako jeden ciąg binarny
df_selected.loc[:, 'binary_sequence'] = df_selected.astype(str).agg(''.join, axis=1)

# Zapisz do pliku tekstowego (po jednym słowie binarnym w wierszu)
df_selected['binary_sequence'].to_csv('unique_sequences.txt', index=False, header=False)

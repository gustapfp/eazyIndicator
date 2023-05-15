import fundamentus as fd
import os

# Define the directory path
dir_path = 'C:\\Users\\gusta\\OneDrive\\Desktop\\Projetos-Web\\Flask\\eazy_indicator\\backend\\data'

# Create the directory if it doesn't exist
if not os.path.exists(dir_path):
    os.makedirs(dir_path)

df = fd.get_resultado()

papers = df.index
for i in range(len(papers)):
  new_df = df.loc[df.index == papers[i]]
  doc_name = f'\\raw_data_{papers[i]}.json'
  new_df.to_json(dir_path + doc_name)

import os
import pysolr

# Create a connection to Solr
solr = pysolr.Solr('http://localhost:8983/solr/my_core', timeout=10)

# Path to the directory containing extracted text files
extracted_text_dir = 'extracted_text'

# Loop through extracted text files and index them into Solr
for filename in os.listdir(extracted_text_dir):
    with open(os.path.join(extracted_text_dir, filename), 'r', encoding='utf-8') as file:
        text = file.read()
        # Index the text into Solr
        solr.add([
            {
                'id': filename,  # Unique identifier for the document
                'text': text  # Extracted text content
            }
        ])

# Commit changes to Solr
solr.commit()


# import os
# import pysolr

# # Connect to Solr
# solr = pysolr.Solr('http://localhost:8983/solr/my_core', timeout=10)

# # Path to the directory containing extracted text files
# extracted_text_dir = 'extracted_text'

# # Loop through extracted text files and index them into Solr
# for filename in os.listdir(extracted_text_dir):
#     with open(os.path.join(extracted_text_dir, filename), 'r', encoding='utf-8') as file:
#         text = file.read()
#         solr.add([
#             {
#                 'id': 1,  # Unique identifier for the document
#                 'text': text  # Extracted text content
#             }
#         ])

# # Commit changes to Solr
# solr.commit()

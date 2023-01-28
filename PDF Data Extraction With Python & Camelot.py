#!/usr/bin/env python
# coding: utf-8

# ###### The purpose of this notebook is to extract tabular data from a pdf document and convert it into a pandas Dataframe. We will use camelot to extract the table data from the pdf, convert it to a pandas dataframe and clean it up. 

# In[1]:


# Step 1 - Import libraries

import camelot
import warnings 
warnings.filterwarnings('ignore')


# In[2]:


# Step 2 - Camelot Function to read in the pdf document
tables = camelot.read_pdf('gst-revenue-collection-march2020.pdf', flavor='stream', pages='0-3')
tables


# In[3]:


# Step 3 - This report gives us details such as accuracy and number of pages containing tables
tables[2].parsing_report


# Please note that 'page' returns the first page with tabular data and no of pages in our pdf document. 

# In[4]:


# Step 4 - This line will give us the shape(no. of rows,no. of columns) of the table in page 2
print('Shape of the table:',tables[2])


# In[5]:


# Step 5 - The following code will extract the table in page 2 of the pdf document.
df = tables[2].df
df


# In[6]:


tables[3].parsing_report


# In[7]:


# Step 6 - The following code will extract the table in page 2 of the pdf document.
df_one = tables[3].df
df_one


# In[8]:


# Step 7 - Appending df and df_one into one dataframe
df_two = df.append(df_one).reset_index(drop=True)
df_two


# In[9]:


# Step 8 - Dropping and replacing the header row as well as the last row
df_two.drop(df_two.index[42:], axis=0, inplace=True)
df_two.drop(df.index[0:1], axis=0, inplace=True)
df_two.columns = df.iloc[1]
df_two.drop(df.index[1], axis=0, inplace=True)
df_two


# In[10]:


df_two.info()


# In[12]:


df_two.to_excel("PdfTablesToExcel.xlsx")


# In[ ]:





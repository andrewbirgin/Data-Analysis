#!/usr/bin/env python
# coding: utf-8

# In[10]:


with open('Retail.txt',encoding="ISO-8859-1") as fh:
    lines = fh.readlines()
product_id_name = {}
purchase_dict = {}
for i in range(1, len(lines)):
    arr = lines[i].lower().strip().split(",")
    stockCode = arr[1].strip()
    desc = arr[2].strip()
    quantity = int(arr[3].strip())
    product_id_name[stockCode] = desc
    purchase_dict[stockCode] = purchase_dict.get(stockCode, 0) + quantity
        
sorted_purchase_dict = sorted(purchase_dict.items(), key = lambda item: item[1], reverse=True)[:10]
for k,v in sorted_purchase_dict:
    print(product_id_name[k])


# In[5]:


with open('Retail.txt',encoding="ISO-8859-1") as fh:
    lines = fh.readlines()
product_id_name = {}
purchase_dict = {}
for i in range(1, len(lines)):
    arr = lines[i].lower().strip().split(",")
    invoice_no = arr[0].strip()
    stockCode = arr[1].strip()
    desc = arr[2].strip()
    product_id_name[stockCode] = desc
    purchase_dict[invoice_no] = purchase_dict.get(invoice_no, []) + [stockCode]

copurchase_dict = {}

for k, v in purchase_dict.items():
    i = 0
    while i < len(v):
        j = i + 1
        while j < len(v):
            if v[i] > v[j]:
                copurchase_dict[(v[j],v[i])] = copurchase_dict.get((v[j],v[i]), 0) + 1
            else:
                copurchase_dict[(v[i],v[j])] = copurchase_dict.get((v[i],v[j]), 0) + 1            
            j += 1
        i += 1
        
sorted_copurchase_dict = sorted(copurchase_dict.items(), key = lambda item: item[1], reverse=True)[:10]
for k, v in sorted_copurchase_dict:
    print(f'{product_id_name[k[0]]}: {product_id_name[k[1]]}')
    
    


# In[ ]:





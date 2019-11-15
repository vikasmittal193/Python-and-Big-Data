#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json, os, sys, re


# In[2]:


with open('schemanotebook.txt','r') as file:
    schema_names = file.readlines()
    #print(schema_names)
    schema_list=[]
    for schema in schema_names:
        result = re.search("schemaName: '(.*)'}",schema)
        schema_list.append(result.group(1))
print(schema_list)


# In[3]:


#for this we need to make two tables in DB, for vertex list and edges. and GraphX will have these two tables as the input
schema_dict={}
schema_id=1 # here it can be the max present in the database 
for schema in schema_list:
    schema_id_dict = {}
    schema_id_dict['id'] = schema_id
    schema_dict[schema] = schema_id_dict
    schema_id = schema_id+1
print(schema_dict)


# In[4]:


with open('./schema_info/table_db_info.txt','r') as file2:
    table_schema=[obj.split('\t') for obj in file2.readlines()]
    for schema,prop in schema_dict.items():
        table_dict={} # for every schema we must have dict to store tables and their ids
        start_ele = prop['id']*10000
        for element in table_schema:
            if(element[0]==schema):
                table_dict[element[1].strip()]=start_ele
                start_ele=start_ele+1
            prop['children'] = table_dict
print(schema_dict) 


# In[38]:


#creating vertex list from schema_dict
vertex_list=[]
table_dict = {} # for storing table and corrresponding ids
for schema,table in schema_dict.items():
    flg=0
    if(schema_dict[schema]['children'] == {}):
        vertex=[]
        vertex_id = schema_dict[schema]['id']
        vertex.append(vertex_id)
        vertex_schema = schema
        vertex.append(vertex_schema)
        vertex_list.append(vertex)
    else:
        for table,table_id in schema_dict[schema]['children'].items():
            #to store schema details in a vertex
            if(flg==0):
                schema_vertex=[]
                schema_vertex_id = schema_dict[schema]['id']
                schema_vertex.append(schema_vertex_id)
                #schema_vertex_table = 'has_child'
                schema_vertex_schema = schema
                schema_vertex.append(schema_vertex_schema)
                vertex_list.append(schema_vertex)
                flg=1
            vertex=[]
            #print(table,table_id)
            vertex_id = table_id
            vertex.append(vertex_id)
            vertex_table = table
            vertex_schema = schema
            temp_list = []
            temp_list.append(vertex_table)
            temp_list.append(vertex_schema)
            vertex.append(temp_list)
            vertex_list.append(vertex)                
            table_dict[schema+'.'+table]=table_id
print(vertex_list)


# In[39]:


#creating edge list from schema_dict
edge_list=[]

#to create schema-table relationship
for schema,table in schema_dict.items():
    if(schema_dict[schema]['children'] == {}):
        continue
    else:
        for table,table_id in schema_dict[schema]['children'].items():
            edge=[]
            srcid = schema_dict[schema]['id']
            destid = table_id
     #      edgename = schema+' > '+table
            edgename = 'schema-table relation'
            edge.append(srcid)
            edge.append(destid)
            edge.append(edgename)
            edge_list.append(edge)

print(edge_list)
#to create edges for connected tables
with open('./schema_info/child_parent_info.txt','r') as file3:
    child_parent_list = [obj.split('\t') for obj in file3.readlines()]
    #rint(child_parent_list)
    for item in child_parent_list:
        edge=[]
        child_table = item[0]+'.'+item[1]
        child_id = table_dict[child_table] if table_dict[child_table] is not None else 0
        parent_table = item[3]+'.'+item[4]
        parent_id = table_dict[parent_table] if table_dict[parent_table] is not None else 0
        edge.append(child_id)
        edge.append(parent_id)
    #   edge.append(child_table+' > '+ parent_table)
        edge.append('child-parent relation')
        edge_list.append(edge)
print(edge_list)


# In[41]:


import csv
with open('vertex_list.csv','w') as file:
    wr = csv.writer(file)
    wr.writerows(vertex_list)
with open('edge_list.csv','w') as file2:
    wr = csv.writer(file2)
    wr.writerows(edge_list)


# In[ ]:





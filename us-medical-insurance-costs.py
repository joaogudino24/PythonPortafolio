#!/usr/bin/env python
# coding: utf-8

# # U.S. Medical Insurance Costs

# ### Project Goals
# 
# 1. Find out the average age of the patients in the dataset.
# 
# 2. Analyze where a majority of the individuals are from.
# 
# 3. Look at the different costs between smokers vs. non-smokers.
# 
# 4. Figure out what the average age is for someone who has at least one child in this dataset.
# 

# ### Import Data

# In[46]:


#importing our data from insurance.csv and storing it in a list

import csv

with open("insurance.csv", newline= "") as insurance_data:
    insurance_reader = csv.DictReader(insurance_data, delimiter= ",")
    insurance_list = []
    for row in insurance_reader:
        insurance_list.append(row)

#creating lists for our columns and storing the information in those lists

age_list = []
sex_list = []
bmi_list = []
children_list = []
smoker_list = []
region_list = []
charges_list = []

for person in insurance_list:
    age_list.append(int(person["age"]))
    sex_list.append(person["sex"])
    bmi_list.append(person["bmi"])
    children_list.append(int(person["children"]))
    smoker_list.append(person["smoker"])
    region_list.append(person["region"])
    charges_list.append(float(person["charges"]))


# ### Analysis

# #### 1. Find out the average age of the patients in the dataset.

# In[29]:


#importing statistics library in order to calculate the average

from statistics import mean

age_average = round(mean(age_list),1)

# another way to calculate the average manually is shown below
#age_average_2 = round((sum(age_list)/len(age_list)),1)

print("The average age of the patients is this dataset is {} years old".format(age_average))


# #### 2. Analyze where a majority of the individuals are from.

# In[35]:


#using a loop we are going to count the number of times each region appears in each insurance data

#creating a list to store the region with more individuals. Creating it with sample data in order to start the for loop
most_common_region = [["Region Example", 0]]

for region in region_list:
    #as we loop into each region in our region list we will continue only if the region has not been already counted
    if region != most_common_region[0][0]:
        #creating a variable to store the number of times the region appears in the list
        region_count = region_list.count(region)
        
        #creating another loop to compare the region_count variable with the most_common_region count at the moment
        if region_count > most_common_region[0][1]:
            #since the region_count is greater than the most_common_region count we are going to update the data stored in most_common_region
            most_common_region.pop()
            most_common_region.append([region, region_count])
    else:
        pass

print(" The most common region is our insurance data is {} with {} records.".format(most_common_region[0][0],most_common_region[0][1]))


# In[83]:


#creating a fuction to categorize and count

def count_categories(list):
    #creating a dictionary to store the categories as keys and the count as values
    categories = {}
    
    # using a for loop to iterate through all elements in a specific list
    for category in list:
    #as we loop into each element we will continue only if the category has not been already counted
        if category not in categories:
            #creating a variable to store the number of times the category has been counted
            category_count = list.count(category)
            categories[category] = category_count
    
    return categories

print("Count of people by region: " + str(count_categories(region_list)))
print("\nCount of people by their smoking preference: " + str(count_categories(smoker_list)))
print("\nCount of people by their gender: " + str(count_categories(sex_list)))


# #### 3. Look at the different costs between smokers vs. non-smokers.

# In[67]:


#creating the variables that will keep a total cost and count of both non smokers and smokers
smoker_total_cost = 0
smoker_count = 0
nonsmoker_total_cost = 0
nonsmoker_count = 0

# using a for loop to iterate through all the indexes in both the smoker_list and charges_list
for i in range(len(smoker_list)-1):
    if smoker_list[i] == "yes":
        smoker_total_cost += charges_list[i]
        smoker_count += 1
    else:
        nonsmoker_total_cost += charges_list[i]
        nonsmoker_count += 1

# calculate the average cost for each category in smoker_list
smoker_average_cost = round((smoker_total_cost/smoker_count),1)
nonsmoker_average_cost = round((nonsmoker_total_cost/nonsmoker_count),1)


print("The average insurance cost of a smoker is {} dollars.\nThe average insurance cost of a non smoker is way less with {} dollars".format(smoker_average_cost, nonsmoker_average_cost))


# #### 4. Figure out what the average age is for someone who has at least one child in this dataset.

# In[73]:


#create a fuction to calculate the average age of someone depending on the least number of children they have
def calculate_average_age(num_child):
    #create a new list to store the ages of the people who have the same number of children or more
    age_list_for_num_child = []
    #using a for loop to iterate through all the indexes in both the age_list and children_list
    for i in range(len(age_list)-1):
        #iterating through the age list through control flow depending on the variable num_child being at least the same to the amount of children 
        if num_child >= children_list[i]:
            age_list_for_num_child.append(age_list[i])
    
    average_age = round(mean(age_list_for_num_child),1)
    
    return "The average age of someone with atleast {} children is {} years old".format(num_child, average_age)

#calling the fuction calculate_average_age(num_child) to store the value in a variable

at_least_one_child_average_age = calculate_average_age(1)
at_least_four_child_average_age = calculate_average_age(4)

print(at_least_one_child_average_age)
print(at_least_four_child_average_age)


# In[ ]:





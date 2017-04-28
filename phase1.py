'''Python program that reads an existing CSV file called input.csv. The csv
file contains columns of data with particular column name. For each column
(or attribute) in the CSV file, your program would detect the data type and do
 the following:
         1. For all columns, find out their mode(s).
         2. For numerical columns (float and integer types), provide
            five-number-summary,
         3. For string, provide unique values of the column values.
   Prodipta Guha, pguha@student.unimelb.edu.au, 27th March 2017.
   Student ID: 793023
'''

import csv
import collections
import math
from lxml import etree

# open the CSV file
csv_file = open("input.csv", "rb")
csv_reader = csv.reader(csv_file)
csv_data = list(csv_reader)
col_length = len(csv_data)

# creating the xml file
root = etree.Element('attributes')  # ROOT ELEMENT

# Attribute of the CSV file
att = csv_data[0]

        
''' ################---Helper functions---############### '''
def isstr(value):
    for i in value:
        try:
            float(i)
            continue
        except ValueError:
            return True
    return False

def isfloat(x):
    for i in x:
        a = float(i)
        b = int(a)
        if a != b:
            return True
        else:
            continue
    return False

def att_type(n1):
    if isstr(n1) is True:
        return 'string'
    elif isfloat(n1) is True:
        return 'float'
    else:
        return 'integer'

def mode(value3):
    value3_stripped = [val.strip() for val in value3]
    count = collections.Counter(value3_stripped)
    m_com = count.most_common(len(count))
    mode_list = [m_com[0][0]]
    z = 0
    while z < len(count):
        if z == (len(count) - 1) or m_com[z][1] != m_com[z+1][1]:
            break
        else:
            mode_list.append(m_com[z+1][0])
            z += 1
    return mode_list

def unique(value4):
    value4_stripped = [val.strip() for val in value4]
    count = collections.Counter(value4_stripped)
    m_com = count.most_common(len(count))
    m_com_reversed = m_com[::-1]
    max_count = len(count)
    uniq_list = [m_com[max_count-1][0]]
    z = 0
    while z < len(count):
        if (z == (len(count) - 1)) or (m_com_reversed[z][1] != m_com_reversed[z+1][1]):
            break
        else:
            uniq_list.append(m_com_reversed[z+1][0])
            z += 1
    return uniq_list


# FIVE NUMBER SUMMARY: MIN, Q1, MEDIAN, Q3, MAX
def min_v(value9):
    value9 = map(float, value9)
    min_val = min(value9)
    return min_val

def q1(value6):
    value6 = sorted(map(float, value6))
    if '.' in str(q1_rank):
        fl = int(math.floor(q1_rank)) - 1
        cl = int(math.ceil(q1_rank)) - 1
        q1_val = (value6[fl] + value6[cl])/2.0
        return q1_val
    else:
        q1_rank_int = int(q1_rank)
        q1_val = value6[q1_rank_int]
        return q1_val

def median(value5):
    value5 = sorted(map(float, value5))
    if '.' in str(med_rank):
        fl = int(math.floor(med_rank)) - 1
        cl = int(math.ceil(med_rank)) - 1
        med = (value5[fl] + value5[cl])/2.0
        return med
    else:
        medi_rank_int = int(med_rank)
        med = value5[medi_rank_int]
        return med

def q3(value7):
    value7 = sorted(map(float, value7), reverse=True)
    if '.' in str(q1_rank):
        fl = int(math.floor(q1_rank)) - 1
        cl = int(math.ceil(q1_rank)) - 1
        q3_val = (value7[fl] + value7[cl])/2.0
        return q3_val
    else:
        q1_rank_int = int(q1_rank)
        q3_val = value7[q1_rank_int]
        return q3_val
        
def max_v(value8):
    value8 = map(float, value8)
    max_val = max(value8)
    return max_val

# Number of rows and columns
n_row = col_length - 1

# RANKS
med_rank = (float(n_row) + 1.0) / 2.0
q1_rank = (math.floor(med_rank)+1)/2

if n_row is 0:
    print("No data available, not being able to process. Try with a different dataset.")
else:
    n_col = len(att)
    # iterate through every column
    columns = collections.defaultdict(list)
    with open('input.csv') as file:
        reader = csv.DictReader(file)
        for row in reader:
            for (k, v) in row.items():
                columns[k].append(v)

    f = 0
    while f < n_col:
        a = (columns[att[f]])  # iterating through each column

        att_name = att[f].strip(' ')
        attribute_type = att_type(a)

        # building the xml
        attribute = etree.SubElement(root, "attribute")
        root[f].attrib["type"] = attribute_type

        name = etree.Element("name")
        attribute.insert(0, name)
        attribute[0].text = att_name

        if attribute_type is 'string':

            # MODES
            modes__ = etree.Element("modes")
            attribute.insert(1, modes__)

            mod_list = mode(a)
            for i in mod_list:
                mode_____ = etree.Element("mode")
                modes__.insert(0, mode_____)
                modes__[0].text = i

            # UNIQUES0
            uniques__ = etree.Element("uniques")
            attribute.insert(2, uniques__)

            uni_list = unique(a)
            for j in uni_list:
                unique_____ = etree.Element("unique")
                uniques__.insert(0, unique_____)
                uniques__[0].text = j
        else:

            # PROPERTIES
            properties = etree.Element("properties")
            attribute.insert(1, properties)

            # MINIMUM VALUE
            property1 = etree.Element("property")
            properties.insert(2, property1)
            properties[0].attrib["name"] = "min"
            min_num = str(min_v(a))
            properties[0].text = min_num

            # FIRST QUARTILE VALUE
            property2 = etree.Element("property")
            properties.insert(3, property2)
            properties[1].attrib["name"] = "q1"
            q1_num = str(q1(a))
            properties[1].text = q1_num

            # MEDIAN VALUE
            property3 = etree.Element("property")
            properties.insert(4, property3)
            properties[2].attrib["name"] = "median"
            med_num = str(median(a))
            properties[2].text = med_num

            # THIRD QUARTILE VALUE
            property4 = etree.Element("property")
            properties.insert(5, property4)
            properties[3].attrib["name"] = "q3"
            q3_num = str(q3(a))
            properties[3].text = q3_num

            # MAXIMUM VALUE
            property5 = etree.Element("property")
            properties.insert(6, property5)
            properties[4].attrib["name"] = "max"
            max_num = str(max_v(a))
            properties[4].text = max_num

            # MODES
            modes__ = etree.Element("modes")
            attribute.insert(2, modes__)

            # MODE VALUES
            mod_list = mode(a)
            for i in mod_list:
                mode_____ = etree.Element("mode")
                modes__.insert(0, mode_____)
                modes__[0].text = i

        f += 1

    # writing the output.xml and returning summary.dtd
    output = etree.tostring(root, pretty_print=True, xml_declaration=True,
                            doctype='<!DOCTYPE attributes [<!ELEMENT attributes (attribute*)><!ELEMENT attribute (name, properties?, modes?, uniques?)><!ELEMENT name (#PCDATA)><!ELEMENT properties (property+)><!ELEMENT property (#PCDATA)><!ELEMENT modes (mode+)><!ELEMENT mode (#PCDATA)><!ELEMENT uniques (unique+)><!ELEMENT unique (#PCDATA)><!ATTLIST attribute type (integer|float|string) #REQUIRED><!ATTLIST property name (min|q1|median|q3|max) #REQUIRED>]>', encoding="UTF-8")
    open('output.xml', 'w').write(output)

    ''' 
=====================================================================
   Program written by Prodipta Guha, as Project of Phase 1.
   Foundation of Informatics.
   Semester 1 2017

NOTE: Assuming if the column contains any string (anything other than numerical values) will be considered as a string column.
================================================================== 
    '''

    # DONE! 9.5/10 -> xD

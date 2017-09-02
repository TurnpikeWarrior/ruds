
# Academy of Py


```python
#Dependencies
import pandas as pd
import numpy as np
```


```python
#CSV Files
schools_complete = "raw_data/schools_complete.csv"
students_complete = "raw_data/students_complete.csv"

schools_data = pd.read_csv(schools_complete, encoding='iso-8859-1')
students_data = pd.read_csv(students_complete, encoding='iso-8859-1')
```


```python
schools_data.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School ID</th>
      <th>school_name</th>
      <th>type</th>
      <th>size</th>
      <th>budget</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Huang High School</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Figueroa High School</td>
      <td>District</td>
      <td>2949</td>
      <td>1884411</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Shelton High School</td>
      <td>Charter</td>
      <td>1761</td>
      <td>1056600</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Hernandez High School</td>
      <td>District</td>
      <td>4635</td>
      <td>3022020</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Griffin High School</td>
      <td>Charter</td>
      <td>1468</td>
      <td>917500</td>
    </tr>
  </tbody>
</table>
</div>




```python
students_data.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Student ID</th>
      <th>student_name</th>
      <th>gender</th>
      <th>grade</th>
      <th>school_name</th>
      <th>reading_score</th>
      <th>math_score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Paul Bradley</td>
      <td>M</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>66</td>
      <td>79</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Victor Smith</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>94</td>
      <td>61</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Kevin Rodriguez</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>90</td>
      <td>60</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Dr. Richard Scott</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>67</td>
      <td>58</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Bonnie Ray</td>
      <td>F</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>97</td>
      <td>84</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Merging both CSV files
complete_data = pd.merge(students_data, schools_data, how="left", on=["school_name", "school_name"])
complete_data.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Student ID</th>
      <th>student_name</th>
      <th>gender</th>
      <th>grade</th>
      <th>school_name</th>
      <th>reading_score</th>
      <th>math_score</th>
      <th>School ID</th>
      <th>type</th>
      <th>size</th>
      <th>budget</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Paul Bradley</td>
      <td>M</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>66</td>
      <td>79</td>
      <td>0</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Victor Smith</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>94</td>
      <td>61</td>
      <td>0</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Kevin Rodriguez</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>90</td>
      <td>60</td>
      <td>0</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Dr. Richard Scott</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>67</td>
      <td>58</td>
      <td>0</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Bonnie Ray</td>
      <td>F</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>97</td>
      <td>84</td>
      <td>0</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
    </tr>
  </tbody>
</table>
</div>



## District Summary 


```python
# Total Schools
total_schools = schools_data["School ID"].count()
total_schools
```




    15




```python
# Total Students
total_students = complete_data["Student ID"].count()
total_students
```




    39170




```python
# Total Budget
total_budget = schools_data["budget"].sum()
total_budget
```




    24649428




```python
# Average Math Score
district_avg_math_score = students_data["math_score"].mean() 
district_avg_math_score
```




    78.98537145774827




```python
# Average Reading Score
district_avg_reading_score = students_data["reading_score"].mean() 
district_avg_reading_score
```




    81.87784018381414




```python
# % Passing Math
district_passing_math_count = (students_data.loc[students_data["math_score"]>70]).count()["student_name"]
district_passing_math_percentage = district_passing_math_count / total_students * 100
district_passing_math_percentage
```




    72.392136839417915




```python
# % Passing Reading
district_passing_reading_count = (students_data.loc[students_data["reading_score"]>70]).count()["student_name"]
district_passing_reading_percentage = district_passing_reading_count / total_students * 100
district_passing_reading_percentage
```




    82.971661986213945




```python
# Overall Passing Rate
district_overall_passing_rate = (district_passing_math_percentage + district_passing_reading_percentage) / 2
district_overall_passing_rate
```




    77.681899412815937



### District Summary Table


```python
district_summary = pd.DataFrame({"Total Schools": [total_schools],
                                 "Total Students": [total_students],
                                 "Total Budgets": [total_budget],
                                 "Average Math Score": [district_avg_math_score],
                                 "Average Reading Score": [district_avg_reading_score],
                                 "% Passing Math": [district_passing_math_percentage],
                                 "% Passing Reading": [district_passing_reading_percentage],
                                 "Overall Passing Rate": [district_overall_passing_rate]})

district_summary = district_summary[["Total Schools", 
                                     "Total Students", 
                                     "Total Budgets", 
                                     "Average Math Score", 
                                     "Average Reading Score",
                                     "% Passing Math",
                                     "% Passing Reading",
                                     "Overall Passing Rate"]]

district_summary
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Schools</th>
      <th>Total Students</th>
      <th>Total Budgets</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>15</td>
      <td>39170</td>
      <td>24649428</td>
      <td>78.985371</td>
      <td>81.87784</td>
      <td>72.392137</td>
      <td>82.971662</td>
      <td>77.681899</td>
    </tr>
  </tbody>
</table>
</div>



## School Summary


```python
# School Name
ss_school_type = schools_data.set_index(["school_name"])["type"]
ss_school_type
```




    school_name
    Huang High School        District
    Figueroa High School     District
    Shelton High School       Charter
    Hernandez High School    District
    Griffin High School       Charter
    Wilson High School        Charter
    Cabrera High School       Charter
    Bailey High School       District
    Holden High School        Charter
    Pena High School          Charter
    Wright High School        Charter
    Rodriguez High School    District
    Johnson High School      District
    Ford High School         District
    Thomas High School        Charter
    Name: type, dtype: object




```python
# Total Students per School
ss_total_students = complete_data["school_name"].value_counts()
ss_total_students
```




    Bailey High School       4976
    Johnson High School      4761
    Hernandez High School    4635
    Rodriguez High School    3999
    Figueroa High School     2949
    Huang High School        2917
    Ford High School         2739
    Wilson High School       2283
    Cabrera High School      1858
    Wright High School       1800
    Shelton High School      1761
    Thomas High School       1635
    Griffin High School      1468
    Pena High School          962
    Holden High School        427
    Name: school_name, dtype: int64




```python
# Total School Budget
ss_total_budget = schools_data["budget"].sum()
ss_total_budget
```




    24649428




```python
# Per School Budget
ss_total_school_budget = schools_data.groupby(["school_name"]).sum()["budget"]
ss_total_school_budget
```




    school_name
    Bailey High School       3124928
    Cabrera High School      1081356
    Figueroa High School     1884411
    Ford High School         1763916
    Griffin High School       917500
    Hernandez High School    3022020
    Holden High School        248087
    Huang High School        1910635
    Johnson High School      3094650
    Pena High School          585858
    Rodriguez High School    2547363
    Shelton High School      1056600
    Thomas High School       1043130
    Wilson High School       1319574
    Wright High School       1049400
    Name: budget, dtype: int64




```python
# Average Math Score per School
ss_avg_math_score = complete_data.groupby(["school_name"]).mean()["math_score"]
ss_avg_math_score
```




    school_name
    Bailey High School       77.048432
    Cabrera High School      83.061895
    Figueroa High School     76.711767
    Ford High School         77.102592
    Griffin High School      83.351499
    Hernandez High School    77.289752
    Holden High School       83.803279
    Huang High School        76.629414
    Johnson High School      77.072464
    Pena High School         83.839917
    Rodriguez High School    76.842711
    Shelton High School      83.359455
    Thomas High School       83.418349
    Wilson High School       83.274201
    Wright High School       83.682222
    Name: math_score, dtype: float64




```python
# Average Reading Score per School
ss_avg_reading_score = complete_data.groupby(["school_name"]).mean()["reading_score"]
ss_avg_reading_score
```




    school_name
    Bailey High School       81.033963
    Cabrera High School      83.975780
    Figueroa High School     81.158020
    Ford High School         80.746258
    Griffin High School      83.816757
    Hernandez High School    80.934412
    Holden High School       83.814988
    Huang High School        81.182722
    Johnson High School      80.966394
    Pena High School         84.044699
    Rodriguez High School    80.744686
    Shelton High School      83.725724
    Thomas High School       83.848930
    Wilson High School       83.989488
    Wright High School       83.955000
    Name: reading_score, dtype: float64




```python
# % Passing Math per School
ss_passing_math = complete_data[(complete_data["math_score"] > 70)]
ss_passing_math_list = ss_passing_math.groupby(["school_name"]).count()["student_name"] / ss_total_students * 100
ss_passing_math_list
```




    Bailey High School       64.630225
    Cabrera High School      89.558665
    Figueroa High School     63.750424
    Ford High School         65.753925
    Griffin High School      89.713896
    Hernandez High School    64.746494
    Holden High School       90.632319
    Huang High School        63.318478
    Johnson High School      63.852132
    Pena High School         91.683992
    Rodriguez High School    64.066017
    Shelton High School      89.892107
    Thomas High School       90.214067
    Wilson High School       90.932983
    Wright High School       90.277778
    dtype: float64




```python
# % Passing Reading per School
ss_passing_reading = complete_data[(complete_data["reading_score"] > 70)]
ss_passing_reading_list = ss_passing_reading.groupby(["school_name"]).count()["student_name"] / ss_total_students * 100
ss_passing_reading_list
```




    Bailey High School       79.300643
    Cabrera High School      93.864370
    Figueroa High School     78.433367
    Ford High School         77.510040
    Griffin High School      93.392371
    Hernandez High School    78.187702
    Holden High School       92.740047
    Huang High School        78.813850
    Johnson High School      78.281874
    Pena High School         92.203742
    Rodriguez High School    77.744436
    Shelton High School      92.617831
    Thomas High School       92.905199
    Wilson High School       93.254490
    Wright High School       93.444444
    dtype: float64




```python
# Overall Passing Rate per School
ss_overall_passing_rate = (ss_passing_math_list + ss_passing_reading_list) / 2
ss_overall_passing_rate
```




    Bailey High School       71.965434
    Cabrera High School      91.711518
    Figueroa High School     71.091896
    Ford High School         71.631982
    Griffin High School      91.553134
    Hernandez High School    71.467098
    Holden High School       91.686183
    Huang High School        71.066164
    Johnson High School      71.067003
    Pena High School         91.943867
    Rodriguez High School    70.905226
    Shelton High School      91.254969
    Thomas High School       91.559633
    Wilson High School       92.093736
    Wright High School       91.861111
    dtype: float64




```python
# Per Student Budget per School
spending_per_student = ss_total_school_budget / ss_total_students
spending_per_student
```




    Bailey High School       628.0
    Cabrera High School      582.0
    Figueroa High School     639.0
    Ford High School         644.0
    Griffin High School      625.0
    Hernandez High School    652.0
    Holden High School       581.0
    Huang High School        655.0
    Johnson High School      650.0
    Pena High School         609.0
    Rodriguez High School    637.0
    Shelton High School      600.0
    Thomas High School       638.0
    Wilson High School       578.0
    Wright High School       583.0
    dtype: float64



### School Summary Table


```python
school_summary = pd.DataFrame({"School Type": ss_school_type,
                                "Total Students": ss_total_students,
                                "Total School Budget": ss_total_school_budget,
                                "Per Student Budget": spending_per_student,
                                "Average Math Score": ss_avg_math_score,
                                "Average Reading Score": ss_avg_reading_score,
                                "% Passing Math": ss_passing_math_list,
                                "% Passing Reading": ss_passing_reading_list,
                                "Overall Passing Rate": ss_overall_passing_rate})

school_summary = school_summary[["School Type", 
                                 "Total Students", 
                                 "Total School Budget", 
                                 "Per Student Budget",
                                 "Average Math Score",
                                 "Average Reading Score", 
                                 "% Passing Math", 
                                 "% Passing Reading", 
                                 "Overall Passing Rate"]]

school_summary
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>Overall Passing Rate</th>
      <th>Per Student Budget</th>
      <th>School Type</th>
      <th>Total School Budget</th>
      <th>Total Students</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Bailey High School</th>
      <td>64.630225</td>
      <td>79.300643</td>
      <td>77.048432</td>
      <td>81.033963</td>
      <td>71.965434</td>
      <td>628.0</td>
      <td>District</td>
      <td>3124928</td>
      <td>4976</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>89.558665</td>
      <td>93.864370</td>
      <td>83.061895</td>
      <td>83.975780</td>
      <td>91.711518</td>
      <td>582.0</td>
      <td>Charter</td>
      <td>1081356</td>
      <td>1858</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>63.750424</td>
      <td>78.433367</td>
      <td>76.711767</td>
      <td>81.158020</td>
      <td>71.091896</td>
      <td>639.0</td>
      <td>District</td>
      <td>1884411</td>
      <td>2949</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>65.753925</td>
      <td>77.510040</td>
      <td>77.102592</td>
      <td>80.746258</td>
      <td>71.631982</td>
      <td>644.0</td>
      <td>District</td>
      <td>1763916</td>
      <td>2739</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>89.713896</td>
      <td>93.392371</td>
      <td>83.351499</td>
      <td>83.816757</td>
      <td>91.553134</td>
      <td>625.0</td>
      <td>Charter</td>
      <td>917500</td>
      <td>1468</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>64.746494</td>
      <td>78.187702</td>
      <td>77.289752</td>
      <td>80.934412</td>
      <td>71.467098</td>
      <td>652.0</td>
      <td>District</td>
      <td>3022020</td>
      <td>4635</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>90.632319</td>
      <td>92.740047</td>
      <td>83.803279</td>
      <td>83.814988</td>
      <td>91.686183</td>
      <td>581.0</td>
      <td>Charter</td>
      <td>248087</td>
      <td>427</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>63.318478</td>
      <td>78.813850</td>
      <td>76.629414</td>
      <td>81.182722</td>
      <td>71.066164</td>
      <td>655.0</td>
      <td>District</td>
      <td>1910635</td>
      <td>2917</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>63.852132</td>
      <td>78.281874</td>
      <td>77.072464</td>
      <td>80.966394</td>
      <td>71.067003</td>
      <td>650.0</td>
      <td>District</td>
      <td>3094650</td>
      <td>4761</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>91.683992</td>
      <td>92.203742</td>
      <td>83.839917</td>
      <td>84.044699</td>
      <td>91.943867</td>
      <td>609.0</td>
      <td>Charter</td>
      <td>585858</td>
      <td>962</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>64.066017</td>
      <td>77.744436</td>
      <td>76.842711</td>
      <td>80.744686</td>
      <td>70.905226</td>
      <td>637.0</td>
      <td>District</td>
      <td>2547363</td>
      <td>3999</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>89.892107</td>
      <td>92.617831</td>
      <td>83.359455</td>
      <td>83.725724</td>
      <td>91.254969</td>
      <td>600.0</td>
      <td>Charter</td>
      <td>1056600</td>
      <td>1761</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>90.214067</td>
      <td>92.905199</td>
      <td>83.418349</td>
      <td>83.848930</td>
      <td>91.559633</td>
      <td>638.0</td>
      <td>Charter</td>
      <td>1043130</td>
      <td>1635</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>90.932983</td>
      <td>93.254490</td>
      <td>83.274201</td>
      <td>83.989488</td>
      <td>92.093736</td>
      <td>578.0</td>
      <td>Charter</td>
      <td>1319574</td>
      <td>2283</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>90.277778</td>
      <td>93.444444</td>
      <td>83.682222</td>
      <td>83.955000</td>
      <td>91.861111</td>
      <td>583.0</td>
      <td>Charter</td>
      <td>1049400</td>
      <td>1800</td>
    </tr>
  </tbody>
</table>
</div>



### Top 5 Performing Schools (By Passing Rate)


```python
top_performing_schools = school_summary.sort_values(["Overall Passing Rate"], ascending=False)
top_performing_schools.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>Overall Passing Rate</th>
      <th>Per Student Budget</th>
      <th>School Type</th>
      <th>Total School Budget</th>
      <th>Total Students</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Wilson High School</th>
      <td>90.932983</td>
      <td>93.254490</td>
      <td>83.274201</td>
      <td>83.989488</td>
      <td>92.093736</td>
      <td>578.0</td>
      <td>Charter</td>
      <td>1319574</td>
      <td>2283</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>91.683992</td>
      <td>92.203742</td>
      <td>83.839917</td>
      <td>84.044699</td>
      <td>91.943867</td>
      <td>609.0</td>
      <td>Charter</td>
      <td>585858</td>
      <td>962</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>90.277778</td>
      <td>93.444444</td>
      <td>83.682222</td>
      <td>83.955000</td>
      <td>91.861111</td>
      <td>583.0</td>
      <td>Charter</td>
      <td>1049400</td>
      <td>1800</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>89.558665</td>
      <td>93.864370</td>
      <td>83.061895</td>
      <td>83.975780</td>
      <td>91.711518</td>
      <td>582.0</td>
      <td>Charter</td>
      <td>1081356</td>
      <td>1858</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>90.632319</td>
      <td>92.740047</td>
      <td>83.803279</td>
      <td>83.814988</td>
      <td>91.686183</td>
      <td>581.0</td>
      <td>Charter</td>
      <td>248087</td>
      <td>427</td>
    </tr>
  </tbody>
</table>
</div>



### Bottom 5 Performing Schools (By Passing Rate)


```python
bottom_performing_schools = school_summary.sort_values(["Overall Passing Rate"], ascending=True)
bottom_performing_schools.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>Overall Passing Rate</th>
      <th>Per Student Budget</th>
      <th>School Type</th>
      <th>Total School Budget</th>
      <th>Total Students</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Rodriguez High School</th>
      <td>64.066017</td>
      <td>77.744436</td>
      <td>76.842711</td>
      <td>80.744686</td>
      <td>70.905226</td>
      <td>637.0</td>
      <td>District</td>
      <td>2547363</td>
      <td>3999</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>63.318478</td>
      <td>78.813850</td>
      <td>76.629414</td>
      <td>81.182722</td>
      <td>71.066164</td>
      <td>655.0</td>
      <td>District</td>
      <td>1910635</td>
      <td>2917</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>63.852132</td>
      <td>78.281874</td>
      <td>77.072464</td>
      <td>80.966394</td>
      <td>71.067003</td>
      <td>650.0</td>
      <td>District</td>
      <td>3094650</td>
      <td>4761</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>63.750424</td>
      <td>78.433367</td>
      <td>76.711767</td>
      <td>81.158020</td>
      <td>71.091896</td>
      <td>639.0</td>
      <td>District</td>
      <td>1884411</td>
      <td>2949</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>64.746494</td>
      <td>78.187702</td>
      <td>77.289752</td>
      <td>80.934412</td>
      <td>71.467098</td>
      <td>652.0</td>
      <td>District</td>
      <td>3022020</td>
      <td>4635</td>
    </tr>
  </tbody>
</table>
</div>



### Math Scores by Grade


```python
nineth_grade = complete_data[(complete_data["grade"] == "9th")]
tenth_grade = complete_data[(complete_data["grade"] == "10th")]
eleventh_grade = complete_data[(complete_data["grade"] == "11th")]
twelfth_grade = complete_data[(complete_data["grade"] == "12th")]

nineth_math = nineth_grade.groupby(["school_name"]).mean()["math_score"]
tenth_math = tenth_grade.groupby(["school_name"]).mean()["math_score"]
eleventh_math = eleventh_grade.groupby(["school_name"]).mean()["math_score"]
twelfth_math = twelfth_grade.groupby(["school_name"]).mean()["math_score"]

math_scores_by_grade = pd.DataFrame({"9th Grade": nineth_math, 
                                     "10th Grade": tenth_math,
                                     "11th Grade": eleventh_math,
                                     "12th Grade": twelfth_math})

math_scores_by_grade = math_scores_by_grade[["9th Grade", "10th Grade", "11th Grade", "12th Grade"]]

math_scores_by_grade
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>9th Grade</th>
      <th>10th Grade</th>
      <th>11th Grade</th>
      <th>12th Grade</th>
    </tr>
    <tr>
      <th>school_name</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Bailey High School</th>
      <td>77.083676</td>
      <td>76.996772</td>
      <td>77.515588</td>
      <td>76.492218</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>83.094697</td>
      <td>83.154506</td>
      <td>82.765560</td>
      <td>83.277487</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>76.403037</td>
      <td>76.539974</td>
      <td>76.884344</td>
      <td>77.151369</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>77.361345</td>
      <td>77.672316</td>
      <td>76.918058</td>
      <td>76.179963</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>82.044010</td>
      <td>84.229064</td>
      <td>83.842105</td>
      <td>83.356164</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>77.438495</td>
      <td>77.337408</td>
      <td>77.136029</td>
      <td>77.186567</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>83.787402</td>
      <td>83.429825</td>
      <td>85.000000</td>
      <td>82.855422</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>77.027251</td>
      <td>75.908735</td>
      <td>76.446602</td>
      <td>77.225641</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>77.187857</td>
      <td>76.691117</td>
      <td>77.491653</td>
      <td>76.863248</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>83.625455</td>
      <td>83.372000</td>
      <td>84.328125</td>
      <td>84.121547</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>76.859966</td>
      <td>76.612500</td>
      <td>76.395626</td>
      <td>77.690748</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>83.420755</td>
      <td>82.917411</td>
      <td>83.383495</td>
      <td>83.778976</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>83.590022</td>
      <td>83.087886</td>
      <td>83.498795</td>
      <td>83.497041</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>83.085578</td>
      <td>83.724422</td>
      <td>83.195326</td>
      <td>83.035794</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>83.264706</td>
      <td>84.010288</td>
      <td>83.836782</td>
      <td>83.644986</td>
    </tr>
  </tbody>
</table>
</div>



### Reading Scores by Grade


```python
nineth_grade = complete_data[(complete_data["grade"] == "9th")]
tenth_grade = complete_data[(complete_data["grade"] == "10th")]
eleventh_grade = complete_data[(complete_data["grade"] == "11th")]
twelfth_grade = complete_data[(complete_data["grade"] == "12th")]

nineth_math = nineth_grade.groupby(["school_name"]).mean()["reading_score"]
tenth_math = tenth_grade.groupby(["school_name"]).mean()["reading_score"]
eleventh_math = eleventh_grade.groupby(["school_name"]).mean()["reading_score"]
twelfth_math = twelfth_grade.groupby(["school_name"]).mean()["reading_score"]

reading_scores_by_grade = pd.DataFrame({"9th Grade": nineth_math, 
                                        "10th Grade": tenth_math,
                                        "11th Grade": eleventh_math,
                                        "12th Grade": twelfth_math})

reading_scores_by_grade = reading_scores_by_grade[["9th Grade", "10th Grade", "11th Grade", "12th Grade"]]

reading_scores_by_grade
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>9th Grade</th>
      <th>10th Grade</th>
      <th>11th Grade</th>
      <th>12th Grade</th>
    </tr>
    <tr>
      <th>school_name</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Bailey High School</th>
      <td>81.303155</td>
      <td>80.907183</td>
      <td>80.945643</td>
      <td>80.912451</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>83.676136</td>
      <td>84.253219</td>
      <td>83.788382</td>
      <td>84.287958</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>81.198598</td>
      <td>81.408912</td>
      <td>80.640339</td>
      <td>81.384863</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>80.632653</td>
      <td>81.262712</td>
      <td>80.403642</td>
      <td>80.662338</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>83.369193</td>
      <td>83.706897</td>
      <td>84.288089</td>
      <td>84.013699</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>80.866860</td>
      <td>80.660147</td>
      <td>81.396140</td>
      <td>80.857143</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>83.677165</td>
      <td>83.324561</td>
      <td>83.815534</td>
      <td>84.698795</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>81.290284</td>
      <td>81.512386</td>
      <td>81.417476</td>
      <td>80.305983</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>81.260714</td>
      <td>80.773431</td>
      <td>80.616027</td>
      <td>81.227564</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>83.807273</td>
      <td>83.612000</td>
      <td>84.335938</td>
      <td>84.591160</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>80.993127</td>
      <td>80.629808</td>
      <td>80.864811</td>
      <td>80.376426</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>84.122642</td>
      <td>83.441964</td>
      <td>84.373786</td>
      <td>82.781671</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>83.728850</td>
      <td>84.254157</td>
      <td>83.585542</td>
      <td>83.831361</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>83.939778</td>
      <td>84.021452</td>
      <td>83.764608</td>
      <td>84.317673</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>83.833333</td>
      <td>83.812757</td>
      <td>84.156322</td>
      <td>84.073171</td>
    </tr>
  </tbody>
</table>
</div>



### Scores by School Spending


```python
school_spending_bins = [0, 500, 600, 700]
school_spending = ["< $500", "$500 - 600", "$600 - 700"]

school_summary["Per Student Budget"] = pd.cut(spending_per_student, school_spending_bins, labels=school_spending)

scores_spending_math = school_summary.groupby(["Per Student Budget"]).mean()["Average Math Score"]
scores_spending_reading = school_summary.groupby(["Per Student Budget"]).mean()["Average Reading Score"]
scores_spending_passing_math = school_summary.groupby(["Per Student Budget"]).mean()["% Passing Math"]
scores_spending_passing_reading = school_summary.groupby(["Per Student Budget"]).mean()["% Passing Reading"]
scores_spending_overall_passing_rate = (scores_spending_passing_math / scores_spending_passing_reading) / 2

scores_by_school_spending_summary = pd.DataFrame({"Average Math Score": scores_spending_math,
                                                  "Average Reading Score": scores_spending_reading,
                                                  "% Passing Math": scores_spending_passing_math,
                                                  "% Passing Reading": scores_spending_passing_reading, 
                                                  "Overall Passing Rate": scores_spending_overall_passing_rate})

scores_by_school_spending_summary = scores_by_school_spending_summary[["Average Math Score",
                                                                       "Average Reading Score", 
                                                                       "% Passing Math", 
                                                                       "% Passing Reading", 
                                                                       "Overall Passing Rate"]]

scores_by_school_spending_summary.fillna(0)
scores_by_school_spending_summary
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Passing Rate</th>
    </tr>
    <tr>
      <th>Per Student Budget</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt; $500</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>$500 - 600</th>
      <td>83.43621</td>
      <td>83.892196</td>
      <td>90.258770</td>
      <td>93.184236</td>
      <td>0.484303</td>
    </tr>
    <tr>
      <th>$600 - 700</th>
      <td>78.93069</td>
      <td>81.847684</td>
      <td>72.172965</td>
      <td>82.677322</td>
      <td>0.436474</td>
    </tr>
  </tbody>
</table>
</div>



### Scores by School Size


```python
school_size_bin = [0, 1000, 2000, 5000]
school_size = ["< 1000", "1000 - 2000", "2000 - 5000"]

school_summary["School Size"] = pd.cut(school_summary["Total Students"], school_size_bin, labels=school_size)

scores_size_math = school_summary.groupby(["School Size"]).mean()["Average Math Score"]
scores_size_reading = school_summary.groupby(["School Size"]).mean()["Average Reading Score"]
scores_size_passing_math = school_summary.groupby(["School Size"]).mean()["% Passing Math"]
scores_size_passing_reading = school_summary.groupby(["School Size"]).mean()["% Passing Reading"]
scores_size_overall_passing_rate = (scores_size_passing_math + scores_size_passing_reading) / 2

scores_by_school_size_summary = pd.DataFrame({"Average Math Score": scores_size_math,
                                              "Average Reading Score": scores_size_reading,
                                              "% Passing Math": scores_size_passing_math,
                                              "% Passing Reading": scores_size_passing_reading,
                                              "Overall Passing Rate": scores_size_overall_passing_rate})

scores_by_school_size_summary = scores_by_school_size_summary[["Average Math Score",
                                                               "Average Reading Score", 
                                                               "% Passing Math", 
                                                               "% Passing Reading", 
                                                               "Overall Passing Rate"]]

scores_by_school_size_summary
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Passing Rate</th>
    </tr>
    <tr>
      <th>School Size</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt; 1000</th>
      <td>83.821598</td>
      <td>83.929843</td>
      <td>91.158155</td>
      <td>92.471895</td>
      <td>91.815025</td>
    </tr>
    <tr>
      <th>1000 - 2000</th>
      <td>83.374684</td>
      <td>83.864438</td>
      <td>89.931303</td>
      <td>93.244843</td>
      <td>91.588073</td>
    </tr>
    <tr>
      <th>2000 - 5000</th>
      <td>77.746417</td>
      <td>81.344493</td>
      <td>67.631335</td>
      <td>80.190800</td>
      <td>73.911067</td>
    </tr>
  </tbody>
</table>
</div>



### Scores by School Type


```python
scores_type_avg_math = school_summary.groupby(["School Type"]).mean()["Average Math Score"]
scores_type_avg_reading = school_summary.groupby(["School Type"]).mean()["Average Reading Score"]
scores_type_passing_math = school_summary.groupby(["School Type"]).mean()["% Passing Math"]
scores_type_passing_reading = school_summary.groupby(["School Type"]).mean()["% Passing Reading"]
scores_overall_passing_rate = (scores_type_passing_math + scores_type_passing_reading) / 2 

scores_by_school_type_summary = pd.DataFrame({"Average Math Score": scores_type_avg_math, 
                                              "Average Reading Score": scores_type_avg_reading,
                                              "% Passing Math": scores_type_passing_math, 
                                              "% Passing Reading": scores_type_passing_reading,
                                              "Overall Passing Rate": scores_overall_passing_rate})

scores_by_school_type_summary = scores_by_school_type_summary[["Average Math Score", 
                                                               "Average Reading Score", 
                                                               "% Passing Math", 
                                                               "% Passing Reading", 
                                                               "Overall Passing Rate"]]

scores_by_school_type_summary
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Passing Rate</th>
    </tr>
    <tr>
      <th>School Type</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Charter</th>
      <td>83.473852</td>
      <td>83.896421</td>
      <td>90.363226</td>
      <td>93.052812</td>
      <td>91.708019</td>
    </tr>
    <tr>
      <th>District</th>
      <td>76.956733</td>
      <td>80.966636</td>
      <td>64.302528</td>
      <td>78.324559</td>
      <td>71.313543</td>
    </tr>
  </tbody>
</table>
</div>



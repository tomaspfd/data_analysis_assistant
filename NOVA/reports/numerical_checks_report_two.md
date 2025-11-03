# Numeric Data Quality Analysis Report

This report details the comprehensive analysis of numeric and quantitative columns in the dataset, focusing on outliers, invalid values, and distributional issues.

A full issue summary table is saved to reports/numerical_checks_table_two.csv.

## 1. Numeric Column Analysis

### Column: `cargo_volume_l`

- **Original Data Type**: `object`

- **Issue**: Contains non-numeric strings that prevent direct conversion to numeric.

  - **Examples**: Examples: ["10 Banana Boxes", "31 Banana Boxes", "13 Banana Boxes"]

  - **Recommendation**: Convert to numeric by extracting digits. Handle non-numeric strings like '10 Banana Boxes' by mapping or setting to NaN. Then impute missing values.


### Column: `top_speed_kmh`

- **Data Type**: `int64`

- **Missing Values**: 0 (0.00%)

- **Summary Statistics**:

  - Count: 478.00

  - Mean: 185.49

  - Std: 34.25

  - Min: 125.00

  - 25%: 160.00

  - 50%: 180.00

  - 75%: 201.00

  - Max: 325.00

  - **Skewness**: 0.65

- **Invalid Values**: No obvious invalid values (e.g., non-positive where not allowed) detected.

- **Outliers (IQR Method)**: Detected 6 outliers.

  - **Bounds**: [98.50, 262.50]

  - **Examples**: [270, 290, 325]

  - **Recommendation**: Investigate values outside [98.50, 262.50]. Consider capping, transformation, or removal based on domain knowledge.

- **Outliers (Z-score Method)**: Detected 4 outliers.

  - **Examples**: [290, 325, 305]

  - **Recommendation**: Investigate values with Z-score > 3 or < -3. Consider capping, transformation, or removal based on domain knowledge.


### Column: `battery_capacity_kWh`

- **Data Type**: `float64`

- **Missing Values**: 0 (0.00%)

- **Summary Statistics**:

  - Count: 478.00

  - Mean: 74.04

  - Std: 20.33

  - Min: 21.30

  - 25%: 60.00

  - 50%: 76.15

  - 75%: 90.60

  - Max: 118.00

  - **Skewness**: -0.11

- **Invalid Values**: No obvious invalid values (e.g., non-positive where not allowed) detected.

- **Outliers (IQR Method)**: No significant outliers detected.

- **Outliers (Z-score Method)**: No significant outliers detected.


### Column: `number_of_cells`

- **Data Type**: `float64`

- **Missing Values**: 202 (42.26%)

- **Summary Statistics**:

  - Count: 276.00

  - Mean: 485.29

  - Std: 1210.82

  - Min: 72.00

  - 25%: 150.00

  - 50%: 216.00

  - 75%: 324.00

  - Max: 7920.00

  - **Skewness**: 4.97

- **Invalid Values**: No obvious invalid values (e.g., non-positive where not allowed) detected.

- **Outliers (IQR Method)**: Detected 12 outliers.

  - **Bounds**: [-111.00, 585.00]

  - **Examples**: [6600.0, 5400.0, 4416.0]

  - **Recommendation**: Investigate values outside [-111.00, 585.00]. Consider capping, transformation, or removal based on domain knowledge.

- **Outliers (Z-score Method)**: Detected 12 outliers.

  - **Examples**: [6600.0, 5400.0, 4416.0]

  - **Recommendation**: Investigate values with Z-score > 3 or < -3. Consider capping, transformation, or removal based on domain knowledge.


### Column: `torque_nm`

- **Data Type**: `float64`

- **Missing Values**: 7 (1.46%)

- **Summary Statistics**:

  - Count: 471.00

  - Mean: 498.01

  - Std: 241.46

  - Min: 113.00

  - 25%: 305.00

  - 50%: 430.00

  - 75%: 679.00

  - Max: 1350.00

  - **Skewness**: 0.83

- **Invalid Values**: No obvious invalid values (e.g., non-positive where not allowed) detected.

- **Outliers (IQR Method)**: Detected 4 outliers.

  - **Bounds**: [-256.00, 1240.00]

  - **Examples**: [1350.0, 1340.0]

  - **Recommendation**: Investigate values outside [-256.00, 1240.00]. Consider capping, transformation, or removal based on domain knowledge.

- **Outliers (Z-score Method)**: Detected 4 outliers.

  - **Examples**: [1350.0, 1340.0]

  - **Recommendation**: Investigate values with Z-score > 3 or < -3. Consider capping, transformation, or removal based on domain knowledge.


### Column: `efficiency_wh_per_km`

- **Data Type**: `int64`

- **Missing Values**: 0 (0.00%)

- **Summary Statistics**:

  - Count: 478.00

  - Mean: 162.90

  - Std: 34.32

  - Min: 109.00

  - 25%: 143.00

  - 50%: 155.00

  - 75%: 177.75

  - Max: 370.00

  - **Skewness**: 2.41

- **Invalid Values**: No obvious invalid values (e.g., non-positive where not allowed) detected.

- **Outliers (IQR Method)**: Detected 14 outliers.

  - **Bounds**: [90.88, 229.88]

  - **Examples**: [370, 266, 242]

  - **Recommendation**: Investigate values outside [90.88, 229.88]. Consider capping, transformation, or removal based on domain knowledge.

- **Outliers (Z-score Method)**: Detected 9 outliers.

  - **Examples**: [370, 266, 282]

  - **Recommendation**: Investigate values with Z-score > 3 or < -3. Consider capping, transformation, or removal based on domain knowledge.


### Column: `range_km`

- **Data Type**: `int64`

- **Missing Values**: 0 (0.00%)

- **Summary Statistics**:

  - Count: 478.00

  - Mean: 393.18

  - Std: 103.29

  - Min: 135.00

  - 25%: 320.00

  - 50%: 397.50

  - 75%: 470.00

  - Max: 685.00

  - **Skewness**: -0.16

- **Invalid Values**: No obvious invalid values (e.g., non-positive where not allowed) detected.

- **Outliers (IQR Method)**: No significant outliers detected.

- **Outliers (Z-score Method)**: No significant outliers detected.


### Column: `acceleration_0_100_s`

- **Data Type**: `float64`

- **Missing Values**: 0 (0.00%)

- **Summary Statistics**:

  - Count: 478.00

  - Mean: 6.88

  - Std: 2.73

  - Min: 2.20

  - 25%: 4.80

  - 50%: 6.60

  - 75%: 8.20

  - Max: 19.10

  - **Skewness**: 0.88

- **Invalid Values**: No obvious invalid values (e.g., non-positive where not allowed) detected.

- **Outliers (IQR Method)**: Detected 19 outliers.

  - **Bounds**: [-0.30, 13.30]

  - **Examples**: [13.3, 14.2, 19.1]

  - **Recommendation**: Investigate values outside [-0.30, 13.30]. Consider capping, transformation, or removal based on domain knowledge.

- **Outliers (Z-score Method)**: Detected 1 outliers.

  - **Examples**: [19.1]

  - **Recommendation**: Investigate values with Z-score > 3 or < -3. Consider capping, transformation, or removal based on domain knowledge.


### Column: `fast_charging_power_kw_dc`

- **Data Type**: `float64`

- **Missing Values**: 1 (0.21%)

- **Summary Statistics**:

  - Count: 477.00

  - Mean: 125.01

  - Std: 58.21

  - Min: 29.00

  - 25%: 80.00

  - 50%: 113.00

  - 75%: 150.00

  - Max: 281.00

  - **Skewness**: 1.04

- **Invalid Values**: No obvious invalid values (e.g., non-positive where not allowed) detected.

- **Outliers (IQR Method)**: Detected 26 outliers.

  - **Bounds**: [-25.00, 255.00]

  - **Examples**: [281.0, 259.0, 260.0]

  - **Recommendation**: Investigate values outside [-25.00, 255.00]. Consider capping, transformation, or removal based on domain knowledge.

- **Outliers (Z-score Method)**: No significant outliers detected.


### Column: `towing_capacity_kg`

- **Data Type**: `float64`

- **Missing Values**: 26 (5.44%)

- **Summary Statistics**:

  - Count: 452.00

  - Mean: 1052.26

  - Std: 737.85

  - Min: 0.00

  - 25%: 500.00

  - 50%: 1000.00

  - 75%: 1600.00

  - Max: 2500.00

  - **Skewness**: -0.10

- **Invalid Values**: No obvious invalid values (e.g., non-positive where not allowed) detected.

- **Outliers (IQR Method)**: No significant outliers detected.

- **Outliers (Z-score Method)**: No significant outliers detected.


### Column: `seats`

- **Data Type**: `int64`

- **Missing Values**: 0 (0.00%)

- **Summary Statistics**:

  - Count: 478.00

  - Mean: 5.26

  - Std: 1.00

  - Min: 2.00

  - 25%: 5.00

  - 50%: 5.00

  - 75%: 5.00

  - Max: 9.00

  - **Skewness**: 2.00

- **Invalid Values**: No obvious invalid values (e.g., non-positive where not allowed) detected.

- **Outliers (IQR Method)**: Detected 95 outliers.

  - **Bounds**: [5.00, 5.00]

  - **Examples**: [4, 7, 9]

  - **Recommendation**: Investigate values outside [5.00, 5.00]. Consider capping, transformation, or removal based on domain knowledge.

- **Outliers (Z-score Method)**: Detected 18 outliers.

  - **Examples**: [9, 2]

  - **Recommendation**: Investigate values with Z-score > 3 or < -3. Consider capping, transformation, or removal based on domain knowledge.


### Column: `length_mm`

- **Data Type**: `int64`

- **Missing Values**: 0 (0.00%)

- **Summary Statistics**:

  - Count: 478.00

  - Mean: 4678.51

  - Std: 369.21

  - Min: 3620.00

  - 25%: 4440.00

  - 50%: 4720.00

  - 75%: 4961.00

  - Max: 5908.00

  - **Skewness**: -0.48

- **Invalid Values**: No obvious invalid values (e.g., non-positive where not allowed) detected.

- **Outliers (IQR Method)**: Detected 9 outliers.

  - **Bounds**: [3658.50, 5742.50]

  - **Examples**: [3631, 5908, 3620]

  - **Recommendation**: Investigate values outside [3658.50, 5742.50]. Consider capping, transformation, or removal based on domain knowledge.

- **Outliers (Z-score Method)**: Detected 2 outliers.

  - **Examples**: [5908]

  - **Recommendation**: Investigate values with Z-score > 3 or < -3. Consider capping, transformation, or removal based on domain knowledge.


### Column: `width_mm`

- **Data Type**: `int64`

- **Missing Values**: 0 (0.00%)

- **Summary Statistics**:

  - Count: 478.00

  - Mean: 1887.36

  - Std: 73.66

  - Min: 1610.00

  - 25%: 1849.00

  - 50%: 1890.00

  - 75%: 1939.00

  - Max: 2080.00

  - **Skewness**: -0.75

- **Invalid Values**: No obvious invalid values (e.g., non-positive where not allowed) detected.

- **Outliers (IQR Method)**: Detected 14 outliers.

  - **Bounds**: [1714.00, 2074.00]

  - **Examples**: [1683, 1622, 1610]

  - **Recommendation**: Investigate values outside [1714.00, 2074.00]. Consider capping, transformation, or removal based on domain knowledge.

- **Outliers (Z-score Method)**: Detected 5 outliers.

  - **Examples**: [1622, 1610, 1652]

  - **Recommendation**: Investigate values with Z-score > 3 or < -3. Consider capping, transformation, or removal based on domain knowledge.


### Column: `height_mm`

- **Data Type**: `int64`

- **Missing Values**: 0 (0.00%)

- **Summary Statistics**:

  - Count: 478.00

  - Mean: 1601.13

  - Std: 130.75

  - Min: 1329.00

  - 25%: 1514.00

  - 50%: 1596.00

  - 75%: 1665.00

  - Max: 1986.00

  - **Skewness**: 0.64

- **Invalid Values**: No obvious invalid values (e.g., non-positive where not allowed) detected.

- **Outliers (IQR Method)**: Detected 14 outliers.

  - **Bounds**: [1287.50, 1891.50]

  - **Examples**: [1959, 1911, 1910]

  - **Recommendation**: Investigate values outside [1287.50, 1891.50]. Consider capping, transformation, or removal based on domain knowledge.

- **Outliers (Z-score Method)**: No significant outliers detected.


### Column: `cargo_volume_l_numeric`

- **Data Type**: `float64`

- **Missing Values**: 4 (0.84%)

- **Summary Statistics**:

  - Count: 474.00

  - Mean: 493.86

  - Std: 187.01

  - Min: 151.00

  - 25%: 385.00

  - 50%: 470.00

  - 75%: 544.50

  - Max: 1410.00

  - **Skewness**: 1.94

- **Invalid Values**: No obvious invalid values (e.g., non-positive where not allowed) detected.

- **Outliers (IQR Method)**: Detected 32 outliers.

  - **Bounds**: [145.75, 783.75]

  - **Examples**: [793.0, 1050.0, 989.0]

  - **Recommendation**: Investigate values outside [145.75, 783.75]. Consider capping, transformation, or removal based on domain knowledge.

- **Outliers (Z-score Method)**: Detected 8 outliers.

  - **Examples**: [1410.0, 1390.0, 1340.0]

  - **Recommendation**: Investigate values with Z-score > 3 or < -3. Consider capping, transformation, or removal based on domain knowledge.


## 2. Summary of Findings

A full issue summary table is saved to reports/numerical_checks_table_two.csv.

END OF REPORT
# Numeric Data Quality Analysis Report
This report details the findings from a comprehensive deep-dive analysis of all numeric and quantitative columns in the dataset. Issues related to data type inconsistencies, invalid values, unit mismatches, and potential outliers are documented.
## Column: `top_speed_kmh`
- **Original Data Type**: `int64`
- **Missing Values**: 0 (0.00%)
- **Summary Statistics**:
  - Count: 478.0
  - Mean: 185.49
  - Std: 34.25
  - Min: 125.0
  - 25%: 160.0
  - 50% (Median): 180.0
  - 75%: 201.0
  - Max: 325.0
- **Potential Outliers/Unusual Ranges**: No obvious outliers based on heuristic checks.

## Column: `battery_capacity_kWh`
- **Original Data Type**: `float64`
- **Missing Values**: 0 (0.00%)
- **Summary Statistics**:
  - Count: 478.0
  - Mean: 74.04
  - Std: 20.33
  - Min: 21.3
  - 25%: 60.0
  - 50% (Median): 76.15
  - 75%: 90.6
  - Max: 118.0
- **Potential Outliers/Unusual Ranges**: No obvious outliers based on heuristic checks.

## Column: `number_of_cells`
- **Original Data Type**: `float64`
- **Missing Values**: 202 (42.26%)
- **Summary Statistics**:
  - Count: 276.0
  - Mean: 485.29
  - Std: 1210.82
  - Min: 72.0
  - 25%: 150.0
  - 50% (Median): 216.0
  - 75%: 324.0
  - Max: 7920.0
- **Potential Outliers/Unusual Ranges**: No obvious outliers based on heuristic checks.

## Column: `torque_nm`
- **Original Data Type**: `float64`
- **Missing Values**: 7 (1.46%)
- **Summary Statistics**:
  - Count: 471.0
  - Mean: 498.01
  - Std: 241.46
  - Min: 113.0
  - 25%: 305.0
  - 50% (Median): 430.0
  - 75%: 679.0
  - Max: 1350.0
- **Potential Outliers/Unusual Ranges**: No obvious outliers based on heuristic checks.

## Column: `efficiency_wh_per_km`
- **Original Data Type**: `int64`
- **Missing Values**: 0 (0.00%)
- **Summary Statistics**:
  - Count: 478.0
  - Mean: 162.90
  - Std: 34.32
  - Min: 109.0
  - 25%: 143.0
  - 50% (Median): 155.0
  - 75%: 177.75
  - Max: 370.0
- **Potential Outliers/Unusual Ranges**: No obvious outliers based on heuristic checks.

## Column: `range_km`
- **Original Data Type**: `int64`
- **Missing Values**: 0 (0.00%)
- **Summary Statistics**:
  - Count: 478.0
  - Mean: 393.18
  - Std: 103.29
  - Min: 135.0
  - 25%: 320.0
  - 50% (Median): 397.5
  - 75%: 470.0
  - Max: 685.0
- **Potential Outliers/Unusual Ranges**: No obvious outliers based on heuristic checks.

## Column: `acceleration_0_100_s`
- **Original Data Type**: `float64`
- **Missing Values**: 0 (0.00%)
- **Summary Statistics**:
  - Count: 478.0
  - Mean: 6.88
  - Std: 2.73
  - Min: 2.2
  - 25%: 4.8
  - 50% (Median): 6.6
  - 75%: 8.2
  - Max: 19.1
- **Potential Outliers/Unusual Ranges**: No obvious outliers based on heuristic checks.

## Column: `fast_charging_power_kw_dc`
- **Original Data Type**: `float64`
- **Missing Values**: 1 (0.21%)
- **Summary Statistics**:
  - Count: 477.0
  - Mean: 125.01
  - Std: 58.21
  - Min: 29.0
  - 25%: 80.0
  - 50% (Median): 113.0
  - 75%: 150.0
  - Max: 281.0
- **Potential Outliers/Unusual Ranges**: No obvious outliers based on heuristic checks.

## Column: `towing_capacity_kg`
- **Original Data Type**: `float64`
- **Missing Values**: 26 (5.44%)
- **Summary Statistics**:
  - Count: 452.0
  - Mean: 1052.26
  - Std: 737.85
  - Min: 0.0
  - 25%: 500.0
  - 50% (Median): 1000.0
  - 75%: 1600.0
  - Max: 2500.0
- **Potential Outliers/Unusual Ranges**: No obvious outliers based on heuristic checks.

## Column: `cargo_volume_l`
- **Original Data Type**: `object`
- **Type Consistency Check**: This column is of `object` type. Attempting conversion to numeric.
  - **Issue**: Contains non-numeric string values.
  - **Examples of Problematic Values**: 10 Banana Boxes, 31 Banana Boxes, 13 Banana Boxes
- **Missing Values**: 4 (0.84%)
- **Summary Statistics**:
  - Count: 474.0
  - Mean: 493.86
  - Std: 187.01
  - Min: 151.0
  - 25%: 385.0
  - 50% (Median): 470.0
  - 75%: 544.5
  - Max: 1410.0
- **Potential Outliers/Unusual Ranges**: No obvious outliers based on heuristic checks.

## Column: `seats`
- **Original Data Type**: `int64`
- **Missing Values**: 0 (0.00%)
- **Summary Statistics**:
  - Count: 478.0
  - Mean: 5.26
  - Std: 1.00
  - Min: 2.0
  - 25%: 5.0
  - 50% (Median): 5.0
  - 75%: 5.0
  - Max: 9.0
- **Potential Outliers/Unusual Ranges**: No obvious outliers based on heuristic checks.

## Column: `length_mm`
- **Original Data Type**: `int64`
- **Missing Values**: 0 (0.00%)
- **Summary Statistics**:
  - Count: 478.0
  - Mean: 4678.51
  - Std: 369.21
  - Min: 3620.0
  - 25%: 4440.0
  - 50% (Median): 4720.0
  - 75%: 4961.0
  - Max: 5908.0
- **Potential Outliers/Unusual Ranges**: No obvious outliers based on heuristic checks.

## Column: `width_mm`
- **Original Data Type**: `int64`
- **Missing Values**: 0 (0.00%)
- **Summary Statistics**:
  - Count: 478.0
  - Mean: 1887.36
  - Std: 73.66
  - Min: 1610.0
  - 25%: 1849.0
  - 50% (Median): 1890.0
  - 75%: 1939.0
  - Max: 2080.0
- **Potential Outliers/Unusual Ranges**: No obvious outliers based on heuristic checks.

## Column: `height_mm`
- **Original Data Type**: `int64`
- **Missing Values**: 0 (0.00%)
- **Summary Statistics**:
  - Count: 478.0
  - Mean: 1601.13
  - Std: 130.75
  - Min: 1329.0
  - 25%: 1514.0
  - 50% (Median): 1596.0
  - 75%: 1665.0
  - Max: 1986.0
- **Potential Outliers/Unusual Ranges**: No obvious outliers based on heuristic checks.

A full issue summary table is saved to reports/numerical_checks_table.csv.
END OF REPORT
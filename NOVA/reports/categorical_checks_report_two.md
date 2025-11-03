# Categorical, Text, and Date Data Quality Analysis Report
This report details findings from a deep-dive analysis of categorical, text, and potential date columns in the dataset.
## Column: `brand`
- **Data Type**: `object` (Pandas inferred)
- **Unique Values (including NaN)**: 59 out of 478 (12.34%)

## Column: `model`
- **Data Type**: `object` (Pandas inferred)
- **Unique Values (including NaN)**: 478 out of 478 (100.00%)
  - **Flag**: High Cardinality
    - **Examples**: ['001 Long Range RWD', 'SQ6 e-tron Sportback', 'e-Tourneo Custom L2 160 kW']

## Column: `battery_type`
- **Data Type**: `object` (Pandas inferred)
- **Unique Values (including NaN)**: 1 out of 478 (0.21%)
  - **Flag**: Non-informative (Constant) Column
    - **Examples**: Lithium-ion

## Column: `fast_charge_port`
- **Data Type**: `object` (Pandas inferred)
- **Unique Values (including NaN)**: 3 out of 478 (0.63%)

## Column: `cargo_volume_l`
- **Data Type**: `object` (Pandas inferred)
- **Unique Values (including NaN)**: 141 out of 478 (29.50%)
  - **Flag**: Non-numeric Text Values
    - **Examples**: ['10 Banana Boxes', '31 Banana Boxes', '13 Banana Boxes']

## Column: `drivetrain`
- **Data Type**: `object` (Pandas inferred)
- **Unique Values (including NaN)**: 3 out of 478 (0.63%)

## Column: `segment`
- **Data Type**: `object` (Pandas inferred)
- **Unique Values (including NaN)**: 15 out of 478 (3.14%)

## Column: `car_body_type`
- **Data Type**: `object` (Pandas inferred)
- **Unique Values (including NaN)**: 8 out of 478 (1.67%)

## Column: `source_url`
- **Data Type**: `object` (Pandas inferred)
- **Unique Values (including NaN)**: 478 out of 478 (100.00%)
  - **Flag**: High Cardinality
    - **Examples**: ['https://ev-database.org/car/1934/Zeekr-001-Performance-AWD', 'https://ev-database.org/car/3044/Audi-SQ6-e-tron-Sportback', 'https://ev-database.org/car/3164/Ford-e-Tourneo-Custom-L2-160-kW']

A full issue summary table is saved to reports/categorical_checks_table_two.csv.
END OF REPORT
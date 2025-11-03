# Data Integrity Check Report

This report details the findings from a rigorous data integrity analysis of the `electric_vehicles_spec_2025.csv` dataset.

### Missing Values Analysis

The following columns have missing values:

- **`number_of_cells`**: 202 missing values (42.26%)
- **`towing_capacity_kg`**: 26 missing values (5.44%)
- **`torque_nm`**: 7 missing values (1.46%)
- **`fast_charging_power_kw_dc`**: 1 missing values (0.21%)
- **`fast_charge_port`**: 1 missing values (0.21%)
- **`model`**: 1 missing values (0.21%)
- **`cargo_volume_l`**: 1 missing values (0.21%)


### Constant Columns Analysis

- **`battery_type`**: Only one unique value: 'Lithium-ion'


### Missingness Patterns

Found 25 rows with multiple missing values.
Example rows with multiple missing values (first 3 rows):
```json
[
  {
    "brand": "Aiways",
    "model": "U5",
    "top_speed_kmh": 150,
    "battery_capacity_kWh": 60.0,
    "battery_type": "Lithium-ion",
    "number_of_cells": NaN,
    "torque_nm": 310.0,
    "efficiency_wh_per_km": 156,
    "range_km": 315,
    "acceleration_0_100_s": 7.5,
    "fast_charging_power_kw_dc": 78.0,
    "fast_charge_port": "CCS",
    "towing_capacity_kg": NaN,
    "cargo_volume_l": "496",
    "seats": 5,
    "drivetrain": "FWD",
    "segment": "JC - Medium",
    "length_mm": 4680,
    "width_mm": 1865,
    "height_mm": 1700,
    "car_body_type": "SUV",
    "source_url": "https://ev-database.org/car/1678/Aiways-U5"
  },
  {
    "brand": "Aiways",
    "model": "U6",
    "top_speed_kmh": 160,
    "battery_capacity_kWh": 60.0,
    "battery_type": "Lithium-ion",
    "number_of_cells": NaN,
    "torque_nm": 315.0,
    "efficiency_wh_per_km": 150,
    "range_km": 350,
    "acceleration_0_100_s": 7.0,
    "fast_charging_power_kw_dc": 78.0,
    "fast_charge_port": "CCS",
    "towing_capacity_kg": NaN,
    "cargo_volume_l": "472",
    "seats": 5,
    "drivetrain": "FWD",
    "segment": "JC - Medium",
    "length_mm": 4805,
    "width_mm": 1880,
    "height_mm": 1641,
    "car_body_type": "SUV",
    "source_url": "https://ev-database.org/car/1766/Aiways-U6"
  },
  {
    "brand": "Dongfeng",
    "model": "Box 31.4 kWh",
    "top_speed_kmh": 140,
    "battery_capacity_kWh": 29.0,
    "battery_type": "Lithium-ion",
    "number_of_cells": NaN,
    "torque_nm": 160.0,
    "efficiency_wh_per_km": 126,
    "range_km": 190,
    "acceleration_0_100_s": 12.5,
    "fast_charging_power_kw_dc": 50.0,
    "fast_charge_port": "CCS",
    "towing_capacity_kg": NaN,
    "cargo_volume_l": "326",
    "seats": 5,
    "drivetrain": "FWD",
    "segment": "B - Compact",
    "length_mm": 4020,
    "width_mm": 1810,
    "height_mm": 1570,
    "car_body_type": "Hatchback",
    "source_url": "https://ev-database.org/car/3035/Dongfeng-Box-314-kWh"
  }
]
```


### Duplicate Rows Analysis

No exact duplicate rows found.


### Partial Duplicate Analysis (Brand + Model)

No partial duplicates found based on 'brand' and 'model' combination.


### Uniqueness and Key Constraints

- **`source_url`**: All values are unique. This column can serve as a primary key.
- **`brand` + `model`**: All combinations are unique. This combination can serve as a composite primary key.


### Data Type and Format Mismatches

- **`cargo_volume_l`**: Stored as `object` but contains non-numeric string values (e.g., '10 Banana Boxes') and `float` for `NaN`. This column requires significant cleaning to be converted to a numeric type.
  Problematic examples: 10 Banana Boxes, 31 Banana Boxes, 13 Banana Boxes
- **`model`**: Stored as `object` but contains `float` for `NaN` values. This is a common pandas behavior but technically a mixed type.
- **`fast_charge_port`**: Stored as `object` but contains `float` for `NaN` values, similar to `model`.


A full issue summary table is saved to reports/integrity_checks_table.csv.

END OF REPORT

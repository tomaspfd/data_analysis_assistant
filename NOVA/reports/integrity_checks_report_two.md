# Data Integrity Diagnostic Report - Phase Two

## 1. Column-level Type Consistency

### `cargo_volume_l` - Non-numeric Values
- **Issue**: The `cargo_volume_l` column, intended to store cargo volume in liters, contains non-numeric string values. This prevents direct numerical analysis and type conversion.
- **Evidence**:
```
| model              | cargo_volume_l   |
|:-------------------|:-----------------|
| Q6 e-tron quattro  | 10 Banana Boxes  |
| MIFA 9             | 31 Banana Boxes  |
| EQS SUV 580 4MATIC | 13 Banana Boxes  |
```

## 2. Structural & Schema Checks

### Column Naming Conventions
- **Issue**: All column names are expected to follow a consistent `snake_case` convention without spaces or special characters.
- **Evidence**:
```
Problematic column names found: battery_capacity_kWh
```

### Current DataFrame Schema
- **Issue**: Documentation of the current data types for each column.
- **Evidence**:
```
brand                         object
model                         object
top_speed_kmh                  int64
battery_capacity_kWh         float64
battery_type                  object
number_of_cells              float64
torque_nm                    float64
efficiency_wh_per_km           int64
range_km                       int64
acceleration_0_100_s         float64
fast_charging_power_kw_dc    float64
fast_charge_port              object
towing_capacity_kg           float64
cargo_volume_l                object
seats                          int64
drivetrain                    object
segment                       object
length_mm                      int64
width_mm                       int64
height_mm                      int64
car_body_type                 object
source_url                    object
```

## 3. Cross-field and Multi-column Validation

### `seats` - Zero Seats
- **Issue**: The `seats` column contains entries where the number of seats is reported as 0. A car is expected to have at least one seat.
- **Evidence**:
No entries with 0 seats found.
### Numerical Columns - Negative Values
- **Issue**: Several numerical columns contain negative values, which are physically impossible for the attributes they represent (e.g., speed, capacity, dimensions).
- **Evidence**:
No negative values found in relevant numerical columns.
### `top_speed_kmh` - Zero Top Speed
- **Issue**: The `top_speed_kmh` column contains entries with a reported top speed of 0 km/h, which is unrealistic for a functional vehicle.
- **Evidence**:
No entries with 0 km/h top speed found.
### `acceleration_0_100_s` - Zero Acceleration Time
- **Issue**: The `acceleration_0_100_s` column contains entries with a reported acceleration time of 0 seconds, which is physically impossible.
- **Evidence**:
No entries with 0 seconds acceleration time found.
### `efficiency_wh_per_km` - Zero or Negative Efficiency
- **Issue**: The `efficiency_wh_per_km` column contains zero or negative values, which are physically impossible for energy consumption.
- **Evidence**:
No zero or negative efficiency values found.
### `number_of_cells` - Non-Positive Values
- **Issue**: The `number_of_cells` column contains non-positive values (excluding NaN), which is physically impossible for the count of battery cells.
- **Evidence**:
No non-positive values found in `number_of_cells` (excluding NaN).
### `cargo_volume_l` - Negative Values (after numeric conversion)
- **Issue**: After attempting to convert `cargo_volume_l` to a numeric type, some entries resulted in negative values, which are physically impossible for volume.
- **Evidence**:
No negative values found in `cargo_volume_l` after numeric conversion.
A full issue summary table is saved to reports/integrity_checks_table_two.csv.
END OF REPORT

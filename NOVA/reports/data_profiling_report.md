# Dataset Baseline Profiling Report for electric_vehicles_spec_2025.csv

## Table of Contents
- [Dataset Overview](#dataset-overview)
- [Per-Column Documentation](#per-column-documentation)
- [Data Types and Missingness Overview](#data-types-and-missingness-overview)
- [Online Research Summary](#online-research-summary)
- [Disclaimer](#disclaimer)

## Dataset Overview
- Shape: 478 rows × 22 columns
- Columns: ['brand', 'model', 'top_speed_kmh', 'battery_capacity_kWh', 'battery_type', 'number_of_cells', 'torque_nm', 'efficiency_wh_per_km', 'range_km', 'acceleration_0_100_s', 'fast_charging_power_kw_dc', 'fast_charge_port', 'towing_capacity_kg', 'cargo_volume_l', 'seats', 'drivetrain', 'segment', 'length_mm', 'width_mm', 'height_mm', 'car_body_type', 'source_url']

### Pandas Data Types
- brand: object  
- model: object  
- top_speed_kmh: int64  
- battery_capacity_kWh: float64  
- battery_type: object  
- number_of_cells: float64  
- torque_nm: float64  
- efficiency_wh_per_km: int64  
- range_km: int64  
- acceleration_0_100_s: float64  
- fast_charging_power_kw_dc: float64  
- fast_charge_port: object  
- towing_capacity_kg: float64  
- cargo_volume_l: object  
- seats: int64  
- drivetrain: object  
- segment: object  
- length_mm: int64  
- width_mm: int64  
- height_mm: int64  
- car_body_type: object  
- source_url: object  

## Per-Column Documentation

### brand
- **Description:** Manufacturer/brand of the electric vehicle.
- **Pandas Data Type:** object
- **Missing Values:** 0 (0.0%)
- **Unique Values:** 59
#### Top 10 Value Counts (Categorical)

| Value           | Count |
|-----------------|-------|
| Mercedes-Benz   | 42    |
| Audi            | 28    |
| Porsche         | 26    |
| Volkswagen      | 23    |
| Ford            | 22    |
| BMW             | 20    |
| Peugeot         | 19    |
| Volvo           | 18    |
| BYD             | 17    |
| Smart           | 17    |

- **Most Frequent Value:** Mercedes-Benz, occurring 8.79% of the time
- **Actionable Flags:** ['No action needed']

### model
- **Description:** Specific model name of the electric vehicle.
- **Pandas Data Type:** object
- **Missing Values:** 1 (0.21%)
- **Unique Values:** 477
#### Top 10 Value Counts (Categorical)

| Value                                  | Count |
|----------------------------------------|-------|
| 500e Convertible                       | 1     |
| 500e Hatchback                         | 1     |
| 600e Scorpionissima                    | 1     |
| 600e Turismo                           | 1     |
| U5                                     | 1     |
| U6                                     | 1     |
| Romeo Junior Elettrica 54 kWh          | 1     |
| Romeo Junior Elettrica 54 kWh Veloce   | 1     |
| A290 Electric 180 hp                   | 1     |
| A290 Electric 220 hp                   | 1     |

- **Most Frequent Value:** 500e Convertible, occurring 0.21% of the time
- **Actionable Flags:** ['Needs imputation due to 0.21% missingness', 'High cardinality: >90% unique values', 'Needs type conversion: Inconsistent numeric encoding']

### top_speed_kmh
- **Description:** Top speed in kilometers per hour.
- **Pandas Data Type:** int64
- **Missing Values:** 0 (0.0%)
- **Unique Values:** 38
#### Summary Statistics (Numeric)

| Metric | Value   |
|--------|---------|
| mean   | 185.49  |
| std    | 34.25   |
| min    | 125.0   |
| 25%    | 160.0   |
| 50%    | 180.0   |
| 75%    | 201.0   |
| max    | 325.0   |
| count  | 478     |

- **Actionable Flags:** ['No action needed']

### battery_capacity_kWh
- **Description:** Battery capacity measured in kilowatt-hours (kWh).
- **Pandas Data Type:** float64
- **Missing Values:** 0 (0.0%)
- **Unique Values:** 121
#### Summary Statistics (Numeric)

| Metric | Value    |
|--------|----------|
| mean   | 74.04    |
| std    | 20.33    |
| min    | 21.3     |
| 25%    | 60.0     |
| 50%    | 76.15    |
| 75%    | 90.6     |
| max    | 118.0    |
| count  | 478      |

- **Actionable Flags:** ['No action needed']

### battery_type
- **Description:** Type of battery technology used, e.g. Lithium-ion.
- **Pandas Data Type:** object
- **Missing Values:** 0 (0.0%)
- **Unique Values:** 1
#### Top 10 Value Counts (Categorical)

| Value       | Count |
|-------------|-------|
| Lithium-ion | 478   |

- **Most Frequent Value:** Lithium-ion, occurring 100.0% of the time
- **Actionable Flags:** ['Non-informative: Constant column']

### number_of_cells
- **Description:** Number of battery cells that comprise the battery pack.
- **Pandas Data Type:** float64
- **Missing Values:** 202 (42.26%)
- **Unique Values:** 38
#### Summary Statistics (Numeric)

| Metric | Value    |
|--------|----------|
| mean   | 485.29   |
| std    | 1210.82  |
| min    | 72.0     |
| 25%    | 150.0    |
| 50%    | 216.0    |
| 75%    | 324.0    |
| max    | 7920.0   |
| count  | 276      |

- **Actionable Flags:** ['Needs imputation due to 42.26% missingness']

### torque_nm
- **Description:** Torque generated, measured in Newton-meters (Nm).
- **Pandas Data Type:** float64
- **Missing Values:** 7 (1.46%)
- **Unique Values:** 128
#### Summary Statistics (Numeric)

| Metric | Value   |
|--------|---------|
| mean   | 498.01  |
| std    | 241.46  |
| min    | 113.0   |
| 25%    | 305.0   |
| 50%    | 430.0   |
| 75%    | 679.0   |
| max    | 1350.0  |
| count  | 471     |

- **Actionable Flags:** ['Needs imputation due to 1.46% missingness']

### efficiency_wh_per_km
- **Description:** Energy efficiency in watt-hours per kilometer.
- **Pandas Data Type:** int64
- **Missing Values:** 0 (0.0%)
- **Unique Values:** 112
#### Summary Statistics (Numeric)

| Metric | Value    |
|--------|----------|
| mean   | 162.9    |
| std    | 34.32    |
| min    | 109.0   |
| 25%    | 143.0    |
| 50%    | 155.0    |
| 75%    | 177.75   |
| max    | 370.0    |
| count  | 478      |

- **Actionable Flags:** ['No action needed']

### range_km
- **Description:** Estimated driving range in kilometers on a full charge.
- **Pandas Data Type:** int64
- **Missing Values:** 0 (0.0%)
- **Unique Values:** 88
#### Summary Statistics (Numeric)

| Metric | Value    |
|--------|----------|
| mean   | 393.18   |
| std    | 103.29   |
| min    | 135.0    |
| 25%    | 320.0    |
| 50%    | 397.5    |
| 75%    | 470.0    |
| max    | 685.0    |
| count  | 478      |

- **Actionable Flags:** ['No action needed']

### acceleration_0_100_s
- **Description:** Time in seconds to accelerate from 0 to 100 km/h.
- **Pandas Data Type:** float64
- **Missing Values:** 0 (0.0%)
- **Unique Values:** 97
#### Summary Statistics (Numeric)

| Metric | Value   |
|--------|---------|
| mean   | 6.88    |
| std    | 2.73    |
| min    | 2.2     |
| 25%    | 4.8     |
| 50%    | 6.6     |
| 75%    | 8.2     |
| max    | 19.1    |
| count  | 478     |

- **Actionable Flags:** ['No action needed']

### fast_charging_power_kw_dc
- **Description:** Maximum fast charging power in kW for DC charging.
- **Pandas Data Type:** float64
- **Missing Values:** 1 (0.21%)
- **Unique Values:** 71
#### Summary Statistics (Numeric)

| Metric | Value   |
|--------|---------|
| mean   | 125.01  |
| std    | 58.21   |
| min    | 29.0    |
| 25%    | 80.0    |
| 50%    | 113.0   |
| 75%    | 150.0   |
| max    | 281.0   |
| count  | 477     |

- **Actionable Flags:** ['Needs imputation due to 0.21% missingness']

### fast_charge_port
- **Description:** Type of charging port used for fast charging (e.g. CCS).
- **Pandas Data Type:** object
- **Missing Values:** 1 (0.21%)
- **Unique Values:** 2
#### Top 10 Value Counts (Categorical)

| Value   | Count |
|---------|-------|
| CCS     | 476   |
| CHAdeMO | 1     |
| nan     | 1     |

- **Most Frequent Value:** CCS, occurring 99.58% of the time
- **Actionable Flags:** ['Needs imputation due to 0.21% missingness']

### towing_capacity_kg
- **Description:** Towing capacity in kilograms, if applicable.
- **Pandas Data Type:** float64
- **Missing Values:** 26 (5.44%)
- **Unique Values:** 26
#### Summary Statistics (Numeric)

| Metric | Value    |
|--------|----------|
| mean   | 1052.26  |
| std    | 737.85   |
| min    | 0.0      |
| 25%    | 500.0    |
| 50%    | 1000.0   |
| 75%    | 1600.0   |
| max    | 2500.0   |
| count  | 452      |

- **Actionable Flags:** ['Needs imputation due to 5.44% missingness']

### cargo_volume_l
- **Description:** Cargo/trunk volume in liters.
- **Pandas Data Type:** object
- **Missing Values:** 1 (0.21%)
- **Unique Values:** 140
#### Top 10 Value Counts (Categorical)

| Value | Count |
|-------|-------|
| 520   | 17    |
| 519   | 10    |
| 407   | 10    |
| 490   | 10    |
| 570   | 9     |
| 405   | 9     |
| 446   | 9     |
| 620   | 9     |
| 603   | 8     |
| 326   | 8     |

- **Most Frequent Value:** 520, occurring 3.56% of the time
- **Actionable Flags:** ['Needs imputation due to 0.21% missingness', 'Needs type conversion: Inconsistent numeric encoding']

### seats
- **Description:** Number of seats in the vehicle.
- **Pandas Data Type:** int64
- **Missing Values:** 0 (0.0%)
- **Unique Values:** 7
#### Summary Statistics (Numeric)

| Metric | Value  |
|--------|--------|
| mean   | 5.26   |
| std    | 1.0    |
| min    | 2.0    |
| 25%    | 5.0    |
| 50%    | 5.0    |
| 75%    | 5.0    |
| max    | 9.0    |
| count  | 478    |

- **Actionable Flags:** ['No action needed']

### drivetrain
- **Description:** Drive configuration (e.g., FWD, RWD, AWD).
- **Pandas Data Type:** object
- **Missing Values:** 0 (0.0%)
- **Unique Values:** 3
#### Top 10 Value Counts (Categorical)

| Value | Count |
|-------|-------|
| AWD   | 191   |
| FWD   | 156   |
| RWD   | 131   |

- **Most Frequent Value:** AWD, occurring 39.96% of the time
- **Actionable Flags:** ['No action needed']

### segment
- **Description:** Market segment classification (e.g., Compact, Medium).
- **Pandas Data Type:** object
- **Missing Values:** 0 (0.0%)
- **Unique Values:** 15
#### Top 10 Value Counts (Categorical)

| Value         | Count |
|---------------|-------|
| JC - Medium   | 91    |
| JD - Large    | 58    |
| F - Luxury    | 51    |
| N - Passenger Van | 47    |
| JB - Compact  | 44    |
| C - Medium    | 34    |
| E - Executive | 30    |
| JF - Luxury   | 30    |
| B - Compact   | 29    |
| D - Large     | 28    |

- **Most Frequent Value:** JC - Medium, occurring 19.04% of the time
- **Actionable Flags:** ['No action needed']

### length_mm
- **Description:** Length of the vehicle in millimeters.
- **Pandas Data Type:** int64
- **Missing Values:** 0 (0.0%)
- **Unique Values:** 172
#### Summary Statistics (Numeric)

| Metric | Value    |
|--------|----------|
| mean   | 4678.51  |
| std    | 369.21   |
| min    | 3620.0   |
| 25%    | 4440.0   |
| 50%    | 4720.0   |
| 75%    | 4961.0   |
| max    | 5908.0   |
| count  | 478      |

- **Actionable Flags:** ['No action needed']

### width_mm
- **Description:** Width of the vehicle in millimeters.
- **Pandas Data Type:** int64
- **Missing Values:** 0 (0.0%)
- **Unique Values:** 108
#### Summary Statistics (Numeric)

| Metric | Value    |
|--------|----------|
| mean   | 1887.36  |
| std    | 73.66    |
| min    | 1610.0   |
| 25%    | 1849.0   |
| 50%    | 1890.0   |
| 75%    | 1939.0   |
| max    | 2080.0   |
| count  | 478      |

- **Actionable Flags:** ['No action needed']

### height_mm
- **Description:** Height of the vehicle in millimeters.
- **Pandas Data Type:** int64
- **Missing Values:** 0 (0.0%)
- **Unique Values:** 162
#### Summary Statistics (Numeric)

| Metric | Value    |
|--------|----------|
| mean   | 1601.13  |
| std    | 130.75   |
| min    | 1329.0   |
| 25%    | 1514.0   |
| 50%    | 1596.0   |
| 75%    | 1665.0   |
| max    | 1986.0   |
| count  | 478      |

- **Actionable Flags:** ['No action needed']

### car_body_type
- **Description:** Body style of the vehicle (e.g., Hatchback, SUV).
- **Pandas Data Type:** object
- **Missing Values:** 0 (0.0%)
- **Unique Values:** 8
#### Top 10 Value Counts (Categorical)

| Value                | Count |
|----------------------|-------|
| SUV                  | 244   |
| Sedan                | 63    |
| Hatchback            | 57    |
| Small Passenger Van  | 47    |
| Liftback Sedan       | 33    |
| Station/Estate       | 27    |
| Cabriolet            | 5     |
| Coupe                | 2     |

- **Most Frequent Value:** SUV, occurring 51.05% of the time
- **Actionable Flags:** ['No action needed']

### source_url
- **Description:** URL of the source data from EV-database.org.
- **Pandas Data Type:** object
- **Missing Values:** 0 (0.0%)
- **Unique Values:** 478
#### Top 10 Value Counts (Categorical)

| Value                                                        | Count |
|--------------------------------------------------------------|-------|
| https://ev-database.org/car/1904/Abarth-500e-Convertible      | 1     |
| https://ev-database.org/car/1903/Abarth-500e-Hatchback        | 1     |
| https://ev-database.org/car/3057/Abarth-600e-Scorpionissima    | 1     |
| https://ev-database.org/car/3056/Abarth-600e-Turismo           | 1     |
| https://ev-database.org/car/1678/Aiways-U5                     | 1     |
| https://ev-database.org/car/1766/Aiways-U6                     | 1     |
| https://ev-database.org/car/2184/Alfa-Romeo-Junior-Elettrica-54-kWh | 1  |
| https://ev-database.org/car/2185/Alfa-Romeo-Junior-Elettrica-54-kWh-Veloce | 1  |
| https://ev-database.org/car/2268/Alpine-A290-Electric-180-hp   | 1     |
| https://ev-database.org/car/2269/Alpine-A290-Electric-220-hp   | 1     |

- **Most Frequent Value:** https://ev-database.org/car/1904/Abarth-500e-Convertible, occurring 0.21% of the time
- **Actionable Flags:** ['High cardinality: >90% unique values']

## Data Types and Missingness Overview
Refer to the per-column documentation above for type mismatches such as numeric data stored as strings and inconsistent encodings.

## Missingness Overview
The report above indicates the missing values per column. Downstream agents should consider imputation for columns with significant missingness.

## Categorical Value Summaries
For non-numeric columns, top 10 value counts are provided for quick inspection of category distributions.

## Non-informative / Constant Columns
Columns flagged as having all missing values or being constant (one unique value) are noted in the per-column documentation.

## Short Notes for Downstream Diagnostics
- Duplicate rows/columns were not checked in this report.
- No cleaning, dropping, or alteration was performed in this report—this is descriptive profiling only.

## Online Research Summary
The dataset provides detailed specifications of electric vehicles, including information on performance, battery, efficiency, dimensions, and market segmentation. This dataset is validated by EV-database.org and is suitable for comparative analysis of EV performance, market trend explorations, and segment analysis. It can be used in studies on advancements in battery technology, charging infrastructure, and the evolving EV market dynamics. Recent developments in the domain include rapid advancements in battery efficiencies and the expansion of fast charging networks. This external context may aid in correlating technical specifications with market trends and policy effects.

## Disclaimer
No cleaning, dropping, or alteration was performed in this report—this is descriptive profiling only.
END OF REPORT
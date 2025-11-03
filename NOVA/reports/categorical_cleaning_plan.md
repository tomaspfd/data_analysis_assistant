
# Categorical Data Cleaning Plan

This plan outlines the necessary cleaning steps for the `electric_vehicles_spec_2025.csv` dataset, based on the categorical diagnostic reports and baseline profiling.

## Cleaning Actions Table

| Issue | Column(s)/Row(s) | Recommended Cleaning Action | Justification |
|---|---|---|---|
| Constant Column / Non-informative | `battery_type` | Drop the column. | This column has only one unique value ('Lithium-ion') across all entries, providing no discriminatory information for analysis. |
| Mixed Data Types, Needs Imputation, High Cardinality, Rare/Singleton Categories | `model` | 1. Convert column to string type, replacing NaN with 'Unknown Model'.<br>2. Keep high cardinality and rare/singleton categories as is. | Ensures data consistency for categorical operations. 'Unknown Model' is a suitable placeholder for the single missing value. High cardinality is expected for a unique identifier like 'model' and does not require further cleaning for its intended use. |
| Mixed Data Types, Needs Imputation, Rare/Singleton Categories | `fast_charge_port` | 1. Convert column to string type, replacing NaN with the mode ('CCS').<br>2. Keep rare/singleton categories as is. | Ensures data consistency. Mode imputation ('CCS') is appropriate for the single missing value given its high frequency. 'CHAdeMO' is a valid, albeit rare, port type and should be preserved. |
| Mixed Data Types, Non-numeric strings, Needs Imputation, Rare/Singleton Categories | `cargo_volume_l` | 1. Extract numeric values from strings; convert non-numeric entries (e.g., 'Banana Boxes') to NaN.<br>2. Convert the column to a numeric type (float).<br>3. Impute all missing values (original NaNs and those from non-numeric strings) with the median. | This column is intended to be numeric. Non-numeric text is data corruption and should be treated as missing. Converting to numeric and imputing allows for quantitative analysis. Rare numeric values are natural and do not require specific handling. |
| Needs Imputation (High Percentage) | `number_of_cells` | Impute missing values with the median. | With 42.26% missing values, median imputation is a robust strategy to retain as much data as possible for this numerical feature, without introducing significant bias from extreme values. |
| Needs Imputation | `torque_nm` | Impute missing values with the median. | A small percentage (1.46%) of missing numerical data can be effectively imputed with the median to maintain data integrity. |
| Needs Imputation | `fast_charging_power_kw_dc` | Impute the single missing value with the median. | A single missing numerical value is best handled by imputing with a central tendency measure like the median. |
| Needs Imputation | `towing_capacity_kg` | Impute missing values with the median. | Median imputation is a suitable approach for a moderate percentage (5.44%) of missing numerical data, especially for a feature that might have a skewed distribution. |
| Rare/Singleton Categories | `brand` | Keep as is. | These are legitimate brand names. Altering or grouping them without specific domain knowledge or a clear analytical need would lead to loss of information. |
| Rare/Singleton Categories | `segment` | Keep as is. | These are valid market segments. While some are less common, they accurately describe vehicle classifications and should be preserved. |
| Rare Categories | `car_body_type` | Keep as is. | 'Coupe' is a valid car body type. It represents a distinct category and should not be altered. |
| High Cardinality, Rare/Singleton Categories | `source_url` | Keep as is. | This column serves as a unique identifier (URL source) for each entry. High cardinality is expected and desired for such an identifier and does not require cleaning. |

## Top-Priority Cleaning Actions

1.  **Handle `cargo_volume_l`**: This is the most critical step due to mixed data types and non-numeric strings. Extract numeric values, convert non-numeric to NaN, convert column to `float`, and then impute missing values with the median.
2.  **Drop `battery_type`**: This column is constant and provides no analytical value.
3.  **Handle `model`**: Convert to `str` type, replacing NaN with 'Unknown Model' to ensure type consistency and handle the missing value.
4.  **Handle `fast_charge_port`**: Convert to `str` type, replacing NaN with the mode ('CCS') for consistency and completeness.
5.  **Impute `number_of_cells`**: Address the high percentage of missing values by imputing with the median.
6.  **Impute `towing_capacity_kg`**: Impute missing values with the median.
7.  **Impute `torque_nm`**: Impute missing values with the median.
8.  **Impute `fast_charging_power_kw_dc`**: Impute the single missing value with the median.

## Notes for Implementation

*   **Assumptions for `cargo_volume_l`**: We assume that non-numeric entries like "Banana Boxes" are data errors and should be treated as missing data (NaN) rather than attempting to convert them to a specific volume.
*   **Imputation Strategy**: Median imputation is chosen for numerical columns due to its robustness to outliers. For categorical columns, mode imputation or a specific placeholder is used. This is a standard and generally robust approach.
*   **High Cardinality Columns**: `model` and `source_url` are retained as identifiers. If these columns were to be used as features in a machine learning model, further feature engineering (e.g., target encoding, hashing) might be necessary, but this is beyond the scope of basic data cleaning.
*   **Rare Categories**: Valid rare categories in `brand`, `segment`, `car_body_type`, and `fast_charge_port` are preserved as they represent genuine data points and do not indicate data quality issues requiring alteration.

This plan is based strictly on the categorical findings.

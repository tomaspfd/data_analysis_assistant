
# Numerical Cleaning Plan for electric_vehicles_spec_2025.csv

This plan outlines the recommended cleaning actions for the identified numerical data quality issues, based on the provided diagnostic reports.

## Cleaning Actions Table

| Issue | Column(s)/Row(s) | Recommended Cleaning Action | Justification |
|---|---|---|---|
| Non-informative (constant) column | `battery_type` | Drop the `battery_type` column. | This column has only one unique value ('Lithium-ion'), providing no discriminatory information for analysis. |
| Missing Values & Data Type Mismatch | `model` | Convert `model` to string type. Impute the single missing value with 'Unknown Model'. | Ensures type consistency for the column. 'Unknown Model' is a suitable placeholder for a high-cardinality identifier, preserving the row without introducing bias. |
| Missing Values & Data Type Mismatch | `fast_charge_port` | Convert `fast_charge_port` to string type. Impute the single missing value with the mode ('CCS'). | Ensures type consistency. Imputing with the mode is appropriate for a categorical column with very few missing values, especially when one category is overwhelmingly dominant (CCS: 99.79%). |
| Data Type Mismatch (non-numeric strings) & Missing Values | `cargo_volume_l` | 1. Extract numeric values from strings (e.g., '10 Banana Boxes' becomes 10). Non-numeric parts should be removed. <br> 2. Convert the column to a numeric type (float). <br> 3. Impute any remaining missing values (including those resulting from non-numeric string conversion) with the median of the column. | This ensures the column is usable as a quantitative feature. Extracting numbers from problematic entries allows retaining valuable information. Median imputation is robust to potential outliers and provides a central tendency estimate. |
| Missing Values | `number_of_cells` | Impute missing values using the median of the column. | Median imputation is robust to outliers and provides a central tendency estimate for the missing values, allowing the column to be used in analysis despite high missingness. |
| Missing Values | `towing_capacity_kg` | Impute missing values using the median of the column. | Median imputation is robust to outliers and provides a reasonable estimate for the missing values. |
| Missing Values | `torque_nm` | Impute missing values using the median of the column. | Median imputation is robust to outliers and provides a reasonable estimate for the missing values. |
| Missing Values | `fast_charging_power_kw_dc` | Impute missing values using the median of the column. | Median imputation is robust to outliers and provides a reasonable estimate for the missing value. |

## Top-Priority Cleaning Actions

1.  **Clean and Convert `cargo_volume_l`**: This is the most critical step as it involves both type conversion from problematic strings to numeric and then handling missing values. This must be done first to make the column usable.
2.  **Standardize and Impute `model` and `fast_charge_port`**: These columns have mixed types due to `NaN` values and require conversion to string before imputation.
3.  **Impute `number_of_cells`**: Given the high percentage of missing values (42.26%), addressing this early is important to maximize the utility of the column.
4.  **Impute `towing_capacity_kg`, `torque_nm`, and `fast_charging_power_kw_dc`**: These columns have fewer missing values and can be imputed after the more complex type conversions.
5.  **Drop `battery_type`**: This is a straightforward action that can be performed at any convenient point, as it's a constant column.

## Notes, Assumptions, and Risks

*   **`cargo_volume_l`**: The assumption for 'Banana Boxes' entries is that the leading number represents the volume in liters, and the text is extraneous. If this assumption is incorrect, these values might need to be treated as entirely missing or require a different conversion logic.
*   **Imputation Strategy**: For numerical columns, median imputation is chosen for its robustness to outliers. For categorical columns, mode imputation or a placeholder is used. The choice of imputation method can impact downstream analysis, especially for `number_of_cells` due to its high missingness. More sophisticated imputation methods (e.g., regression imputation, K-nearest neighbors imputation) could be considered if higher accuracy is required and computational resources allow.
*   **Outliers**: The reports indicate no obvious outliers based on heuristic checks for numerical columns. However, a dedicated outlier analysis might be beneficial for certain columns (e.g., `number_of_cells` given its high standard deviation relative to the mean) if specific analytical goals require it. This plan focuses solely on the flagged numerical issues.

This plan is based strictly on the numerical findings.

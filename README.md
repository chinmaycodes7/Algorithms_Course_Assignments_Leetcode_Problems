# Student Grouping Tool

This project helps in dividing students into groups in three different ways using their branch information from an Excel file.

### Features

* **Branchwise Groups** → All students of the same branch in one group (ignores `n`).
* **Uniform Groups** → Students from the same branch distributed into `n` groups.
* **Mixed Groups** → Students from different branches combined into `n` groups (round-robin style).

### Input

* Excel file with student details (`Name`, `Email`, `Roll`).

### Output

* CSV files saved inside separate folders:

  * `branchwise_groups/`
  * `uniform_groups/`
  * `mixed_groups/`


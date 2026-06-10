# Dataset Understanding Framework

## Purpose

The Dataset Understanding Layer helps ODIF inspect an unknown tabular dataset before analysis, reporting, or dashboard work begins.

The goal is to answer:

- What is this dataset?
- What columns exist?
- What data types appear to exist?
- Which columns appear to be dimensions?
- Which columns appear to be measures?
- Which columns may be dates or timestamps?
- What metrics may be calculated?
- What relationships may exist?
- What validation opportunities may exist?
- What analyses may be possible?

## Version 1 Input Contract

Version 1 accepts one unknown tabular dataset.

The dataset my eventually come from:

- CSV file
- Spreadsheet
- SQL table
- pandas DataFrame

For framework purposes, all inputs are treated as rows and columns.

## Required Input

- Column names
- Row values

## Optional Inputs - Later

- Business question
- Expected schema
- Known primary key
- Known date column
- Known metric definitions
- Source system notes

## Version 1 Assumption

ODIF assumes no prior business context, no expected schema, and no known metric definitions.

## Human Review Principle

The Dataset Understanding Layer should support user review and correction before downstream validation, metric discovery, analysis, or reporting.

Automated assessment should be treated as an initial interpretation, not a final truth.

Users should be able to provide feedback such as:

- Renaming columns
- Confirming column meanings
- Correcting inferred column types
- Identifying dimensions
- identifying measures
- Identifying date or timestamp fields
- Identifying IDs or keys
- Providing business rules
- Confirming or rejecting suggested metrics

The framework should preserve the difference between:

- System-inferred understanding
- User-confirmed understanding

This allows ODIF to improve accuracy while keeping the user involved in business context decisions.

## Human-in-the-loop Pipeline Principle

ODIF is intentionally designed with human-in-the-loop validation and decision steps at key handoff points.

The Dataset Understanding Layer is one of those handoff points.

Automated assessment should help the user form an initial interpretation, but the user should be able to review, correct, confirm, or reject that interpretation before the pipeline proceeds.

This matters because later stages depend on the quality of earlier decisions.

For example:
- Column classification affects metric discovery.
- Metric discovery affects validation opportunities.
- Validation results affect analysis trust.
- Analysis trust affects reporting.
- Reporting affects decision support.

The pipeline should preserve a clear distinction between:

- System-inferred understanding
- User-confirmed understanding
- User-corrected understanding

This makes ODIF more explainable, auditable, and trustworthy.

## Processing State 1: Dataset Inventory

### Purpose

Dataset Inventory indentifies the basic shape of the dataset before ODIF attempts to infer meaning, assess quality, discover metrics, or recommend analyses.

This stage answers:

- How many rows exist?
- How mant columns exist?
- What column names exist?

### Output

Dataset Inventory should produce:

- Row count
- Column count
- Column names

### Excluded From This Stage

Dataset Inventory should not yet include:

- Data type inference
- Null counts
- Distinct counts
- Sample values
- Column classification
- Metric discovery
- Validation checks

Those belong to later processing stages.

---

## Hujman Review Checkpoint 1: Shape Review

### Purpose

Shape Review gives the user an opportunity to confirm whether the dataset structure matches expectations before ODIF performs deeper assessment.

This checkpoint asks:

- Is this the expected number of rows?
- Is this the expected number of columns?
- Are any expected columns missing?
- Are any unexpected columns present?
- Should any columns be renamed before continuing?

### Possible User Actions

The user may:

- Confirm the dataset shape
- Flag missing columns
- Flag unexpected columns
- Rename unclear columns
- Stop the pipeline if the dataset appears incorrect

### Design Principle

ODIF should not proceed from dataset shape to deeper interpretation until the user has had the opportunity to review the basic structure.

## Processing Stage 2: Structural Assessment

### Purpose

Structural Assessment examines the contents of each column to determine the apparent structure of the dataset.

This stage attempts to answer:

- What type of data appears to exist in each column>
- Which columns appear numeric?
- Which columns appear textual?
- Which columns appear date or timestamp based?
- Which columns appear boolean?

## Structural vs Record-Level Assessment

ODIF distinguishes between structural issues and record-level issues.

Examples:
- Missing columns
- Incorrect data types
- Schema drift
- Incosistent structural formats
- Unexpected dataset structures

Record-level issues affect individual records within an otherwise interpretable dataset.

Examples:

- Null values
- Duplicate values
- Invalid values
- Rule violations
- Outliers

These issue types should be tracked and reported separately because they often rquire different remediation paths and different business decisions.

# CS452 Project Repository

This repository contains materials and implementations for the CS452 course project, focusing on analyzing academic performance data in Turkey.

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Overview

The CS452 project involves analyzing academic performance data of Turkish universities and academicians. The project includes data processing, normalization, and visualization to derive meaningful insights.

## Project Structure

The repository is organized as follows:

```
cs452/
├── Academics_List.ipynb
├── Academics_Performance.py/
├── Faculty_Performance.py/
├── GenderColumnAdder.py/
├── Gender_Performance.py/
├── NamingMatching.ipynb
├── Türkiye Akademisyen Dataları.7z
├── University_Performances.py/
├── Vakif_Devlet_Comparison.py/
├── data_merger.ipynb
├── group_articles_with_count.py/
├── language_pie_plot.py/
├── match_articles.py/
└── merge_outputs.py/
```

- `Academics_List.ipynb`: Jupyter Notebook for listing academicians.
- `Academics_Performance/`: Directory containing scripts and data related to academic performance analysis.
- `FacultyPerformance/`: Directory for faculty performance evaluation.
- `GenderColumnAdder/`: Scripts for adding gender columns to datasets.
- `GenderPerformance/`: Analysis related to performance based on gender.
- `NamingMatching.ipynb`: Notebook for name matching and normalization.
- `Türkiye Akademisyen Dataları.7z`: Compressed dataset of Turkish academicians.
- `University_Performances/`: University performance analysis scripts.
- `Vakif_Devlet_Comparison/`: Comparison between Vakıf (private) and Devlet (public) universities.
- `data_merger.ipynb`: Notebook for merging various datasets.
- `group_articles_with_count/`: Scripts for grouping articles with count metrics.
- `language_pie_plot/`: Visualization scripts for language distribution in publications.
- `match_articles/`: Scripts for matching articles across datasets.
- `merge_outputs/`: Directory for merged output files.

## Installation

To set up the project on your local machine:

1. Clone the repository:
   ```bash
   git clone https://github.com/ceyhuntopal/cs452.git
   ```

2. Navigate to the project directory:
   ```bash
   cd cs452
   ```

3. Install dependencies (if applicable):
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the Jupyter Notebooks:

1. Ensure you have Jupyter installed. If not, install it:
   ```bash
   pip install jupyter
   ```

2. Start the Jupyter Notebook server:
   ```bash
   jupyter notebook
   ```

3. Open the desired `.ipynb` file from the Jupyter interface.

For running scripts:

1. Navigate to the respective directory:
   ```bash
   cd Academics_Performance
   ```

2. Execute the script:
   ```bash
   python script_name.py
   ```

## Features

- **Academic Performance Analysis:** Evaluate and visualize the performance of academicians.
- **University Comparisons:** Compare performances between different types of universities.
- **Gender-Based Analysis:** Analyze academic data with respect to gender.
- **Data Merging and Cleaning:** Tools for merging and cleaning datasets for analysis.

## Contributing

We welcome contributions! To contribute:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature-name"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.
---

For further questions, please contact the repository maintainer or open an issue in the GitHub tracker.

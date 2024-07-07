# Exercise Badges

![](https://byob.yarr.is/Xinia400/MADE-Homework/score_ex1) ![](https://byob.yarr.is/Xinia400/MADE-Homework/score_ex2) ![](https://byob.yarr.is/Xinia400/MADE-Homework/score_ex3) ![](https://byob.yarr.is/Xinia400/MADE-Homework/score_ex4) ![](https://byob.yarr.is/Xinia400/MADE-Homework/score_ex5)


# Methods of Advanced Data Engineering Python Data Pipeline Project


## Project Title
# Analyzing the Impact of Air Quality on Crop Production in Germany

<img src="project\images\projectimg.png" width="800" height="466">

## Key Questions
What is the potential impact of Air quality on Crop production, how do their relationship correlates and what this analysis inform and bring potential benefit for future agricultural practices and policy decisions?


## Project Overview
The aim of this project is to explore and quantify the impact of air quality on crop production based on rescent years using a comprehensive data analysis and machine learning approach. Given the growing concerns about environmental pollution and its potential effects on agriculture, this analysis aims to provide valuable insights that could inform policy decisions and farming practices.

### Datasets
## Datasource 1: Kaggle.com (World Air Quality Data 2024)
Metadata URL: https://www.kaggle.com/datasets/kaggle/meta-kaggle-code
Data URL: https://www.kaggle.com/datasets/kanchana1990/world-air-quality-data-2024-updated/download?datasetVersionNumber=1

## Datasource 2: FAO.org (Crops and Livestocks products)
Metadata URL: https://www.fao.org/faostat/en/#data/QCL/metadata
Data URL: https://bulks-faostat.fao.org/production/Production_Crops_Livestock_E_Europe.zip

## Installation and Usage
Instructions for setting up the project environment and running the analysis scripts.

```bash
# Clone the repository
git clone https://github.com/Xinia400/MADE-Homework.git

# Install dependencies
pip install pandas requests sqlite3 matplotlib seaborn scikit-learn
```

## Tools and Technologies Used
- Data Analysis: Python (Pandas,Numpy), Machine learning model (Gradient Boosting Regressor)
- Visualization: Matplotlib, Seaborn
- Version Control: Git, GitHub

[**Project Data Report**](project/data_report.pdf): Detailed documentation on data cleaning and pipeline procedures.

[**Project Analysis Report**](project/analysis_report.pdf): Comprehensive final report featuring data analysis and visualizations.

[**Project Visualization**](project/Analysis_Visualization.ipynb): Jupyter Notebook demonstrating exploratory data analysis (EDA) for 
the project.

[**Presentation Slides**](project/slides.pdf)

[**Presenation Video Link**](project/presentation-video.md)

## Data Pipeline and Testing

### Automated Data Pipeline
Discover the script [here](project/pipeline.py).

Our project implements an automated data pipeline designed for analyzing the impact of air quality on crop production, encompassing the following steps:

1. **Data Retrieval**: Air quality and crop production datasets are automatically collected from relevant sources on a regular basis.
2. **Data Processing**: The datasets undergo essential cleaning and transformation processes to ensure accuracy, consistency, and compatibility.
3. **Data Integration**: The processed data is merged into a structured format, facilitating comprehensive and detailed analysis.

This pipeline ensures that our data on air quality and crop production is consistently accurate and ready for in-depth trend and impact analysis.

### Testing Script
Explore the script [here](project/test.py).

To ensure the integrity of our data pipeline, we've developed a comprehensive testing script that includes:
1. **Verification of Data Retrieval**: Ensures that air quality and crop production data is accurately fetched from the specified sources.
2. **Validation of Data Processing**: Confirms that cleaning and transformation processes are correctly applied to both datasets.
3. **Integrity Assurance**: Maintains data consistency and accuracy throughout the entire pipeline.

### Continuous Integration Workflow
View the workflow configuration [here](.github/workflows/project.yml).

To maintain the robustness of our data pipeline, we utilize an automated workflow via GitHub Actions:

- **Continuous Integration (CI)**: The testing script is triggered automatically with every push to the main branch. This ensures that any updates or changes do not disrupt the pipeline's functionality and accuracy.

Our CI workflow ensures a reliable, error-free approach to analyzing the impact of air quality on crop production, delivering high-quality outcomes for the project.

## How to Run the Data Pipeline and Tests
Provide detailed instructions on how to execute the data pipeline and run the test scripts. Include any necessary commands or steps to set up the environment.

```bash
# command to run the data pipeline
python3 project/pipeline.py

# command to execute the test script
python3 project/test.py
```
## Contributing
Feel free to contribute this project by following these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourContribution`).
3. Make your changes and commit them (`git commit -am 'Add Data'`).
4. Push to the branch (`git push origin feature/YourContribution`).
5. Create a new Pull Request &
6. Focus Data Limitations.

Please ensure your code is well-documented.

## Limitations

### Data Limitations:

- **Missing Data**: The datasets had instances of missing values. These missing values were handled through various imputation techniques, which could potentially skew the results if the imputed values do not accurately reflect the true missing values.
- **Data Consistency**: Due to the presence of inconsistent data collection methods and inappropriate factors, we faced problem with finding efective correlation directly which affects the comparability of the results.

### Result Limitations:

- **Limited Variables**: The analysis primarily focused on the relationship between air quality (various pollutants) and crop production. This may not capture all the relevant factors influencing crop production, such as soil quality, weather conditions, and agricultural practices, thus limiting the comprehensiveness of the findings.
- **Non-Linear Relationships**: While the analysis explored non-linear relationships using machine learning models, there could still be complex interactions between variables that were not fully captured. The models used might not account for all underlying patterns and influences, leading to potential oversimplifications. These limitations highlight the need for more comprehensive and consistent data collection practices and the inclusion of additional relevant variables to enhance the robustness and reliability of future analyses.

## Authors and Acknowledgment
This project was initiated and completed by Xinia Apchora. 
I would like to extend my gratitude to our tutors **Philip Heltweg** and **Georg Schwarz**, as well as the **Friedrich-Alexander-Universität Erlangen-Nürnberg (FAU) MADE(Methods of Advanced Data Engineering) team**, for their guidance and support throughout this project.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
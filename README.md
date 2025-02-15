
# AI Odyssey Hackathon: Trend Analysis

![GitHub](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Dash](https://img.shields.io/badge/Dash-2.0%2B-orange)
![Plotly](https://img.shields.io/badge/Plotly-5.0%2B-green)

Welcome to the **AI Odyssey Hackathon: Trend Analysis** project! This repository contains the code and resources for analyzing and visualizing trends from X and Tiktok data. The project leverages Python, Dash, and Plotly to create an interactive dashboard for exploring real-time trends and insights.

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Project Structure](#project-structure)
6. [Contributing](#contributing)
7. [License](#license)
8. [Acknowledgments](#acknowledgments)

---

## Project Overview

This project was developed as part of the **AI Odyssey Hackathon**, focusing on analyzing trends from Twitter data. The goal is to provide a user-friendly dashboard that visualizes key insights, such as popular hashtags, trending topics, and sentiment analysis. The dashboard is built using **Dash**, a Python framework for building analytical web applications, and **Plotly** for interactive visualizations.

---

## Features

- **Real-Time Data**: Visualizations are updated dynamically based on the latest data.
- **Trend Analysis**: Analyze popular hashtags, trending topics, and user engagement.
- **Sentiment Analysis**: Understand the sentiment behind tweets (positive, negative, neutral).
- **Content Generation** : based on the most trends we can generate videos images and texts 
---

## Installation

To set up the project locally, follow these steps:

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

# AI Odyssey Hackathon - Trend Analysis

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/rebhimohamedamine/ai-odyssey-hackathon-trend-analysis.git
cd ai-odyssey-hackathon-trend-analysis
```

### 2. Install Required Libraries
```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables
1. Create a `.env` file in the root directory.
2. Add your Twitter API credentials (if applicable):

```
TWITTER_API_KEY=your_api_key
TWITTER_API_SECRET_KEY=your_api_secret_key
TWITTER_ACCESS_TOKEN=your_access_token
TWITTER_ACCESS_TOKEN_SECRET=your_access_token_secret
```

### 4. Run the Program
- **TikTok Analysis:** The submitted file is a Jupyter Notebook that has already been executed.
- **X (Twitter) Analysis:** Due to project size limitations on GitHub, the full project is available as a zipped file. A link to the file will be shared via Google Drive.

For any issues, feel free to reach out!
for tiktok analysis the code is genrated by a notebook so all the installation are already done .Moreover , the code is accompaigned with comments explainning the steps and the outputs


**X_analysis**
- **Data Extraction**: Fetch new data from X (Twitter) using the `extractor.py` script.
- **Preprocessing**: Clean and preprocess data using `pretreatment.py`. 
- **Engagement Analysis**: Calculate engagement scores for tweets using `engagement_score.py`.
- **Text Analysis**: Analyze tweet text for sentiment, word frequency using `tweet_text_analysis.py`.
- **Hashtag Analysis**: Identify  popular hashtags using `hashtag_analysis.py`.
- **Tweet Generation**: Generate tweets using AI models with `tweeter_generation.py`.
-**Dashboarding**:create a dashboard with `dashboard.py`

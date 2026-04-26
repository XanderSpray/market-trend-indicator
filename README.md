# market-trend-indicator
Market trend indicator using 21-day SMA and 8/21 EMA crossover to classify bullish and bearish conditions.

Market Trend Indicator (Python)
## Overview

This project implements a simple market trend classification model using technical indicators. It combines trend-following and momentum-based signals to classify market conditions.

Strategy
- **21-day SMA**: Identifies overall trend
- **8/21 EMA crossover**: Captures short-term momentum

## Signal Logic
- **Strong Bull**: Price above SMA + bullish EMA crossover  
- **Weak Bull**: Price above SMA + bearish EMA crossover  
- **Recovery**: Price below SMA + bullish EMA crossover  
- **Bear**: Price below SMA + bearish EMA crossover

## Example Output

Latest Signal: Strong Bull

## How to Run
pip install yfinance pandas matplotlib
python main.py

## Key Takeaways
- Indicators are lagging and react to price changes
- Performance may degrade in sideways markets
- Model prioritizes simplicity and interpretability

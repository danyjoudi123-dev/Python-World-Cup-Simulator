# 2026 FIFA World Cup Simulator

A Python program that simulates the entire 2026 FIFA World Cup from the group stage through to the final.

## Features

* Simulates all 12 FIFA World Cup groups.
* Uses FIFA World Rankings to assign team strength ratings.
* Randomly generates realistic match scores based on team ratings.
* Calculates group standings using:
  * Points
  * Goal Difference
  * Goals Scored
* Automatically determines the teams that advance to the knockout stage.
* Simulates every knockout round until a World Cup champion is crowned.

## Project Structure

```
wc.py          # Tournament logic and match simulation
wc_groups.py   # World Cup groups and team ratings
wc_ko.py       # r32 stage bracket
```

## How It Works

Each nation is assigned a rating derived from its FIFA World Ranking. Higher-rated teams have a greater probability of scoring goals during each simulated match.

Every team plays the other teams in its group once. The program updates the standings after each match and ranks teams by:

1. Points
2. Goal Difference
3. Goals Scored

After the group stage, the qualifiers progress into the knockout bracket, where single-elimination matches determine the eventual World Cup champion.

Because match outcomes are generated randomly, every tournament produces different results.

## Requirements

* Python 3.x

## Running the Simulator

```bash
python3 wc.py
```

## Future Improvements

* More realistic goal probability model
* Penalty shootouts
* Home and away form adjustments
* Interactive menu
* Tournament statistics and records
* Export results to CSV


** NOTE ** 
The following website is entirely AI generated, it is merely used as a web based UI for the simulator 
https://danyjoudi123-dev.github.io/Python-World-Cup-Simulator/ 

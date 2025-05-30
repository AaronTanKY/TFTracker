# 🧠 TFTracker

TFTracker is a personal project designed to explore and analyze **TFT (Teamfight Tactics)** match data using Riot Games' official API. This tool will help identify top-performing strategies among the best players in North America by programmatically tracking game history and trait usage.

## 🎯 Goal (Phase 1)

The goal of this initial phase is to:

1. **Fetch the top 50 Challenger players** from the `NA1` region using `/tft/league/v1/challenger`.
2. **Extract each player’s PUUID**.
3. **For each PUUID**, call `/tft/match/v1/matches/by-puuid/{puuid}/ids` to retrieve their last 20 match IDs.
4. **Fetch full match data** using `/tft/match/v1/matches/{matchId}`.
5. **Filter each match**:
   - If a player placed **1st to 4th**, extract the **traits and units** used in that game.
6. **Aggregate all matches** across the 50 players and compute the **top 3 most frequently used traits** among top-placing matches.

## 📈 Future Plans

- Incorporate players from all different regions
- Integrate LLMs somehow to summarize and make more specifi recommendations for the meta and items, etc.

## 👨‍💻 Author

Aaron Tan  
Mechanical Engineering @ UCLA  
Project inspired by curiosity + TFT addiction 😄

---

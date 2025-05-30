from utils import (
    get_top_players_puuids,
    get_match_ids_for_puuid
)

def main():
    region = input("Enter your region: ")
    puuids = get_top_players_puuids(region)

    i = 1

    for puuid in puuids:
        match_ids = get_match_ids_for_puuid(region, puuid)
        for match_id in match_ids:
            print(f"Match {i}: {match_id}")
            i = i + 1
        pause = input("paused")
        
        
if __name__ == "__main__":
    main()
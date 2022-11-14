# Import data from StatsBomb Open data set via StatsBomb API 
from statsbombpy import sb

def ExG_Goal():
    # Read in data
    # compet = sb.competitions()

    # Choose which competition to analyze; here for example, UEFA Euro 2020
    sb.matches(competition_id=55, season_id=43)

    # Chose which match to analyze; here for example, Final: Italy vs England
    events = sb.events(match_id=3795506)

    # Subset dataframe
    eventsdf = events[['team', 'type', 'minute', 'location', 'shot_end_location', 'shot_outcome', 'shot_statsbomb_xg', 'shot_type', 'player' ]]

    # Subset Shot dataframe
    shotdf = eventsdf.loc[eventsdf['type']=='Shot']

    # Calculate Expected Goal and Actual Goal
    Italy_df = shotdf.loc[shotdf['team']=='Italy']
    Goal_Italy = Italy_df.shot_outcome
    ExG_Italy = Italy_df.shot_statsbomb_xg.sum()
    England_df = shotdf.loc[shotdf['team']=='England']
    Goal_England = England_df.shot_outcome
    ExG_England = England_df.shot_statsbomb_xg.sum()
    Italy_Goal = 0
    England_Goal = 0
    for i in Goal_England:
        if i == 'Goal':
            England_Goal +=1
    for j in Goal_Italy:
        if j == 'Goal':
            Italy_Goal +=1


    return f"Italy's Expected Goal is {ExG_Italy:.2f}, and England's Expected Goal is {ExG_England:.2f}; the final socre is {Italy_Goal} : {England_Goal}"

if __name__ =='__main__':

    print(ExG_Goal())
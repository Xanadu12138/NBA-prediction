from numpy.core.fromnumeric import ptp
from config import * 
import pandas as pd 

# Get Player stats during specific season.

def GetInfoBySeason(season,fileName):
    '''
    [Function Name]    GetInfoBySeason
    [Function]         Filter players' or team selected season stats.
    [Author]           Yucong Dai
    [Paramter]         Season which can be modified in config.
    [Return]           Cleaned dataframe
    '''

    df = pd.read_csv(fileName)
    df = df[df['Season'] == season]
    df = df.reset_index(drop = True)
    return df  

# Group by team, select top player in each team
def GroupByteam(df):
    '''
    [Function Name]    GroupByteam
    [Function]         Generate teams' stats, using top5 players in each team.
    [Author]           Yucong Dai
    [Paramter]         Cleaned season stats dataframe(Type: pd.Dataframe)
    [Return]           teamGroup dataframe
    '''
    teamDf = df.copy(deep = True)
    teamDf = teamDf[0:0]
    
    groups = df.groupby('Tm').groups
    for group in groups:
        cols = list(groups[group])
        currentTeam = df.loc[cols]
        # Select top 5 player in team, sorted by Gs
        currentTeam.sort_values('GS',inplace = True, ascending = False)
        currentTeam = currentTeam[:5]
        teamDf = teamDf.append(currentTeam)

    # Group by team and sum
    teamGroup = teamDf.groupby('Tm').sum()
    teamGroup = teamGroup.drop(['GS', 'G'], axis = 1) 
    return teamGroup
    
# Select stats for predict
def ExtractEssentials(df):
    '''
    [Function Name]    ExtractEssentials
    [Function]         Extract attibute to evaluate a player.
    [Author]           Yucong Dai
    [Paramter]         Players' stats dataframe(Type: pd.dataframe)
    [Return]           
    '''
    df = df.loc[:,selectedAttr]
    # TOV, PF have negative infulence on player's performence
    # hence take its negative values
    df[['TOV', 'PF']] = -df[['TOV', 'PF']]
    return df


# Filter useful stats of schlist
def SelectTeamStats(teamDf):
    '''
    [Function Name]    SelectTeamStats
    [Function]         Filter NBA teams from all teams.
    [Author]           Yucong Dai
    [Paramter]         teamGroup Dataframe(type:pd.dataframe)
    [Return]           Cleaned team result history Dataframe.
    '''
    resultDf = pd.read_csv('data/schlist.csv')
    #print(resultDf.head())


if __name__ == "__main__":
    df= GetInfoBySeason('2018-19','data/playerstats.csv')
    df = ExtractEssentials(df)
    teamDf = GroupByteam(df)
    SelectTeamStats(teamDf)
    
    # Save csv files
    df.to_csv('data/' + season +'cleanedstats.csv')
    teamDf.to_csv('data/' + season + 'teamstats.csv')
    
    

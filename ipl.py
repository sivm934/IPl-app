import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
st.set_page_config(layout='wide',page_title='IPl Analysis')
df=pd.read_csv('ipl-matches.csv')
st.title('🏏Ipl Stats Dashboard Analysis ')
st.subheader("This data will show the result of 2008-22 seasons:")

season=st.sidebar.selectbox('Select Season',sorted(df['Season'].unique(),reverse=True))
team=st.sidebar.selectbox('Select Team',sorted(df['Team1'].unique()))

filtered = df[(df['Season'] == season) & ((df['Team1'] == team) | (df['Team2'] == team))]
st.subheader(f"{team}'s Performance in {season}")
table=filtered[['Date', 'Team1', 'Team2','TossWinner', 'WinningTeam', 'Venue','WonBy']].reset_index(drop=True)
table.index=table.index+1
st.write(table)

#win and lose number
matches_played = len(filtered)
wins = (filtered['WinningTeam'] == team).sum()
losses = matches_played - wins

st.write(f"📊 Matches Played: {matches_played}")
st.write(f"✅ Wins: {wins}")
st.write(f"❌ Losses: {losses}")

#opponent

opponents = filtered.apply(lambda x: x['Team2'] if x['Team1'] == team else x['Team1'], axis=1)
st.write("🏏 Most Common Opponent:", opponents.value_counts().idxmax())


# Match Outcomes
win_count = filtered['WinningTeam'].value_counts()
st.subheader("🏆 Match Wins")
st.bar_chart(win_count)

st.subheader("🎲 Toss Decisions")
toss_decision = filtered['TossWinner'].value_counts()
st.bar_chart(toss_decision)


 #Player of the Match
top_players = filtered['Player_of_Match'].value_counts().head(5)
st.subheader("🌟 Top Players of the Match")
st.table(top_players)

# Win Distribution
st.subheader("📍 Venues with Most Wins")
venue_wins = filtered['Venue'].value_counts().head(5)
st.bar_chart(venue_wins)

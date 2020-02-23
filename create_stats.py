import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(font_scale=1.5)
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "teams_site.settings")
import django
django.setup()
from api.models import Team

def print_stats(team1, team2, nombre, value):
    df = pd.read_csv('players_20.csv')
    team1 = df.loc[df['club'] == team1]
    team2 = df.loc[df['club'] == team2]
    teams = [team1, team2]
    values = ['club', 'overall','pace', 'attacking_finishing', 'dribbling', \
              'value_eur', 'release_clause_eur', 'defending']
    for team in teams:
        team['value_eur'] = team['value_eur'].apply(lambda x: x / 1000000)
        team['release_clause_eur'] = team['release_clause_eur'].apply(lambda x: x / 1000000)
        team = team.loc[team['release_clause_eur'] > 0]
        team = team[values]
    

    merged = pd.concat([team1, team2])

    fig, axes = plt.subplots(1,3, figsize=(20,8))

    ax1 = sns.barplot(x='club', y='pace', data=merged, ax=axes[0], palette=color, alpha=0.9)
    ax1.set(ylabel='Velocidad')
    ax2 = sns.barplot(x='club', y='defending', data=merged, ax=axes[1], palette=color, alpha=0.9)
    ax2.set(ylabel='Defensa')
    sns.barplot(x='club', y='dribbling', data=merged, ax=axes[2],palette=color, alpha=0.9)
    plt.savefig('api/static/' + nombre + '_stats.png')
    
    plt.figure(figsize=(50,19))
    sns.catplot(x='club', y='overall', data=merged, palette=color, linewidth=1.5)
    plt.title('Calidad de jugadores')
    plt.savefig('api/static/' +nombre + '_overall.png')

    plt.figure(figsize=(6,7))
    y = ''
    if value == 'value':
        y = 'value_eur'
    else:
        y = 'release_clause_eur'
    
    ax = sns.catplot(x='club', y=y, data=merged, palette=color, linewidth=1.5)
    ax.set(ylabel='Millones (EUR)')
    plt.title('Valor € del equipo')
    plt.savefig('api/static/' + nombre + '_value.png')

team1, team2 = Team.objects.values_list('name', 'color').values()

color = sns.color_palette([team1['color'], team2['color']])
nombre = str(team1['name']) + '_' + str(team2['name'])
print_stats(team1['name'], team2['name'], nombre, 'value')
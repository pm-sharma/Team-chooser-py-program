from random import choice
players = ['Snik','pm','md','satin','vivaan','vikash','rj','suru']

#file = open('team.txt','r')
#players = file.read().splitlines()

print(players)

teamA = []
teamB = []

while len(players)>0:
    playerA = choice(players)
    teamA.append(playerA)  
    players.remove(playerA)


    playerB = choice(players)
    teamB.append(playerB)
    players.remove(playerB)

file = open("players_team.txt","w+")

file = file.write("Your teams")


print('Team A :' , teamA)

print('Team B :' , teamB)


#with open('players_team','w') as filehandle:
 #   for listitem1 in teamA:
  #      filehandle.write('%s\n' % listitem)

#with open('players_team','w') as filehandle:
 #   for listitem2 in teamB:

  #      filehandle.write('%s\n' % listitem)

for listitem1 in teamA:
    file = open("players_team.txt","a")

    file = file.append(listitem1)


for listitem2 in teamB:
    file = open("players_team.txt","a")

    file = file.append(listitem2)

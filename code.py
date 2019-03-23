# --------------
import yaml

# Read the data of the format .yaml type
with open(path) as file :
    data = yaml.load(file)
# Find data type of the file
type_of_data = type(data)
print('The data type of the file is ' , type_of_data)
# In which city, and at which venue the match was played and where was it played ?
city = data['info']['city']
print('The city where the match was played is', city)

venue = data['info']['venue']
print('The venue where the match was played is ', venue)
# Which are all the teams that played in the tournament ? How many teams participated in total?
Teams = data['info']['teams']
print('The teams that participated were ' + Teams[0], 'and' + ' ' + Teams[1])
print('There are total of ' + str(len(Teams)) + ' teams that played in tournament')
# Which team won the toss and what was the decision of toss winner ?
toss_winner = data['info']['toss']['winner']
print('The team that won the toss was', toss_winner)

toss_decision = data['info']['toss']['decision']
print('The decision of the toss winner was to', toss_decision)
# Find the first bowler and first batsman who played the first ball of the first inning
first_bowler = data['innings'][0]['1st innings']['deliveries'][0][0.1]['bowler']
first_batsman = data['innings'][0]['1st innings']['deliveries'][0][0.1]['batsman']
print('The first bowler was', first_bowler)
print('The first batsman was', first_batsman)
# How many deliveries were delivered in first inning ?
first_innings_deliveries = len(data['innings'][0]['1st innings']['deliveries'])
print('A total of' + ' ' + str(first_innings_deliveries)+ ' ' + 'deliveries delivered in the first innings')
# How many deliveries were delivered in second inning ?
second_innings_deliveries = len(data['innings'][1]['2nd innings']['deliveries'])
print('A total of' + ' ' +str(second_innings_deliveries)+ ' ' + 'deliveries delivered in the second innings')
# Which team won and how ?
match_winner = data['info']['outcome']['winner']
method_of_winning = data['info']['outcome']['by']['runs']

print('The winning team was' +' '+ match_winner +' ' +'by'+ ' ' + str(method_of_winning)+ ' ' +'runs')



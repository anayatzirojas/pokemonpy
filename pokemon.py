import time 
import random 
print()
print ('_' *80)
print ('A wild Jigglypuff!! appears!!')
time.sleep(0.3)
print("The background music chages...")
time.sleep(0.3)
print(" YOU ONLY HAVE ONE POKEMON!")
time.sleep(0.3)
print()
print("I choose you, Clammi!!")
time.sleep(0.3)
print()

#Starting HPs
Clammi_hp = 200
jiggly_hp = 125

print('Orignial HP')
print('- Clammi HP: ' + str(Clammi_hp))
time.sleep(0.3)
print('-Jigglypuff HP: ' + str(jiggly_hp))
time.sleep(0.3)
print()
time.sleep(0.3)

while Clammi_hp > 0 and jiggly_hp > 0:
	print('Battle options:')
	time.sleep(0.3)
	print('- [1] K.O')
	time.sleep(0.3)
	print('- [2] Bodyslam ')
	time.sleep(0.3)
	print('- [3] Super Kick ')
	time.sleep(0.3)
	print('- [4] Crunch')
	time.sleep(0.3)
	print('- [5] Capture')
	time.sleep(0.3)
	print('- [6] Run')
	time.sleep(0.3)
	your_move = input('Chose a move using the corresponding number: ')
	print()

	if your_move == '1':
		Clammi_hp = Clammi_hp + 50
		print('Clammi uses K.O, his HP increases to ' + str(Clammi_hp))
		time.sleep(0.3)
	elif your_move == '2':
		jiggly_hp = jiggly_hp - 10
		print('Clammi uses Bodyslam and deals 10 damage to Jigglypuff')
		time.sleep(0.3)
	elif your_move == '3':
		jiggly_hp = jiggly_hp - 30
		print('Clammi uses Super Kick and deals 30 damage to Jigglypuff')
		time.sleep(0.3)
	elif your_move == '4':
		jiggly_hp = jiggly_hp - 40
		print ('Clammi uses Crunch and deals 40 damage to Jigglypuff')
		time.sleep(0.3)
	elif your_move == '5':
		capture_roll = random.randint(0,125)
		if capture_roll > jiggly_hp:
			print('You have caught Jigglypuff')
			break
		else:
			print('You tried to capture Jigglypuff, but it escaped')
	elif your_move =='6':
		run_away = random.randint(0,200)
		if run_away < snorlax_hp:
			print('You have ran from the battle')
			break
		else:
			print('You tried to run from the battle but failed')
	print()

	#Jigglypuff attacks
	enemy_move = random.randint(1,2)
	enemy_move = str(enemy_move)

	if enemy_move == '1':
		Clammi_hp = Clammi_hp - 30
		jiggly_hp = jiggly_hp + 30
		print('Jigglypuff uses Sing and deals 30 damage while recovering 30 HP')
		time.sleep(0.3)
	elif enemy_move == '2':
		Clammi_hp = Clammi_hp - 50
		print('Jigglypuff uses Body Slam and deals 50 damage')
		time.sleep(0.3)
	print()

	# check for overkill
	if Clammi_hp < 0:
		Clammi_hp = 0 
	if jiggly_hp < 0:
		jiggly_hp = 0
	print('Updated HP')
	print('- Clammi HP: ' + str(Clammi_hp))
	time.sleep(0.3)
	print('-Jigglypuff HP: ' + str(jiggly_hp))
	time.sleep(0.3)
	print()
	time.sleep(0.3)
 


if Clammi_hp == 0:
	print('Clammi has lost the battle the winner is Jigglypuff')
elif jiggly_hp == 0:
	print('Jigglypuff has lost the battle the winner is Clammi')




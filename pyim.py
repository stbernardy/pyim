import sys #imports sys, used to kill the game
import time #used to time the responses

e = "emerly35:" #Making Emerly's username equal e
leftChat = "emerly35 has left the chat." #Default exit message
em = "Emily" #Emily var
end = "GAME OVER." #Variable that ends the game

print ("Your only goal is to get laid, may the odds forever be in your favor.")
time.sleep(3)
print ("Enter in your username: ") #Enter in username here
username = raw_input("> ")

print ("Enter in your first name: ")
name = raw_input ("> ")

print ("{0} has signed in").format(e) #Emily has signed in
time.sleep(2) #Delays chat for 2 seconds

print ("{0} {1}! hey!").format(e, name)

print (" 1. Whats up?\n 2. whatcha doin?\n 3. hows it shaking?")
response = raw_input("> ") #1st response from you

if response == "1":
	print("{0} Whats up?").format(username)
	time.sleep(2)
	print ("{0} i'm just doing some homework and listening to music, you?").format(e)
elif response == "2":
	print ("{0} whatcha doooiin").format(username)
	time.sleep(2)
	print ("{0} i'm just doing some homework and listening to music, you?").format(e)
elif response == "3":
	print ("{0} hows dat ass shakin girl? haaa").format(username)
	time.sleep(2)
	print ("{0} haha, it's shaking i guess?").format(e)
	time.sleep(2)
	print ("{0} i'm just doing some homework and listening to music, you?").format(e)

else:
	print end
	sys.exit()

#---------------------------------------------------------------------------------------Next portion

print (" 1. homework too\n 2. just chilling\n 3. video games")
response1 = raw_input("> ")

if response1 == "1":
	print ("{0}im doing homework and slabbin my meat").format(username)
	time.sleep(1)
	print ("{0} that sucks, well you trying to come over?").format(e)

elif response1 == "2":
	print ("{0} just chillin, you know tryin to get some of dat A1 head").format(username)
	time.sleep(1.5)
	print ("{0} just chillin huh? Well maybe you should quit being a cuck and come over...").format(e)

elif response1 == "3":
	print ("{0}just playin video games").format(username)
	time.sleep(2)
	print ("{0} well maybe you should go outside?").format(e)
	outsideResponse = raw_input("> ")

	if outsideResponse == "fuck off" or "sorry" or "excuse me?" or "excuse me" or "what?" or "what": #Aggressive responses
		print ("{0} hey I have to go... bye lol").format(e)
		print ("{0}").format(leftChat)
		print end
		sys.exit()

	elif outsideResponse == "ok" or "okay" or "Ok" or "Okay" or "k" or "K" or "k." or "K.": #Passive aggressive responses
		print ("{0} Thanks.").format(e)
		print ("{0}").format(leftChat)
		print end
		sys.exit()

	else:
		print end
		sys.exit()
else:
	print end
	sys.exit()

#------------------------------------------------------------------------------------------------------------Next section

print (" 1. Yeah maybe I should come over and freak yah?\n 2. i'm actually against sex, but thanks anyways,\n 3. what are you saying?")
response3 = raw_input("> ") 

if response3 == "1":
	print("{0} yeah, maybe I should come over and freak yah?").format(user_name)
	time.sleep(1)
	print ("{0} ummmmmm what? is that a sex joke? I do not commit sex, goodbye {1}.").format(e, name)
	time.sleep(0.5)
	print end
	sys.exit()
	print ("1. So should I come over and shmang?\n 2. I actually just showered\n 3. what's your sister doing?")
	response31 = raw_input ("> ")

	if response31 == "1":
		print ("{0} ").format(username)
		print ("{0}").format(leftChat)
		print end
		sys.exit()

	elif response31 == "2":
		print ("{0}Well that's cool, haha").format(e)
		print ("1. Yeah it is, my nuts feel great!\n 2. Yeah lol\n 3. We should shower together.")
		response311 = raw_input("> ")

		if response311 == "1": #response311 and 312 are just versions that fall under response3
			print ("{0} that's disgusting, bye.").format(e)
			print ("{0}").format(leftChat)
			print end
			sys.exit()
		elif response311 == "2":
			print ("{0} Yeah...... well I have to go feed my fish, so i'll ttyl.").format(e)
			print ("{0}").format(leftChat)
			print end
			sys.exit()
		elif response311 == "3":
			print ("{0} Haaa what? Maybe some other time, I have to go feed my grandma... see ya....lol").format(e)
			print ("{0}").format(leftChat)
			print end
			sys.exit()
		else:
			print ("Yah done fucked this game up cuh, aborted.")
			sys.exit()

	elif response31 == "3":
		print ("{0} i'm not sure.... why?").format(e)
		print ("1. I'm just curious haa\n 2. I want to slip my jimmy in her trousers\n 3. three way haaa, wyd.")
		response312 = raw_input ("> ")

	if response312 == "1":
		print ("{0} okay, that's kind of weird... maybe you should talk to her... ttyl.").format(e)
		print ("{0}").format(leftChat)
		print end
		sys.exit()

	elif response312 == "2":
		print ("{0} she actually told me she was DTF, her number is 253-468-8391... give her a ring, she's HORNY NOW!").format(e)
		print ("1. you're damn right im gonna call dat booty\n 2. i was kidding, i dont sex people\n 3. does her snatch have an odor?")
		response3121 = raw_input("> ")

		if response3121 == "1":
			print ("{0} i'll let you two be ;) have fun!").format(e)
			print ("{1}").format(leftChat)
			print end
			sys.exit()
		elif response3121 == "2":
			print ("{0} HA, LOL you fucking little virgin, why are you even talking to me? KTHXBAI.").format(e)
			print ("{0} {1}").format(leftChat)

		elif response3121 == "3":
			print ("{0} why yes, it did have a unique musk come out of it earlier, but pussy is pussy, right?").format(e)
			print ("1. sure\n 2. no, not at all\n 3. she goan get dis dick today by moonrise!")
			pussy = raw_input("> ")

			if pussy =="1":
				print ("{0} lol").format(e)
				print ("{1}").format(leftChat)
				print end
				sys.exit()
			elif pussy =="2":
				print ("{0} well you had your chance cowboy, she's already smashing another man and im tired, night").format(e)
				print ("{0}").format(leftChat)
				print end
				sys.exit()
			elif pussy =="3":
				print ("{0} lovely, i'm sure she's all primed up... just come over for christs sake").format(e)
				print ("{0}").format(leftChat)
				print end
				sys.exit()
			else:
				print ("You broke the game, start over")
				sys.exit()


elif response3 == "2":
	print ("{0} im actually against intercourse, but thanks for the offer...").format(username)
	time.sleep(2)
	print ("{0} Are you serious?").format(e)
	yesOrNo = raw_input("> ")
	
	if yesOrNo == "No" or "what do you think?" or "nah" or "not at all" :
		time.sleep(2)
		print ("{0} Quit fucking around, I'll talk to you tomorrow.").format(e)
		print ("{0}").format(leftChat)
		print end
		sys.quit()

	elif yesOrNo == "Yes" or "yes" or "yah" or "sort of" or "kind of":
		time.slee(2)
		print ("{0} Well damn, arlighty then lol.... well I got to get goin, I have another man i can hit up").format(e)
		print ("{0} has left the chat.").format(e)

	else:
		print ("You have broken the game, this game is now null")
		sys.exit()


elif response3 == "3":
	print ("{0} you know.... ;)").format(e)
	print ("1. no i dont know you cunt\n 2. what? and do what?\n 3. so we fuckin?")
	fuckin = raw_input("> ")

	if fuckin == "1":
		print ("{0} well that was kind of rude... kind of kinky, but i'll hit you up some other time, bye").format(e)
		print ("{0}").format(leftChat)
		print end
		sys.exit()
	elif fuckin == "2":
		print ("{0} have sex you dingleberry").format(e)
		print ("1. i'll pass, i dont partake in \"sex\"\n 2. sorry, i have limp dick and can't smang\n 3. like, right now?")	
		fuckin1 = raw_input("> ")

		if fuckin1 == "1":
			print ("{0} im sorry, i dont partake in \"sex\"").format(username)
			time.sleep(2)
			print ("{0} hah you're kidding right?").format(e)
			print ("1. no i'm not, can you stop offending me?\n 2. yes i am, lemme butter dem cakes haaaaa\n 3. im a virgin, leave me alone.")
			fuckin11 = raw_input("> ")

			if fuckin11 == "1":
				print("{0} no i'm not, can you stop offending me you bigot?").format(e)
				time.sleep(2)
				print ("{0} ahhhh i'm sorry, I didn't know you were a little bitch {1}, makes sense though, toodles").format(e, name)
				time.sleep(1)
				print ("{0}").format(leftChat)
				sys.exit()
			elif fuckin11 == "2":
				print ("{0} yes i am, lemme butter dem cakes haaaaaaaa").format(username)
				time.sleep(2)
				print ("{0} oh {1}, come over right this instant, i have a lot of cakes to butter ;)").format(e, name)

				print ("1. what's your addy?\n 2. are you parents home?\n 3. can i sleep with your sister instead?")
				addy = raw_input("> ")

				if addy == "1":
					print ("{0} whats your addy, imma finna slide through..").format(username)
					time.sleep(3)
					print ("{0} its 104 S Jameson St.... OMG im so wet!!").format(e)
					time.sleep(1)
					print ("{0} ill see you when you get here ;).. im getting off").format(e)
					time.sleep(0.5)
					print ("{0} im actually kind of embarresed rn...").format(e)
					print ("1. how so?\n 2. yew shit your britches?\n 3. please ellaborate..")

					britches = raw_input("> ")

					if britches == "1":
						print ("{0} how so?").format(username)
						time.sleep(1)
						print ("{0} well i was really excited for you to come over, and well... I just peed all over my bed..").format(e)
						print ("1. that's fucking disgusting\n 2. little moisture wont hurt\n 3. you can come over here ;)")
						wet = raw_input("> ")

						if wet == "1":
							print ("{0} thats fucking disgusting... wtf").format(username)
							time.sleep(4)
							print ("{0} i know... i know... im so sorry.... i have to get going....").format(e)
							time.sleep(0.5)
							print end
							sys.exit()

						elif wet == "2":
							print ("{0} little moisture wont hurt heh ;)").format(username)
							time.sleep(1)
							print ("{0} i dont think you understand how nasty you sound right now...").format(e)
							print ("1. the fuck you mean?? you just pissed yourelf\n 2. thats how the world turns babe haaaa\n 3. well i can find someone else.")
							wet = raw_input("> ") #----------------------------------------------------------------------------------------------------- testing sharing variable wet

							if wet == "1":
								print ("{0} the fuck you mean? you literally just pissed yourself you fucking spineless swine").format(username)
								time.sleep(1)
								print ("{0} ")


					print ("{0}").format(leftChat)
					sys.exit()

				elif addy == "2":
					print ("{0} are you parents home??").format(username)
					time.sleep(2)
					print ("{0} yeah, why?").format(e)
					print ("1. well I dont want to come over if they are\n 2. promise youll be quiet?\n 3. if you're loud, im jamming my sock in your throat.")
					loud = raw_input("> ")

					if loud == "1":
						print ("{0} well, i dont think i should come over if they are home..").format(username)
						time.sleep(3)
						print ("{0} i understand, maybe you can CUM over when they arent home... haha you get it?").format(e)
						print ("1. no i dont get it \n 2. shut up\n 3. that was a terrible pun and you should feel terrible")
						pun = raw_input("> ")

						if pun == "1":
							print ("{0} i dont get it").format(username)
							time.sleep(3)
							print ("{0} nevermind.... have a good night {1}.").format(e, name)
							time.sleep(1)
							print ("{0}").format(leftChat)
							sys.exit()

						elif pun == "2":
							print ("{0} shut up").format(username)
							time.sleep(4)
							print ("{0} you are such an asshole, why do I even bother talking to you?? grow up {1}, sleep well.").format(e, name)
							time.sleep(0.5)
							print ("{0}").format(leftChat)
							sys.exit()

						elif pun == "3":
							print ("{0} that was a terrible pun and you should feel terrible.").format(username)
							time.sleep(2)
							print ("{0} well thanks asshole, i do feel terrible now. anyways, ill see you tomorrow. night").format(e)
							time.sleep(1)
							print ("{0}").format(leftChat)
							sys.exit() #Completed

				elif addy == "3":
					print ("{0} can i sleep wth your sister instead?").format(username)
					time.sleep(3)
					print ("{0} WHAT??? Im sure she wouldnt mind it... let me ask").format(e)
					time.sleep(8)
					print ("{0} she said no, im sorry..").format(e)
					print ("1. well what's her aim?\n 2. is she just not DTF?\n 3. well i dont even want to come over now")

					dtf = raw_input("> ")

					if dtf == "1":
						print ("{0} well what's her aim handle?").format(username)
						time.sleep(2)
						print ("{0} Im not giving it to you, you're acting weird, ill see you tomorrow {1}.").format(e, name)
						time.sleep(1)
						print ("{0}").format(leftChat)
						sys.exit()

					elif dtf == "2":
						print ("{0} is she just not down to get her shit mixed?").format(username)
						time.sleep(2)
						print ("{0} excuse me??").format(e)
						print ("1. you heard me bitch\n 2. IS.SHE.JUST.NOT.DOWN.TO.GET.HER.SHIT.MIXED.\n 3. nevermind")
						shitMixed = raw_input("> ")

						if shitMixed == "1":
							print ("{0} you heard me bitch").format(username)
							time.sleep(1)
							print ("{0}").format(leftChat)
							sys.exit()

						elif shitMixed == "2":
							print ("{0} IS.SHE.JUST.NOT.DOWN.TO.GET.HER.SHIT.MIXED.").format(username)
							time.sleep(3)
							print ("{0} {1} are you serious right now??? maybe not tonight, but I really want some sleep, night!").format(e, name)
							print ("{0}").format(leftChat)
							sys.exit()

						elif shitMixed == "3":
							print ("{0} nevermind, youre being weird... night").format(username)
							print ("{0} WAIT, {1} I have somethi..")
							sys.exit()

						else:
							print ("You broke the game, restart.")
							sys.exit()

					elif dtf == "3":
						print ("{0} well, i dont even want to come over now.").format(username)
						time.sleep(2)
						print ("{0} thats your loss buddy, im about to go to bed, so... night {1}").format(e, name)
						print ("{0} {1}").format(e, name)
						sys.exit()

					else:
						print ("You have reached the pits of this game, you are now terminated and have to start all over.")
						sys.exit()

			elif fuckin11 == "3":
				print ("{0} im a virgin, can you please leave me alone.").format(username)
				time.sleep(3)
				print ("{0} no... i want you inside me.").format(e)
				print ("1. i told you to leave me alone\n 2. you know what, im gonna come over\n 3. you sure?")
				fuckin111 = raw_input("> ")

				if fuckin111 == "1":()

				elif fuckin111 == "2":
					print ("{0} you know what, i think i might come over and shag for a little bit").format(username)
					time.sleep(2)
					print ("{0} ehhhh, I mean... im pretty tired, i have to take an HIV test in the morning").format(e)
					print ("1. fuck it, i want some pussy \n 2. oh, you have HIV?\n 3. wowwww, way to make this conversation awkward")
					hiv = raw_input("> ")

					if hiv == "1":
						print ("{0} you know what {1}, fuck it... I need me some poonanny").format(e, Emily)
						time.sleep(2)
						print ("{0} so my clit hole is all you want from me?")
						print ("1. yes of course?\n 2. duhhh")
						duh = raw_input("> ")

						if duh == "1" or "2":
							print ("{0} Of course bby, i luh you.").format(username)
							time.sleep(2)
							print ("{0} you are disgusting fucking pig, I have AIDS you nasty fuck. Have a good night {1}.").format(e, name)
							print ("{0}").format(leftChat)
							sys.exit()

				elif fuckin111 == "3":
					print ("{0} you sure?? i can make this happen right this instant").format(username)
					time.sleep(2)
					print ("{0} actually, maybe some other time, im really tired... im sorry").format(e)
					print ("1. #wastehistime2016\n 2. haha its fine, ill ttyl\n 3. thats fine, i have other women i can hit up")
					ttyl = raw_input("> ")

					if ttyl == "1":
						print ("{0} #wastehistime2016").format(username)
						time.sleep(2)
						print ("{0} what does that mean, {1}").format(e, name)
						meaning = raw_input(">")

						print ("{0} you know what, im sick of your shit {1}, im going to bed. goodnight.").format(e, name)
						print ("{0}").format(leftChat)
						time.sleep(0.5)
						sys.quit()

					elif ttyl == "2":
						print("{0} its fine, ill text you tomorrow").format(username)
						time.sleep(1)
						print ("{0} okay!").format(e)
						print ("{0}").format(leftChat)
						print end
						sys.quit()

	elif fuckin == "3":
		print ("{0} so we fuckin or nah?").format(username)
		time.sleep(3)
		print ("{0} possibly, im on my period, so it's kind of risky...").format(e)
		print ("1. okay, well i can put a condom on\n 2. yeah lets not risk it\n 3. my pull out game is strong ;)")
		pullOut = raw_input("> ")

		if pullOut == "1":
			print ("{0} well i have plent of condoms to put on, i'll let you pick one out :)").format(username)
			time.sleep(2)
			print ("{0} awwww that's awfully sweet of you, i'm actually about to go to bed, have a good night {1}!").format(username, name)
			print ("{0}").format(leftChat)
			sys.exit()

		elif pullOut == "2":
			print ("{0} yeah i think it's best if we not risk any pregnancies, my mom would kill me").format(username)
			time.sleep(2)
			print ("{0} yeah, you're one smart pup {1}, let's just wait to sex when im done perioding... i have to get some sleep, night {1}!").format(e, name)
			print ("{0}").format(leftChat)
			sys.exit()

		elif pullOut == "3":
			print("{0} aye baby girl, my pull out game is strong AF, i think i can handle this").format(username)
			time.sleep(3)
			print ("{0} you sure? i dont want to get pregnant... you know this is serious stuff {1}").format(e, name)
			print ("1. quit being a cunt and let me muzzle your snuff\n 2. WE WILL BE FINE\n 3. goodbye.")
			pullOut1 = raw_input("> ")

			if pullOut1 == "1":
				print ("{0} quit being a cunt, let me muzzle your snuff").format(username)
				time.sleep(3)
				print ("{0}").format(leftChat)
				sys.exit()

			elif pullOut1 == "2":
				print ("{0} WE WILL BE FINE.").format(username)
				time.sleep(2)
				print ("{0} ehhhh, alright! come on over").format(e)

				print ("{0}").format(leftChat)
				sys.exit()

			elif pullOut1 == "3":
				print ("{0} you know what, you're being a cunt. goodbye.").format(username)
				print end
				sys.exit()

			else:
				print ("You have reached yet again, another stopping point.... please try again.")
				sys.exit()

	else:
		print ("You dimwit, you broke the game. You have you are being kicked back.")
		sys.exit()

else:
	print ("Start over.")
	sys.exit()

#-------------------------------------------------------------------------------------------------------------------------------------










































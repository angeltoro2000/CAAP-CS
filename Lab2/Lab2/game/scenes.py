# imports random madule form library
from random import randint


# the base class for the scenes. 
# Each scene has one variable name, and three functions: enter(), action(), and exit_scene(). 
# Read through the ones given, feel free to add more using the same template I've given you.
# Change, edit, or completely remove the scenes I gave you. Up to you.
class Scene(object):

	def enter(self):
		print ("This is the base scene class that's inherited by the other scenes, so it is not configured yet.")
		print ("Subclass it and implement enter(), action(), and exit_scene() for each scene.")
		exit(1)

class oweek(Scene):

	name='oweek-scene'

	def enter(self):
		print("It's 2018 and you are a freshman at the University of Chicago.\n You will be faced with decisions throughout this first quarter, some of them will harm you and others will benefit you. ")
		print("If you make 5 wrong decisions your gpa will go lower than what is required for you to remain in the uniiversity and will be forced to drop out.")
		return self.action()

	def action(self):
		print("It's O-week and your friend invited to a party.")
		choice=int(input("1. Do you go to the party? \n 2. Do you decide to not go and tell him you rather stay home"))

		if choice ==':q':
			return self.exit_scene(choice)
		try:
			choice=int(choice)
		except ValueError:
			print("That's not a valid option, only ints allowed.")
			return self.exit_scene(self.name)

		if choice==1:
			print("You go to the party, and your friend and you create a stronger bond.")
		elif choice==2:
			print("Your decision to not go out with your friend harmed your relationship")
			print("You ask him for help in a homework another time and he says he rather do something else")
			return self.exit_scene('death')

		def exit_scene(self,outcome):

			return outcome

class studyingspace(Scene):
	
	name ='study space'

	def enter(self):
		print ("You procastinated and now only have one day to write your hum paper.  ")

		return self.action()

		
		
	def action(self):
		choice=int(input("1. stay in your house lounge despite all the distractions. \n 2. Go to the reg and finish your paper and then go hang out with your friends in the house lounge."))
		if choice==1:
			print("You were distracted by all your friends in the lounge and ended up submitting your paper 5 hours late.")
			print("Being with your friends is not always the right decision")
			return self.exit_scene('death')

		elif choice==2:
			print("You finished your paper and sill had enough time to hang out with your friends afterwards.")


		if choice == ':q':
			return self.exit_scene(choice)

		try:
		   choice = int(choice)
		except ValueError:
		   print("That's not an int!")
		   return self.exit_scene(self.name)
		def exit_scene(self,outcome):
			return outcome

class compsci(Scene):

	name = 'compsci-scene'

	def enter(self):
		print("You have a group project with other classmates for computer science. The way it will be graded is you will all write a game but only one will be graded.")
		return self.action()

	def action(self):
		choice = int(input("1. Do you make sure your code is perfect \n 2. Do you make sure that you and all your teammates know what they are doing and can submit a functional code?"))


		try:
			choice = int(choice)

		except ValueError:
			print("That's not a valid option, only ints allowed.")
			return self.exit_scene(self.name)

		if choice == 1:
			print("You had a perfect code, but yours was not the one graded. \n Instead your teammates was the one graded and he didn't do anything.")
		elif choice == 2:
			print("All of your team submitted a code that worked, and although, yours wasn't graded you still got an A because you helped your teammates. ")
			print("You ask him for help in a homework another time and he says he rather do something else")

			return self.exit_scene('death')

		def exit_scene(self, outcome):
				return outcome

class food(Scene):

	name='food-scene'

	def enter(self):
		print("You have a midterm at 4:00 pm. You feel hungry but are not sure whether you should get lunch or wait until after the midterm to eat.")
		return self.action()

	def action(self):
		choice=int(input("1. Get food \n 2. Stay studying and eat later."))

		try:
			choice=int(choice)
		except ValueError:
			print("That's not a valid option, only ints allowed.")
			return self.exit_scene(self.name)

		if choice==1:
			print("You got food and where well rested for you midterms, your grade was a solid A-")
		elif choice==2:
			print("You stayed studying but passed out at around 3 from hunger. You coudn't make the test and failed a test that you knew the material for.")

			return self.exit_scene('death')

	def exit_scene(self, outcome):
			return outcome

class finals(Scene):
	name='final-scene'

	def enter(self):
		print("You are finally done with your first semester of college, just one more challenge before you can get back home for the break.")
		if __name__ == '__main__':
			return self.action()
	def action(self):
		print("You receive the opportunity to work on a really good internship but it would require a 40 hour commitment from you starting the week before finals.")
		choice=int(input("Do you take it? \n 1. Yes. \n 2. No"))

		try:
			choice=int(choice)
		except ValueError:
			("That's not a valid option. Only ints allowed.")
			return self.exit_scene(self.name)

		if choice==1:
			print("Congrats you have a new internship but due to the time you were spending there instead of studying for finals, you failed a class")
			return self.exit_scene('death')

		elif choice==2:
			print("Although, you don't have the internship this mature decision allowed you to excel on your classes and ace your finals.")

		def exit_scene(self, outcome):
			return outcome

class Lifter: 
	
	def __init__(self,name_,body_weight="N/A"): #Initalizes the lifter, with a name, and a bodyweight defaulted to N/A. 
		self.name_ = name_
		self.body_weight = body_weight
		self.lifts = {} #Lifter stats, Lift name, Weight, Reps, with the name and bodyweight of the lifter.
		self.lifts_list_data = [] #No identifying info, just lifter stats.
		self.best_lift = None #Initalize the best lift as None.
		self.best_max = 0 # Best one-rep max used to determine best lift.
		self.normalized_best_max = 0

	def calculate_one_rep_max(self,weight,reps):
		one_rep_max = weight / (1.0278 - 0.0278 * reps) #Calculates one rep max for the lifter.
		return int(one_rep_max) 
	
	def calculate_best_lift(self):

		normalization_ratios = {
			'bench': 1,
			'squat': 1.25,
			'deadlift': 1.5
		} 
						  
		best_lift_local = None
		best_max_local = 0 
		normalized_best_max_local = 0 				  
 

		for lift_name,(weight_,reps_,max_) in self.lifts.items():
			normalized_max = max_ / normalization_ratios.get(lift_name, 1) 
			
			if normalized_max > normalized_best_max_local:
				normalized_best_max_local = normalized_max
				best_max_local = max_ 
				best_lift_local = lift_name

			self.best_lift = best_lift_local
			self.best_max = best_max_local
			
				

	#Adds lift stats to both lists.
	def add_lift(self,lift_name,weight,reps): 
		lifter_one_rep_max = self.calculate_one_rep_max(weight,reps) 
		self.lifts[lift_name] = weight,reps,int(lifter_one_rep_max) 
		#Adds just the numbers to a list used for saving data. 
		self.lifts_list_data.append(lift_name) 
		self.lifts_list_data.append(weight)
		self.lifts_list_data.append(reps)
		self.lifts_list_data.append(int(lifter_one_rep_max))

	def get_lifter_info(self): 
		self.calculate_best_lift()  

		if self.body_weight == "N/A":
			lifters_info = f"\n\nName - {self.name_}\nWeight - {self.body_weight}\n" 
		else:
			lifters_info = f"\n\nName - {self.name_}\nWeight - {self.body_weight} \n" 
		for lift_name,(weight,reps,lift_max) in self.lifts.items(): 
			lifters_info += f"\n{lift_name}: {weight} for {reps} reps\nCalculated 1RM: {lift_max}\n\n"
		
		lifters_info += f"\nBest lift: {self.best_lift} with an Estimated 1RM of {self.best_max}\n\n" 
		return lifters_info 
	
	def __str__(self): #Prints the lifters info.
		 return self.get_lifter_info()
	
	
def load_database():
#program will load the text file, validate the user input, split the items into lists to be used later in the program  
	counter=True
	while counter==True:
		file_name=input("Please enter a filename to load : ")
		try:
			movie_data=open(file_name,"r")
		except:
			print("File not found...Please try again")
			continue
		else:
			movie_list = movie_data.readlines()
			for i in range(len(movie_list)):
				movie_list[i]=movie_list[i].split("\t")
				for j in range(len(movie_list[i])):
					movie_list[i][j]=movie_list[i][j].rstrip("\n")	
			counter=False
#close the file 
	movie_data.close()		
	return movie_list
			
movie_list=[]
#prints all titles in dictionary
def print_all_titles():
	all_titles={}
	for i in range(len(movie_list[0])):
		if movie_list[0][i]!="user":
			all_titles[movie_list[0][i]]=1
	print()
	for item in all_titles:
		if item.lower()!="user":
			print(item)
	print()
#prints the average rating for a specific user entered title
def print_rating(title):
	movie_ratings=[]
	average_score=0
	master_index=0
	for i in movie_list[0]:
		if i.upper()==title.upper():
			master_index=(movie_list[0].index(title))
		else:
			continue
	for j in range(1,len(movie_list)):
		if movie_list[j][master_index]!="0" and movie_list[j][master_index]!=title.title():
			movie_ratings.append(int(movie_list[j][master_index]))
	
	average_score=float(compute_average_rating(movie_ratings))
		
	print("Movie:",format(title,"<20"),"Rating:",format(average_score),sep="\t")
	return movie_ratings
		
#computes average for a list of data			
def compute_average_rating(movie_ratings):
	average_score=0
	for score in (movie_ratings):
		average_score+=int(score)

	average_score=format(average_score/len(movie_ratings),".2f")
	return average_score
def print_ratings():
	for title in movie_list[0]:
		if title!="User":
			print_rating(title)
def add_new_rating():
	flag=1
	new_rating_list=[]
	new_rating_list.append(len(movie_list))
	while flag==1:	
		for i in movie_list[0]:
			if i.lower()!="user":
				print("Enter rating for",i,": ", end="")
				new_rating=input()
				if new_rating.isdigit():
					new_rating=eval(new_rating)
					if new_rating is type(float):
						print("Invalid score!")
						continue
					elif new_rating>=0 and new_rating<=5:
						new_rating_list.append(str(new_rating))
					else:
						print("Invalid entry! Try again")
						continue
		flag+=1
	
	return new_rating_list
					
def remove_rating():
	del_flag=0
	del_user=None
	
	while del_flag==0:
		user_id=input("Please enter user id: ")
		print("user id",user_id)
		if user_id.isdigit()==False:
			print("User not found!")
			continue
		for a in range(1,len(movie_list)):
			if int(movie_list[a][0])==int(user_id):
				del_user=a
				del_flag+=1
			
		if del_flag==0:
			print("User not found!")
			continue
	
	del movie_list[del_user]
	print("User sucessfully deleted!")

				
def terminate_app():
	movie_data=open("updated_ratings.txt","w")
	
	for i in range(len(movie_list)):
		for j in movie_list[i]:
			movie_data.write(str(j)+"\t")
		movie_data.write("\n")
	movie_data.close()
	print("Database updated!","Thank you for using our app, goodbye!",sep="\n")
def main():
#validate user input and ensure the selection is an option from the list
	global movie_list
	movie_list=load_database()
	counter=1
	while counter==1:
		print("Choose one of the following options :","1. Display all contender movie titles","2. Display the average rating for a specific movie","3. Display average rating for all movie titles","4. Add a new user and their ratings into database","5. Remove a user from database (based on user_id)","6. Quit", sep="\n")
		sel=input("Enter your choice from the menu :")
		try:
			sel=eval(sel)
		except ValueError:
			print("Unable to convert to integer!")
			continue
		except NameError:
			print("Unable to convert to integer!")
			continue
		except:
			print("Unknown error occured..")
			continue
		else:
			if sel>6 or sel<1:
				print("Hmm that number is out of range! Try again")	
			elif sel==1:
				print_all_titles()
			elif sel==2:
				title=input("Enter the film name :")
				if title.isdigit():
					print("Hmm please enter a title")
					continue
				else:
					print_rating(title.title())
			elif sel==3:
				print_ratings()	
			elif sel==4:
				new_r=add_new_rating()
				movie_list.append(new_r)
				print(movie_list)				  
			elif sel==5:
				remove_rating()
			elif sel==6:
				terminate_app()	
				counter+=1
main()

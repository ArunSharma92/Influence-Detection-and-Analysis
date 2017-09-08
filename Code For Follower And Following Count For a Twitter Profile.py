import unicodedata
import json
import tweepy

auth = tweepy.OAuthHandler('1DpXmbdT3n1gTMekQ0NzXXXXX', 'ihfeWTdSV3YNjqymWwciuqS4bcwT6JdSVWG5wwS3dabKyXXXXX')
auth.set_access_token('4390387221-sPVsyBQhXkstTGyZKMnSJjUufMOTDIZ6qlXXXXX', 'PsPlJFEPqOuQynQrlh1DZigwLwn45uFi9ddNmzSDXXXXX')

api = tweepy.API(auth)

l = ["@User_Name", "@User_Name1", "@User_Name2", "@User_Name3", "@User_Name4", "@User_Name5"]
m = ["@User_Name6", "@User_Name7", "@User_Name8", "@User_Name9", "@User_Name10"]


file = open('follows_1.txt','w')
t_followers=0
t_following=0

for u in l:
	get_user = api.get_user(screen_name=u)
	print get_user.screen_name
	file.write(str(get_user.screen_name)+"\n")
	print get_user.followers_count
	file.write(str(get_user.followers_count)+"\n")
	print get_user.friends_count
	file.write(str(get_user.friends_count)+"\n\n")
	t_followers = t_followers + get_user.followers_count
	t_following = t_following + get_user.friends_count
	
file.write("Total number of followers: "+str(t_followers))
file.write("Total number of following: "+str(t_following))
	
file = open('follows_2.txt','w')
t_followers=0
t_following=0

for u in m:
	get_user = api.get_user(screen_name=u)
	print get_user.screen_name
	file.write(str(get_user.screen_name)+"\n")
	print get_user.followers_count
	file.write(str(get_user.followers_count)+"\n")
	print get_user.friends_count
	file.write(str(get_user.friends_count)+"\n\n")
	t_followers = t_followers + get_user.followers_count
	t_following = t_following + get_user.friends_count
	
file.write("Total number of followers: "+str(t_followers))
file.write("Total number of following: "+str(t_following))

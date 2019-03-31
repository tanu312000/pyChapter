
chars = 256

def findSubString(self,str, pat):

	 len1 = len(str)
	 len2 = len(pat)

	# check if string's length is less than pattern's
	# length. If yes then no such window can exist
	 if (len1 < len2):
         print("No such window exists")


         hash_str = {0}*chars
         hash_pat = {0}*chars


	#store occurrence ofs characters of pattern
	     for i in range(0,len2):
             hash_pat[pat[i]]
             pat[i]=pat[i]+1

	     start = 0
         start_index = -1
         min_len = MAX

	     # start traversing the string
	     count = 0 #count of characters
	     for j in range(0,len1):
             hash_str[str[j]]
             str[j]=str[j]+1


		#If string's char matches with pattern's char
		#then increment count
		     if (hash_pat[str[j]] != 0 and hash_str[str[j]] <= hash_pat[str[j]] ):
                 count=count+1

		#if all the characters are matched
		     if (count == len2):
                 while ( hash_str[str[start]] > hash_pat[str[start]] or hash_pat[str[start]] == 0):
                     if (hash_str[str[start]] > hash_pat[str[start]]):
                         hash_str[str[start]]
                         str[start]=str[start]-1
				 start=start+1


			#update window size
			 len_window = j - start + 1
			 if (min_len > len_window):
                 min_len = len_window
				 start_index = start


	# If no window found
	if (start_index == -1):
        print("No such window exists")



	#Return substring starting from start_index
	# and length min_len
     return(self.findSubString(start_index, min_len))



str = "this is a test string"
pat = "tist"
print(findSubString("Smallest window is :",str, pat)


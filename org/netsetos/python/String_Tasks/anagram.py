def anagram(s1,s2):

    if (''.join(sorted(s1)) == ''.join(sorted(s2))):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")


anagram("angel","glean")
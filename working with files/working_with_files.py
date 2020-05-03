def main():
    #get the number of videos
    video_number=int(input("enter the number of videos"))
    #open output file-video.txt
    video_files=open("video.txt","w")
    #for loop to enter running time
    for count in range(1,video_number+1):
        #get running time for each video
        running_time=float(input("enter running time for video #"+str(count)+":"))
        #write the running time to video.txt file
        video_files.write(str(running_time)+"\n")
    #close file
    video_files.close()
    print("the running times have been saved to video.txt")
main()


#Crop photos
import PIL.Image
import os
import numpy as np

file_path=''

def setPath():
	print('setPath function')
	os.chdir("processed")
	cwd=os.getcwd()
	print(cwd)
	file_path = cwd
	return file_path

def crop(image_path, coords, saved_location):
	image_obj=PIL.Image.open(image_path)
	cropped_image=image_obj.crop(coords)
	cropped_image.save(saved_location)
	#cropped_image.show()

def cropPhotos(file_path):
	print('cropPhotos function')
	folder = file_path
	print(file_path)
	images = sorted(os.listdir(folder))

	image_array=[]
	cntr=0
	for image in images:
		cntr+=1
		im = PIL.Image.open(folder+'\\'+image)
		image_array.append(np.asarray(im))
		image_out=str(cntr)+"_"+str(image)
		crop(image,(7,600,850,1500), image_out)

	image_array=np.array(image_array)
	#print(image_array.shape)
	#img=os.path.join(file_path,images[1])
	#crop(img,(7,600,850,1500), 'Publix1_cropped.jpg')


def main():
	print('main function')
	file_path=setPath()
	#print(file_path)
	cropPhotos(file_path)
	os.chdir("..")

main()
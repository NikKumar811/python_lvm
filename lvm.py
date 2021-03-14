import subprocess as sp


while True:
					
					print("""
1. To create Physical Volume
2. To display Physical Volume
3. To create Volume Group
4. To display volume group
5. To create logical volume 
6. To display logical volume
7. To extend the logical volume
8. To reduce the logical volume
9. Exit
					""")
					print("\n")
            # Take Input that what operation user would like to perform
					ch=int(input("Enter your choice => "))
					if ch == 1:
						print("Create Physical Volume")
                # Take list of Volume
						drive_name= input("Enter your drive name ")
						pv_create=sp.getoutput("pvcreate {}".format(drive_name))
						print(pv_create)
                # Create Volume Group
						
					elif ch == 2:
						print("Create display Physical Volume")
						drive_name= input("Enter your drive name ")
						lv_disp=sp.getoutput("pvdisplay {}".format(drive_name))
						print(lv_disp)
					
					elif ch == 3:
						print("Create volume Group")
						pv_name= input("Enter your PV name: ")
						vg_name= input("Enter VG name you want create: ")
						vg_create= sp.getoutput("vgcreate {} {}".format(pv_name,vg_name))
						
					elif ch == 4:
						print("Display volume Group")
						vg_name= input("Enter VG name: ")
						vg_disp=sp.getoutput("vgdisplay {}".format(vg_name))
						print(vg_disp)
						
					elif ch == 5:
						print("Create Logical Volume")
						size= int(input("Enter the size of LV: "))
						lv_name= input("Enter the name of LV: ")
						vg_name= input("Enter the name of VG: ")
						lv_create=sp.getoutput("lvcreate --size {}  --name {}  {}".format(size,lv_name,vg_name))
						print(lv_create)
						
				 	elif ch == 6:
						print("Display Logical Volume")
						lv_name= input("Enter the name of LV: ")
						lv_disp= sp.getoutput("lvdisplay {}".format(lv_name))
						print(lv_disp)
						
					elif ch == 7:
						print("Extending Logical Volume")
						lv_name= input("Enter the name of LV: ")
						size= int(input("Enter the size you want extend: "))
						sp.getoutput("lvextend --size {} {}".format(size,lv_name))
						lv_extend= sp.getoutput("resize2fs --size {} {}".format(size,lv_name))
						print(lv_extend)
					
					elif ch == 8:
						print("Reducing Logical Volume")
						lv_name= input("Enter the name of LV: ")
						size= int(input("Enter the size you want reduce: "))
						drive_name= input("Enter drive name to unmount: ")
						sp.getoutput("umount {}".format(drive_name))
						sp.getoutput("e2fsck -f ".format(lv_name))
						sp.getoutput("mkfs.ext4 {}".format(lv_name))
						sp.getoutput("resize2fs  {}  --size {}".format(lv_name,size))
						lv_reduce= sp.getoutput("lvreduce  --size {}  {}".format(size,lv_name))
						sp.getoutput("mount lv_name drive_name".format(lv_name,drive_name))
						print(lv_reduce)
						print("LV is mounted with {}".format(drive_name))
					
					elif ch == 9:
						print("Bye Bye")
						break
	

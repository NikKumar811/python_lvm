import subprocess as sp
from lvm import VolumeGroup,LogicalVolume

while True:
					
					print("""
A). Create Volume Group
B). Display Volume Group Information
C). Extend Volume Group Size
D). Merge two Volume Groups
E). Reduce Volume Group Size
F). Rename Volume Group
G). Remove Volume Group
H). Add Volume From Another Volume Group
I). Exit
					""")
					print("\n")
            # Take Input that what operation user would like to perform
					ch=input("What do you want to do => ")
					if ch == 'A':
						print("Create")
                # Take list of Volume
						volumes=[volume.replace(" ","") for volume in input("Enter volumes : ").split(",")]
						print(volumes)
                # Create Volume Group
						vg_name.create(volumes)
					elif ch == 'B':
                # Display Volume Group Information
						vg_name.display()
					elif ch == 'C':
						print("Extend")
                # Take Volumes List
						volumes=[volume.replace(" ","") for volume in input("Enter volumes : ").split(",")]
                # Extend Volume
						vg_name.extend(volumes)
					elif ch == 'D':
						print("Merge")
                # Take Volume Group which will be merged
						vg = VolumeGroup(input("Merged Volume Group :"))
                # Merge Volume Group
						vg_name.merge(vg)
                # Delete Reference of Merged Volume Group
						del vg
					elif ch == 'E':
						print("Reduce")
                # Reduce Volume Group . For this take input Volume
						vg_name.reduce(input("Enter volume name (which we want to remove from Volume Group) : "))
					elif ch == 'F':
						print("Rename")
                # Rename VOlume Group . Take New Volume Group Name
						vg_name.rename(input("New Volume Group Name : "))
					elif ch == 'G':
						print("Remove")
                # Remove Volume Group
						vg_name.remove()
					elif ch == 'H':
						print("Add")
                # Split Volume form Another Volume Group 
						vg_name.add(VolumeGroup(input("Enter Volume Group : ")),input("Volume Name : "))
					elif ch == 'I':
						break

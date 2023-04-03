
def create_fundraiser():
        name=input("name ")
        title = input("Title: ")
        details = input("Details: ")
        target = int(input("Target amount: "))
        save_fundraisers(name,title,details,target)

def save_fundraisers(name,title,details,target):
        with open('fundraisers.txt', 'a') as f:
                project_info=f"{name}:{title}:{details}:{target}\n"
                f.write(project_info)


def view_all_projects():
          with open('fundraisers.txt', 'r') as f:
             return  f.readlines()


def edit_fundraiser():
        
        lines=view_all_projects()
        name=input("name :")
        title = input("Title: ")
        details = input("Details: ")
        target = int(input("Target amount: "))
        new_lines=[]
        for line in lines:
             if line.startswith(name):
                   project_updated=f"{name}:{title}:{details}:{target}\n"
                   new_lines.append(project_updated)
             else:
                   new_lines.append(line)

        with open('fundraisers.txt','w') as f:
              for line in new_lines:
                    f.write(line)
                    
                   

   
def delete_fundraiser():
        
        name=input("Enter your name: ")
        lines=view_all_projects()
        new_lines=[]
        for line in lines:
              if not line.startswith(name):
                    new_lines.append(line)

       
        with open('fundraisers.txt', 'w') as f:
                 for line in new_lines:
                     name,title,details,target=line.strip("\n").split(":")
                     project_info=f"{name}:{title}:{details}:{target}\n"
                     f.write(project_info)

        
              

              

def fundraise_project():
    print("Enter 1 for Create : " )
    print("Enter 2 for edit : " )
    print("Enter 3 for view : " )
    print("Enter 4  for delete : ")

    choice =(int)(input("Enter your choice: "))
    if choice == 1:
        create_fundraiser()
        
    elif choice == 2:
        edit_fundraiser()
        
    elif choice == 3:
       print(view_all_projects())
    else:
        delete_fundraiser()

    

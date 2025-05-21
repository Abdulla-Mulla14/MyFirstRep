import json

read_file = 'youtube.txt'

def load_data():
    try:
        with open(read_file, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_data_helper(videos):
    with open(read_file, 'w') as file:
        json.dump(videos, file)

def list_all_videos(videos):
    print("\n")
    print("*" * 70)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. video name: {video['name']}, duration: {video['time']}")
    print("\n")
    print("*" * 70)

def add_videos(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)

def update_videos(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to update: "))
    if 1 <= index <= len(videos):
        # if 1 <= index <= len(videos):
        # if index >= 1 and index <= len(videos):
        # index >= 1: the index is not less than 1
        # index <= len(videos): the index is not more than the number of videos 
        name = input("Enter the new video name: ")
        time = input("Enter the new video time: ")
        videos[index-1] = {'name': name, 'time': time}
        save_data_helper(videos)
    else:
        print("Invalid index selected")

def delete_videos(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to be deleted: "))
    if 1 <= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
        print("Successfully Deleted")
    else:
        print("Invalid video index selected")


def main():
    videos = load_data()

    while True:
        print("\n Youtube Manager | Choose an option")
        print("1. List all youtube videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video")
        print("4. Delete a youtube video")
        print("5. Exit the app")
        choice = input("Enter your choice: ")
        # print(videos)

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_videos(videos)
            case '3':
                update_videos(videos)
            case '4':
                delete_videos(videos)
            case '5':
                break
            case _:                        # (_) aise isliye likha gaya hai kyunki agar more than 5 number mila toh user se oo as a Entry Invalid print karega 
                print("Invalid Choice")
            
if __name__ == '__main__':
    main()
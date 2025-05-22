from pymongo import MongoClient
from url import url
from bson import ObjectId

client = MongoClient(url)
db = client["ytmanager"]
video_collection = db["videos"]

# print(video_collection)

def list_videos():
    print("\n")
    print("*" * 70) 
    for video in video_collection.find():
        print(f"ID: {video['_id']}, Name: {video['name']}, Time: {video['time']}")
    print("\n")
    print("*" * 70) 

def add_video(name, time):
    video_collection.insert_one({"name": name, "time": time})

def update_video(video_id, new_name, new_time):
    video_collection.update_one(
        {'_id': ObjectId(video_id)},
        {"$set": {"name": new_name, "time": new_time}}
    )

def delete_video(video_id):
    video_collection.delete_one({'_id': ObjectId(video_id)})


def main():
    while True:
        print("\n  Youtube Manager App")
        print("1. List all youtube videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video")
        print("4. Delete a youtube video")
        print("5. Exit the app")
        choice = input("Enter your choice: ")

        if choice == "1":
            list_videos()
        elif choice == "2":
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_video(name, time)
        elif choice == "3":
            video_id = input("Enter the video id to update: ")
            new_name = input("Enter the new video name: ")
            new_time = input("Enter the new video time: ")
            update_video(video_id, new_name, new_time)
        elif choice == "4":
            video_id = input("Enter the video id to delete: ")
            delete_video(video_id)
        elif choice == "5":
            break
        else:
            print("Invalid Syntax")

        

if __name__ == "__main__":
    main()